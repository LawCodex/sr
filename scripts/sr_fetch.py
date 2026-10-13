#!/usr/bin/env python3
"""Fetch Surinamese legislation published by De Nationale Assemblée (DNA),
https://www.dna.sr/wetgeving/surinaamse-wetten/ .

Categories fetched (each item page links one or more PDFs under /media/):
  geldende-teksten-t-m-2005  consolidated texts in force (status up to 2005)
  wetten-na-2005             laws enacted after 2005
  wijzigingen-na-2005        amending laws enacted after 2005
Skipped: begrotingen (budgets), naturalisatie-wetten (individual
naturalisations), overeenkomsten-verdragen (treaty approval laws).
PDFs are cached in _raw/sr/pdf/. dna.sr has no robots.txt; we wait 1.5 s
between requests.
Usage: sr_fetch.py
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

import requests
from bs4 import BeautifulSoup

BASE = "https://www.dna.sr"
CATS = ["geldende-teksten-t-m-2005", "wetten-na-2005", "wijzigingen-na-2005"]
UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
RAW = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_raw", "sr"))
DELAY = 1.5
s = requests.Session()
s.headers["User-Agent"] = UA


def get(url):
    for i in range(5):
        try:
            r = s.get(url, timeout=300)
            time.sleep(DELAY)
            if r.status_code in (200, 404, 403, 410):
                return r
        except requests.RequestException as e:
            print("  retry", url, e, file=sys.stderr, flush=True)
        time.sleep(5 * (i + 1))
    raise RuntimeError("failed " + url)


class _Failed:
    status_code = 0
    content = b""
    headers = {}


FAILED = _Failed()


def pdf_ok(path):
    if not os.path.exists(path) or os.path.getsize(path) < 100:
        return False
    with open(path, "rb") as f:
        head = f.read(5)
        f.seek(max(0, os.path.getsize(path) - 2048))
        tail = f.read()
    if head != b"%PDF-" or b"%%EOF" not in tail:
        return False
    return subprocess.run(["pdfinfo", path], capture_output=True).returncode == 0


def build_index():
    ip = os.path.join(RAW, "index.json")
    if os.path.exists(ip):
        return json.load(open(ip))
    idx = []
    for cat in CATS:
        soup = BeautifulSoup(get("%s/wetgeving/surinaamse-wetten/%s/" % (BASE, cat)).text, "lxml")
        pages = []
        for a in soup.find_all("a", href=re.compile(r"^/wetgeving/surinaamse-wetten/%s/[^/]+/$" % cat)):
            if a["href"] not in [p[0] for p in pages]:
                pages.append((a["href"], a.get_text(" ", strip=True)))
        for href, title in pages:
            ps = BeautifulSoup(get(BASE + href).text, "lxml")
            h1 = ps.find("h1")
            pdfs = []
            for a in ps.find_all("a", href=re.compile(r"\.pdf$", re.I)):
                u = urllib.parse.urljoin(BASE, a["href"])
                if u not in pdfs:
                    pdfs.append(u)
            idx.append({"category": cat, "page": BASE + href, "title": title or (h1.get_text(" ", strip=True) if h1 else ""),
                        "h1": h1.get_text(" ", strip=True) if h1 else "", "pdfs": pdfs})
            print(cat, title, len(pdfs), flush=True)
    json.dump(idx, open(ip, "w"), indent=1, ensure_ascii=False)
    return idx


def fname(url):
    p = urllib.parse.unquote(urllib.parse.urlparse(url).path).split("/")
    return re.sub(r"[^A-Za-z0-9._-]", "_", p[-2] + "-" + p[-1])


def main():
    os.makedirs(os.path.join(RAW, "pdf"), exist_ok=True)
    idx = build_index()
    bad = []
    for it in idx:
        for u in it["pdfs"]:
            p = os.path.join(RAW, "pdf", fname(u))
            if pdf_ok(p):
                continue
            try:
                r = get(urllib.parse.quote(u, safe=":/%"))
            except RuntimeError as e:
                print('  giving up', e, flush=True)
                r = FAILED
            ok = False
            if r.status_code == 200 and r.content[:5] == b"%PDF-":
                cl = r.headers.get("content-length")
                if not cl or r.headers.get("content-encoding") or int(cl) == len(r.content):
                    open(p, "wb").write(r.content)
                    ok = pdf_ok(p)
            if not ok:
                bad.append({"url": u, "status": r.status_code})
            print(fname(u), ok, flush=True)
    json.dump(bad, open(os.path.join(RAW, "failed.json"), "w"), indent=1)
    print("failed:", len(bad))


if __name__ == "__main__":
    main()
