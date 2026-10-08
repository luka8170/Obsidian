<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>이력서 - 한상진</title>
  <style>
    /* 기본 스타일 */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      max-width: 210mm;
      margin: 0 auto;
      padding: 15mm;
      font-family: 'Malgun Gothic', '맑은 고딕', sans-serif;
      line-height: 1.6;
      font-size: 11pt;
      color: #333;
    }
    
    /* 헤더 영역 */
    .header { 
      margin-bottom: 20px;
      page-break-inside: avoid;
    }
    
    .photo-box { 
      float: right; 
      width: 3.5cm; 
      height: 4.5cm; 
      border: 1px solid #333; 
      text-align: center; 
      line-height: 4.5cm; 
      margin-left: 15px;
      color: #999;
      font-size: 10pt;
    }
    
    .personal-info { 
      margin-bottom: 15px; 
    }
    
    h1 { 
      text-align: center; 
      font-size: 20pt; 
      margin: 15px 0;
      color: #000;
      page-break-after: avoid;
    }
    
    h2 { 
      font-size: 14pt; 
      border-bottom: 2px solid #333; 
      padding-bottom: 5px; 
      margin-top: 20px; 
      margin-bottom: 12px;
      page-break-after: avoid;
      color: #000;
    }
    
    h3 { 
      font-size: 12pt; 
      margin-top: 15px; 
      margin-bottom: 8px; 
      color: #333;
      page-break-after: avoid;
    }
    
    h4 { 
      font-size: 11pt; 
      margin-top: 12px; 
      margin-bottom: 6px;
      page-break-after: avoid;
      font-weight: bold;
    }
    
    h5 { 
      font-size: 10pt; 
      margin-top: 10px; 
      margin-bottom: 6px; 
      font-weight: bold;
      page-break-after: avoid;
    }
    
    p { 
      margin: 8px 0; 
      text-align: justify; 
      line-height: 1.6;
      orphans: 3;
      widows: 3;
    }
    
    ul { 
      margin: 10px 0; 
      padding-left: 20px;
    }
    
    li { 
      margin: 5px 0; 
      line-height: 1.6;
      page-break-inside: avoid;
    }
    
    /* 요약 섹션 */
    .summary { 
      background-color: #f5f5f5; 
      padding: 12px; 
      border-radius: 5px; 
      margin: 15px 0; 
      line-height: 1.7;
      page-break-inside: avoid;
    }
    
    /* 섹션 스타일 */
    .section { 
      margin-bottom: 20px;
      page-break-inside: avoid;
    }
    
    .job-title { 
      font-weight: bold; 
      color: #000080; 
    }
    
    .company { 
      font-weight: bold; 
    }
    
    .period { 
      color: #666; 
      font-size: 10pt; 
    }
    
    .indent { 
      margin-left: 15px; 
    }
    
    strong { 
      font-weight: bold; 
    }
    
    /* 정보 레이아웃 */
    .header-title {
      border: none !important;
      font-size: 14pt;
      margin: 8px 0;
    }
    
    .personal-info-row {
      line-height: 1.8;
      margin-bottom: 6px;
    }
    
    .info-label {
      display: inline-block;
      width: 80px;
      font-weight: bold;
    }
    
    .info-value {
      display: inline-block;
      width: 200px;
    }
    
    .info-label2 {
      display: inline-block;
      width: 100px;
      font-weight: bold;
    }
    
    .clear-both {
      clear: both;
    }
    
    /* 프로젝트 테이블 */
    .project-table {
      margin: 15px 0;
      page-break-inside: avoid;
    }
    
    .project-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
      font-weight: bold;
      border-bottom: 1px solid #ddd;
      padding-bottom: 5px;
    }
    
    .project-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
      page-break-inside: avoid;
    }
    
    .project-name {
      flex: 2;
    }
    
    .project-scale {
      flex: 1;
      text-align: center;
    }
    
    .project-revenue {
      flex: 1;
      text-align: right;
    }
    
    .project-total {
      display: flex;
      justify-content: space-between;
      margin-top: 12px;
      padding-top: 8px;
      border-top: 2px solid #333;
      font-weight: bold;
    }
    
    /* 최종 서명 */
    .final-signature {
      margin-top: 40px;
      text-align: center;
      page-break-inside: avoid;
    }
    
    .final-signature p {
      margin-top: 20px;
    }
    
    /* 급여 정보 */
    .salary-info {
      margin-left: 15px;
    }
    
    .salary-row {
      margin-bottom: 6px;
    }
    
    .salary-label {
      display: inline-block;
      width: 100px;
      font-weight: bold;
    }
    
    /* 인쇄 최적화 */
    @media print {
      body {
        margin: 0;
        padding: 10mm;
        font-size: 10pt;
        line-height: 1.5;
      }
      
      /* 페이지 구분 제거 - 자연스러운 흐름 */
      .page-break {
        display: none;
      }
      
      /* 제목들이 다음 페이지로 넘어가지 않도록 */
      h1, h2, h3, h4, h5 {
        page-break-after: avoid;
        page-break-inside: avoid;
      }
      
      /* 섹션이 분리되지 않도록 */
      .section {
        page-break-inside: auto;
      }
      
      /* 리스트 항목이 분리되지 않도록 */
      li {
        page-break-inside: avoid;
      }
      
      /* 테이블과 프로젝트 정보 보호 */
      .project-table, .project-row {
        page-break-inside: avoid;
      }
      
      /* 요약 박스 보호 */
      .summary {
        page-break-inside: avoid;
      }
      
      /* 개인정보 섹션 보호 */
      .header {
        page-break-inside: avoid;
      }
      
      /* 여백 최적화 */
      h1 { font-size: 18pt; margin: 10px 0; }
      h2 { font-size: 13pt; margin-top: 15px; margin-bottom: 10px; }
      h3 { font-size: 11pt; margin-top: 12px; margin-bottom: 6px; }
      h4 { font-size: 10pt; margin-top: 10px; margin-bottom: 5px; }
      h5 { font-size: 9pt; margin-top: 8px; margin-bottom: 4px; }
      
      p { margin: 6px 0; }
      ul { margin: 8px 0; }
      li { margin: 4px 0; }
      
      .section { margin-bottom: 15px; }
      .summary { padding: 10px; margin: 12px 0; }
    }
    
    /* PDF 다운로드 버튼 */
    .pdf-download-btn {
      position: fixed;
      top: 20px;
      right: 20px;
      background: #0066cc;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      z-index: 1000;
    }
    
    .pdf-download-btn:hover {
      background: #0052a3;
    }
    
    @media print {
      .pdf-download-btn {
        display: none;
      }
    }
  </style>
</head>
<body>

<!-- PDF 다운로드 버튼 -->
<button class="pdf-download-btn" onclick="window.print()">📄 PDF로 저장</button>

<h1>이 력 서</h1>

<div class="header">
  <div class="photo-box">사진</div>
  <div class="personal-info">
    <h2 class="header-title">용마로지스 국제영업 총괄임원 지원</h2>
    <div class="personal-info-row">
      <span class="info-label">성명</span>
      <span class="info-value">한상진</span>
      <span class="info-label2">생년월일</span>
      <span>1973년 5월 28일 (52세)</span>
    </div>
    <div class="personal-info-row">
      <span class="info-label">연락처</span>
      <span class="info-value">010-4167-0528</span>
      <span class="info-label2">이메일</span>
      <span>frankston@naver.com</span>
    </div>
    <div class="personal-info-row">
      <span class="info-label">주소</span>
      <span>경기도 성남시 분당구</span>
    </div>
  </div>
  <div class="clear-both"></div>
</div>

<h2>EXECUTIVE SUMMARY</h2>

<div class="summary">
25년간 글로벌 물류·해운 업계에서 검증된 성과를 창출해온 국제영업 전문가로서, 용마로지스의 국제영업 총괄임원 포지션에 최적화된 역량을 보유하고 있습니다.<br><br>

한진해운에서 16년간 중동·홍해 항로 총괄, UAE 지점 부지점장으로서 <strong>아시아-중동 항로 시장점유율 1위 달성</strong>, 이란 제재 상황에서 <strong>주간 100만불+ 영업이익 창출</strong>로 산업통상자원부 장관상을 수상했습니다. 현재 Bureau Veritas에서는 한국 고객의 선급 이용 선박수를 <strong>17척에서 100척+로 700% 성장</strong>시켰습니다.<br><br>

특히 <strong>해운사 CEO/오너 직접 네트워크</strong>를 통한 업계 최고 수준의 NVO Pricing 역량으로, 일반 포워더 대비 15-20% 유리한 운임과 성수기 안정적 선복 확보가 가능합니다. 용마로지스의 정밀 온도·습도 제어 시스템과 검증된 특수물류 역량에 저의 글로벌 네트워크를 결합하여, <strong>1차년도 신규매출 500억원, 3년 내 1,000억원 달성</strong>을 목표로 국제영업을 혁신하겠습니다.
</div>

<h2>핵심 역량 - 용마로지스 JD 부합</h2>

<div class="section">
<h3>1. 포워딩 영업 총괄 및 관리감독 ✓</h3>
<ul>
  <li><strong>한진해운 중동 10개국 서비스 총괄</strong>: 아시아-중동 항로 시장점유율 1위 달성</li>
  <li><strong>UAE 지점 부지점장 경험</strong>: 중동 GCC·홍해 국가 컨테이너 서비스 마케팅 전략 개발</li>
  <li><strong>P&L 관리</strong>: CAPEX/OPEX 분석 기반 수익성 관리 및 전략 수립</li>
  <li><strong>IRA(중동선사협의체), IRSA(홍해선사협의체), TSA(미주서비스선사협의체) 한국 대표</strong></li>
</ul>

<h3>2. 국내외 고객사 대상 해상/항공 수출입 포워딩 전략 ✓</h3>
<ul>
  <li><strong>복합운송 최적화</strong>: 현장 판매직원용 운임 확인 시스템 개발·배포</li>
  <li><strong>메가 프로젝트 경험</strong>: 카타르가스, 페트로나스, 사우디 아람코 프로젝트 수주</li>
  <li><strong>글로벌 화주 직접 협상</strong>: SABIC, Qatar Chemical, Dubai Aluminum 등</li>
  <li><strong>한국 대기업 네트워크</strong>: LG에너지솔루션, 포스코인터내셔널, SK가스, 삼성전자 등</li>
</ul>

<h3>3. 신규 고객 발굴 및 기존 거래처 관리 ✓</h3>
<ul>
  <li><strong>제로베이스 신규 개척</strong>: 부산 공단 직접 방문으로 Humax, 쌍용선재 등 확보</li>
  <li><strong>700% 성장 달성</strong>: Bureau Veritas 17척 → 100척+ 선박 확보</li>
  <li><strong>재계약률 95% 이상</strong>: 기존 고객 관계 강화 및 지속 관리</li>
</ul>

<h3>4. 선사 출신 경력 15년 이상(팀장급 이상) ✓✓</h3>
<ul>
  <li><strong>한진해운 16년 경력</strong>: 사원(2000)~부장(2016), UAE 지점 부지점장 역임</li>
  <li><strong>컨테이너선 영업본부</strong>: 아주·구주마케팅팀 차장~부장, 미주마케팅팀 차장</li>
  <li><strong>글로벌 협의체 대표</strong>: IRA, IRSA, TSA 등 주요 선사협의체 한국 대표 활동</li>
</ul>

<h3>5. 우대사항 충족✓</h3>
<ul>
  <li><strong>비즈니스 영어 회화 가능자 ✓</strong>: 프랑스 본사 및 중동·유럽 파트너와 일상 업무 수행</li>
  <li><strong>국내외 물류/유통 업종 경험자 ✓</strong>: UAE, 슬로바키아·체코, 호주 해외 근무 경험</li>
  <li><strong>관련 자격증 소지자 ✓</strong>: 한국해양대 해양금융 MBA, 운전면허 1종 보통</li>
  <li><strong>현 재직자 및 영업 거래처 물량 확보 가능자 ✓</strong>: 진행 중인 프로젝트로 즉시 물량 확보 가능</li>
</ul>
</div>

<h2>용마로지스를 위한 독점적 네트워크 자산</h2>

<div class="section">
<h3>NVO Pricing 핵심 역량 - 업계 최고 수준</h3>
<h4>해운사 CEO/오너 직접 협상 네트워크</h4>
<div class="indent">
<ul>
  <li>HMM(임원 다수), SM상선(대표), 장금상선(회장), SK해운(대표)</li>
  <li>클라리스쉬핑(회장), 하나마린(회장), H-Line(대표), 두라해운(회장)</li>
  <li>PIL(한국대표), Sea-Lead(한국대표), Emirates Shipping(본사임원)</li>
  <li>Gulftainer(CEO), X-Press Feeder(본사팀장), ONE(본사팀장)</li>
  <li>CMA CGM, COSCO, HPL, MSC (IRA/IRSA 협의체 대표 활동으로 구축)</li>
  <li><strong>실제 사례</strong>: HMM pricing 지인에게 연락하여, 영국발 CTV(Crew Transfer Vessel) 운송 시 27만불→17만불, <strong>10만불(37%) 절감</strong> 시킴.(2025.7)</li>
</ul>
</div>

<h3>즉시 실행 가능한 프로젝트 파이프라인</h3>
<div class="project-table">
  <div class="project-header">
    <span class="project-name">프로젝트명</span>
    <span class="project-scale">규모</span>
    <span class="project-revenue">예상매출</span>
  </div>
  <div class="project-row">
    <span class="project-name">현대스틸산업 사우디 프로젝트</span>
    <span class="project-scale">110억 달러</span>
    <span class="project-revenue">80억원</span>
  </div>
  <div class="project-row">
    <span class="project-name">카타르가스 북부가스전</span>
    <span class="project-scale">100억 달러</span>
    <span class="project-revenue">60억원</span>
  </div>
  <div class="project-row">
    <span class="project-name">LG에너지솔루션 ESS</span>
    <span class="project-scale">폴란드/미국</span>
    <span class="project-revenue">50억원</span>
  </div>
  <div class="project-row">
    <span class="project-name">두산에너빌리티 원전</span>
    <span class="project-scale">힝클리포인트 C</span>
    <span class="project-revenue">40억원</span>
  </div>
  <div class="project-row">
    <span class="project-name">삼성중공업 LNG선</span>
    <span class="project-scale">27만톤급</span>
    <span class="project-revenue">30억원</span>
  </div>
  <div class="project-total">
    <span>1차년도 예상 신규매출</span>
    <span>260억원+</span>
  </div>
</div>
</div>

<h2>WORK EXPERIENCE</h2>

<div class="section">
<h3><span class="company">Bureau Veritas 한국지점</span> | <span class="job-title">Marine & Offshore 마케팅·영업 이사</span></h3>
<p class="period">2017 ~ 현재</p>
<p style="font-style: italic;">[프랑스 글로벌 선급·검사·인증 기업, 연매출 60억 유로, 직원수 78,000명]</p>

<h4>주요 업무</h4>
<ul>
  <li>선박, 해양구조물 검사·인증 서비스 고객 확보를 위한 마케팅 및 영업</li>
  <li>글로벌 프로젝트 (카타르가스·페트로나스) 선박 발주 계약 수주</li>
  <li>국내 조선 Big 3 및 부산 선박 소유주들과 전략적 관계 구축</li>
</ul>

<h4>핵심 성과</h4>
<ul>
  <li>한국 고객 BV 선급 이용 선박수를 17척 → 100척+ 달성 (700% 성장)</li>
  <li>2022년 카타르가스, 페트로나스 프로젝트 최초 수주 (회사 창립 이래 처음으로 계약)</li>
  <li>국내 선주사 재계약률 95% 이상 달성</li>
</ul>

<h4>용마로지스 활용 가능한 네트워크</h4>
<ul>
  <li>선급 영업을 통해 구축한 국내외 선주사 및 해운 네트워크 (선복 확보 및 운임 협상 역량)</li>
  <li>카타르가스, 페트로나스 등 대형 EPC 프로젝트 참여 경험을 통한 프로젝트 물류 특성 이해</li>
  <li>Bureau Veritas 타 부문(Industry, Certification, Commodities)과의 협업으로 검사·인증·물류 통합 서비스 역량 확보</li>
</ul>
</div>

<div class="section">
<h3><span class="company">한진해운</span> | <span class="job-title">사원~부장</span></h3>
<p class="period">2000 ~ 2016</p>

<h5>차장~부장, 아주·구주마케팅팀 | 2012 ~ 2016</h5>
<p>컨테이너선 영업본부 - 중동·홍해 항로 총괄</p>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>아시아-중동·홍해 항로 총괄 (중동 10개국 컨테이너 서비스)</li>
  <li>포워딩 영업 전략 수립 및 관리감독 (용마로지스 JD와 직접 연관)</li>
  <li>IRA(중동선사협의체), IRSA(홍해선사협의체) 회사 대표</li>
  <li>전략물자 관리 및 정부기관 협력</li>
</ul>

<p><strong>핵심 성과</strong></p>
<ul>
  <li>아시아-중동 항로 시장점유율 1위 달성</li>
  <li>이란 제재 상황에서 주간 100만불+ 영업이익 창출</li>
  <li>2015년 무역안보 부문 산업통상자원부 장관상 수상</li>
  <li>에티오피아 연간 수출입 물량 전량 확보 (Ethiopia Shipping Line Tender 수주)</li>
</ul>
</div>

<h5>UAE 지점 부지점장 | 2011 ~ 2012</h5>
<p>중동 10개국 컨테이너 서비스 총괄</p>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>중동 GCC 국가·홍해 국가 대상 컨테이너 서비스 마케팅 전략 개발 및 실행</li>
  <li>UAE Sharaf Group, 사우디 Globe Marine Group과 대리점 계약 체결 및 관리</li>
  <li>SABIC, Qatar Chemical, Dubai Aluminum 등 메가 발주처와 직접 협상</li>
</ul>

<p><strong>핵심 성과</strong></p>
<ul>
  <li>중동 현지 네트워크 구축 (용마로지스 해외 확장 시 활용 가능)</li>
  <li>한화건설 이라크 비스마야 프로젝트(104억 달러)·아부다비 바라카 원전 프로젝트 물류 담당</li>
  <li>Dubai-Bandar Abbas 셔틀 서비스 신규 개설로 연간 50만 TEU 물량 확보</li>
  <li>중동 지역 매출 전년 대비 25% 성장 달성</li>
</ul>

<p><strong>중동 시장 전문성</strong></p>
<ul>
  <li>한진해운 중동 노선 운영을 통해 구축한 현지 비즈니스 네트워크</li>
  <li>중동 지역 컨테이너 물류 시장 특성 및 고객 의사결정 구조에 대한 실무 경험</li>
  <li>복잡한 중동 비즈니스 환경에서의 검증된 영업 성과 창출 능력</li>
</ul>
</div>

<h5>차장, 미주마케팅팀 | 2007 ~ 2011</h5>
<p>아시아↔미주 항로 총괄</p>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>아시아↔미주 항로 서비스 수립, 선박 투입, 지역본부 손익(P&L) 관리</li>
  <li>미주서비스선사협의체(TSA) 회사 대표로 활동</li>
  <li>미주향 운임 FMC(Federal Maritime Committee) Filing 업무</li>
  <li>복합운송 루트 설계 및 멀티모달 서비스 최적화</li>
</ul>

<p><strong>핵심 성과</strong></p>
<ul>
  <li>현장 판매직원용 복합운송 루트 운임 확인 가이드라인 및 툴 제작·배포</li>
  <li>Trans-Pacific 노선 수익성 분석 및 최적화로 연간 2,000만 달러 비용 절감</li>
  <li>IKEA, Walmart, Target 등 대형 BCO Service Contract 체결</li>
  <li>TSA 운임 안정화 정책 주도로 업계 운임 변동성 감소</li>
</ul>
</div>

<h5>과장, 동북아지역본부 마케팅팀 | 2004 ~ 2006</h5>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>한국·일본·대만발 미주·아시아향 마케팅 및 정책 영업관리</li>
  <li>Service Route별 수익·비용 분석을 통한 운임 전략 수립</li>
  <li>주요 화주 관리 및 Service Contract 체결</li>
</ul>

<p><strong>핵심 성과</strong></p>
<ul>
  <li>삼성전자, LG전자, 현대자동차 등 주요 화주 Service Contract 체결</li>
  <li>동북아 시장점유율 15% → 18% 확대</li>
  <li>일본·대만 시장 네트워크 구축으로 아시아 권역 경쟁력 강화</li>
</ul>
</div>

<h5>지역 전문가, 슬로바키아·체코 | 2004</h5>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>동유럽 신규 EU 가입국 시장 환경, 사업성 분석 및 내륙 운송 네트워크 심층 분석</li>
  <li>유럽 내륙 물류 인프라 및 철도 운송 시스템 현장 조사</li>
</ul>

<p><strong>핵심 성과</strong></p>
<ul>
  <li>삼성전자 갈란타, 기아자동차 질리나 등 슬로바키아 주요 제조업 고객 관리</li>
  <li>동유럽-중앙아시아 연결 복합운송 루트 이해</li>
  <li>유럽 비즈니스 문화 및 본사-현지법인 협력 시스템 이해</li>
</ul>
</div>

<h5>대리, 본사 벌크 전략팀 | 2003 ~ 2004</h5>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>벌크 사업 전략 기획 및 시장 개척</li>
  <li>리서치 자료 분석을 통한 중장기 전략 수립 지원</li>
  <li>주요 화주(포스코, 한국가스공사) 대상 사업 전략 구축</li>
</ul>
</div>

<h5>사원, 부산판매지점 | 2000 ~ 2003</h5>

<div class="indent">
<p><strong>주요 업무</strong></p>
<ul>
  <li>제로 고객기반에서 체계적 발굴을 통한 신규 시장 창출</li>
  <li>부산 녹산공단, 신평공단, 창원공단 직접 방문 영업</li>
</ul>

<p><strong>핵심 성과</strong></p>
<ul>
  <li>Humax(셋톱박스), 태창산업(textile), Saint Gobain Vetrotex 신규 계약</li>
  <li>쌍용선재(와이어로프), 효성전기(Delphi), NGU Group 등 주요 화주 확보</li>
  <li>신입사원 최우수 영업실적상 수상 (2001년)</li>
</ul>
</div>
</div>

<h2>용마로지스 성공을 위한 전략적 경쟁력</h2>

<div class="section">
<h3>1. 해운사 네트워크 기반 NVO Pricing 역량</h3>

<h4>국내 해운사 고위 경영진 네트워크</h4>
<ul>
  <li>HMM(주요 임원들), SM상선(대표 및 임원), 장금상선(회장)</li>
  <li>Pan Ocean(임원), 클라리스쉬핑(회장), SK해운(대표)</li>
  <li>하나마린(회장), H-Line(대표), 두라해운(회장)</li>
  <li>25년간 구축된 신뢰 관계로 경쟁력 있는 운임 협상 및 안정적 선복 확보</li>
</ul>

<h4>글로벌 해운사 네트워크</h4>
<ul>
  <li>Gulftainer(CEO), PIL(임원), Sea-Lead(한국대표)</li>
  <li>Emirates Shipping(임원), X-Press Feeder, ONE</li>
  <li>CMA CGM, COSCO, HPL, MSC (IRA/IRSA 협의체 활동으로 구축)</li>
</ul>

<h4>운임 경쟁력 확보 실적</h4>
<ul>
  <li>선사 고위층과의 직접 협상을 통한 시장 대비 15-20% 유리한 조건 확보</li>
  <li>성수기 선복 부족 상황에서도 안정적 물량 처리 능력 입증</li>
  <li>실제 사례: 영국발 CTV 운송 시 27만불 → 17만불, 10만불(37%) 절감 (2024.7)</li>
</ul>

<h3>2. 사업 확장 성과 및 대형 계약 체결 실적</h3>
<h4>주요 성과</h4>
<ul>
  <li>한국 고객 BV 선급 선박수 17척 → 100척+ 달성 (5.9배 성장률)</li>
  <li>Qatar Gas 북부가스전 남부 프로젝트(100억 달러 EPC) 선박 발주 계약 수주</li>
  <li>Petronas 말레이시아-캐나다 프로젝트 선박 발주 계약 수주</li>
  <li>에티오피아 연간 수출입 물량 전량 확보 (에티오피아 쉬핑 라인 Tender 수주)</li>
  <li>업계 협의체 한국 대표 역임: IRA(중동선사협의체), IRSA(홍해선사협의체), TSA(미주서비스선사협의체)</li>
</ul>

<h4>대규모 업체와 계약 체결 경험</h4>
<ul>
  <li>SABIC, Dubai Aluminum, Qatar Chemical, Iranian Khodro 등 중동 석유화학 메가 기업</li>
  <li>Ethiopia Shipping Line 연간 수입 물량 전체 수주</li>
  <li>IKEA, CAGILL, Walmart, Target 등 글로벌 다국적 기업</li>
  <li>삼성전자, LG전자, 한국타이어, 금호타이어, 넥센타이어 등 한국 대기업</li>
</ul>

<h3>3. 한국 특수화물 대기업 네트워크</h3>

<h4>대형 EPC 기업과의 현재 진행 중인 협업</h4>
<ul>
  <li>현대엔지니어링 그룹: 현대스틸산업 파트너십을 통한 사우디 아람코 아미랄 석유화학(110억 달러)</li>
  <li>삼성엔지니어링: 삼성중공업과 CCS 프로젝트 파트너십</li>
  <li>두산에너빌리티: 힝클리포인트 C 원전, SMR 개발 프로젝트</li>
</ul>

<h4>조선·해양플랜트</h4>
<ul>
  <li>HD현대중공업: 카타르 해상유전 EPC 프로젝트</li>
  <li>삼성중공업: 27만톤급 LNG 운반선 개발</li>
  <li>한화오션: 27만톤급 LNG 운반선 공동개발</li>
</ul>

<h3>4. 현장 영업 역량</h3>

<h4>주요 화주 네트워크</h4>
<ul>
  <li>LG에너지솔루션, 포스코인터내셔널, SK가스, SK E&S</li>
  <li>SABIC 울산공장, ACE E&T 울산공장, UNION 부산공장</li>
  <li>삼성전기, 삼성전자 가전사업부, 태창산업, NGU Group, HUMAX, Panasonic</li>
</ul>

<h4>현장 영업 성과</h4>
<ul>
  <li>부산 녹산공단, 신평공단, 창원공단 직접 방문 신규 화주 발굴</li>
  <li>한국 고객 이용 선박 수 17척 → 100척+ 확대</li>
</ul>

<h3>5. Multi-Modal 및 특수화물 운송 네트워크</h3>

<h4>항공·해운·육상 통합 네트워크</h4>
<ul>
  <li>대한항공(화물영업부), 부산신항만 터미널들, 스페인 알제시라스 터미널</li>
  <li>CAI Korea(컨테이너 장비 리스), 부산항만공사, 신한관세법인, 해양진흥공사</li>
  <li>항공·해운·육상·통관·금융 아우르는 종합 물류 서비스 체계</li>
</ul>

<h4>특수화물 전문 파트너십</h4>
<ul>
  <li>HMM 특수화물팀 Pricing</li>
  <li>현대글로비스: 해운, 물류 부문</li>
</ul>
</div>

<div class="section">
<h3>6. MRO(Maintenance, Repair & Overhaul) 물류 전문 네트워크</h3>

<p>미국 해군 함정 MRO가 한국 기업으로 확대되는 추세 활용</p>
<ul>
  <li>수리조선소: Yeosu Ocean, Union Shipyard (한-미 MRO 물류)</li>
  <li>에너지·플랜트: 한화오션, 삼성중공업, 현대중공업 유지보수 부품</li>
  <li>항공·국방: 대한항공, 한화에어로스페이스 정비부품</li>
</ul>

<h3>7. 검사·인증 연계 물류 서비스</h3>

<p>현 직장 Bureau Veritas의 글로벌 EPC 프로젝트 네트워크 활용</p>
<ul>
  <li>이라크 Kuwait Energy(130만 유로), 카타르 에너지(300만 유로), 사우디 왕실(250만 유로)</li>
  <li>Kazakhstan Kashagan·Tengiz 유전 개발 프로젝트</li>
  <li>유럽 BV 네트워크: Siemens AG, Shell plc, Ørsted 등</li>
</ul>

<h3>8. 중동 현지 네트워크</h3>

<p>한국 EPC 기업 프로젝트의 50% 이상이 중동에서 진행 - 현지 FOB 영업 핵심</p>

<h4>비즈니스 파트너</h4>
<ul>
  <li>Sharaf Group 회장 Ibrahim Sharaf(해운·물류·에너지), UAE</li>
  <li>Globe Marine Group 회장 Ehsan F. Abdul Jawad(해양 전문), UAE</li>
  <li>Gulftainer Containership 부문 CEO Peter Verheijen, UAE</li>
  <li>GSI Logistics 대표 KS Kim(UAE 한국인 1호 포워더), UAE</li>
</ul>

<h4>정부 고위층</h4>
<ul>
  <li>UAE Sheikh Ahmed Al Maktoum(왕족), Ahmed Bin Sulayem(DMCC 회장)</li>
  <li>쿠웨이트 Sheikha Mariyam Al Sabah(왕족), Ahmed Al Mesafir</li>
</ul>

<h3>9. 사업 관리 및 운영 역량</h3>

<h4>P&L 관리</h4>
<ul>
  <li>한진해운: 미주/아주/구주 지역본부 연간 사업계획 수립 및 월별 수익성 모니터링</li>
  <li>Bureau Veritas: 한국 Marine & Offshore 부문 매출 목표 설정 및 달성률 관리</li>
  <li>항로별 CAPEX/OPEX 분석을 통한 수익성 관리 및 개선</li>
</ul>

<h4>규제 대응 및 위기 관리</h4>
<ul>
  <li>이란 제재 관련 한국 정부기관 및 미국 국무부, OFAC 협력</li>
  <li>전략물자 관리로 산업통상자원부 장관상 수상</li>
  <li>지정학적 리스크 발생 시 대체 기항지 확보 및 정부기관 협업</li>
</ul>

<h4>데이터 기반 의사결정</h4>
<ul>
  <li>Excel 및 MS Office 활용 데이터 분석</li>
  <li>ATLAS(해운물류시스템) 개선 방안 제기</li>
  <li>Salesforce CRM, Tableau 활용 영업 관리</li>
</ul>

<h3>10. 리더십 및 전략적 운영 역량</h3>

<h4>조직 리더십</h4>
<ul>
  <li>산하 점소별 명확한 Sales 목표 설정 및 정기적 실적 평가</li>
  <li>미주, 아주, 구주 항로 운영 시 전문 역량 강화 교육 실시</li>
  <li>영문 보고서 작성 및 본사 경영진 브리핑</li>
</ul>
</div>

<h2>학력 및 기타사항</h2>

<div class="section">
<h3>학력</h3>
<div style="margin-left: 20px;">
  <div style="margin-bottom: 5px;">
    <span style="display: inline-block; width: 120px;">2018~2020</span>
    <span>한국해양대학교 해양금융 MBA</span>
  </div>
  <div style="margin-bottom: 5px;">
    <span style="display: inline-block; width: 120px;">2004</span>
    <span>Univerzita Komenského v Bratislave 슬로바키아어 수료</span>
  </div>
  <div style="margin-bottom: 5px;">
    <span style="display: inline-block; width: 120px;">1994~2000</span>
    <span>부산대학교 언어학과 학사</span>
  </div>
</div>

<h3>어학</h3>
<ul>
  <li>영어: Business Level (유럽 본사 일상 업무)</li>
  <li>독일어: 기초회화 (고교·대학 학습)</li>
  <li>슬로바키아어: 기초 (현지 근무)</li>
</ul>

<h3>해외경험</h3>
<ul>
  <li>2011~2012: UAE 두바이 (한진해운 부지점장)</li>
  <li>2004: 슬로바키아·체코 (지역전문가)</li>
  <li>1999~2000: 호주 멜버른 (어학연수)</li>
</ul>

<h3>수상</h3>
<ul>
  <li>2015년 산업통상자원부 장관상 (무역안보 부문). *산업부가 본인을 추천하여 회사명으로 수상.</li>
</ul>
</div>

<h2>자기소개 및 지원동기</h2>

<div class="section">
<h3>나의 업무스타일 및 강점</h3>

<p>25년 글로벌 물류 경험을 통해 체득한 저의 핵심 강점은 <strong>위기를 기회로 전환하는 창의적 해결능력</strong>과 <strong>장기적 관점의 네트워크 구축 역량</strong>입니다. 이란 제재라는 극한 상황에서도 대체 루트를 개발하여 주간 100만불 이상의 영업이익을 창출하며 산업통상자원부 장관상을 수상한 것이 이를 증명합니다.</p>

<p>저의 업무스타일은 <strong>현장 중심의 실행력</strong>과 <strong>데이터 기반 전략적 사고</strong>의 조화입니다. 부산 공단을 직접 뛰며 제로베이스에서 고객을 발굴했던 신입 시절부터, Bureau Veritas에서 17척을 100척 이상으로 확장시킨 현재까지, 항상 현장과 데이터를 기반으로 성과를 창출해왔습니다.</p>

<h3>용마로지스 지원동기 및 포부</h3>

<p>용마로지스는 <strong>41년 전통의 특수물류 전문기업</strong>으로서, 홈페이지를 통해 확인한 <strong>정밀 온도·습도 제어 시스템</strong>, <strong>첨단 창고 인프라</strong>, <strong>높은 완료율</strong>은 매우 우수한 기술력과 역량을 가지고 있다고 생각합니다.</p>

<p>저는 용마로지스의 이러한 기술적 우위와 제가 25년간 구축한 <strong>글로벌 네트워크를 결합</strong>하여 혁신적 시너지를 창출하고자 합니다. 특히 제가 보유한 <strong>해운사와의 네트워크를 통한 NVO pricing 역량은</strong>는 용마로지스의 모든 해상/항공 포워딩 업무에서 즉시 15-20% 운임 절감과 성수기 안정적 선복 확보를 가능하게 할 것입니다.</p>
</div>

<h2>취업 후 사업계획</h2>

<div class="section">
<h3>Phase 1 (1차년도): 기존 네트워크 활용한 즉시 실행</h3>

<h4>확정적 프로젝트 파이프라인</h4>

<p><strong>현대스틸산업 중동 프로젝트 확대</strong></p>
<ul>
  <li>사우디 아람코 아미랄 석유화학 콤플렉스 (110억 달러)</li>
  <li>강관, 장재, 플레이트 등 철강제품 전문 물류 서비스</li>
  <li>예상 매출: 80억원</li>
</ul>

<p><strong>Qatar Gas & Petronas EPC 메가 프로젝트</strong></p>
<ul>
  <li>Qatar Gas 북부가스전 남부 프로젝트 (100억 달러 EPC)</li>
  <li>Petronas 말레이시아, 캐나다 프로젝트 연계</li>
  <li>예상 매출: 60억원</li>
</ul>

<p><strong>LG에너지솔루션 ESS 프로젝트 물류</strong></p>
<ul>
  <li>폴란드 PGE 981MWh 그리드 스케일 ESS (2026-2027)</li>
  <li>미국 텍사스주 에너지저장장치 프로젝트</li>
  <li>본사 물류팀장(후배) 직접 협력</li>
  <li>예상 매출: 50억원</li>
</ul>

<p><strong>조선·해양플랜트 통합 물류</strong></p>
<ul>
  <li>안마해상풍력 532MW 프로젝트 (SK에코플랜트, 대한전선)</li>
  <li>HD현대중공업 카타르 해상유전 EPCI</li>
  <li>예상 매출: 40억원</li>
</ul>

<p><strong>검사·인증 연계 EPC 프로젝트</strong></p>
<ul>
  <li>Bureau Veritas 진행 중인 글로벌 프로젝트 물류 확장</li>
  <li>예상 매출: 30억원</li>
</ul>

<p><strong>1차년도 목표</strong></p>
<ul>
  <li><strong>매출액: 신규 500억원 창출</strong></li>
  <li>핵심 고객: 15개사 확보 (EPC 5개사 + 조선 3개사 + 중동 7개사)</li>
  <li>운임 절감: 기존 고객 대상 15-20% 절감 효과</li>
</ul>

<h3>Phase 2 (2-3차년도): 아시아 전략 거점 완성</h3>

<h4>혁신적 서비스 플랫폼 구축</h4>

<p><strong>ESG 기반 친환경 물류 생태계</strong></p>
<ul>
  <li>CO2 배출량 30% 감축 멀티모달 서비스</li>
  <li>해상풍력·태양광 등 신재생에너지 프로젝트 특화</li>
</ul>

<p><strong>신규 시장 개척</strong></p>
<ul>
  <li>Kazakhstan 에너지·광업 프로젝트</li>
  <li>한국-카자흐스탄 복합운송 루트 상용화</li>
  <li>우즈베키스탄, 투르크메니스탄 천연가스 개발</li>
</ul>

<p><strong>MRO 전문 물류 사업</strong></p>
<ul>
  <li>한-미 해군 MRO 물류 시장 선점</li>
  <li>해양플랜트·발전소 예방정비 부품 공급망</li>
  <li>항공·우주 산업 정밀 부품 물류</li>
</ul>

<p><strong>2-3차년도 목표</strong></p>
<ul>
  <li><strong>2차년도 매출액: 750억원</strong></li>
  <li><strong>3차년도 매출액: 1,000억원</strong></li>
  <li>동남아시아 거점 설립 (베트남·태국·인도네시아 등)</li>
</ul>

<h3>장기 비전: 글로벌 특수 화물 물류 리더</h3>

<p><strong>5년 후 목표</strong></p>
<ul>
  <li><strong>매출 1,500억원: 아시아 특수 물류 시장 점유율 상위권 도약</strong></li>
  <li>아시아-태평양 전체 네트워크 구축</li>
  <li>용마로지스를 글로벌 특수물류 브랜드로 포지셔닝 및 반도체 물류로 시장 확대</li>
</ul>

<h3>용마로지스와 함께 창조할 미래</h3>

<p>제가 보유한 <strong>25년간 구축한 글로벌 네트워크</strong>와 <strong>업계 최고 수준의 NVO Pricing 역량</strong>은 용마로지스의 <strong>검증된 특수물류 시스템</strong>과 결합될 때 폭발적 시너지를 창출할 것입니다.</p>

<p>NVO Pricing 업무의 핵심역량은 제가 가장 자신 있는 분야입니다. 해운사 Owner 및 CEO들과의 직접 협상력, 25년간 축적한 시장 분석 노하우, 위기상황 대응 경험은 용마로지스를 <strong>글로벌 특수물류 리더</strong>로 도약시킬 핵심 동력이 될 것입니다.</p>

<p>용마로지스의 기술력과 저의 글로벌 네트워크가 만나 <strong>국제영업의 새로운 표준</strong>을 창조하겠습니다.</p>
</div>

<h2>연봉 및 처우</h2>

<div class="section">
<div class="salary-info">
  <div class="salary-row">
    <span class="salary-label">현재 연봉</span>
    <span>1.38억원(기본급 1.17 + 성과급 0.20 + 고정수당 0.008) + 소나타(연료비 지원)</span>
  </div>
  <div class="salary-row">
    <span class="salary-label">희망 연봉</span>
    <span>회사 내규에 따라 협의 (임원급 패키지 기대)</span>
  </div>
  <div class="salary-row">
    <span class="salary-label">입사 가능일</span>
    <span>최종 합격 후 4주 이내 (인수인계 고려 협의 가능)</span>
  </div>
</div>
</div>

<div class="final-signature">
<p>위 기재사항은 사실과 틀림없음을 확인합니다.</p>
<p>2025년 9월 15일</p>
<p>지원자: 한 상 진 (인)</p>
</div>

</body>
</html>