# Suriname — LawCodex

Legislation of the Republic of Suriname as plain Markdown, in Dutch, the official language.
Part of [LawCodex](https://github.com/LawCodex).

**Status: partial.** This repo has every law published by De Nationale Assemblée (DNA) as a
text PDF, including the Grondwet. About half of the DNA's PDFs are scanned images, which were
not OCR'd and are listed below.

## What is covered

| Directory | Contents | Files |
|---|---|---|
| `grondwet/` | Grondwet van de Republiek Suriname (S.B. 1987 no. 116), as amended by S.B. 1992 no. 38 | 1 |
| `geldende-teksten/` | Consolidated texts in force as published by the DNA, status up to 2005: Burgerlijk Wetboek, Wetboek van Koophandel, Wetboek van Strafrecht, Wetboek van Strafvordering, tax laws, labour laws and others | 97 |
| `wetten-na-2005/` | Laws enacted after 2005, as published in the Staatsblad (S.B.) | 64 |
| `wijzigingen-na-2005/` | Amending laws enacted after 2005 | 56 |

**Total: 218 texts.** Source:
**De Nationale Assemblée**, "Surinaamse wetten": https://www.dna.sr/wetgeving/surinaamse-wetten/
(sub-pages `geldende-teksten-t-m-2005`, `wetten-na-2005` and `wijzigingen-na-2005`). Each
law page links one or more PDFs. When a page has several PDFs (for example the original law
and a later amendment, or an erratum), they are joined in one file, separated by `---`, in
the order the page gives them. Parliamentary reports (preadvies, eindverslag) are excluded.

## Caveats

- The "geldende teksten" are the DNA's consolidations **up to 2005**. Later amendments are
  published separately under `wijzigingen-na-2005/` and are **not** merged into them.
- The Grondwet text is the 1987 Constitution as amended in 1992, as published by the DNA. Check
  for any later amendments.
- The DNA site lists a "Nieuw Burgerlijk Wetboek" (new Civil Code). Only parliamentary reports
  were linked there, now 404, and no law text, so the new code is **not** included.
  `geldende-teksten/burgerlijk-wetboek-1859.md` is the old Civil Code in its 2005
  consolidation.
- Not fetched: budget laws (`begrotingen`), naturalisation laws (`naturalisatie-wetten`)
  and treaty-approval laws (`overeenkomsten-verdragen`). Secondary legislation
  (staatsbesluiten, beschikkingen) is not covered beyond what the DNA lists.

## Gaps: scanned PDFs (not OCR'd)

These items are on dna.sr only as scanned images with no text layer, so they are not
included. One item ("Wet wijz. Rijwet 1971, Wetboek van Strafvordering 1989") has no PDF at all.

**geldende-teksten-t-m-2005** (81): Amnestiewet SB 1980 no. 27; Amnestiewet SB 1992 no. 68; Archiefbesluit; Archiefwet (2006); DECREET Aanpassings- en Wijzigingswet Strafvordering (1980); DECREET Aansprakelijkheidsverzekering Motorrijtuigen (1986); DECREET C-66 wijz. Surinaams Wetboel van Strafvordering; DECREET Mijnbouw (1986); DECREET Opheffing Hoog Militair Gerechtshof (1983); DECREET houdende aanvulling Militaire Strafpleging (1980); DECREET houdende bekrachtiging op de Landhervorming in Suriname; DECREET houdende wijz. Wet Militaire Strafrechtpleging (1982); DECREET machtiging tot oprichting Stichting Staatsziekenfonds; DECREET uitgifte Domeingrond (1982); DECREET van 17 oktober 1987 tot wijz. decreet houdende regels voor verkiezing van leden voor de volksvertegenwoordigende lichamen in Suriname (Kiesregeling) 1987; DECREET wijz. Kiesregeling (1987); DECREET wijz. Nationaliteit en Ingezetenschap (1983); DECREET wijz. Nationaliteit en Ingezetenschap (1984); DECREET wijz. Surinaamsch Toelatingsbesluit 1938 en andere wettelijke regelingen; DECREET wijz. Wet Militaire Strafrechtspleging (1984); DECREET wijz. Wet Tarieven in Burgerlijke Zaken (1985); DECREET wijz. Wet Waterschapswet 1931; DECREET wijz. Wet van Koophandel (1983); DECREET wijz. verkrijgen bevoegdheid geneeskundige beroepen en uitoefening van die beroepen; DECREET wijz. verkrijgen bevoegdheid geneeskundige beroepen en uitoefening van die beroepen (1); Decreet Loonbelasting; Decreet Wet aansprakelijkheidsverzekering motorrijtuigen & Rijwet 1971; Decreet van 11 december 1987 nadere wijz. "Muntwet 1960"; Decreet van 11 december 1987 nadere wijz. "Muntwet 1960" (1); Decreet wijz. Stedebouwkundige Wet; Domeindecreet 1981; Handelsregisterwet; Hinderwet; Kiesregeling (2005); STAATSBESLUIT wijz. Wet Tarieven in Burgerlijke Zaken (2005); STAATSBESLUIT wijz. Wet van Koophandel (1997); Standaardenwet (1); Surinaams Burgerlijk Wetboek tot regeling omgangswet; Wet Bosbeheer; Wet Goederenverkeer; Wet Huurkoop Onroerend Goed SB 1978 No 32; Wet Huurwaardebelasting 1995; Wet In Staat van Beschuldigingstelling Politieke Ambtsdragers (2001) 25 oktober 2001; Wet Regionale Organen (2000); Wet Tarief van Invoerrechten 2002; Wet Tarief van Invoerrechten 2004; Wet Veiligheid en Beveiliging Burgerluchtvaart; Wet Vernoeming en Herleiding van Guldensbedragen tot Dollarbedragen; Wet Wegenautoriteit (1995); Wet betreffende Universitaire Titulatuur; Wet houdende regelen kandidaatstelling en verkiezing president en vicepresident; Wet op de Staatsschuld 2002; Wet regeling Inkomen en overige financiële voorzieningen president & vicepresident Rep. Sur (1988); Wet toestemming Ontwikkelingsproject Olieplamindustrie Marowijne; Wet van 5 januari 1988; Wet verplichte verzekering tegen wettelijke aansprakelijkheid motorrijtuigen; Wet wijz. "Decreet Uitgifte Domeingrond" (1990); Wet wijz. Aansprakelijkheidsverzekering Motorrijtuigen (1994); Wet wijz. Aansprakelijkheidsverzekering Motorrijtuigen (2000); Wet wijz. Aansprakelijkheidsverzekering Motorrijtuigen (2004); Wet wijz. Decreet Uitgifte Domeingrond (2003); Wet wijz. Huurwaardebelasting 1995 (2002); Wet wijz. Inkomstenbelasting 1922 (2005); Wet wijz. Krankzinnigenwet; Wet wijz. Loterijbelasting (2002); Wet wijz. Militaire Strafrechtpleging (1994); Wet wijz. Muntwet 1960 (1976); Wet wijz. Nationaliteit en Ingezetenschap (1989); Wet wijz. Nationaliteit en Ingezetenschap (2002); Wet wijz. Rijwet 1971 & Wetboek van Strafvordering (1989); Wet wijz. Staatsraad (1994); Wet wijz. Tarieven in Burgerlijke Zaken (2001); Wet wijz. Uitoefening Geneeskundige Beroepen (2003); Wet wijz. Wetboek van Strafvordering (1989); Wet wijz. Wetboek van Strafvordering (2002); Wet wijz. Wetboek van Strafvordering (2004); Wet wijz. Zeevisserijdecreet; Wet wijz. accijns rooktabak en/ of sigaretten 1967 (2000); Wet wijz. financiële voorzieningen Ministers en Onderministers (1993); Wet wijz. financiële voorzieningen ministers en onderministers (1994); Wet wijz. regeling van het Surinamerschap en Ingezetenschap.
**wijzigingen-na-2005** (77): Amnestiewet 2012; Autobusdienstwet; Bankwet 1956; Decreet Arbeidsinspectie; Kiesregeling; Ongevallenregeling; Rijwet 1971; Surinaams Wetboek van Koophandel; Tractatenblad 1963, 28; Wet Accijns Alcoholvrije Dranken; Wet Bekwame Burgers van de Caraibische Gemeenschap; Wet Bieraccijns; Wet Casinobelasting 2002; Wet Hazardspelen; Wet In Staat van Beschuldigingstelling Politieke Ambtsdragers (2007); Wet Regionale Organen en Waterschapswet 1931; Wet Strafbaarstelling Belaging; Wet Surinaams Bureau voor Standaarden; Wet Verdovende Middelen (18 september 2018); Wet aansprakelijkheidsverzekering Motorrijtuigen; Wet accijns rooktabak en/of sigaretten 1967; Wet beëindiging lidmaatschap DNA; Wet geldelijke voorzieningen leden en gewezen leden van De Nationale Assemblee; Wet op de Staatsschuld (2011); Wet op drankhuizen en huizen van openbare vermakelijkheden; Wet op het Statistiekrecht 1973; Wet uitoefening Geneeskundige Beroepen; Wet van 29 december 2016, Wet op de Staatsschuld; Wet van 29 december 2016, machtiging aan de Minister van Financiën tot afwijking obligoplafond; Wet wijz. Advocatenwet; Wet wijz. Amnestiewet; Wet wijz. Arbeidsgeschillenwet 1946; Wet wijz. Arbeidswet 1963; Wet wijz. Coöperatieve Verenigingen 1944 (WET van 16 jan 2017); Wet wijz. Decreet Arbeidsadviescollege; Wet wijz. Fiscaal Identificatienummer (2024); Wet wijz. Grondwet; Wet wijz. Inkomstenbelasting 1922 (WET van 15 december 2016); Wet wijz. Inkomstenbelasting 1922 (WET van 25 april 2016); Wet wijz. Kiesregeling (2023); Wet wijz. Melding Ongebruikelijke Transacties 2016; Wet wijz. Muntwet 1960; Wet wijz. Muntwet 1960 (2003); Wet wijz. Omzetbelasting 1997 (WET van 12 augustus 2021); Wet wijz. Ongevallenregeling; Wet wijz. Personeelswet en nadere wijz. Ambtenarenpensioenwet 1972; Wet wijz. Petroleumwet (2022); Wet wijz. Petroleumwet 1990 (S.B. 1991 no.7, zoals gewijz. bij 2001 no.58); Wet wijz. Surinaams Burgerlijk Wetboek; Wet wijz. Surinamerschap en het Ingezetenschap; Wet wijz. Toezicht en Controle Kansspelen (S.B. 2009 no. 78); Wet wijz. Vacantiewet 1975; Wet wijz. Veiligheidswet 1947; Wet wijz. Vuurwapenwet; Wet wijz. Werkvergunning Vreemdelingen (S.B. 1981 no. 62, zoals laatstelijk gewijz. bij S.B. 2002 no.23); Wet wijz. Wet Bekwame Burgers Caraïbische Gemeenschap; Wet wijz. Wet Belasting over de Toegevoegde Waarde (BTW 2023 verbeterblad); Wet wijz. Wet Bieraccijns (2021); Wet wijz. Wet Uitvoering Burgerlijke Uitzonderingstoestand (S.B. 2020 no. 151); Wet wijz. Wet op de Staatsschuld (2016); Wet wijz. Wet op de Staatsschuld (2017); Wet wijz. Wetboek v Strafrecht & Wet ter voorkoming en bestrijding Money Laundering en Terrorismefin & Wet Strafbaarstelling Money Laundering; Wet wijz. Wetboek van Militair Strafrecht (G.B. 1975 no. 173); Wet wijz. enige tariefposten betreffende vlees en eetbare slachtafvallen van pluimvee van de tarieflijst; Wet wijz. geldelijke voorzieningen leden en gewezen leden van De Nationale Assemblée; Wet wijz. op de Jaarrekening (S.B. 2017 no. 84); Wetboek van Burgerlijke Rechtsvordering; Wetboek van Strafrecht; Wetboek van Strafrecht (17 april 2009); Wetboek van Strafrecht ivm herziening zedenmisdrijven; Wetboek van Strafvordering; Wetboek van strafvordering ivm DNA-onderzoek in strafzaken; Wijz. Rijwet 1971 (wet van 11 maart 2022); Wijz. Surinaams Burgerlijk Wetboek, zoals laatstelijk gewijz. bij S.B. 2016 no. 67 (wet van 16 maart 2022); Wijziging Wet Identificatieplicht Dienstverleners; Wijziging Wet Internationale Sancties; wijz. Wetboek van Strafrecht (16 september 2014).
**wetten-na-2005** (69): Aanvulling registers Burgerlijke Stand; Arbeidsbemiddelingswet 2017; Comptabiliteitswet 2015; Electriciteitswet 2016; Herziene Handvest "Organisation of Islamic Cooperation (OIC)"; International Convention for Suppression Financing Terrorism; Loterijwet (2023); Machtigingswet "Suriname National & Foreign Investment NV, afgekort SNFI N.V.; Ontslagwet 2018; Postwet 2005; Presidentieel Besluit Wet Uitvoering Burgerlijke Uitzonderingstoestand (S.B. 2020 no. 151) (S.B. 2021 no. 01); Presidentieel Besluit toetreding Sur tot United Nations Convention against Torture and other Cruel, Inhuman Punishment (UNCAT); Tabakswet 2013; Toetreding Suriname tot Rome Statute of the International Criminal Court (1); Uitvoerrecht op hout; VERBETERBLAD op Staatsblad 2022 no.121 (Wet Belasting over de Toegevoegde Waarde 2022); WHO Framework Convention on Tobacco Control; Wet Algemeen Pensioen 2014; Wet Ambtssymbool President; Wet Arbeid Kinderen en Jeugdige Personen; Wet Auteursrecht 1913; Wet Bedrijven en Beroepen; Wet Belasting over de Toegevoegde Waarde 2022; Wet Bestrijding Huiselijk Geweld; Wet Bloedvoorziening; Wet Caribbean Development Bank; Wet Collectieve Arbeidsovereenkomst; Wet DNA-databank in strafzaken; Wet Dierenwelzijn (WET van 16 jan '17); Wet Elektronische Uitgifte Staats-en Advertentieblad; Wet Energie Autoriteit Suriname; Wet Financiele Voorzieningen Rekenkamer van Suriname (2005); Wet Hazardspelen, alsmede nadere wijz. Wetboek v Strafrecht, Wetboek v Strafvordering & Wet Casinobelasting 2002; Wet Huisvestingsplan voor de periode 2012 tot en met 2017; Wet Inspectie Vlees en overige Dierlijke Producten; Wet Instelling Kustwacht; Wet Internationale Sancties; Wet Kapitaalmarkt 2014; Wet Maritieme Zones; Wet Militair Uniform; Wet Minimum Uurloon; Wet NIVS; Wet NOVA; Wet Nationale Basiszorgverzekering; Wet Omzetting Arbeidsovereenkomst voor Bepaalde Tijd naar Arbeidsovereenkomst Onbepaalde Tijd; Wet Opvanginstellingen; Wet PSA; Wet Pensioenfondsen en Voorzieningsfondsen; Wet Reisdocumenten; Wet Rekenkamer Suriname 2019; Wet Rij- en Voertuigenbelasting; Wet STCW; Wet Spaar- en Stabilisatiefonds Suriname 2017; Wet Suriname Business Forum; Wet Suriname Chartered Accountants Institute; Wet Tarieven Gezondheidszorg; Wet Ter Beschikking Stellen Arbeidskrachten door Intermediairs (2017); Wet Verlenging Burgerlijke Uitzonderingstoestand 2021; Wet Vijfde Landbouwtelling; Wet Voorafgaande Vracht-informatieverstrekking 2022; Wet Vrijheid Vakverenigingen; Wet achtste Algemene Volkstelling; Wet houdende bekrachtiging Beschikking minister Financiën; Wet rechtmatigheid en rechtspositie Rekenkamer Suriname; Wet ter beperking van het gebruik van tabak en tabaksproducten; Wet toezicht en Controle Kansspelen; Wet tot regeling van de geldelijke voorzieningen van de leden en gewezen leden van De Nationale Assemblée; Wet wijz. Autobusdienstwet; Zaadwet.

## Format

One Markdown file per law with YAML front matter (`title`, `identifier` (Staatsblad or
Gouvernementsblad number when it appears in the title), `type`, `jurisdiction`, `language`,
`date`, `status`, `source` (DNA page), `source_pdf`, `consolidation`, `retrieved`). Text
was extracted with `pdftotext` (no OCR) and kept as extracted. BOEK / TITEL / HOOFDSTUK /
AFDELING / PARAGRAAF lines become `##` headings and articles become `### Artikel N`.
Running page headers and page numbers were removed.

## Licence / copyright

The DNA's [copyright notice](https://www.dna.sr/copyright/auteursrechten/) allows parts of the
site's content to be reused on condition that the source is cited, with a link. Every file
cites its source URL. Laws are official texts of the Republic of Suriname. This is not an
official publication; consult the *Staatsblad van de Republiek Suriname*.

## Regenerate

```sh
pip install -r scripts/requirements.txt   # plus poppler-utils
python3 scripts/sr_fetch.py     # index + PDFs into ../_raw/sr
python3 scripts/sr_convert.py   # Markdown
```

Retrieved: 2026-10-13.
