---
source: "Salesforce Marine Training 2021 (v1.2) + Marine Training 2022 (v1.0)"
date: 2026-06-30
tags: [#비즈니스, #시스템]
related: "[[salesforce-mo-세일즈프로시저-2025]], [[salesforce-crm-대시보드운영]]"
---

# BV M&O Salesforce Marine 세일즈 프로세스 기초

## 핵심 인사이트

- **Salesforce 목적 3가지**: ① Client Orientation (전략 고객 추적·관계 강화) ② Sales Consistency (상업 정보 추적가능성·팀 효율) ③ Reporting (대시보드·KPI 모니터링). Mercury 시스템 대체 CRM
- **5단계 세일즈 여정**: Activity/Lead 생성 → Opportunity Completion → Proposal Under Preparation → Proposal Issued → Deal Conclusion (Won/Lost/Cancelled/Abandoned)
- **Marine 3대 세일즈 범위**:
  - **NC**: 조선소와 체결하는 계약. 선주/선주대리인이 관여하나 최종 계약 주체는 조선소. Campaign 모델 필수
  - **CAC (NS)**: 선주/선박관리사와 체결하는 5년 정기 계약. 독립 Opportunity 또는 Campaign 연결
  - **OTHER**: 독립 계약 (ISM/ISPS/MLC, Cybersecurity, IHM, ISO&DOC, BVS, TMC, Matdan 등)
- **Salesforce 4대 오브젝트 관계**: Campaign (여러 Lead/Opp 묶음) → Lead (정보 불완전한 잠재 딜) → Company + Contact → Opportunity (검증된 딜, 서비스 코드 + Object type 필수 입력). Opp Win 시 FLEX에 자동 신규 Client 생성
- **Probability to Win 스테이지별 기준 (2022 업데이트)**:
  - Opportunity: 기본 5%, 수동 범위 5~50%
  - Proposal Under Preparation: 기본 30%, 수동 15~99% (→ 5~99%로 확대 예정)
  - Proposal Issued: 기본 30%, 수동 15~99%
  - Closed Won: 100% / Lost/Abandoned/Cancelled: 0% (수정 불가)
- **NC 확률 계산 공식**: Opp 확률 = P(선주 발주) × P(해당 조선소 선택) × P(조선소가 BV 선택). Campaign 총합 확률 = 모든 조선소별 Opp 확률의 합 (초과 불가)
- **Roles & Responsibilities**: 전체 보기는 누구나 가능. 생성은 누구나 가능, 수정은 Owner만 가능. 딜을 처음 인지한 사람이 먼저 등록 → 나중에 소유권 이전 가능. **데이터 정확성 최종 책임은 Owner**
- **Object Category 3종**: Marine / Marine Green (친환경 추진선 식별용) / Offshore. 서비스 코드: NC = M10/M11, NS = N10/N11, BVN under NC = P20, 기타 인증 = N40/N41/N50/N60/N70/N71

## 내 사업 적용 액션

- [ ] 모든 딜을 Lead로 먼저 등록 → 조선소/선주/금액/타입 확인되면 즉시 Opportunity로 전환
- [ ] NC 딜 생성 시 Campaign 먼저 생성 → Child Opportunity 연결 구조 준수
- [ ] Opportunity Name 규칙: "선주명/선박크기 및 타입" (예: Bonny Gas Transport/174K LNG carriers)
- [ ] 친환경 추진선 관련 딜은 Object Type = "Marine Green" 선택 → 그린 파이프라인 별도 추적

## 원문 발췌

> "As soon as you hear about a new potential deal, you are expected to check if it has already been tracked in Salesforce. If not, you are expected to track it, even though you will not be the Owner."

> "Marine & Offshore activities use essentially opportunities. Frame Agreements are mainly used by M&O Services."
