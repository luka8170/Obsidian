#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# 파일 경로
ref_file = '/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/Sales Target/cd list, Oct 2025 1.md'
target_file = '/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/Sales Target/CD List.md'
output_file = '/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/내부 회의 내부 작업/Sales Target/CD List.md'

# 참고 파일 읽기
print("Reading reference file...")
df_ref = pd.read_csv(ref_file, sep='|', skiprows=1, skipinitialspace=True)
df_ref.columns = df_ref.columns.str.strip()
df_ref = df_ref.iloc[:, 1:-1]  # 양쪽 끝의 빈 컬럼 제거
df_ref = df_ref[df_ref['Ship Name1'].str.strip() != '----------------------']
print(f"Reference file: {len(df_ref)} rows")

# 업데이트할 파일 읽기
print("Reading target file...")
df_target = pd.read_csv(target_file, sep='|', skiprows=2, skipinitialspace=True)
df_target.columns = df_target.columns.str.strip()
df_target = df_target.iloc[:, 1:-1]  # 양쪽 끝의 빈 컬럼 제거
df_target = df_target[df_target['Ship Name1'].str.strip() != '----------------------']
print(f"Target file: {len(df_target)} rows")

# Ship Name과 Commercial Owner 매핑 생성
print("Creating mapping...")
owner_mapping = dict(zip(df_ref['Ship Name1'].str.strip(), df_ref['Commercial Owner'].str.strip()))
print(f"Mapping created: {len(owner_mapping)} ships")

# Commercial Owner 업데이트
print("Updating Commercial Owner...")
update_count = 0
for idx, row in df_target.iterrows():
    ship_name = str(row['Ship Name1']).strip()
    if ship_name in owner_mapping:
        new_owner = owner_mapping[ship_name]
        old_owner = str(row['Commercial Owner']).strip()
        if new_owner != old_owner:
            df_target.at[idx, 'Commercial Owner'] = new_owner
            update_count += 1
            print(f"  Updated: {ship_name} | {old_owner} -> {new_owner}")

print(f"\nTotal updates: {update_count}")

# 마크다운 테이블 형식으로 저장
print("Saving updated file...")
with open(output_file, 'w', encoding='utf-8') as f:
    # 헤더
    f.write("# CD List\n\n")
    
    # 컬럼 헤더
    f.write("|")
    for col in df_target.columns:
        f.write(f" {col} |")
    f.write("\n")
    
    # 구분선
    f.write("|")
    for col in df_target.columns:
        f.write(":-" + "-" * (len(col)-1) + "|")
    f.write("\n")
    
    # 데이터 행
    for _, row in df_target.iterrows():
        f.write("|")
        for col in df_target.columns:
            value = str(row[col]) if pd.notna(row[col]) else "nan"
            f.write(f" {value} |")
        f.write("\n")

print(f"File saved: {output_file}")
print("Done!")
