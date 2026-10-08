#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# 파일 경로
input_file = '/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/Sales Target/CD List.md'
output_file = '/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/Sales Target/CD List.md'

# 파일 읽기
print("Reading file...")
df = pd.read_csv(input_file, sep='|', skiprows=2, skipinitialspace=True)
df.columns = df.columns.str.strip()
df = df.iloc[:, 1:-1]  # 양쪽 끝의 빈 컬럼 제거

print(f"Initial rows: {len(df)}")

# 구분선 행 제거 (여러 패턴 체크)
df = df[~df['Commercial Owner'].str.strip().str.contains('^:?-+:?$', regex=True, na=False)]
df = df[df['Ship Name1'].str.strip() != '----------------------']
df = df[~df['Ship Name1'].str.strip().str.contains('^:?-+:?$', regex=True, na=False)]

# No 컬럼이 있으면 제거
if 'No' in df.columns:
    df = df.drop('No', axis=1)

print(f"After cleaning: {len(df)} rows")

# 행 번호 열 추가 (1부터 시작)
df.insert(0, 'No', range(1, len(df) + 1))
print("Row numbers added")

# 마크다운 테이블 형식으로 저장
print("Saving file...")
with open(output_file, 'w', encoding='utf-8') as f:
    # 헤더
    f.write("# CD List\n\n")
    
    # 컬럼 헤더
    f.write("|")
    for col in df.columns:
        f.write(f" {col} |")
    f.write("\n")
    
    # 구분선
    f.write("|")
    for col in df.columns:
        f.write(":-" + "-" * (len(col)-1) + "|")
    f.write("\n")
    
    # 데이터 행
    for _, row in df.iterrows():
        f.write("|")
        for col in df.columns:
            value = str(row[col]) if pd.notna(row[col]) else "nan"
            f.write(f" {value} |")
        f.write("\n")

print(f"File saved: {output_file}")
print("Done!")
