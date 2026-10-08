#!/usr/bin/env python3

from docx import Document
import PyPDF2

print("="*80)
print("Word 파일 상세 분석")
print("="*80)

word_file = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/**2. QG 계약서/POSSM/최종 정리/내가 보낸 파일들/word/25.8.6. 송부) FYF AGREEMENT - POSSM(PAN OCEAN)_(as of Apr 30 2025) rev2.docx"

try:
    doc = Document(word_file)
    
    # Print all paragraphs containing "ANNEX C"
    print("\n[Paragraphs containing 'ANNEX C']")
    for i, para in enumerate(doc.paragraphs):
        if "ANNEX C" in para.text:
            print(f"Paragraph {i}: {para.text[:200]}")
    
    # Print all table contents (first 50 tables)
    print(f"\n[Total tables: {len(doc.tables)}]")
    
    annex_c_found = False
    for table_idx, table in enumerate(doc.tables):
        # Check if this table is in ANNEX C section
        table_text = ""
        for row in table.rows:
            for cell in row.cells:
                table_text += cell.text + " "
        
        if "ANNEX C" in table_text or annex_c_found:
            if "ANNEX C" in table_text:
                annex_c_found = True
                print(f"\n{'='*80}")
                print(f"ANNEX C Table found! (Table {table_idx})")
                print(f"{'='*80}")
            
            print(f"\nTable {table_idx}:")
            for row_idx, row in enumerate(table.rows):
                cells = [cell.text.strip() for cell in row.cells]
                print(f"  Row {row_idx}: {cells}")
                
                # Stop after showing enough rows
                if row_idx > 30:
                    print("  ... (more rows)")
                    break
            
            # Stop after showing a few ANNEX C tables
            if annex_c_found and table_idx > min(len(doc.tables), 45):
                break

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
