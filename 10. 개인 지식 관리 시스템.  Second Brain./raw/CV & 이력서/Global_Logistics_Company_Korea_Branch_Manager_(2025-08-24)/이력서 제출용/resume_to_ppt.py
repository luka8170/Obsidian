#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
이력서를 PPT로 변환하는 스크립트
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_resume_presentation():
    # 새 프레젠테이션 생성
    prs = Presentation()
    
    # 슬라이드 크기를 A4 비율로 설정 (16:9 -> 4:3 비율로 변경)
    prs.slide_width = Inches(11.69)  # A4 가로
    prs.slide_height = Inches(8.27)  # A4 세로
    
    # 색상 테마 정의 (네이비 블루 계열 - 전문적이고 신뢰감 있는 색상)
    primary_color = RGBColor(47, 85, 151)    # 네이비 블루
    secondary_color = RGBColor(240, 248, 255)  # 연한 블루 그레이
    text_color = RGBColor(51, 51, 51)        # 진한 그레이
    accent_color = RGBColor(70, 130, 180)    # 스틸 블루
    
    # 슬라이드 1: 표지
    slide1 = prs.slides.add_slide(prs.slide_layouts[6])  # 빈 레이아웃
    
    # 배경색 설정
    background = slide1.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = secondary_color
    
    # 상단 네이비 헤더
    header_shape = slide1.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(2.5)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    # 이름 (크고 굵게)
    name_box = slide1.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(10), Inches(1))
    name_frame = name_box.text_frame
    name_frame.text = "한상진 (HAN SANGJIN)"
    name_p = name_frame.paragraphs[0]
    name_p.font.name = "Arial"
    name_p.font.size = Pt(48)
    name_p.font.bold = True
    name_p.font.color.rgb = RGBColor(255, 255, 255)
    name_p.alignment = PP_ALIGN.CENTER
    
    # 직책/포지션
    position_box = slide1.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(10), Inches(0.8))
    position_frame = position_box.text_frame
    position_frame.text = "글로벌 물류 전문가 | 25년 경력 | Project Logistics Specialist"
    position_p = position_frame.paragraphs[0]
    position_p.font.name = "Arial"
    position_p.font.size = Pt(20)
    position_p.font.color.rgb = RGBColor(255, 255, 255)
    position_p.alignment = PP_ALIGN.CENTER
    
    # 연락처 정보
    contact_info = [
        "📧 frankston@naver.com",
        "📱 010-4167-0528", 
        "📍 경기도 성남시 분당구",
        "🎂 1973년 5월 28일 (52세)"
    ]
    
    y_pos = 3.0
    for info in contact_info:
        contact_box = slide1.shapes.add_textbox(Inches(1), Inches(y_pos), Inches(9), Inches(0.4))
        contact_frame = contact_box.text_frame
        contact_frame.text = info
        contact_p = contact_frame.paragraphs[0]
        contact_p.font.name = "Arial"
        contact_p.font.size = Pt(16)
        contact_p.font.color.rgb = text_color
        contact_p.alignment = PP_ALIGN.CENTER
        y_pos += 0.5
    
    return prs

def add_summary_slide(prs, primary_color, secondary_color, text_color, accent_color):
    # 슬라이드 2: 요약
    slide2 = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide2.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # 헤더
    header_shape = slide2.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    header_box = slide2.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = "PROFESSIONAL SUMMARY"
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(32)
    header_p.font.bold = True
    header_p.font.color.rgb = RGBColor(255, 255, 255)
    header_p.alignment = PP_ALIGN.CENTER
    
    # 요약 내용
    summary_text = """25년 글로벌 물류 전문가로서 검증된 성장 실적과 독창적 네트워크 자산을 보유한 전략적 리더

핵심 성과:
• 한국 고객 BV 선급 선박수 17척 → 100척+ 달성 (700% 성장)
• 중동 항로 시장점유율 1위 달성 (한진해운 재직시)
• 이란 제재 상황에서 주간 100만불+ 영업이익 창출
• 산업통상자원부 장관상 수상 (2015년)

전문 영역:
• 중동·미주·유럽·아시아 글로벌 시장 전문성
• EPC 프로젝트 물류 (Project Logistics)
• 멀티모달 서비스 및 복합운송
• 위기관리 및 국제 규제 대응"""

    summary_box = slide2.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(10.5), Inches(6))
    summary_frame = summary_box.text_frame
    summary_frame.text = summary_text
    summary_frame.word_wrap = True
    
    for paragraph in summary_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(16)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(12)

def add_experience_slide1(prs, primary_color, secondary_color, text_color, accent_color):
    # 슬라이드 3: 경력사항 1 (Bureau Veritas)
    slide3 = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide3.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # 헤더
    header_shape = slide3.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    header_box = slide3.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = "WORK EXPERIENCE - 현재"
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(32)
    header_p.font.bold = True
    header_p.font.color.rgb = RGBColor(255, 255, 255)
    header_p.alignment = PP_ALIGN.CENTER
    
    # Bureau Veritas 경력
    experience_text = """Bureau Veritas 한국지점 | Marine & Offshore 마케팅·영업 이사
2017 ~ 현재

선박, 해양구조물 및 EPC 프로젝트 관련 검사 서비스 이용 고객 확보 위한 마케팅 및 영업

핵심 성과:
• 한국 고객 BV 선급 이용 선박수를 17척 → 100척+ 달성 (700% 성장)
• 2022년 카타르가스, 페트로나스 프로젝트 최초 수주 (회사 창립 이래 처음)
• 국내 조선 Big 3 및 부산 선박 소유주들과 전략적 관계 구축

물류 사업 연관성:
• 중동·유럽·아시아 대형 EPC 프로젝트 현장에 대한 깊은 이해
• 해양구조물, 프로젝트 화물의 안전성 및 규제 준수 관련 전문 네트워크 보유
• Bureau Veritas Industry, Certification, Commodities 부문과의 협력 경험"""

    experience_box = slide3.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(10.5), Inches(6))
    experience_frame = experience_box.text_frame
    experience_frame.text = experience_text
    experience_frame.word_wrap = True
    
    for paragraph in experience_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(14)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(8)

def add_experience_slide2(prs, primary_color, secondary_color, text_color, accent_color):
    # 슬라이드 4: 경력사항 2 (한진해운 - 주요 성과)
    slide4 = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide4.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # 헤더
    header_shape = slide4.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    header_box = slide4.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = "WORK EXPERIENCE - 한진해운 주요 성과"
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(28)
    header_p.font.bold = True
    header_p.font.color.rgb = RGBColor(255, 255, 255)
    header_p.alignment = PP_ALIGN.CENTER
    
    # 한진해운 주요 성과
    experience_text = """한진해운 | 차장~부장 (2000 ~ 2016)

아주마케팅팀 차장~부장 (2012 ~ 2016)
컨테이너선 영업본부 - 중동·홍해 항로 총괄

주요 성과:
• 아시아-중동 항로 시장점유율 1위 달성
• 이란 제재 상황에서 주간 100만불+ 영업이익 창출
• IRA(중동선사협의체), IRSA(홍해선사협의체) 회사 대표
• 2015년 무역안보 부문 산업통상자원부 장관상 수상

UAE 지점 부지점장 (2011 ~ 2012)
중동 10개국 총괄

• 중동·홍해 10개국 대상 통합 마케팅 전략 개발 및 실행
• Sharaf Group, Globe Marine Group과 대리점 계약 체결 (현재까지 지속)
• 아부다비 바라카 원전 프로젝트 화물 운송 참여
• SABIC, Qatar Chemical, Dubai Aluminum 등 메가 발주처 직접 계약"""

    experience_box = slide4.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(10.5), Inches(6))
    experience_frame = experience_box.text_frame
    experience_frame.text = experience_text
    experience_frame.word_wrap = True
    
    for paragraph in experience_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(14)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(8)

def add_education_skills_slide(prs, primary_color, secondary_color, text_color, accent_color):
    # 슬라이드 5: 학력 및 스킬
    slide5 = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide5.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # 헤더
    header_shape = slide5.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    header_box = slide5.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = "EDUCATION & SKILLS"
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(32)
    header_p.font.bold = True
    header_p.font.color.rgb = RGBColor(255, 255, 255)
    header_p.alignment = PP_ALIGN.CENTER
    
    # 좌측: 학력
    education_box = slide5.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(5.5), Inches(3))
    education_frame = education_box.text_frame
    education_text = """EDUCATION

한국해양대학교
해양금융학 MBA (2018.03 ~ 2020.03)

부산대학교
언어학과 학사 (1994.03 ~ 2000.02)

해외근무 및 다국가 협업 경험:
• 2011~2012: 두바이, UAE (중동 10개국 총괄)
• 2004: 브라티슬라바, 슬로바키아 & 프라하, 체코
• 1999~2000: 멜버른, 호주 (어학연수)"""
    
    education_frame.text = education_text
    education_frame.word_wrap = True
    
    for paragraph in education_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(12)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(8)
    
    # 우측: 스킬 및 자격
    skills_box = slide5.shapes.add_textbox(Inches(6), Inches(1.5), Inches(5.5), Inches(3))
    skills_frame = skills_box.text_frame
    skills_text = """SKILLS & CERTIFICATIONS

Technical Skills:
• 글로벌 물류 전문성
• Project Logistics
• EPC 프로젝트 관리
• 복합운송 루트 설계
• 멀티모달 서비스 최적화
• 손익 관리
• 전략적 네트워크 구축
• 위기 관리
• 국제 규제 대응
• ESG 규제 대응

Languages:
• 영어: Business Level
• 독일어: 기초회화 및 읽기 가능

Certifications:
• 1종보통운전면허"""
    
    skills_frame.text = skills_text
    skills_frame.word_wrap = True
    
    for paragraph in skills_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(12)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(6)

def add_network_slide(prs, primary_color, secondary_color, text_color, accent_color):
    # 슬라이드 6: 전략적 네트워크
    slide6 = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide6.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # 헤더
    header_shape = slide6.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    header_box = slide6.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = "STRATEGIC NETWORK & PARTNERSHIPS"
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(28)
    header_p.font.bold = True
    header_p.font.color.rgb = RGBColor(255, 255, 255)
    header_p.alignment = PP_ALIGN.CENTER
    
    # 네트워크 내용
    network_text = """중동 현지화 네트워크:
• Sharaf Group 회장 Ibrahim Sharaf (해운·물류·에너지 포트폴리오)
• Globe Marine Group 회장 Ehsan F. Abdul Jawad (해양 사업 전문)
• Gulftainer CEO Peter Verheijen (독점적 운임 및 선복 확보 MOU)
• UAE 왕족: Sheikh Ahmed Al Maktoum, Ahmed Bin Sulayem(DMCC 회장)
• 쿠웨이트 왕족: Sheikha Mariyam Al Sabah, Ahmed Al Mesafir

한국 EPC 및 조선·해양플랜트 네트워크:
• 현대엔지니어링 그룹: 현대스틸산업 파트너십 (사우디 아람코 110억달러 프로젝트)
• 삼성엔지니어링: 삼성중공업 CCS 프로젝트 파트너십
• 두산에너빌리티: 힝클리포인트 C 원전, SMR 개발 관련 물류
• HD현대중공업, 삼성중공업, 한화오션: 해양플랜트 및 LNG 운반선 프로젝트

글로벌 해운사 네트워크:
• 국내: HMM(총괄부사장), SM상선(대표), 장금상선(회장), SK해운(대표)
• 해외: PIL, Sea-Lead, Emirates Shipping, CMA CGM, COSCO, ONE"""

    network_box = slide6.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(10.5), Inches(6))
    network_frame = network_box.text_frame
    network_frame.text = network_text
    network_frame.word_wrap = True
    
    for paragraph in network_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(13)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(8)

def add_business_plan_slide(prs, primary_color, secondary_color, text_color, accent_color):
    # 슬라이드 7: 사업계획
    slide7 = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide7.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # 헤더
    header_shape = slide7.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = primary_color
    header_shape.line.fill.background()
    
    header_box = slide7.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = "WR GROUP 한국지사 사업계획"
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(28)
    header_p.font.bold = True
    header_p.font.color.rgb = RGBColor(255, 255, 255)
    header_p.alignment = PP_ALIGN.CENTER
    
    # 사업계획 내용
    plan_text = """Phase 1 (1차년도): 기존 네트워크 활용한 즉시 실행
• 매출액: 500억원 목표
• 현대스틸산업 중동 프로젝트 (사우디 아람코 아미랄 석유화학 110억달러)
• Qatar Gas & Petronas EPC 메가 프로젝트 물류 참여
• LG에너지솔루션 ESS 프로젝트 (폴란드, 미국 텍사스)
• 조선·해양플랜트 통합 물류 (안마해상풍력 532MW)

Phase 2-3 (2-3차년도): 아시아 전략 거점 완성
• 2차년도: 900억원, 3차년도: 1,500억원
• ESG 기반 친환경 물류 생태계 구축
• 신규 시장 개척: 카자흐스탄, 우즈베키스탄, 투르크메니스탄
• MRO 전문 물류 사업 확장
• 베트남·태국·인도네시아 거점 설립

장기 비전 (5년 후):
• 매출 3,000억원: 아시아 EPC 물류 시장 점유율 1위
• 독일 본사 유럽 네트워크 + 아시아·중동 네트워크 결합
• 글로벌 EPC 물류 업계의 새로운 표준 창조"""

    plan_box = slide7.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(10.5), Inches(6))
    plan_frame = plan_box.text_frame
    plan_frame.text = plan_text
    plan_frame.word_wrap = True
    
    for paragraph in plan_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(13)
        paragraph.font.color.rgb = text_color
        paragraph.space_after = Pt(10)

def main():
    # 색상 정의
    primary_color = RGBColor(47, 85, 151)    # 네이비 블루
    secondary_color = RGBColor(240, 248, 255)  # 연한 블루 그레이
    text_color = RGBColor(51, 51, 51)        # 진한 그레이
    accent_color = RGBColor(70, 130, 180)    # 스틸 블루
    
    # 프레젠테이션 생성
    print("이력서 PPT 생성 시작...")
    prs = create_resume_presentation()
    
    # 각 슬라이드 추가
    print("요약 슬라이드 추가...")
    add_summary_slide(prs, primary_color, secondary_color, text_color, accent_color)
    
    print("경력사항 슬라이드 추가...")
    add_experience_slide1(prs, primary_color, secondary_color, text_color, accent_color)
    add_experience_slide2(prs, primary_color, secondary_color, text_color, accent_color)
    
    print("학력 및 스킬 슬라이드 추가...")
    add_education_skills_slide(prs, primary_color, secondary_color, text_color, accent_color)
    
    print("네트워크 슬라이드 추가...")
    add_network_slide(prs, primary_color, secondary_color, text_color, accent_color)
    
    print("사업계획 슬라이드 추가...")
    add_business_plan_slide(prs, primary_color, secondary_color, text_color, accent_color)
    
    # 파일 저장
    output_path = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1.1. Project private/job search/Global_Logistics_Company_Korea_Branch_Manager_(2025-08-24)/이력서 제출용/한상진_이력서_WR_Group_Professional.pptx"
    prs.save(output_path)
    
    print(f"이력서 PPT가 성공적으로 생성되었습니다: {output_path}")
    print("\n생성된 슬라이드:")
    print("1. 표지 (개인정보 및 연락처)")
    print("2. 전문가 요약 (핵심 성과 및 전문 영역)")
    print("3. 현재 경력 (Bureau Veritas)")
    print("4. 이전 경력 (한진해운 주요 성과)")
    print("5. 학력 및 스킬")
    print("6. 전략적 네트워크 및 파트너십")
    print("7. WR Group 한국지사 사업계획")

if __name__ == "__main__":
    main()
