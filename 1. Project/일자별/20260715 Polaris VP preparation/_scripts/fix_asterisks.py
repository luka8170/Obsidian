import docx, os, re
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

BASE = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/일자별/*** 20260715 Polaris VP preparation ***/별도 제안서 draft"

FILES = [
    "Project 1 (Qingdao VLOC)/Annexes/Annex F - BV Commercial Terms Summary (EN).docx",
    "Project 1 (Qingdao VLOC)/Annexes/Annex F - BV Commercial Terms Summary (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex A - BV Dry Bulk VLOC Track Record (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex A - BV Dry Bulk VLOC Track Record (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex E - BV Project Organization & CVs (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex E - BV Project Organization & CVs (KR).docx",
    "Project 2 (Hengli BC)/Annexes/Annex F - BV Commercial Terms Summary (EN).docx",
    "Project 2 (Hengli BC)/Annexes/Annex F - BV Commercial Terms Summary (KR).docx",
]

DARK_BLUE = RGBColor(0x00, 0x04, 0x9C)
BLACK = RGBColor(0x00, 0x00, 0x00)
FMT = {
    "title": dict(font="Arial", size=28, bold=True,  color=DARK_BLUE, align=WD_ALIGN_PARAGRAPH.CENTER),
    "h2":    dict(font="Arial", size=14, bold=True,  color=DARK_BLUE, align=None),
    "h3":    dict(font="Arial", size=12, bold=True,  color=DARK_BLUE, align=None),
}
NUM_H3 = re.compile(r'^\d+\.\d+(\.\d+)?\s+\S')
NUM_H2 = re.compile(r'^\d+\.\s+\S')
ANNEX_TITLE = re.compile(r'^ANNEX\s+[A-Z]\s*[–\-]', re.I)
KNOWN_H2 = {"table of contents","executive summary","preamble","conclusion","next steps",
            "why bureau veritas","value summary","list of annexes","commercial terms",
            "sources","note"}

def classify(text, idx):
    t = text.strip()
    if not t:
        return None
    if idx == 0 or ANNEX_TITLE.match(t):
        return "title"
    if NUM_H3.match(t):
        return "h3"
    if NUM_H2.match(t):
        return "h2"
    if t.lower().rstrip(':') in KNOWN_H2 and len(t) < 60:
        return "h2"
    return None

def apply_direct(run, spec):
    run.font.name = spec["font"]
    run.font.size = Pt(spec["size"])
    run.font.bold = spec["bold"]
    run.font.color.rgb = spec["color"]
    rpr = run._element.get_or_add_rPr()
    rFonts = rpr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = rpr.makeelement(qn('w:rFonts'), {})
        rpr.append(rFonts)
    rFonts.set(qn('w:ascii'), spec["font"])
    rFonts.set(qn('w:hAnsi'), spec["font"])
    rFonts.set(qn('w:eastAsia'), "맑은 고딕")

for rel in FILES:
    path = os.path.join(BASE, rel)
    doc = docx.Document(path)
    n_strip = 0
    n_fmt = 0
    for idx, p in enumerate(doc.paragraphs):
        if '**' in p.text:
            for r in p.runs:
                if '**' in r.text:
                    r.text = r.text.replace('**', '')
                    n_strip += 1
        kind = classify(p.text, idx)
        if kind:
            spec = FMT[kind]
            if spec["align"] is not None:
                p.alignment = spec["align"]
            for r in p.runs:
                apply_direct(r, spec)
                n_fmt += 1
    doc.save(path)
    print(f"strip={n_strip:3d} fmt_runs={n_fmt:3d} | {rel}")

print("done")
