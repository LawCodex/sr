#!/usr/bin/env python3
"""Convert the PDFs fetched by sr_fetch.py into Markdown.

  grondwet/grondwet-van-de-republiek-suriname.md
  geldende-teksten/<slug>.md     consolidated texts (status up to 2005)
  wetten-na-2005/<slug>.md       laws enacted after 2005
  wijzigingen-na-2005/<slug>.md  amending laws enacted after 2005
Text is extracted with pdftotext (no OCR); scanned PDFs are listed as gaps
in _raw/sr/gaps.json.
Usage: sr_convert.py
"""
import collections
import datetime
import json
import os
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sr_fetch import RAW, fname  # noqa: E402

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TODAY = datetime.date.today().isoformat()
DIRS = {"geldende-teksten-t-m-2005": "geldende-teksten", "wetten-na-2005": "wetten-na-2005",
        "wijzigingen-na-2005": "wijzigingen-na-2005"}
HEAD_RE = re.compile(r"^(HOOFDSTUK|Hoofdstuk|AFDELING|Afdeling|TITEL|Titel|BOEK|Boek|PARAGRAAF|Paragraaf|DEEL|Deel)\s+"
                     r"([IVXLC]+|\d+[A-Za-z]?|[A-Z]|EERSTE|TWEEDE|DERDE|VIERDE|VIJFDE|ZESDE|ZEVENDE|ACHTSTE|NEGENDE|TIENDE)\b.{0,120}$")
ORD_RE = re.compile(r"^(EERSTE|TWEEDE|DERDE|VIERDE|VIJFDE|ZESDE|ZEVENDE|ACHTSTE|NEGENDE|TIENDE|ELFDE|TWAALFDE)\s+"
                    r"(AFDELING|PARAGRAAF|TITEL|BOEK|HOOFDSTUK)\b.{0,80}$")
ART_RE = re.compile(r"^(Artikel|ARTIKEL|Art\.)\s+(\d+[a-zA-Z]*(?:\.\d+)?|[IVXLC]+)\s*[.:]?\s*(.{0,200})$")
MONTHS = {m: i + 1 for i, m in enumerate(["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus",
                                          "september", "oktober", "november", "december"])}


def slug(t, n=90):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:n].rstrip("-")


def yq(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def pages_of(p):
    return subprocess.run(["pdftotext", "-enc", "UTF-8", p, "-"], capture_output=True).stdout.decode("utf-8", "replace").split("\f")


def is_scan(pages):
    n = max(1, len(pages) - 1)
    return len(re.sub(r"\s", "", "".join(pages))) < 150 * n


def convert(pages):
    cnt = collections.Counter()
    for p in pages:
        ls = [l.strip() for l in p.split("\n") if l.strip()]
        for l in set(ls[:3] + ls[-3:]):
            cnt[re.sub(r"\d+", "#", l)] += 1
    np_ = len([p for p in pages if p.strip()])
    running = {k for k, c in cnt.items() if np_ >= 4 and c >= max(3, np_ * 0.3) and len(k) < 100}
    out = []
    for p in pages:
        ls = p.split("\n")
        nb = [i for i, l in enumerate(ls) if l.strip()]
        edge = set(nb[:3] + nb[-3:])
        for i, l in enumerate(ls):
            st = re.sub(r"\s+", " ", l).strip()
            if not st:
                if out and out[-1] != "":
                    out.append("")
                continue
            if i in edge and (re.sub(r"\d+", "#", st) in running or re.fullmatch(r"[-– ]*\d{1,4}[-– ]*", st)):
                continue
            if HEAD_RE.match(st) or ORD_RE.match(st):
                out += ["", "## " + st, ""]
                continue
            m = ART_RE.match(st)
            if m and (not m.group(3) or m.group(3)[:1].isupper() or m.group(3)[:1] in "(1234567890"):
                out += ["", "### Artikel " + m.group(2), ""]
                if m.group(3):
                    out.append(m.group(3))
                continue
            if re.match(r"^[#>*+\-=|`]", st):
                st = "\\" + st
            st = re.sub(r"^(\d+)([.)])(\s)", r"\1\\\2\3", st)
            out.append(st)
        if out and out[-1] != "":
            out.append("")
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def sb_ident(t):
    m = re.search(r"S\.?\s?B\.?\s*(\d{4})\s*(?:no\.?|nr\.?)\s*(\d+)", t, re.I)
    if m:
        return "S.B. %s no. %s" % (m.group(1), m.group(2))
    m = re.search(r"G\.?\s?B\.?\s*(\d{4})\s*(?:no\.?|nr\.?)\s*(\d+)", t, re.I)
    return "G.B. %s no. %s" % (m.group(1), m.group(2)) if m else ""


def date_of(t):
    m = re.search(r"(\d{1,2})\s+([a-z]+)\s+(\d{4})", t.lower())
    if m and m.group(2) in MONTHS:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2)], int(m.group(1)))
    return ""


def main():
    idx = json.load(open(os.path.join(RAW, "index.json")))
    gaps, counts, used = [], collections.Counter(), set()
    for it in idx:
        title = re.sub(r"\s+", " ", it["h1"] or it["title"]).strip()
        if not it["pdfs"]:
            gaps.append({"title": title, "page": it["page"], "reason": "no PDF on page"})
            continue
        bodies = []
        for u in it["pdfs"]:
            if re.search(r"preadvies|eindverslag|aanb|amendement|intrekking", u, re.I):
                continue  # parliamentary reports, not the law text
            p = os.path.join(RAW, "pdf", fname(u))
            if not os.path.exists(p):
                gaps.append({"title": title, "url": u, "reason": "download failed"})
                continue
            pages = pages_of(p)
            if is_scan(pages):
                gaps.append({"title": title, "url": u, "reason": "scanned PDF without text layer"})
                continue
            bodies.append((u, convert(pages)))
        if not bodies:
            continue
        is_gw = it["category"] == "geldende-teksten-t-m-2005" and title.lower().startswith("grondwet")
        d = "grondwet" if is_gw else DIRS[it["category"]]
        typ = "constitution" if is_gw else ("wijzigingswet" if it["category"] == "wijzigingen-na-2005" else "wet")
        tl = title.lower()
        if not is_gw:
            if tl.startswith("decreet"):
                typ = "decreet"
            elif tl.startswith(("besluit", "staatsbesluit")):
                typ = "besluit"
            elif "wetboek" in tl:
                typ = "code"
        path = os.path.join(OUT, d, slug(it["page"].rstrip("/").rsplit("/", 1)[1]) + ".md")
        if path in used:
            path = path[:-3] + "-2.md"
        used.add(path)
        fm = ["---", "title: " + yq(title)]
        ident = sb_ident(title)
        if ident:
            fm.append("identifier: " + yq(ident))
        fm += ["type: " + typ, "jurisdiction: sr", "language: nl"]
        dt = date_of(title)
        if dt:
            fm.append("date: " + dt)
        fm += ["status: " + ("in_force" if it["category"] != "wijzigingen-na-2005" else "in_force"),
               "source: " + yq(it["page"])]
        fm.append("source_pdf: " + yq(bodies[0][0]) if len(bodies) == 1 else
                  "source_pdf: [" + ", ".join(yq(u) for u, _ in bodies) + "]")
        if it["category"] == "geldende-teksten-t-m-2005":
            fm.append('consolidation: "geldende tekst (DNA), stand t/m 2005"')
        fm += ["retrieved: " + TODAY, "---"]
        body = "\n\n---\n\n".join(b for _, b in bodies)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write("\n".join(fm) + "\n\n# " + title + "\n\n" + body)
        counts[d] += 1
    json.dump(gaps, open(os.path.join(RAW, "gaps.json"), "w"), indent=1, ensure_ascii=False)
    print(dict(counts), "gaps:", len(gaps))


if __name__ == "__main__":
    main()
