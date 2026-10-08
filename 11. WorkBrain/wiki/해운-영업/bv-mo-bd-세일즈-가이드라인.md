---
source: "Salesforce 28th coffee (2026-03)"
date: 2026-06-30
tags: [#비즈니스, #시스템]
related: "[[salesforce-mo-세일즈프로시저-2025]], [[salesforce-crm-대시보드운영]], [[bv-internal]]"
---

# BV M&O BD & Sales 가이드라인 (LEAP 28)

## 핵심 인사이트

- **BD vs Sales 역할 구분**: BD = Lead 발굴·검증 → Opportunity 전환 (네트워킹·마케팅·직접 접촉). Sales = 검증된 Opportunity → 계약 체결 (Go/NoGo · 제안서 · EC · 서명)
- **용어 정의 통일 (공식)**:
  - **Lead**: 니즈 미확인 잠재 기회 (1개 Lead → 복수 Opportunity 가능)
  - **Opportunity**: 니즈 공식 표명 + 예산 추정 + 타임라인 추정 가능한 검증된 건
  - **Secured Opportunity**: 선주가 조선소 발주 확정 + BV 낙찰 의향 표명, 단 계약 미체결 (NC에만 적용)
  - **Won Opportunity**: 서명된 계약으로만 인정 (법적 구속력 있는 문서 필수)
- **Engagement Committee (EC)**: 1m€ 이상 기회는 Legal + Financial + Commercial 3중 승인 필수. **Win Strategy 회의가 아니라 리스크 관리 프로세스** — Salesforce 내 Opportunity Engagement 탭에서 처리
- **LEAP 28 SPP 3대 전략 영역**: Transition Services / Green & Low Emission Ships / Cybersecurity — 이 영역 딜은 우선순위 관리
- **Salesforce 4단계 루틴**:
  1. 매일: 최초 단계에서 즉시 Opp 등록 후 컨텍스트 변화 시 업데이트
  2. 매월 마지막 주: 월간 미팅 전 New wins·BU·GSC·Object type·Close date/Stage 전체 점검
  3. 월간 미팅 중: Salesforce 대시보드로 Sales & Pipeline 리뷰
  4. 말일: 마감 전 최종 데이터 확인
- **월간 미팅 5대 의제**: ① 전체 실적(win vs target) ② Key wins & Secured Opp ③ 대형 딜·Must Win·SPP ④ 주요 패배 원인 ⑤ Key activities(과거/다음 액션)

## M&O 서비스 코드 참고

| 코드 | 서비스 | 영역 |
|------|--------|------|
| M10 | Classification & Certification | NC |
| N10 | Classification & Certification | NS |
| O40 | CAP (Condition Assessment) | Advisory |
| O50 | Verifuel | Advisory |
| O85 | Decarbonization | Advisory |
| C77~C87 | Cybersecurity (People/OT/IoT/IT) | Advisory |
| P10/20/30 | TAC, Product Cert, QS Approval | BVN |

## 내 사업 적용 액션

- [ ] 모든 접촉을 Lead로 즉시 등록 → 니즈 확인 후 Opportunity로 전환하는 2단계 습관 세팅
- [ ] 1m€ 이상 딜은 Proposal 준비 전 EC 탭 사전 점검 (Scope Gate → Commercial Gate → Contractual Obligation)
- [ ] 월간 미팅 전 마지막 주에 Salesforce 데이터 정비 루틴 캘린더 등록
- [ ] SPP 해당 딜(탄소중립·사이버보안)은 별도 태그로 파이프라인에서 우선 관리

## 원문 발췌

> "Booking can be done only when a legally binding document exists!"

> "It is NOT a Win Strategy Meeting" (EC에 대한 오해 방지 강조)
