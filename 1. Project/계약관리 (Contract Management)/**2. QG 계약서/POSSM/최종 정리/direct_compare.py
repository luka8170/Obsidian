#!/usr/bin/env python3

from docx import Document
import PyPDF2
import re

print("="*80)
print("ANNEX C 검사 횟수 - 원본 파일 직접 비교")
print("="*80)

# 1. Read Word file (내가 보낸 파일)
print("\n[1] Word 파일 읽기 (내가 보낸 파일)...")
word_file = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/**2. QG 계약서/POSSM/최종 정리/내가 보낸 파일들/word/25.8.6. 송부) FYF AGREEMENT - POSSM(PAN OCEAN)_(as of Apr 30 2025) rev2.docx"

try:
    doc = Document(word_file)
    
    word_surveys = {}
    
    # Search in all tables
    for table_idx, table in enumerate(doc.tables):
        for row_idx, row in enumerate(table.rows):
            cells = [cell.text.strip() for cell in row.cells]
            
            # Print rows that might contain survey data
            row_text = " | ".join(cells)
            
            # Check for DOK
            if "DOK" in row_text and "Periodical Bottom" in row_text:
                print(f"\n  Found DOK row (Table {table_idx}, Row {row_idx}):")
                print(f"  Cells: {cells}")
                if len(cells) >= 3:
                    word_surveys['DOK'] = cells[2] if len(cells) > 2 else cells[-1]
            
            # Check for TPSC
            if "TPSC" in row_text and "Portside" in row_text:
                print(f"\n  Found TPSC row (Table {table_idx}, Row {row_idx}):")
                print(f"  Cells: {cells}")
                if len(cells) >= 3:
                    word_surveys['TPSC'] = cells[2] if len(cells) > 2 else cells[-1]
            
            # Check for TSBC
            if "TSBC" in row_text and "Starboard" in row_text:
                print(f"\n  Found TSBC row (Table {table_idx}, Row {row_idx}):")
                print(f"  Cells: {cells}")
                if len(cells) >= 3:
                    word_surveys['TSBC'] = cells[2] if len(cells) > 2 else cells[-1]
    
    print(f"\n내가 보낸 Word 파일 검사 횟수:")
    print(f"  DOK:  '{word_surveys.get('DOK', 'NOT FOUND')}'")
    print(f"  TPSC: '{word_surveys.get('TPSC', 'NOT FOUND')}'")
    print(f"  TSBC: '{word_surveys.get('TSBC', 'NOT FOUND')}'")

except Exception as e:
    print(f"Error reading Word file: {e}")
    import traceback
    traceback.print_exc()

# 2. Read PDF file (POSSM이 보낸 파일)
print("\n" + "="*80)
print("[2] PDF 파일 읽기 (POSSM이 보낸 파일)...")
pdf_file = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/**2. QG 계약서/POSSM/최종 정리/possm 최종 날인 완료 송부 파일/pdf/POSSM-BV FIVE YEAR FEE AGREEMENT (2025) - POSSM SIGNED, ANNEX B, C 수정.pdf"

try:
    pdf_surveys = {}
    
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        print(f"  Total pages: {len(pdf_reader.pages)}")
        
        # Extract text from all pages
        full_text = ""
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            full_text += page_text
            
            # Look for ANNEX C and survey data
            if "ANNEX C" in page_text or "DOK" in page_text or "TPSC" in page_text or "TSBC" in page_text:
                print(f"\n  Page {page_num + 1} contains survey keywords")
                
                lines = page_text.split('\n')
                for i, line in enumerate(lines):
                    if "DOK" in line and "Periodical" in line:
                        print(f"    DOK line: {line.strip()}")
                        # Try to extract number
                        numbers = re.findall(r'\b\d+\b', line)
                        if numbers:
                            pdf_surveys['DOK'] = numbers[-1]
                    
                    if "TPSC" in line and "Portside" in line:
                        print(f"    TPSC line: {line.strip()}")
                        numbers = re.findall(r'\b\d+\b', line)
                        if numbers:
                            pdf_surveys['TPSC'] = numbers[-1]
                    
                    if "TSBC" in line and "Starboard" in line:
                        print(f"    TSBC line: {line.strip()}")
                        # Check for dash or number
                        if '-' in line and 'TSBC' in line:
                            pdf_surveys['TSBC'] = '-'
                        else:
                            numbers = re.findall(r'\b\d+\b', line)
                            if numbers:
                                pdf_surveys['TSBC'] = numbers[-1]
    
    print(f"\nPOSSM이 보낸 PDF 파일 검사 횟수:")
    print(f"  DOK:  '{pdf_surveys.get('DOK', 'NOT FOUND')}'")
    print(f"  TPSC: '{pdf_surveys.get('TPSC', 'NOT FOUND')}'")
    print(f"  TSBC: '{pdf_surveys.get('TSBC', 'NOT FOUND')}'")

except Exception as e:
    print(f"Error reading PDF file: {e}")
    import traceback
    traceback.print_exc()

# 3. Compare
print("\n" + "="*80)
print("최종 비교 결과")
print("="*80)
print(f"{'검사코드':<10} {'내가 보낸 (Word)':<20} {'POSSM 최종 (PDF)':<20} {'변경사항':<30}")
print("-"*80)

for survey in ['DOK', 'TPSC', 'TSBC']:
    word_val = word_surveys.get(survey, '?')
    pdf_val = pdf_surveys.get(survey, '?')
    
    if word_val == pdf_val:
        change = "동일"
    elif word_val == '?' or pdf_val == '?':
        change = "확인 불가"
    else:
        change = f"변경: {word_val} → {pdf_val}"
    
    print(f"{survey:<10} {word_val:<20} {pdf_val:<20} {change:<30}")

print("="*80)
