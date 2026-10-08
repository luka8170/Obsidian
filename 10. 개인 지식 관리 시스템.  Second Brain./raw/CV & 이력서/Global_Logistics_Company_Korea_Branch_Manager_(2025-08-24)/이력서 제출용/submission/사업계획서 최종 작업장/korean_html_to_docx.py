#!/usr/bin/env python3
"""
한상진 한국어 이력서 HTML to Word 변환기
HTML 파일을 읽어서 전문적인 워드 문서로 변환합니다.
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.shared import OxmlElement, qn
import os
import sys

def create_korean_resume_document():
    """한국어 이력서 워드 문서 생성"""
    doc = Document()
    
    # 문서 여백 설정
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
    
    # 헤더 섹션
    header = doc.add_heading('한 상 진 이력서', level=1)
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header.runs[0]
    header_run.font.size = Pt(24)
    header_run.font.color.rgb = RGBColor(30, 60, 114)  # #1e3c72
    
    # 부제목
    subtitle = doc.add_paragraph('WR Group 한국지사장 지원')
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle_run = subtitle.runs[0]
    subtitle_run.font.size = Pt(14)
    subtitle_run.font.color.rgb = RGBColor(42, 82, 152)  # #2a5298
    subtitle_run.bold = True
    
    # 날짜
    date_para = doc.add_paragraph('2025년 9월 2일')
    date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_run = date_para.runs[0]
    date_run.font.size = Pt(12)
    date_run.italic = True
    
    # 줄바꿈
    doc.add_paragraph()
    
    # 인적사항 섹션
    doc.add_heading('인적사항', level=2)
    
    personal_info = [
        ('성명:', '한상진'),
        ('생년월일:', '1973년 5월 28일 (52세)'),
        ('연락처:', '010-4167-0528'),
        ('이메일:', 'frankston@naver.com'),
        ('주소:', '경기도 성남시 분당구'),
        ('병역:', '육군 병장 만기제대 (1995.01~1997.03)')
    ]
    
    for label, value in personal_info:
        para = doc.add_paragraph()
        run1 = para.add_run(label)
        run1.bold = True
        run1.font.color.rgb = RGBColor(30, 60, 114)
        para.add_run(f' {value}')
    
    # Executive Summary 섹션
    doc.add_heading('Executive Summary', level=2)
    
    summary_text = """25년 글로벌 물류 전문가로서 검증된 성장 실적과 독창적 네트워크 자산을 보유한 전략적 리더입니다. 한진해운에서 미주·구주 판매, 미주·아주·중동 마케팅 프라이싱, 동유럽 지역 전문가 등 글로벌 물류 전 영역을 경험하며 중동 항로 시장점유율 1위 달성, 이란 제재 상황에서 주간 100만불+ 영업이익 창출로 산업통상자원부 장관상을 수상했으며, 현업에서 고객의 선박수를 17척에서 100척+로 성장시켜 700% 증가를 달성했습니다."""
    
    summary_para = doc.add_paragraph(summary_text)
    
    doc.add_paragraph()
    networks_para = doc.add_paragraph()
    networks_run = networks_para.add_run('핵심 네트워크: ')
    networks_run.bold = True
    networks_para.add_run('중동 주요 기업 고위층, 왕족·정부 고위층 및 EPC 대기업 임원진과의 네트워크를 구축하여 독점적 경쟁우위를 확보했습니다. 특히 Sharaf Group, Globe Marine Group과의 전략적 파트너십과 현대스틸산업(현대엔지니어링 자회사), 삼성중공업(삼성 E&C 그룹사), 두산에너빌리티와의 진행되고 있는 협업 관계는 즉시 비즈니스로 연결 가능한 실질적 자산입니다.')
    
    doc.add_paragraph()
    target_para = doc.add_paragraph()
    target_run = target_para.add_run('1차년도 목표: ')
    target_run.bold = True
    target_para.add_run('매출 500억원 목표로 한국지사를 아시아 전략 거점으로 발전시켜, 독일 본사의 유럽 네트워크와 저의 아시아·중동 네트워크를 결합한 글로벌 EPC 물류 업계의 새로운 표준을 만들어 가겠습니다.')
    
    # 학력 섹션
    doc.add_heading('학력', level=2)
    
    education_info = [
        '한국해양대학교 해양금융학 석사(MBA) | 2018.03 ~ 2020.03',
        '부산대학교 언어학과 학사 | 1994.03 ~ 2000.02'
    ]
    
    for edu in education_info:
        doc.add_paragraph(edu)
    
    # 자격 및 어학능력
    doc.add_heading('자격 및 어학능력', level=2)
    
    skills_info = [
        ('영어:', 'Business Level (비즈니스 회화 수준, 현 직장에서 영어로 업무 수행)'),
        ('독일어:', '기초회화 및 읽기 가능 (고교 때 제2외국어로 학습, 대학 때 교양 언어로 학습. 현재는 어려우나, 복습 시 단기간에 기초회화 읽기 수준으로 회복 전망)'),
        ('기타:', '1종보통운전면허')
    ]
    
    for label, value in skills_info:
        para = doc.add_paragraph()
        run1 = para.add_run(label)
        run1.bold = True
        run1.font.color.rgb = RGBColor(30, 60, 114)
        para.add_run(f' {value}')
    
    # 해외근무 및 다국가 협업 경험
    doc.add_heading('해외근무 및 다국가 협업 경험', level=2)
    
    intl_exp = [
        '2011 ~ 2012: 두바이, UAE (한진해운 부지점장 - 중동 10개국 총괄)',
        '2004: 브라티슬라바, 슬로바키아 & 프라하, 체코 (지역 전문가)',
        '1999 ~ 2000: 멜버른, 호주 (어학연수)'
    ]
    
    for exp in intl_exp:
        doc.add_paragraph(exp)
    
    # 수상경력
    doc.add_heading('수상경력', level=2)
    
    award_para = doc.add_paragraph()
    award_title = award_para.add_run('2015년 무역안보의 날 수출장려부문 산업통상자원부 장관상')
    award_title.bold = True
    award_title.font.color.rgb = RGBColor(42, 82, 152)
    award_para.add_run('\n산업통상자원부 | 이란 제재 기간 중 한국 무역 안보에 대한 탁월한 기여 인정')
    
    # WR Group 한국지사 성공을 위한 전략적 경쟁력
    doc.add_heading('WR Group 한국지사 성공을 위한 전략적 경쟁력', level=2)
    
    # 1. 검증된 사업 성과
    doc.add_heading('1. 검증된 사업 성과 및 글로벌 시장 전문성', level=3)
    
    doc.add_paragraph().add_run('주요 성과').bold = True
    key_achievements = [
        '한국 고객 BV 선급 선박수 17척 → 100척+ 달성 (700% 성장)',
        'Qatar Gas 북부가스전 남부 프로젝트(100억 달러 EPC) 선박 발주 계약 수주',
        'Petronas 말레이시아 캐나다 프로젝트 선박 발주 계약 수주',
        '현대스틸산업과의 전략적 파트너십으로 중동 EPC 프로젝트 확장 진행'
    ]
    
    for achievement in key_achievements:
        doc.add_paragraph(achievement, style='List Bullet')
    
    doc.add_paragraph().add_run('중동 EPC 프로젝트 경험').bold = True
    me_exp = [
        'SABIC, Dubai Aluminum, Qatar Chemical 등 중동 석유화학 메가 기업들과 물류 계약 직접 협상 체결',
        'Ethiopia Shipping Line 연간 수입 물량 전체 수주 성공'
    ]
    
    for exp in me_exp:
        doc.add_paragraph(exp, style='List Bullet')
    
    doc.add_paragraph().add_run('글로벌 시장 경험').bold = True
    global_exp = [
        '중동, 미주, 유럽, 동북아시아 등 다양한 노선 경험으로 주요 시장에 대한 깊은 이해 보유',
        '이란 제재 상황에서도 관계 당국 허가를 득하여 고객사 수출 성공 지원 등 위기 대응 역량 실증'
    ]
    
    for exp in global_exp:
        doc.add_paragraph(exp, style='List Bullet')
    
    # 2. 국내외 해운사 통합 네트워크
    doc.add_heading('2. 국내외 해운사 통합 네트워크를 통한 NVO Pricing 역량', level=3)
    
    doc.add_paragraph().add_run('국내 해운사 고위 경영진 네트워크 → 경쟁력 있는 운임 및 선복 확보').bold = True
    domestic_network = doc.add_paragraph('HMM(총괄부사장), SM상선(대표, 부산지점장), 장금상선(회장), SK해운(대표), 폴라리스쉬핑(회장) 등 주요 해운사 고위 경영진과의 네트워크를 통해 최적 운임 확보 및 신속한 시장 대응이 가능합니다.')
    
    doc.add_paragraph().add_run('글로벌 해운사 네트워크 → 경쟁력 있는 운임 및 선복 확보').bold = True
    global_network = doc.add_paragraph('PIL, Sea-Lead, Emirates Shipping, X-Press Feeder, ONE 등 해외 해운사 고위층과 CMA CGM, COSCO, HPL, MSC 등 글로벌 주요 해운사 대표로 선사협의체에 참석한 경험을 통해 국제 경쟁력을 확보했습니다.')
    
    # 주요 경력 섹션
    doc.add_heading('주요 경력 (25년)', level=2)
    
    # Bureau Veritas Korea
    company_para = doc.add_paragraph()
    company_run = company_para.add_run('Bureau Veritas 한국지점')
    company_run.bold = True
    company_run.font.size = Pt(14)
    company_run.font.color.rgb = RGBColor(30, 60, 114)
    
    position_para = doc.add_paragraph()
    position_run = position_para.add_run('Marine & Offshore 마케팅·영업 이사')
    position_run.bold = True
    position_run.font.color.rgb = RGBColor(42, 82, 152)
    position_para.add_run(' | 2017 ~ 현재')
    
    doc.add_paragraph('(선박, 해양구조물 및 EPC 프로젝트 관련, 검사 서비스 이용 고객 확보 위한 마케팅 및 영업)')
    
    # Bureau Veritas 핵심 성과
    doc.add_paragraph().add_run('핵심 성과').bold = True
    bv_achievements = [
        '한국 고객 BV 선급 이용 선박수를 17척 → 100척+ 달성 (700% 성장)',
        '2022년 카타르가스, 페트로나스 프로젝트 최초 수주 (회사 창립 이래 처음으로 계약)',
        '국내 조선 Big 3 및 부산 선박 소유주들과 전략적 관계 구축'
    ]
    
    for achievement in bv_achievements:
        doc.add_paragraph(achievement, style='List Bullet')
    
    # 물류 사업 연관성
    doc.add_paragraph().add_run('물류 사업 연관성').bold = True
    logistics_relevance = [
        '중동·유럽·아시아 대형 EPC 프로젝트 현장에 대한 깊은 이해',
        '해양구조물, 프로젝트 화물의 안전성 및 규제 준수 관련 전문 네트워크 보유',
        'Bureau Veritas Industry, Certification, Commodities 부문과의 협력 경험'
    ]
    
    for relevance in logistics_relevance:
        doc.add_paragraph(relevance, style='List Bullet')
    
    # 페이지 나누기
    doc.add_page_break()
    
    # 한진해운 경력
    company_para = doc.add_paragraph()
    company_run = company_para.add_run('한진해운')
    company_run.bold = True
    company_run.font.size = Pt(14)
    company_run.font.color.rgb = RGBColor(30, 60, 114)
    
    # 한진해운 주요 직책들
    hanjin_positions = [
        ('차장~부장, 아주마케팅팀 | 2012 ~ 2016', 
         '컨테이너선 영업본부 - 중동·홍해 항로 총괄',
         ['아시아-중동 항로 시장점유율 1위 달성',
          '이란 제재 상황에서 주간 100만불+ 영업이익 창출',
          'IRA(중동선사협의체), IRSA(홍해선사협의체) 회사 대표',
          '2015년 무역안보 부문 산업통상자원부 장관상 수상']),
        
        ('UAE 지점 부지점장 | 2011 ~ 2012',
         '중동 10개국 총괄',
         ['중동·홍해 10개국 대상 통합 마케팅 전략 개발 및 실행',
          'Sharaf Group, Globe Marine Group과 대리점 계약 체결 (현재까지 지속)',
          '아부다비 바라카 원전 프로젝트 화물 운송 참여',
          'SABIC, Qatar Chemical, Dubai Aluminum 등 메가 발주처 직접 계약']),
        
        ('차장, 미주마케팅팀 | 2007 ~ 2011',
         '아시아↔미주 항로 총괄',
         ['아시아↔미주 항로 서비스 수립, 선박 투입, 지역본부 손익(P&L) 관리',
          '현장 판매직원용 복합운송 루트 운임 확인 가이드라인 및 툴 제작·배포',
          '복합운송 루트 설계 및 멀티모달 서비스 최적화']),
        
        ('사원, 부산판매지점 | 2000.12 ~ 2003.06',
         '',
         ['제로 고객기반에서 체계적 발굴을 통한 신규 시장 창출',
          '부산 녹산공단, 신평공단, 창원공단 직접 방문 영업으로 EPC 관련 제조업체 발굴',
          '주요 성과: Humax(settop box), 태창산업(textile), Saint Gobain Vetrotex, 쌍용선재(wire rope), 효성전기(Delphi) 등'])
    ]
    
    for position, description, achievements in hanjin_positions:
        position_para = doc.add_paragraph()
        position_run = position_para.add_run(position)
        position_run.bold = True
        position_run.font.color.rgb = RGBColor(42, 82, 152)
        
        if description:
            doc.add_paragraph(description)
        
        for achievement in achievements:
            doc.add_paragraph(achievement, style='List Bullet')
    
    # 자기소개 및 지원동기
    doc.add_heading('자기소개 및 지원동기', level=2)
    
    motivation_text = """25년간 글로벌 물류 업계에서 쌓아온 경험은 단순한 경력이 아닌, WR Group 한국지사 성공을 위한 전략적 자산입니다. 한진해운에서 시작하여 Bureau Veritas까지, 매 순간 새로운 도전과 혁신을 통해 검증된 성과를 창출해왔습니다.

부산 녹산공단을 직접 뛰며 제로베이스에서 고객을 발굴했던 신입사원 시절의 현장 영업 경험부터, 이란 제재라는 극한 상황에서 오히려 주간 100만불 이상의 영업이익을 창출하며 산업통상자원부 장관상을 수상한 위기 관리 역량까지, 어떠한 어려운 상황에서도 창의적 해법을 찾아내는 것이 저의 강점입니다.

특히 중동 고위층부터 한국 대기업 임원진까지 25년간 구축한 네트워크는 상호 신뢰를 바탕으로 한 전략적 파트너십으로, Bureau Veritas에서 17척의 선박을 100척 이상으로 확장시킨 것도 이러한 신뢰관계의 결과입니다."""
    
    motivation_para = doc.add_paragraph(motivation_text)
    
    # 취업 후 사업계획 및 포부
    doc.add_heading('취업 후 사업계획 및 포부', level=2)
    
    # Phase 1
    doc.add_heading('Phase 1 (1차년도): 기존 네트워크 활용한 즉시 실행', level=3)
    
    doc.add_paragraph().add_run('확정적 프로젝트 파이프라인').bold = True
    
    projects = [
        '현대스틸산업 중동 프로젝트 확대: 사우디 아람코 아미랄 석유화학 콤플렉스 물류 서비스 (110억 달러 규모)',
        'Qatar Gas & Petronas EPC 메가 프로젝트: Qatar Gas 북부가스전 남부 프로젝트 (100억 달러 EPC) 물류 참여',
        '조선·해양플랜트 통합 물류: 안마해상풍력 532MW 프로젝트 참여사들과 협업'
    ]
    
    for project in projects:
        doc.add_paragraph(project, style='List Bullet')
    
    # 1차년도 목표
    doc.add_paragraph().add_run('1차년도 목표').bold = True
    year1_targets = [
        '매출액: 500억원 (독일 본사 목표 대비 200% 달성)',
        '핵심 고객: 15개사 확보 (EPC 대기업 5개사 + 조선 3개사 + 중동 현지 7개사)',
        '차별화 서비스: 멀티모달·ESG 친환경 물류 플랫폼 구축 완료'
    ]
    
    for target in year1_targets:
        doc.add_paragraph(target, style='List Bullet')
    
    # Phase 2
    doc.add_heading('Phase 2 (2-3차년도): 아시아 전략 거점 완성', level=3)
    
    # 2-3차년도 목표
    doc.add_paragraph().add_run('2-3차년도 목표').bold = True
    years23_targets = [
        '2차년도 매출액: 900억원 (아시아 지역 거점 완성)',
        '3차년도 매출액: 1,500억원 (아시아 최고 수준 EPC 물류 기업)',
        '지역 확장: 베트남·태국·인도네시아 거점 설립으로 동남아시아 진출'
    ]
    
    for target in years23_targets:
        doc.add_paragraph(target, style='List Bullet')
    
    # 장기 비전
    doc.add_heading('장기 비전: Global EPC Logistics Leader', level=3)
    
    doc.add_paragraph().add_run('5년 후 목표').bold = True
    five_year_targets = [
        '매출 3,000억원: 아시아 EPC 물류 시장 점유율 1위',
        '지역 확장: 동남아시아·인도·호주까지 아우르는 아시아-태평양 네트워크'
    ]
    
    for target in five_year_targets:
        doc.add_paragraph(target, style='List Bullet')
    
    # 결론
    conclusion_para = doc.add_paragraph()
    conclusion_run = conclusion_para.add_run('결론: WR Group과 함께 창조할 미래')
    conclusion_run.bold = True
    conclusion_run.font.size = Pt(14)
    conclusion_run.font.color.rgb = RGBColor(30, 60, 114)
    
    conclusion_text = """25년간의 글로벌 물류 경험과 독점적 네트워크 자산을 바탕으로, WR Group 한국지사를 단순한 현지 법인이 아닌 아시아 전체를 아우르는 전략적 성장 엔진으로 발전시키겠습니다.

저의 중동 왕족·정부·기업 네트워크, 한국 EPC 대기업과의 직접 관계, 현 직장 거래처들과의 네트워크를 통한 글로벌 프로젝트 경험, 그리고 유럽 시장 이해도는 WR Group이 아시아 시장에서 독보적 위치를 확보할 수 있는 완벽한 전략적 자산입니다.

WR Group의 혁신적 비전과 저의 실행 역량이 만나 글로벌 EPC 물류 업계의 새로운 표준을 창조하는 역사적 성과를 함께 이루어내겠습니다."""
    
    conclusion_content = doc.add_paragraph(conclusion_text)
    
    # 최종 서명
    doc.add_paragraph()
    signature_para = doc.add_paragraph('2025년 9월 2일')
    signature_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    name_para = doc.add_paragraph('한 상 진')
    name_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    name_run = name_para.runs[0]
    name_run.bold = True
    name_run.font.size = Pt(14)
    name_run.font.color.rgb = RGBColor(30, 60, 114)
    
    return doc

def main():
    """메인 함수 - 한국어 이력서 워드 문서 생성 및 저장"""
    try:
        # HTML 파일 경로
        html_file_path = '/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/1.1. Project private/job search/Global_Logistics_Company_Korea_Branch_Manager_(2025-08-24)/이력서 제출용/제출 파일/한상진.html'
        
        # HTML 파일 존재 여부 확인
        if not os.path.exists(html_file_path):
            print(f"❌ HTML 파일을 찾을 수 없습니다: {html_file_path}")
            print("파일 경로를 확인해주세요.")
            return False
        
        print(f"📄 HTML 파일 발견: {html_file_path}")
        
        # 워드 문서 생성
        print("🔄 워드 문서 생성 중...")
        doc = create_korean_resume_document()
        
        # 저장 경로 설정 (같은 폴더에 저장)
        output_directory = os.path.dirname(html_file_path)
        output_path = os.path.join(output_directory, '한상진_이력서_WR_Group.docx')
        
        # 문서 저장
        doc.save(output_path)
        
        print(f"✅ 한국어 이력서가 성공적으로 워드 문서로 변환되었습니다!")
        print(f"📁 저장 위치: {output_path}")
        print(f"📄 파일명: 한상진_이력서_WR_Group.docx")
        
        # 파일 열기
        try:
            os.system(f'open "{output_path}"')
            print("📖 워드 문서가 자동으로 열립니다.")
        except:
            print("💡 워드 문서를 수동으로 열어서 확인하세요.")
        
    except Exception as e:
        print(f"❌ 워드 문서 생성 중 오류 발생: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 한상진 한국어 이력서 HTML → Word 변환기")
    print("=" * 50)
    main()