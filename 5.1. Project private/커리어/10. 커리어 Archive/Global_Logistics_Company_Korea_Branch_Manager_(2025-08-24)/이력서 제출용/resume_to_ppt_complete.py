#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
이력서를 PPT로 변환하는 스크립트 - 전체 내용 포함 버전
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_resume_presentation():
    # 새 프레젠테이션 생성
    prs = Presentation()
    
    # 슬라이드 크기를 A4 비율로 설정
    prs.slide_width = Inches(11.69)  # A4 가로
    prs.slide_height = Inches(8.27)  # A4 세로
    
    return prs

def get_colors():
    # 색상 테마 정의 (네이비 블루 계열)
    return {
        'primary': RGBColor(47, 85, 151),      # 네이비 블루
        'secondary': RGBColor(240, 248, 255),   # 연한 블루 그레이
        'text': RGBColor(51, 51, 51),          # 진한 그레이
        'accent': RGBColor(70, 130, 180),      # 스틸 블루
        'white': RGBColor(255, 255, 255)
    }

def add_header(slide, title, colors):
    """공통 헤더 추가"""
    header_shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(1.2)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = colors['primary']
    header_shape.line.fill.background()
    
    header_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(10.5), Inches(0.8))
    header_frame = header_box.text_frame
    header_frame.text = title
    header_p = header_frame.paragraphs[0]
    header_p.font.name = "Arial"
    header_p.font.size = Pt(28)
    header_p.font.bold = True
    header_p.font.color.rgb = colors['white']
    header_p.alignment = PP_ALIGN.CENTER

def add_text_content(slide, content, x, y, width, height, font_size, colors):
    """텍스트 콘텐츠 추가"""
    text_box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(height))
    text_frame = text_box.text_frame
    text_frame.text = content
    text_frame.word_wrap = True
    
    for paragraph in text_frame.paragraphs:
        paragraph.font.name = "Arial"
        paragraph.font.size = Pt(font_size)
        paragraph.font.color.rgb = colors['text']
        paragraph.space_after = Pt(8)

def add_cover_slide(prs, colors):
    """슬라이드 1: 표지"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색 설정
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['secondary']
    
    # 상단 네이비 헤더
    header_shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), 
        Inches(11.69), Inches(2.5)
    )
    header_shape.fill.solid()
    header_shape.fill.fore_color.rgb = colors['primary']
    header_shape.line.fill.background()
    
    # 이름
    name_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(10), Inches(1))
    name_frame = name_box.text_frame
    name_frame.text = "한상진 (HAN SANGJIN)"
    name_p = name_frame.paragraphs[0]
    name_p.font.name = "Arial"
    name_p.font.size = Pt(48)
    name_p.font.bold = True
    name_p.font.color.rgb = colors['white']
    name_p.alignment = PP_ALIGN.CENTER
    
    # 직책/포지션
    position_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(10), Inches(0.8))
    position_frame = position_box.text_frame
    position_frame.text = "글로벌 물류 전문가 | 25년 경력 | Project Logistics Specialist"
    position_p = position_frame.paragraphs[0]
    position_p.font.name = "Arial"
    position_p.font.size = Pt(20)
    position_p.font.color.rgb = colors['white']
    position_p.alignment = PP_ALIGN.CENTER
    
    # 연락처 정보
    contact_info = [
        "📧 frankston@naver.com",
        "📱 010-4167-0528", 
        "📍 경기도 성남시 분당구",
        "🎂 1973년 5월 28일 (52세)",
        "🎖️ 병역: 육군 병장 만기제대 (1995~1997)"
    ]
    
    y_pos = 3.0
    for info in contact_info:
        contact_box = slide.shapes.add_textbox(Inches(1), Inches(y_pos), Inches(9), Inches(0.4))
        contact_frame = contact_box.text_frame
        contact_frame.text = info
        contact_p = contact_frame.paragraphs[0]
        contact_p.font.name = "Arial"
        contact_p.font.size = Pt(16)
        contact_p.font.color.rgb = colors['text']
        contact_p.alignment = PP_ALIGN.CENTER
        y_pos += 0.5

def add_summary_slide(prs, colors):
    """슬라이드 2: 요약"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # 배경색
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "PROFESSIONAL SUMMARY", colors)
    
    summary_text = """25년 글로벌 물류 전문가로서 검증된 성장 실적과 독창적 네트워크 자산을 보유한 전략적 리더입니다.

한진해운에서 미주·구주 판매, 미주·아주·중동 마케팅 프라이싱, 동유럽 지역 전문가 등 글로벌 물류 전 영역을 경험하며 중동 항로 시장점유율 1위 달성, 이란 제재 상황에서 주간 100만불+ 영업이익 창출로 산업통상자원부 장관상을 수상했으며, 현업에서 고객의 선박수를 17척에서 100척+로 성장시켜 700% 증가를 달성했습니다.

중동 주요 기업 고위층, 왕족·정부 고위층 및 EPC 대기업 임원진과의 네트워크를 구축하여 독점적 경쟁우위를 확보했습니다. 특히 Sharaf Group, Globe Marine Group과의 전략적 파트너십과 현대스틸산업(현대엔지니어링 자회사), 삼성중공업(삼성 E&C 그룹사), 두산에너빌리티와의 진행되고 있는 협업 관계는 즉시 비즈니스로 연결 가능한 실질적 자산입니다.

WR Group의 Project Logistics 전문성에 부합하는 역량을 보유했습니다. 현업에서 TIC(Testing, Inspection, Certification) 업계 전반의 경험을 쌓았고, 한진해운 재직 당시 유럽 내부 intermodal service를 직접 이용하며 슬로바키아·체코 근무를 통해 현장 체험을 축적했으며, TIC 업계에서의 폭넓은 경험을 바탕으로 EPC 프로젝트 현장에서 요구되는 각종 인증 및 검사 기준에 부합하는 전문적인 프로젝트 물류 서비스를 제공할 수 있습니다."""

    add_text_content(slide, summary_text, 0.5, 1.5, 10.5, 6, 14, colors)

def add_current_experience_slide(prs, colors):
    """슬라이드 3: 현재 경력 - Bureau Veritas"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "CURRENT POSITION - Bureau Veritas", colors)
    
    experience_text = """Bureau Veritas 한국지점 | Marine & Offshore 마케팅·영업 이사
2017 ~ 현재

선박, 해양구조물 및 EPC 프로젝트 관련, 검사 서비스 이용 고객 확보 위한 마케팅 및 영업

핵심 성과:
• 한국 고객 BV 선급 이용 선박수를 17척 → 100척+ 달성 (700% 성장)
• 2022년 카타르가스, 페트로나스 프로젝트 최초 수주 (회사 창립 이래 처음으로 계약)
• 국내 조선 Big 3 및 부산 선박 소유주들과 전략적 관계 구축

물류 사업 연관성:
• 중동·유럽·아시아 대형 EPC 프로젝트 현장에 대한 깊은 이해
• 해양구조물, 프로젝트 화물의 안전성 및 규제 준수 관련 전문 네트워크 보유
• Bureau Veritas Industry, Certification, Commodities 부문과의 협력 경험

TIC 업계 전반 경험으로 EPC 프로젝트 현장에서 요구되는 각종 인증 및 검사 기준에 부합하는 전문적인 프로젝트 물류 서비스 제공 가능"""

    add_text_content(slide, experience_text, 0.5, 1.5, 10.5, 6, 14, colors)

def add_hanjin_overview_slide(prs, colors):
    """슬라이드 4: 한진해운 개요"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "HANJIN SHIPPING EXPERIENCE OVERVIEW (2000-2016)", colors)
    
    experience_text = """한진해운 | 차장~부장 (2000 ~ 2016)
글로벌 물류 전 영역 경험 - 16년간 체계적 성장

주요 담당 영역:
• 미주·구주 판매 (현장 영업)
• 미주·아주·중동 마케팅 프라이싱 (전략 기획)
• 동유럽 지역 전문가 (시장 개척)
• 벌크 사업 전략 (사업 개발)
• 글로벌 항로 운영 (P&L 관리)

글로벌 근무 경험:
• UAE 지점 부지점장 (2011-2012): 중동 10개국 총괄
• 슬로바키아·체코 지역 전문가 (2004): 동유럽 신규 시장 개척
• 본사 전략팀 - 벌크/컨테이너 사업 기획

핵심 성과:
• 아시아-중동 항로 시장점유율 1위 달성
• 이란 제재 상황에서 주간 100만불+ 영업이익 창출
• 2015년 무역안보 부문 산업통상자원부 장관상 수상
• 제로베이스에서 부산 신규 고객 발굴 및 시장 창출"""

    add_text_content(slide, experience_text, 0.5, 1.5, 10.5, 6, 14, colors)

def add_hanjin_detail1_slide(prs, colors):
    """슬라이드 5: 한진해운 상세 경력 1 (아주마케팅팀)"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "HANJIN SHIPPING - 아주마케팅팀 (2012-2016)", colors)
    
    experience_text = """차장~부장, 아주마케팅팀 | 2012 ~ 2016
컨테이너선 영업본부 - 중동·홍해 항로 총괄

주요 성과:
• 아시아-중동 항로 시장점유율 1위 달성
• 이란 제재 상황에서 주간 100만불+ 영업이익 창출
• IRA(중동선사협의체), IRSA(홍해선사협의체) 회사 대표
• 2015년 무역안보 부문 산업통상자원부 장관상 수상

업무 내용:
• 중동·홍해 항로 전체 수익성 관리 및 전략 수립
• 이란 제재 관련 한국 정부기관 및 미국 국무부, OFAC와 협력하여 전략물자 관리
• 복잡한 중동 정치상황에서 한국 무역업체들의 수출 지원
• 선사협의체 대표로서 업계 전체 정책 방향 설정 참여

특별 성과 - 위기관리 역량:
이란 제재라는 극한 상황에서도 관계 당국의 허가를 득하여 한국 기업들의 정상적인 무역 활동을 지원하며, 
동시에 회사 수익성을 극대화하여 산업통상자원부로부터 무역안보 기여 공로를 인정받음"""

    add_text_content(slide, experience_text, 0.5, 1.5, 10.5, 6, 14, colors)

def add_hanjin_detail2_slide(prs, colors):
    """슬라이드 6: 한진해운 상세 경력 2 (UAE 지점)"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "HANJIN SHIPPING - UAE 지점 부지점장 (2011-2012)", colors)
    
    experience_text = """UAE 지점 부지점장 | 2011 ~ 2012
중동 10개국 총괄

주요 성과:
• 중동·홍해 10개국 대상 통합 마케팅 전략 개발 및 실행
• Sharaf Group, Globe Marine Group과 대리점 계약 체결 (현재까지 지속)
• 아부다비 바라카 원전 프로젝트 화물 운송 참여
• SABIC, Qatar Chemical, Dubai Aluminum 등 메가 발주처 직접 계약

중동 시장 전문성 확보:
• 중동 왕족·정부 고위층·주요 기업 CEO 통합 네트워크 구축
• EPC 프로젝트 현지 특성, 문화, 의사결정 구조에 대한 깊은 이해
• 복잡한 중동 비즈니스 환경에서 검증된 성과 창출 능력

핵심 파트너십:
• Sharaf Group: 해운·물류·에너지 포트폴리오 보유, EPC 관리회사와 장기 협력
• Globe Marine Group: 해양 사업 전문 그룹, 독점적 협력 관계
• 중동 주요 석유화학 기업들과의 직접 계약 체결 경험

현재까지 지속되는 네트워크:
UAE 근무 중 구축한 관계들이 현재 Bureau Veritas 업무와 향후 WR Group 사업에 
직접적으로 활용 가능한 전략적 자산으로 작용"""

    add_text_content(slide, experience_text, 0.5, 1.5, 10.5, 6, 14, colors)

def add_hanjin_detail3_slide(prs, colors):
    """슬라이드 7: 한진해운 상세 경력 3 (미주마케팅팀)"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "HANJIN SHIPPING - 미주마케팅팀 & 기타 경력 (2004-2011)", colors)
    
    experience_text = """차장, 미주마케팅팀 | 2007 ~ 2011
아시아↔미주 항로 총괄

• 아시아↔미주 항로 서비스 수립, 선박 투입, 지역본부 손익(P&L) 관리
• 현장 판매직원용 복합운송 루트 운임 확인 가이드라인 및 툴 제작·배포
• 복합운송 루트 설계 및 멀티모달 서비스 최적화

대리, 동북아 지역 본부 마케팅팀 | 2004 ~ 2006
• 한국·일본·대만발 미주·아시아향 마케팅 및 정책 영업관리
• Service Route별 수익·비용 분석을 통한 운임 전략 수립
• 수익 모델 기반 사업계획 수립 및 산하 점소 목표 달성 관리
• 한국발 주요 화주 관리 및 Service Contract 체결

지역 전문가, 슬로바키아·체코 | 2004
• 동유럽 신규 EU 가입국 시장 환경, 사업성 분석 및 내륙 운송 네트워크 심층 분석
• 유럽 내륙 물류 인프라 및 철도 운송 시스템 현장 조사 및 본사 보고
• 삼성전자 갈란타, 기아자동차 질리나 등 슬로바키아 주요 제조업 고객 관리
• 동유럽-중앙아시아 연결 복합운송 루트 이해
• 유럽 비즈니스 문화 및 본사-현지법인 협력 시스템 이해

대리, 본사 벌크 전략팀 | 2003 ~ 2004
• 벌크 사업 전략 기획 및 시장 개척
• 리서치 자료 분석을 통한 중장기 전략 수립 지원 및 주요 화주 대상 사업 전략 구축"""

    add_text_content(slide, experience_text, 0.5, 1.5, 10.5, 6, 13, colors)

def add_hanjin_detail4_slide(prs, colors):
    """슬라이드 8: 한진해운 상세 경력 4 (부산판매지점)"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "HANJIN SHIPPING - 부산판매지점 (2000-2003)", colors)
    
    experience_text = """사원, 부산판매지점 | 2000 ~ 2003
현장 영업의 기초 확립

핵심 성과:
• 제로 고객기반에서 체계적 발굴을 통한 신규 시장 창출
• 부산 녹산공단, 신평공단, 창원공단 직접 방문 영업으로 EPC 관련 제조업체 발굴

주요 발굴 고객:
• Humax (settop box) - 미주향 전자제품 수출
• 태창산업 (textile) - 섬유제품 글로벌 수출
• Saint Gobain Vetrotex - 프랑스 글로벌 기업 한국 법인
• 쌍용선재 (wire rope) - 해양·건설용 특수 케이블
• 효성전기 (Delphi 협력사) - 자동차 부품 수출

영업 방식 및 성과:
• 산업단지별 체계적 방문 영업으로 신규 화주 지속 발굴
• 복합운송 서비스 제안을 통한 고객 맞춤형 물류 솔루션 제공
• 장기 Service Contract 체결로 안정적 물량 확보

현장 경험의 가치:
이 시기 축적한 현장 영업 경험은 현재까지도 고객 니즈 파악과 
신규 시장 개척에 핵심적인 역량으로 작용하고 있으며,
WR Group에서도 제로베이스 시장 개척에 직접 활용 가능한 실무 경험임"""

    add_text_content(slide, experience_text, 0.5, 1.5, 10.5, 6, 14, colors)

def add_education_slide(prs, colors):
    """슬라이드 9: 학력 및 해외경험"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "EDUCATION & INTERNATIONAL EXPERIENCE", colors)
    
    education_text = """EDUCATION

한국해양대학교 | 해양금융학 MBA
2018.03 ~ 2020.03
• 해운·물류 산업 특화 MBA 과정
• 글로벌 해운 금융 및 물류 전략 심화 학습

부산대학교 | 언어학과 학사
1994.03 ~ 2000.02
• 언어학 전공을 통한 글로벌 커뮤니케이션 역량 기반 구축

해외근무 및 다국가 협업 경험:

2011 ~ 2012: 두바이, UAE (한진해운 부지점장 - 중동 10개국 총괄)
• 중동 현지 비즈니스 문화 및 의사결정 구조 깊이 이해
• 아랍 왕족, 정부 고위층, 기업 CEO들과의 직접 네트워킹
• 다국적 팀 관리 및 현지 직원들과의 협업 경험

2004: 브라티슬라바, 슬로바키아 & 프라하, 체코 (지역 전문가)
• 동유럽 신규 EU 가입국 시장 분석 및 비즈니스 기회 발굴
• 유럽 내륙 물류 시스템 및 철도 네트워크 현장 연구
• 유럽 비즈니스 문화 이해 및 본사-현지법인 협력 시스템 경험

1999 ~ 2000: 멜버른, 호주 (어학연수)
• 영어 실력 향상 및 서구 문화 이해도 제고
• 다문화 환경에서의 적응력 및 글로벌 마인드 함양"""

    add_text_content(slide, education_text, 0.5, 1.5, 10.5, 6, 13, colors)

def add_skills_slide(prs, colors):
    """슬라이드 10: 기술 및 어학 능력"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "TECHNICAL SKILLS & LANGUAGES", colors)
    
    skills_text = """TECHNICAL SKILLS

글로벌 물류 전문성:
• Project Logistics (EPC 프로젝트 특화)
• 복합운송 루트 설계 및 멀티모달 서비스 최적화
• 국제 해상·항공·육상 운송 통합 관리
• 위험물 및 특수화물 운송 전문성

사업 관리 역량:
• 손익(P&L) 관리 및 수익성 분석
• 전략적 네트워크 구축 및 파트너십 관리
• 위기 관리 및 국제 규제 대응
• ESG 규제 대응 및 친환경 물류 전략

IT 및 시스템 활용:
• IBM CRM, Salesforce 활용 경험
• Tableau를 활용한 데이터 분석 및 시각화
• Excel 고급 기능 활용한 재무 분석

LANGUAGES

영어: Business Level
• 비즈니스 회화 수준으로 현 직장에서 영어로 업무 수행
• 글로벌 본사 및 해외 지사와의 원활한 커뮤니케이션
• 영문 보고서 작성 및 프레젠테이션 능력

독일어: 기초회화 및 읽기 가능
• 고교 시절 제2외국어로 학습, 대학 시절 교양 언어로 심화 학습
• 현재는 기초 수준이나, 복습을 통해 단기간 내 기초회화·읽기 수준으로 회복 가능
• WR Group 독일 본사와의 커뮤니케이션에 활용 가능성

CERTIFICATIONS & AWARDS

자격증:
• 1종보통운전면허

수상 경력:
• 2015년 무역안보의 날 수출장려부문 산업통상자원부 장관상
  (이란 제재 기간 중 한국 무역 안보에 대한 탁월한 기여 인정)"""

    add_text_content(slide, skills_text, 0.5, 1.5, 10.5, 6, 12, colors)

def add_network1_slide(prs, colors):
    """슬라이드 11: 전략적 네트워크 1 - 중동"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "STRATEGIC NETWORK 1 - 중동 현지화 네트워크", colors)
    
    network_text = """중동 현지화 네트워크

한국 EPC 기업 프로젝트의 50% 이상이 중동에서 진행되어, 현지 FOB 영업이 핵심적 중요성을 갖습니다. 
정부 고위층-왕족-주요 기업 CEO를 아우르는 통합 네트워크로 현지 영향력을 확보했습니다.

핵심 비즈니스 파트너:

Sharaf Group 회장 Ibrahim Sharaf
• 해운·물류·에너지 포트폴리오 보유
• EPC 관리회사와 장기 협력 관계
• 중동 전역 물류 네트워크 소유

Globe Marine Group 회장 Ehsan F. Abdul Jawad
• 해양 사업 전문 그룹
• 중동 주요 항만 터미널 운영권 보유
• 해양 플랜트 물류 특화 서비스

Gulftainer CEO Peter Verheijen
• 독점적 운임 및 선복 확보 위한 MOU 체결
• 중동 최대 컨테이너 터미널 운영사

GSI Logistics(UAE) 대표 KS Kim
• UAE 1호 포워더
• 한국계 물류 기업으로 현지 특화 서비스 제공

왕족 및 정부 고위층:

UAE:
• Sheikh Ahmed Al Maktoum (왕족) - 두바이 항공 및 해운 정책 결정권자
• Ahmed Bin Sulayem (DMCC 회장) - 두바이 정부 핵심 인사

쿠웨이트:
• Sheikha Mariyam Al Sabah (왕족) - 쿠웨이트 경제정책 자문
• Ahmed Al Mesafir (정부 인사) - 쿠웨이트 물류 정책 담당

이러한 네트워크는 WR Group의 중동 진출 시 즉시 활용 가능한 전략적 자산입니다."""

    add_text_content(slide, network_text, 0.5, 1.5, 10.5, 6, 12, colors)

def add_network2_slide(prs, colors):
    """슬라이드 12: 전략적 네트워크 2 - 한국 EPC"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "STRATEGIC NETWORK 2 - 한국 EPC 및 조선·해양플랜트", colors)
    
    network_text = """한국 EPC 및 조선·해양플랜트 네트워크

대형 EPC 기업:

현대엔지니어링 그룹
• 현대스틸산업 파트너십을 통한 현대엔지니어링의 사우디 아람코 아미랄 석유화학(110억 달러) 관련 물류 화물 확보
• 현재 진행 중인 비즈니스 관계로 즉시 연결 가능

삼성엔지니어링
• 삼성중공업과 CCS 프로젝트 파트너십을 통해 계열사인 삼성엔지니어링 물량 확보
• 글로벌 EPC 프로젝트 물류 서비스 제공 기회

두산에너빌리티
• 현 직장 타 부서가 진행하는 힝클리포인트 C 원전, SMR 개발 관련하여 두산에너빌리티 물류 화물 확보
• 원전 및 발전설비 특수 운송 전문성 활용

동아건설산업
• 과거 리비아 대수로 프로젝트(104억달러) 진행한 건설사
• 현재 SM그룹 산하, SM 그룹 CEO들과의 네트워크로 동아건설 프로젝트 화물 확보

조선·해양플랜트:

HD현대중공업
• 해양플랜트 40년 이상의 경험으로 카타르 해상유전 EPC 프로젝트 등 다수 프로젝트 진행 중
• 현재 임원들과의 네트워크로 물류 화물 확보

삼성중공업
• CCS 파트너, 27만톤급 LNG 운반선 개발
• 현재 임원들과의 네트워크로 물류 화물 확보

한화오션
• 27만톤급 LNG 운반선 공동개발
• 현재 임원들과의 네트워크로 물류 화물 확보

신재생에너지:
현재 진행 중인 해상풍력 프로젝트 참여사들의 물류 화물 확보
• 안마해상풍력 532MW (SK에코플랜트, 대한전선, LS마린솔루션)
• Gray Whale 3 해상풍력 500MW (BadaEnergy, TotalEnergies, 현대중공업)
• LG에너지솔루션: 본사물류팀장인 후배를 통해, 폴란드 ESS, 미국 텍사스 ESS 프로젝트 물류 서비스 제공"""

    add_text_content(slide, network_text, 0.5, 1.5, 10.5, 6, 11, colors)

def add_network3_slide(prs, colors):
    """슬라이드 13: 전략적 네트워크 3 - 해운사 및 물류"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "STRATEGIC NETWORK 3 - 해운사 및 물류 네트워크", colors)
    
    network_text = """국내외 해운사 통합 네트워크를 통한 NVO Pricing 역량

국내 해운사 고위 경영진 네트워크 → 경쟁력 있는 운임 및 선복 확보:
• HMM(총괄부사장), SM상선(대표, 부산지점장), 장금상선(회장), SK해운(대표), 폴라리스쉬핑(회장) 등 주요 해운사 고위 경영진과의 네트워크를 통해 최적 운임 확보 및 신속한 시장 대응이 가능합니다.
• 선주협회(상무)를 통한 협력 기반도 구축되어 있습니다.

글로벌 해운사 네트워크 → 경쟁력 있는 운임 및 선복 확보:
• PIL, Sea-Lead, Emirates Shipping, X-Press Feeder, ONE 등 해외 해운사 고위층
• CMA CGM, COSCO, HPL, MSC 등 글로벌 주요 해운사 대표로 선사협의체에 참석한 경험을 통해 국제 경쟁력을 확보했습니다.

멀티모달 및 특수화물 네트워크:

종합 물류 서비스 기반:
• 대한항공(화물영업부), 부산신항만 터미널, 스페인 알제시라스 터미널, CAI Korea, 부산항만공사, 신한관세법인 등과 협력하여 항공·해운·육상·통관·금융 종합 서비스 기반을 구축했습니다.

HMM 특수화물팀:
• 2025년 약 20만 TEU 처리(2007년 4만 TEU 대비 5배 성장)하는 팀으로, 운임 및 선복 배정 핵심 담당자들과의 네트워크
• 최근 영국발 한국향 선박 운송에서 10만불 운임 절감 성공

현대글로비스:
• 프로젝트 물류, 설비 물류, 벌크 물류 협력

주요 화주 네트워크:
• LG 에너지솔루션, 포스코인터네셔널, SK 가스, SK E&S, SABIC 울산공장, ACE E&T 울산공장, UNION 부산공장, 삼성전기, 삼성전자 가전사업부, 태창산업, NGU Group, HUMAX, 쌍용선재 등과 지속적인 관계를 유지하고 있습니다."""

    add_text_content(slide, network_text, 0.5, 1.5, 10.5, 6, 11, colors)

def add_network4_slide(prs, colors):
    """슬라이드 14: 전략적 네트워크 4 - MRO 및 통합 서비스"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "STRATEGIC NETWORK 4 - MRO 및 검사·인증 통합 서비스", colors)
    
    network_text = """MRO 및 검사·인증 통합 서비스 네트워크

MRO 전문 네트워크:

수리조선소:
• Yeosu Ocean, Union Shipyard (한-미 MRO 물류)
• 선박 수리 및 개조 관련 특수 부품 운송

에너지·플랜트:
• 두산중공업, 삼성중공업, 현대중공업 유지보수 부품
• 발전소, 해양플랜트 정기 점검 및 긴급 수리 부품 공급

석유화학:
• SK에너지, LG화학, 한화토탈 MRO 자재
• 화학 플랜트 정비용 특수 장비 및 부품

항공·국방:
• 대한항공, KAI, 한화에어로스페이스 정비부품
• 항공기 엔진 및 항공우주 부품 정밀 운송

검사·인증 고객군 연계 물류 서비스 확장:

선급 서비스 연계:
선급 서비스는 해상 운송 안전성 검증, 해양플랜트 설계 검토, 대형 장비 운송 검증 등 프로젝트 화물 운송과 밀접히 관련이 있습니다.

Bureau Veritas 부문별 협력:
• Industry(위험관리), Certification(ISO 인증), Commodities(품질검사), GSIT(통관·규제) 부문과의 협력을 통해 다양한 검사 및 인증 고객군들로부터 물류 서비스 고객을 확보할 수 있습니다.

현재 진행 중인 글로벌 EPC 프로젝트:
• 이라크 Kuwait Energy 130만 유로
• 카타르 에너지 300만 유로
• 사우디 왕실 250만 유로
위 프로젝트들과 연계한 물류 비즈니스 확장이 가능합니다.

중앙아시아 네트워크:
Kazakhstan의 Kashagan 유전 개발 프로젝트 및 Tengiz 유전 확장 프로젝트와 연관된 네트워크와 유럽 GSIT 네트워크(Siemens AG, Shell plc, Ørsted)를 활용한 한-카자흐스탄 철도 루트 개발을 통해 중국 경유 대안을 제시하여 검사+인증+물류 통합 서비스의 글로벌 확장을 실현할 수 있습니다."""

    add_text_content(slide, network_text, 0.5, 1.5, 10.5, 6, 11, colors)

def add_business_plan1_slide(prs, colors):
    """슬라이드 15: 사업계획 Phase 1"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "사업계획 PHASE 1 (1차년도) - 기존 네트워크 활용", colors)
    
    plan_text = """Phase 1 (1차년도): 기존 네트워크 활용한 즉시 실행

확정적 프로젝트 파이프라인:

현대스틸산업 중동 프로젝트 확대:
• 사우디 아람코 아미랄 석유화학 콤플렉스 물류 서비스 (110억 달러 규모)
• 현재 진행 중인 비즈니스 관계 기반 단계적 확장
• 강관, 장재, 플레이트 등 철강제품 전문 물류 서비스

Qatar Gas & Petronas EPC 메가 프로젝트:
• Qatar Gas 북부가스전 남부 프로젝트 (100억 달러 EPC) 물류 참여
• Petronas 말레이시아, 캐나다 프로젝트 연계
• 기존 중동 네트워크와 Bureau Veritas 관계 동시 활용

조선·해양플랜트 통합 물류:
• 안마해상풍력 532MW 프로젝트 참여사들과 협업 (SK에코플랜트, 대한전선)
• HD현대중공업 카타르 해상유전 EPCI 프로젝트 연계
• 해상풍력·해양플랜트 특수장비 운송 서비스
• MRO 비즈니스 관련 물류 비즈니스 참여로 한국-미국간 물류 비즈니스 공급 목표

LG에너지솔루션 ESS 프로젝트 물류:
• 폴란드 PGE 981MWh 그리드 스케일 ESS 프로젝트 (2026-2027): 배터리 시스템 설계, 조달, 시공(EPC) 일괄 수행 방식 물류 지원
• 미국 텍사스주 에너지저장장치(ESS) 프로젝트: 번스 앤 맥도넬 EPC 업무와 연계한 배터리 공급 물류
• 북미 3공장 36GWh 생산 설비 관련 기자재 및 완제품 운송
• 본사 물류팀장인 후배를 통한 직접 협력으로 참여 용이성 확보

1차년도 목표:
• 매출액: 500억원 (독일 본사 목표 대비 200% 달성)
• 핵심 고객: 15개사 확보 (EPC 대기업 5개사 + 조선 3개사 + 중동 현지 7개사)
• 차별화 서비스: 멀티모달·ESG 친환경 물류 플랫폼 구축 완료"""

    add_text_content(slide, plan_text, 0.5, 1.5, 10.5, 6, 12, colors)

def add_business_plan2_slide(prs, colors):
    """슬라이드 16: 사업계획 Phase 2-3"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "사업계획 PHASE 2-3 (2-3차년도) - 아시아 전략 거점", colors)
    
    plan_text = """Phase 2 (2-3차년도): 아시아 전략 거점 완성

혁신적 서비스 플랫폼 구축:

ESG 기반 친환경 물류 생태계:
• 독일 본사 철도 네트워크와 연계한 CO2 배출량 30% 감축 멀티모달 서비스
• 해상풍력·태양광 등 신재생에너지 프로젝트 특화 물류 시스템

신규 시장 개척:
• Bureau Veritas Kazakhstan 네트워크 활용한 에너지·광업 프로젝트
• 한국-카자흐스탄 복합운송 루트 상용화
• 우즈베키스탄, 투르크메니스탄 천연가스 개발 프로젝트 물류

MRO 전문 물류 사업:
• 기존 고객사(두산에너빌리티, LG에너지솔루션 등) 유지보수 부품 특화 물류
• 해양플랜트·발전소 예방정비 및 긴급 수리 부품 공급망 구축
• 항공·우주 산업 정밀 부품 물류 서비스 확장

2-3차년도 목표:
• 2차년도 매출액: 900억원 (아시아 지역 거점 완성)
• 3차년도 매출액: 1,500억원 (아시아 최고 수준 EPC 물류 기업)
• 지역 확장: 베트남·태국·인도네시아 거점 설립으로 동남아시아 진출

한국지사를 아시아 전략 허브로 발전:

독일 본사와의 완벽한 시너지:
• 유럽 비즈니스 문화 이해 + 본사-현지법인 협력 시스템 경험
• 독일 철도 네트워크와 아시아-중동 해상 루트의 멀티모달 연결

WR Group 글로벌 성장 견인:
• 아시아 EPC 시장 선점을 통한 유럽-중동-아시아 삼각 네트워크 완성
• 한국 기술력(조선·원전·석유화학)과 독일 물류 혁신의 시너지
• 중국 의존도 감축을 원하는 글로벌 기업들의 대안 공급망 역할"""

    add_text_content(slide, plan_text, 0.5, 1.5, 10.5, 6, 12, colors)

def add_vision_slide(prs, colors):
    """슬라이드 17: 장기 비전 및 결론"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = colors['white']
    
    add_header(slide, "장기 비전 & WR GROUP과 함께 창조할 미래", colors)
    
    vision_text = """장기 비전: Global EPC Logistics Leader

5년 후 목표:
• 매출 3,000억원: 아시아 EPC 물류 시장 점유율 1위
• 지역 확장: 동남아시아·인도·호주까지 아우르는 아시아-태평양 네트워크

WR Group 글로벌 전략에서 한국지사의 역할:
• 서구 선진 물류 기술과 아시아 역동적 성장의 융합
• 차세대 글로벌 물류 표준 창조를 통한 업계 선도 기업으로 도약

지원동기 및 포부:

25년간 글로벌 물류 업계에서 쌓아온 경험은 단순한 경력이 아닌, WR Group 한국지사 성공을 위한 전략적 자산입니다. 한진해운에서 시작하여 Bureau Veritas까지, 매 순간 새로운 도전과 혁신을 통해 검증된 성과를 창출해왔습니다.

부산 녹산공단을 직접 뛰며 제로베이스에서 고객을 발굴했던 신입사원 시절의 현장 영업 경험부터, 이란 제재라는 극한 상황에서 오히려 주간 100만불 이상의 영업이익을 창출하며 산업통상자원부 장관상을 수상한 위기 관리 역량까지, 어떠한 어려운 상황에서도 창의적 해법을 찾아내는 것이 저의 강점입니다.

특히 중동 고위층부터 한국 대기업 임원진까지 25년간 구축한 네트워크는 상호 신뢰를 바탕으로 한 전략적 파트너십으로, Bureau Veritas에서 17척의 선박을 100척 이상으로 확장시킨 것도 이러한 신뢰관계의 결과입니다.

결론: WR Group과 함께 창조할 미래

25년간의 글로벌 물류 경험과 독점적 네트워크 자산을 바탕으로, WR Group 한국지사를 단순한 현지 법인이 아닌 아시아 전체를 아우르는 전략적 성장 엔진으로 발전시키겠습니다.

저의 중동 왕족·정부·기업 네트워크, 한국 EPC 대기업과의 직접 관계, 현 직장 거래처들과의 네트워크를 통한 글로벌 프로젝트 경험, 그리고 유럽 시장 이해도는 WR Group이 아시아 시장에서 독보적 위치를 확보할 수 있는 완벽한 전략적 자산입니다.

WR Group의 혁신적 비전과 저의 실행 역량이 만나 글로벌 EPC 물류 업계의 새로운 표준을 창조하는 역사적 성과를 함께 이루어내겠습니다."""

    add_text_content(slide, vision_text, 0.5, 1.5, 10.5, 6, 11, colors)

def main():
    # 색상 정의
    colors = get_colors()
    
    # 프레젠테이션 생성
    print("완전한 이력서 PPT 생성 시작...")
    prs = create_resume_presentation()
    
    # 슬라이드들 추가
    print("표지 슬라이드 추가...")
    add_cover_slide(prs, colors)
    
    print("요약 슬라이드 추가...")
    add_summary_slide(prs, colors)
    
    print("현재 경력 슬라이드 추가...")
    add_current_experience_slide(prs, colors)
    
    print("한진해운 경력 슬라이드들 추가...")
    add_hanjin_overview_slide(prs, colors)
    add_hanjin_detail1_slide(prs, colors)
    add_hanjin_detail2_slide(prs, colors)
    add_hanjin_detail3_slide(prs, colors)
    add_hanjin_detail4_slide(prs, colors)
    
    print("학력 및 스킬 슬라이드 추가...")
    add_education_slide(prs, colors)
    add_skills_slide(prs, colors)
    
    print("네트워크 슬라이드들 추가...")
    add_network1_slide(prs, colors)
    add_network2_slide(prs, colors)
    add_network3_slide(prs, colors)
    add_network4_slide(prs, colors)
    
    print("사업계획 슬라이드들 추가...")
    add_business_plan1_slide(prs, colors)
    add_business_plan2_slide(prs, colors)
    
    print("비전 및 결론 슬라이드 추가...")
    add_vision_slide(prs, colors)
    
    # 파일 저장
    output_path = "/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1.1. Project private/job search/Global_Logistics_Company_Korea_Branch_Manager_(2025-08-24)/이력서 제출용/한상진_이력서_WR_Group_Complete.pptx"
    prs.save(output_path)
    
    print(f"\n완전한 이력서 PPT가 성공적으로 생성되었습니다: {output_path}")
    print("\n생성된 슬라이드 (총 17장):")
    print("1. 표지 (개인정보 및 연락처)")
    print("2. 전문가 요약 (25년 경력 핵심 요약)")
    print("3. 현재 경력 (Bureau Veritas 상세)")
    print("4. 한진해운 경력 개요 (2000-2016)")
    print("5. 한진해운 - 아주마케팅팀 (2012-2016)")
    print("6. 한진해운 - UAE 지점장 (2011-2012)")
    print("7. 한진해운 - 미주마케팅 & 기타 (2004-2011)")
    print("8. 한진해운 - 부산판매지점 (2000-2003)")
    print("9. 학력 및 해외경험")
    print("10. 기술 및 어학 능력")
    print("11. 전략적 네트워크 1 - 중동")
    print("12. 전략적 네트워크 2 - 한국 EPC")
    print("13. 전략적 네트워크 3 - 해운사 및 물류")
    print("14. 전략적 네트워크 4 - MRO 및 통합 서비스")
    print("15. 사업계획 Phase 1 (1차년도)")
    print("16. 사업계획 Phase 2-3 (2-3차년도)")
    print("17. 장기 비전 및 결론")

if __name__ == "__main__":
    main()
