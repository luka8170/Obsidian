---
updated: 2026-10-22
tags: [비즈니스, 시스템, 마스터]
related: [[해운-영업/bv-cap-서비스-영업전략]], [[해운-영업/bv-cpm-gtm-머스트윈전략]], [[해운-영업/bv-mo-bd-세일즈-가이드라인]], [[salesforce-crm-대시보드운영]], [[salesforce-marine-세일즈프로세스-기초]], [[salesforce-mo-세일즈프로시저-2025]]
source: "2025년 BV Salesforce coaching session 3편(CRM 대시보드 운영, Marine 세일즈 프로세스 기초, M&O 세일즈 프로시저 2025)을 종합한 마스터 페이지. 각 원문은 salesforce/ 폴더의 개별 페이지 참조."
---

# Salesforce CRM 마스터

BV M&O 영업에서 Salesforce를 어떻게 쓰는지 — 오브젝트 구조, 세일즈 여정, 확률 기준, 대시보드 운영, KPI — 를 하나로 묶은 페이지. salesforce/ 폴더 3개 코칭 세션 노트를 주제별로 재구성했다.

## 핵심 인사이트

### 1. Salesforce의 목적과 위치
- **3대 목적**: ① Client Orientation (전략 고객 추적·관계 강화) ② Sales Consistency (상업 정보 추적가능성·팀 효율) ③ Reporting (대시보드·KPI 모니터링)
- 기존 Mercury 시스템을 대체하는 CRM. "No need to use excel file to be updated regularly — reports and dashboard are updated in real time, all sales history in a single place"
- Marine & Offshore 활동은 기본적으로 Opportunity 중심. Frame Agreement는 주로 M&O Services가 사용

### 2. 오브젝트 구조 (Campaign → Lead/Opp)
- **4대 오브젝트 관계**: Campaign(여러 Lead/Opp 묶음) → Lead(정보 불완전한 잠재 딜) → Company + Contact → Opportunity(검증된 딜, 서비스 코드 + Object type 필수)
- Opportunity Win 시 FLEX에 자동으로 신규 Client 생성
- **Object Category 3종**: Marine / Marine Green(친환경 추진선 식별용) / Offshore
- **서비스 코드**: NC = M10/M11, NS = N10/N11, BVN under NC = P20, 기타 인증 = N40/N41/N50/N60/N70/N71

### 3. 4대 세일즈 영역 (필수 입력, NC·NS·BVN은 Campaign 연결 필수)
| 영역 | 내용 | 계약 주체 |
|---|---|---|
| **NC** | 조선소와 체결하는 신조 계약 | 조선소 (선주/선주대리인 관여하나 최종 계약자는 조선소). Campaign 모델 필수 |
| **NS (CAC)** | 선주/선박관리사와 체결하는 5년 정기 계약 (New Delivery·Renewal) | 선주/선박관리사. 독립 Opportunity 또는 Campaign 연결 |
| **BVN** | 장비 제조사 대상 | — |
| **OTHER** | 독립 계약 (ISM/ISPS/MLC, Cybersecurity, IHM, ISO&DOC, BVS, TMC, Matdan 등) | — |

### 4. 세일즈 여정 5단계
Activity/Lead 생성 → Opportunity Completion → Proposal Under Preparation → Proposal Issued → Deal Conclusion (Won/Lost/Cancelled/Abandoned)

- Opportunity Name 규칙: "선주명/선박크기 및 타입" (예: Bonny Gas Transport/174K LNG carriers)
- 딜을 처음 인지한 사람이 먼저 Lead로 등록 → 나중에 Owner 이전 가능. "As soon as you hear about a new potential deal, check if it's already tracked. If not, track it, even if you won't be the Owner."

### 5. Probability to Win 기준표 — 연도별 변화에 주의
2022년 업데이트와 2025년(22nd coffee) 기준이 다르다. **최신(2025) 기준을 따를 것**:

| 단계 | 2022 기준 | 2025 기준 |
|---|---|---|
| Opportunity | 기본 5%, 수동 5~50% | 기본 5%, 자신 있으면 25% (갱신형 70%) |
| Proposal Under Prep | 기본 30%, 수동 15~99%(→5~99% 확대 예정) | 기본 5%, 최대 70% |
| Proposal Issued | 기본 30%, 수동 15~99% | 기본 25%, 낙찰 확신 시 90% |
| Closed Won/Lost | 100% / 0% (수정 불가) | 동일 (자동) |

- 2025년 기준 **수동 입력 금지, 드롭다운 선택만 가능** — 임의 숫자 입력 불가
- **NC 확률 계산 공식**: Opp 확률 = P(선주 발주) × P(해당 조선소 선택) × P(조선소가 BV 선택). Campaign 총합 확률 = 모든 조선소별 Opp 확률의 합 (초과 불가)

### 6. Roles & Responsibilities
- 전체 보기(View)는 누구나 가능. 생성도 누구나 가능. **수정은 Owner만** 가능
- **데이터 정확성 최종 책임은 Owner**

### 7. 대시보드·리포트 운영
- **Report → Dashboard 순서 필수**: Report를 먼저 만들어야 Dashboard 생성 가능. Dashboard는 Summary/Matrix 리포트 타입의 시각적 표현
- **4가지 리포트 타입**: Tabular(단순 목록, 대시보드 불가) / Summary(소계+차트, 대시보드 적합) / Joined(최대 5블록) / Matrix(행+열 교차 집계)
- **대시보드 그래픽 4종**: Gauge(목표 대비 진척) / Table(Top5 등 순위) / Metric(단일 숫자) / Chart(비교) — 대시보드당 최대 20 컴포넌트
- **계층별 파이프라인 추적**: 개인(Sales Rep Dashboard) → 팀(Team Selling Pipeline) → 로컬팀(Local Team Pipeline) → 글로벌(Excom/Zone Dashboard) 4단계
- 즐겨찾기(Favorite) 등록으로 주간/월간 리뷰 시 원클릭 접근

### 8. 2025년 DQM 3대 KPI + 이상적 파이프라인 분포
- **DQM KPI**: ① Win ratio (닫힌 건 중 수주율) ② Proposal lifetime (Close date vs 생성일 간격 — 짧으면 파이프라인 가시성 부족) ③ Logging frequency (주 1회 이상 로그인)
- **이상적 Pipeline 분포**: Opportunity 60~65% / Proposal Under Prep 10~15% / Proposal Issued 20~30%
- **주간 리뷰 3대 지표**: ① Close date 갱신 여부 ② Overdue + 14일 내 만기 Opp 정리 ③ 리드 전환율(New lead current year)
- **Engagement Committee**: 3m€ 이상 기회는 Salesforce 내 EC 프로세스 필수, 대시보드에서 실시간 추적
- "Small pipeline means no visibility! Let's show our BD efforts by registering maximum of opportunities" / "We need to learn from our failure. Let's be as exhaustive as possible in registering opportunities."

## 내 사업 적용 액션 (3개 원문 공통 종합)
- [ ] 모든 딜을 Lead로 먼저 등록 → 조선소/선주/금액/타입 확인되면 즉시 Opportunity로 전환
- [ ] NC/NS/BVN 딜은 Campaign 먼저 생성 후 Child Opportunity 연결 구조 준수
- [ ] Opportunity Name 규칙("선주명/선박크기 및 타입") 통일 적용
- [ ] Probability 값은 2025년 기준표대로만 선택 (임의 입력 금지)
- [ ] 친환경 추진선 딜은 Object Type = "Marine Green"으로 별도 추적
- [ ] Sales Rep Dashboard 주간 월요일 루틴 확인 + Overdue Opp 14일 기준 알림 설정
- [ ] 파이프라인 분포를 월 1회 확인 (Opportunity 60%+ 유지 여부)
- [ ] 3m€ 이상 규모 딜은 EC 프로세스 체크리스트 사전 준비
- [ ] 주간 리뷰용 리포트/대시보드 3개 Favorite 등록

## 세부 페이지
- [[salesforce-crm-대시보드운영]] — Report/Dashboard 타입, 그래픽 종류, 계층별 파이프라인
- [[salesforce-marine-세일즈프로세스-기초]] — 오브젝트 구조, NC/CAC/OTHER 범위, Roles & Responsibilities, 2022년 확률 기준
- [[salesforce-mo-세일즈프로시저-2025]] — 4대 세일즈 영역, 2025년 확률 기준, DQM KPI, EC 프로세스

## 관련 페이지
- [[해운-영업/bv-cap-서비스-영업전략]]
- [[해운-영업/bv-cpm-gtm-머스트윈전략]]
- [[해운-영업/bv-mo-bd-세일즈-가이드라인]]

## 미반영/추가 필요
- **폴더 분리 이슈 (lint 감사 발견)**: 같은 Salesforce 코칭 세션에서 나온 `bv-cap-서비스-영업전략`, `bv-cpm-gtm-머스트윈전략`, `bv-mo-bd-세일즈-가이드라인` 3개 파일이 `해운-영업/`에 따로 분류되어 있다. 현재는 이 마스터 페이지의 `related`로만 교차 연결해두었음. 추후 결정 필요: ① `salesforce/`와 `해운-영업/` 두 폴더를 통합할지 ② 지금처럼 분리 유지하고 상호 링크로만 연결할지 — vault 구조 정리 시점에 사용자와 논의할 것.
- 2022년과 2025년 Probability 기준표가 공존하는데, 2025 코칭 세션이 최신이므로 실무에는 2025 기준만 적용 중. 혹시 2026년 업데이트된 세션이 있었다면 추가 반영 필요.
- `sinokor-detail`처럼 Opportunity 단위 실제 적용 사례(우리 영업 파이프라인을 Salesforce 오브젝트로 매핑한 구체 예시)는 아직 기록되지 않음.
