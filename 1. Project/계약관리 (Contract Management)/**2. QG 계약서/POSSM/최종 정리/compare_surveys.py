#!/usr/bin/env python3

from docx import Document
import PyPDF2
import re

print("="*80)
print("ANNEX C 검사 횟수 비교")
print("="*80)

# 1. Read Word file (내가 보낸 파일)
print("\n[1] 내가 보낸 Word 파일 읽기...")
word_file = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/**2. QG 계약서/POSSM/최종 정리/내가 보낸 파일들/word/25.8.6. 송부) FYF AGREEMENT - POSSM(PAN OCEAN)_(as of Apr 30 2025) rev2.docx"

doc = Document(word_file)

word_surveys = {}

for table in doc.tables:
    for row in table.rows:
        cells = [cell.text.strip() for cell in row.cells]
        
        # Check if this is a survey row
        if len(cells) >= 3:
            survey_code = cells[0]
            survey_name = cells[1] if len(cells) > 1 else ""
            survey_count = cells[2] if len(cells) > 2 else ""
            
            # Look for specific surveys
            if survey_code in ["DOK", "TPSC", "TSBC"]:
                word_surveys[survey_code] = {
                    "name": survey_name,
                    "count": survey_count
                }
                print(f"  {survey_code}: {survey_name} = {survey_count}")

# 2. Read PDF file (POSSM이 보낸 파일)
print("\n[2] POSSM이 보낸 PDF 파일 읽기...")
pdf_file = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/**2. QG 계약서/POSSM/최종 정리/possm 최종 날인 완료 송부 파일/pdf/POSSM-BV FIVE YEAR FEE AGREEMENT (2025) - POSSM SIGNED, ANNEX B, C 수정.pdf"

pdf_surveys = {}

with open(pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Extract text from all pages
    full_text = ""
    for page in pdf_reader.pages:
        full_text += page.extract_text()
    
    # Find ANNEX C section
    lines = full_text.split('\n')
    
    in_annex_c = False
    for i, line in enumerate(lines):
        if "ANNEX C" in line:
            in_annex_c = True
            print(f"  Found ANNEX C at line {i}")
        
        if in_annex_c:
            # Look for survey lines
            if re.search(r'\bDOK\b', line):
                # Try to extract count
                parts = line.split()
                for j, part in enumerate(parts):
                    if 'DOK' in part and j+1 < len(parts):
                        count_match = re.search(r'\d+', ' '.join(parts[j:]))
                        if count_match:
                            pdf_surveys['DOK'] = count_match.group()
                print(f"  Found DOK line: {line.strip()}")
            
            if re.search(r'\bTPSC\b', line):
                parts = line.split()
                for j, part in enumerate(parts):
                    if 'TPSC' in part and j+1 < len(parts):
                        count_match = re.search(r'\d+', ' '.join(parts[j:]))
                        if count_match:
                            pdf_surveys['TPSC'] = count_match.group()
                print(f"  Found TPSC line: {line.strip()}")
            
            if re.search(r'\bTSBC\b', line):
                parts = line.split()
                for j, part in enumerate(parts):
                    if 'TSBC' in part:
                        # Check if followed by number or dash
                        if '-' in ' '.join(parts[j:j+5]):
                            pdf_surveys['TSBC'] = '-'
                        else:
                            count_match = re.search(r'\d+', ' '.join(parts[j:]))
                            if count_match:
                                pdf_surveys['TSBC'] = count_match.group()
                print(f"  Found TSBC line: {line.strip()}")

# 3. Compare
print("\n" + "="*80)
print("비교 결과")
print("="*80)
print(f"{'검사항목':<10} {'내가 보낸 버전':<20} {'POSSM 최종':<20} {'변경':<20}")
print("-"*80)

for survey in ['DOK', 'TPSC', 'TSBC']:
    word_val = word_surveys.get(survey, {}).get('count', '?')
    pdf_val = pdf_surveys.get(survey, '?')
    
    if word_val == pdf_val:
        change = "변경 없음"
    else:
        change = f"{word_val} → {pdf_val}"
    
    print(f"{survey:<10} {word_val:<20} {pdf_val:<20} {change:<20}")

print("="*80)
