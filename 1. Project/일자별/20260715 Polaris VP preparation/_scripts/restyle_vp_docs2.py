import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import os, traceback

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

DARK_BLUE = RGBColor(0x00, 0x04, 0x9C)
BLACK = RGBColor(0x00, 0x00, 0x00)

SPEC = {
    "Title":     dict(font="Arial", size=36, bold=True,  color=DARK_BLUE, align=WD_ALIGN_PARAGRAPH.CENTER),
    "Heading 1": dict(font="Arial", size=36, bold=True,  color=DARK_BLUE, align=WD_ALIGN_PARAGRAPH.CENTER),
    "Subtitle":  dict(font="Arial", size=16, bold=False, color=BLACK,     align=WD_ALIGN_PARAGRAPH.CENTER),
    "Heading 2": dict(font="Arial", size=14, bold=True,  color=DARK_BLUE, align=None),
    "Heading 3": dict(font="Arial", size=12, bold=True,  color=DARK_BLUE, align=None),
    "Heading 4": dict(font="Arial", size=11, bold=True,  color=DARK_BLUE, align=None),
    "Normal":    dict(font="Arial", size=10, bold=False, color=BLACK,     align=None),
}

def set_style(doc, name, spec):
    if name not in [s.name for s in doc.styles]:
        return False
    st = doc.styles[name]
    st.font.name = spec["font"]
    st.font.size = Pt(spec["size"])
    st.font.bold = spec["bold"]
    st.font.color.rgb = spec["color"]
    rpr = st.element.get_or_add_rPr()
    rFonts = rpr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = rpr.makeelement(qn('w:rFonts'), {})
        rpr.append(rFonts)
    rFonts.set(qn('w:ascii'), spec["font"])
    rFonts.set(qn('w:hAnsi'), spec["font"])
    rFonts.set(qn('w:eastAsia'), "맑은 고딕")
    if spec["align"] is not None:
        st.paragraph_format.alignment = spec["align"]
    return True

def bake_direct_formatting(doc, spec_map):
    """Apply font/size/bold/color directly on every run so the look survives
    even if Word later flattens/normalizes style-based formatting on open."""
    n = 0
    for p in doc.paragraphs:
        spec = spec_map.get(p.style.name)
        if not spec:
            continue
        if spec["align"] is not None:
            p.alignment = spec["align"]
        for r in p.runs:
            r.font.name = spec["font"]
            r.font.size = Pt(spec["size"])
            r.font.bold = spec["bold"]
            r.font.color.rgb = spec["color"]
            rpr = r._element.get_or_add_rPr()
            rFonts = rpr.find(qn('w:rFonts'))
            if rFonts is None:
                rFonts = rpr.makeelement(qn('w:rFonts'), {})
                rpr.append(rFonts)
            rFonts.set(qn('w:ascii'), spec["font"])
            rFonts.set(qn('w:hAnsi'), spec["font"])
            rFonts.set(qn('w:eastAsia'), "맑은 고딕")
            n += 1
    return n

results = []
for rel in FILES:
    path = os.path.join(BASE, rel)
    try:
        doc = docx.Document(path)
        applied = [name for name, spec in SPEC.items() if set_style(doc, name, spec)]
        n_baked = bake_direct_formatting(doc, SPEC)
        doc.save(path)
        results.append((rel, "OK", applied, n_baked))
    except Exception as e:
        results.append((rel, "ERROR: " + str(e), [], 0))
        traceback.print_exc()

print("\n=== SUMMARY ===")
for rel, status, applied, n_baked in results:
    print(f"{status:6s} | runs_baked={n_baked:4d} | applied={applied} | {rel}")

ok = sum(1 for r in results if r[1] == "OK")
print(f"\n{ok}/{len(FILES)} files processed successfully")
