#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
카드사 이용내역 통합 스크립트 (Mac용)
작성자: Claude
목적: 신한/현대/하나카드, SRT, 하이패스 데이터 통합
"""

import pandas as pd
import os
from datetime import datetime
import re

# 파일 경로 설정
BASE_PATH = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1. Project/비용 정리"
INPUT_FOLDER = os.path.join(BASE_PATH, "원본파일")
OUTPUT_FILE = os.path.join(BASE_PATH, "통합정산.xlsx")

def clean_amount(amount_str):
    """금액 문자열을 숫자로 변환"""
    if pd.isna(amount_str):
        return 0
    # 콤마 제거 후 숫자 변환
    return int(str(amount_str).replace(',', '').replace(' ', ''))

def standardize_datetime(date_str, time_str=None):
    """날짜시간을 표준 형식으로 변환"""
    try:
        if time_str is None:
            # 날짜에 시간이 포함된 경우
            if ' ' in str(date_str):
                return pd.to_datetime(date_str)
            else:
                return pd.to_datetime(date_str)
        else:
            # 날짜와 시간이 분리된 경우
            datetime_str = f"{date_str} {time_str}"
            return pd.to_datetime(datetime_str)
    except:
        return pd.NaT

def process_shinhan_card():
    """신한카드 데이터 처리"""
    file_path = os.path.join(INPUT_FOLDER, "신한카드.csv")
    
    if not os.path.exists(file_path):
        print(f"신한카드 파일을 찾을 수 없습니다: {file_path}")
        return pd.DataFrame()
    
    try:
        # CSV 읽기 (인코딩 시도)
        encodings = ['utf-8', 'cp949', 'euc-kr']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                break
            except:
                continue
        
        if df is None:
            print("신한카드 파일 인코딩 오류")
            return pd.DataFrame()
        
        # 컬럼 정리
        df['거래일시'] = pd.to_datetime(df['거래일'], errors='coerce')
        df['가맹점명'] = df['가맹점명'].astype(str)
        df['금액'] = df['금액'].apply(clean_amount)
        df['구분'] = df['이용구분'].astype(str)
        df['카드사'] = '신한카드'
        df['원본파일'] = '신한카드'
        
        # 필요한 컬럼만 선택
        result = df[['거래일시', '가맹점명', '금액', '구분', '카드사', '원본파일']].copy()
        print(f"신한카드: {len(result)}건 처리 완료")
        return result
        
    except Exception as e:
        print(f"신한카드 처리 오류: {e}")
        return pd.DataFrame()

def process_hyundai_card():
    """현대카드 데이터 처리"""
    file_path = os.path.join(INPUT_FOLDER, "현대카드.csv")
    
    if not os.path.exists(file_path):
        print(f"현대카드 파일을 찾을 수 없습니다: {file_path}")
        return pd.DataFrame()
    
    try:
        encodings = ['utf-8', 'cp949', 'euc-kr']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                break
            except:
                continue
        
        if df is None:
            print("현대카드 파일 인코딩 오류")
            return pd.DataFrame()
        
        # 날짜 표준화 (2025년 8월 2일 → 2025-08-02)
        def convert_korean_date(date_str):
            try:
                # "2025년 8월 2일" 형식 처리
                date_str = str(date_str)
                date_str = re.sub(r'년\s*', '-', date_str)
                date_str = re.sub(r'월\s*', '-', date_str)
                date_str = re.sub(r'일.*', '', date_str)
                return pd.to_datetime(date_str, errors='coerce')
            except:
                return pd.NaT
        
        df['거래일시'] = df.apply(lambda x: 
            pd.to_datetime(f"{convert_korean_date(x['승인일']).strftime('%Y-%m-%d')} {x['승인시각']}", 
                          errors='coerce'), axis=1)
        
        df['가맹점명'] = df['가맹점명'].astype(str)
        df['금액'] = df['승인금액'].apply(clean_amount)
        df['구분'] = df['이용구분'].astype(str)
        df['카드사'] = '현대카드'
        df['원본파일'] = '현대카드'
        
        result = df[['거래일시', '가맹점명', '금액', '구분', '카드사', '원본파일']].copy()
        print(f"현대카드: {len(result)}건 처리 완료")
        return result
        
    except Exception as e:
        print(f"현대카드 처리 오류: {e}")
        return pd.DataFrame()

def process_hana_card():
    """하나카드 데이터 처리"""
    file_path = os.path.join(INPUT_FOLDER, "하나카드.csv")
    
    if not os.path.exists(file_path):
        print(f"하나카드 파일을 찾을 수 없습니다: {file_path}")
        return pd.DataFrame()
    
    try:
        encodings = ['utf-8', 'cp949', 'euc-kr']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                break
            except:
                continue
        
        if df is None:
            print("하나카드 파일 인코딩 오류")
            return pd.DataFrame()
        
        # 날짜시간 통합 (2025.07.28 + 19:10:31)
        df['거래일시'] = df.apply(lambda x: 
            pd.to_datetime(f"{str(x['이용일']).replace('.', '-')} {str(x['이용시간'])[:5]}", 
                          errors='coerce'), axis=1)
        
        df['가맹점명'] = df['가맹점명'].astype(str)
        df['금액'] = df['승인금액'].apply(clean_amount)
        df['구분'] = df['이용구분'].astype(str)
        df['카드사'] = '하나카드'
        df['원본파일'] = '하나카드'
        
        result = df[['거래일시', '가맹점명', '금액', '구분', '카드사', '원본파일']].copy()
        print(f"하나카드: {len(result)}건 처리 완료")
        return result
        
    except Exception as e:
        print(f"하나카드 처리 오류: {e}")
        return pd.DataFrame()

def process_srt():
    """SRT 데이터 처리"""
    file_path = os.path.join(INPUT_FOLDER, "SRT.csv")
    
    if not os.path.exists(file_path):
        print(f"SRT 파일을 찾을 수 없습니다: {file_path}")
        return pd.DataFrame()
    
    try:
        # 탭 구분자로 읽기
        encodings = ['utf-8', 'cp949', 'euc-kr']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, sep='\t', encoding=encoding)
                break
            except:
                continue
        
        if df is None:
            print("SRT 파일 인코딩 오류")
            return pd.DataFrame()
        
        # 날짜시간 통합
        df['거래일시'] = df.apply(lambda x: 
            pd.to_datetime(f"{x['발매일자']} {str(x['발매시간'])[:5]}", 
                          errors='coerce'), axis=1)
        
        # 가맹점명을 "SRT 출발역→도착역" 형태로 생성
        df['가맹점명'] = df.apply(lambda x: f"SRT {x['출발역']}→{x['도착역']}", axis=1)
        df['금액'] = df['영수금액'].apply(clean_amount)
        df['구분'] = '교통비'
        df['카드사'] = 'SRT'
        df['원본파일'] = 'SRT'
        
        result = df[['거래일시', '가맹점명', '금액', '구분', '카드사', '원본파일']].copy()
        print(f"SRT: {len(result)}건 처리 완료")
        return result
        
    except Exception as e:
        print(f"SRT 처리 오류: {e}")
        return pd.DataFrame()

def process_hipass():
    """하이패스 데이터 처리"""
    file_path = os.path.join(INPUT_FOLDER, "하이패스.csv")
    
    if not os.path.exists(file_path):
        print(f"하이패스 파일을 찾을 수 없습니다: {file_path}")
        return pd.DataFrame()
    
    try:
        encodings = ['utf-8', 'cp949', 'euc-kr']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                break
            except:
                continue
        
        if df is None:
            print("하이패스 파일 인코딩 오류")
            return pd.DataFrame()
        
        # 날짜시간 표준화 (2025/06/06 13:53:29 → 2025-06-06 13:53)
        def convert_hipass_datetime(datetime_str):
            try:
                datetime_str = str(datetime_str)
                # 날짜 부분의 / 를 - 로 변경
                date_part = datetime_str.split(' ')[0].replace('/', '-')
                time_part = datetime_str.split(' ')[1][:5]  # 초 제거
                return pd.to_datetime(f"{date_part} {time_part}", errors='coerce')
            except:
                return pd.NaT
        
        df['거래일시'] = df['거래일시'].apply(convert_hipass_datetime)
        
        # 가맹점명을 "하이패스 입구→출구" 형태로 생성
        df['가맹점명'] = df.apply(lambda x: f"하이패스 {x['입구']}→{x['출구']}", axis=1)
        df['금액'] = df['청구금액'].apply(clean_amount)
        df['구분'] = '교통비'
        df['카드사'] = '하이패스'
        df['원본파일'] = '하이패스'
        
        result = df[['거래일시', '가맹점명', '금액', '구분', '카드사', '원본파일']].copy()
        print(f"하이패스: {len(result)}건 처리 완료")
        return result
        
    except Exception as e:
        print(f"하이패스 처리 오류: {e}")
        return pd.DataFrame()

def auto_categorize(merchant_name, current_category):
    """가맹점명 기반 자동 분류"""
    merchant_name = str(merchant_name).lower()
    
    # 교통비
    if any(keyword in merchant_name for keyword in ['택시', '지하철', '버스', 'srt', '하이패스']):
        return '교통비'
    
    # 식비
    if any(keyword in merchant_name for keyword in ['카페', '커피', '스타벅스', '이디야', '맥도날드', '버거킹', '치킨', '피자']):
        return '식비'
    
    # 유류비
    if any(keyword in merchant_name for keyword in ['주유', 'gs칼텍스', 'sk에너지', '현대오일뱅크']):
        return '유류비'
    
    # 사무용품
    if any(keyword in merchant_name for keyword in ['다이소', '문구', '오피스', '복사']):
        return '사무용품'
    
    # 기존 분류가 있으면 유지
    return current_category

def main():
    """메인 실행 함수"""
    print("=" * 50)
    print("카드사 이용내역 통합 스크립트 시작")
    print("=" * 50)
    
    # 각 카드사 데이터 처리
    all_data = []
    
    processors = [
        ("신한카드", process_shinhan_card),
        ("현대카드", process_hyundai_card), 
        ("하나카드", process_hana_card),
        ("SRT", process_srt),
        ("하이패스", process_hipass)
    ]
    
    for name, processor in processors:
        print(f"\n{name} 처리 중...")
        data = processor()
        if not data.empty:
            all_data.append(data)
    
    if not all_data:
        print("처리할 데이터가 없습니다.")
        return
    
    # 모든 데이터 통합
    print("\n데이터 통합 중...")
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # 날짜순 정렬
    combined_df = combined_df.sort_values('거래일시').reset_index(drop=True)
    
    # 자동 분류 적용
    print("자동 분류 적용 중...")
    combined_df['분류'] = combined_df.apply(
        lambda x: auto_categorize(x['가맹점명'], x['구분']), axis=1
    )
    
    # 월별 집계 추가
    combined_df['년월'] = combined_df['거래일시'].dt.strftime('%Y-%m')
    
    # Excel 파일로 저장
    print(f"\nExcel 파일 저장 중: {OUTPUT_FILE}")
    
    with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
        # 전체 데이터
        combined_df.to_excel(writer, sheet_name='전체내역', index=False)
        
        # 월별 집계
        monthly_summary = combined_df.groupby(['년월', '카드사', '분류'])['금액'].sum().reset_index()
        monthly_summary.to_excel(writer, sheet_name='월별집계', index=False)
        
        # 분류별 집계
        category_summary = combined_df.groupby(['분류', '카드사'])['금액'].sum().reset_index()
        category_summary.to_excel(writer, sheet_name='분류별집계', index=False)
    
    print("=" * 50)
    print("통합 완료!")
    print(f"총 {len(combined_df)}건의 데이터를 처리했습니다.")
    print(f"저장 위치: {OUTPUT_FILE}")
    print("=" * 50)
    
    # 요약 정보 출력
    print("\n📊 카드사별 집계:")
    card_summary = combined_df.groupby('카드사')['금액'].agg(['count', 'sum'])
    for card, data in card_summary.iterrows():
        print(f"  {card}: {data['count']}건, {data['sum']:,}원")
    
    print("\n📊 분류별 집계:")
    category_summary = combined_df.groupby('분류')['금액'].sum().sort_values(ascending=False)
    for category, amount in category_summary.items():
        print(f"  {category}: {amount:,}원")

if __name__ == "__main__":
    main()