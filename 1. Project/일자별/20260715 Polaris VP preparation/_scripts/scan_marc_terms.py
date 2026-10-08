import docx, os

BASE = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/일자별/*** 20260715 Polaris VP preparation ***/별도 제안서 draft"

FILES = [
    "Project 1 (Qingdao VLOC)/Value Proposition to Polaris - Project 1 (Qingdao VLOC) (EN).docx",
    "Project 1 (Qingdao VLOC)/Value Proposition to Polaris - Project 1 (Qingdao VLOC) (KR).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex A - BV Dry Bulk VLOC Track Record (EN).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex A - BV Dry Bulk VLOC Track Record (KR).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex C - BV VLOC Liquefaction Assessment (EN).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex C - BV VLOC Liquefaction Assessment (KR).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex D - BV Qingdao Beihai Track Record (EN).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex D - BV Qingdao Beihai Track Record (KR).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex E - BV Project Organization & CVs (EN).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex E - BV Project Organization & CVs (KR).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex F - BV Commercial Terms Summary (EN).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex F - BV Commercial Terms Summary (KR).docx",
    "Project 2 (Hengli BC)/Value Proposition to Polaris - Project 2 (Hengli BC) (EN).docx",
    "Project 2 (Hengli BC)/Value Proposition to Polaris - Project 2 (Hengli BC) (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex A - BV Dry Bulk VLOC Track Record (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex A - BV Dry Bulk VLOC Track Record (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex B - BV Hengli Site Organization (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex B - BV Hengli Site Organization (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex E - BV Project Organization & CVs (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex E - BV Project Organization & CVs (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex F - BV Commercial Terms Summary (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex F - BV Commercial Terms Summary (KR).docx",
]

KEYS = ["1,213", "49.2 million", "11.8 years", "12.8 years", "41 newbuilding",
        "less than 5 years old", "iron ore fines", "liquefaction",
        "VLOC", "SDARI", "methanol, ammonia", "ammonia, LNG",
        "AGS3D", "VeriSTAR", "220,000", "future-proof delivery",
        "Sources", "출처"]

for rel in FILES:
    path = os.path.join(BASE, rel)
    d = docx.Document(path)
    hits = {}
    for idx, p in enumerate(d.paragraphs):
        t = p.text
        for k in KEYS:
            if k.lower() in t.lower():
                hits.setdefault(k, []).append(idx)
    print("===", rel)
    for k in KEYS:
        if k in hits:
            print("   ", k, "->", hits[k])
