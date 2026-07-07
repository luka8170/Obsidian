---
source: "Salesforce 22nd coffee (2025-02-24)"
date: 2026-06-30
tags: [#비즈니스, #시스템]
related: "[[bv-internal]], [[salesforce-crm-대시보드운영]]"
---

# BV M&O Salesforce 세일즈 프로시저 2025

## 핵심 인사이트

- **4가지 세일즈 영역 (필수 입력)**: NC(조선소 계약) / NS(선주 CAC·New Delivery·Renewal) / BVN(장비 제조사 대상) / OTHER(독립 계약) — NC·NS·BVN은 무조건 Campaign에 연결 필수
- **Probability to Win 기준표 (수동 입력 금지, 선택만 가능)**:
  - Opportunity 단계: 기본 5%, 자신 있으면 25% (갱신형은 70%)
  - Proposal Under Prep: 기본 5%, 최대 70%
  - Proposal Issued: 기본 25%, 낙찰 확신 시 90%
  - Closed Won: 100% / Closed Lost: 0% (자동)
- **2025년 DQM 3대 KPI**: ① Win ratio (닫힌 건 중 수주율) ② Proposal lifetime (Close date vs 생성일 간격 — 짧으면 파이프라인 가시성 부족) ③ Logging frequency (주 1회 이상 로그인)
- **Engagement Committee**: 3m€ 이상 기회는 Salesforce 내 EC 프로세스 필수 — 대시보드에서 실시간 추적
- **이상적 Pipeline 분포**: Opportunity 60/65% / Proposal Under Prep 10/15% / Proposal Issued 20/30%

## 내 사업 적용 액션

- [ ] 나의 Opportunity 분류를 NC/NS/OTHER 구분에 맞춰 Campaign 연결 습관화
- [ ] 각 Opp의 Probability 값을 스테이지 기준표대로 유지 (임의 입력 금지)
- [ ] 파이프라인 분포를 월 1회 확인 — Opportunity 60%+ 유지 여부 체크
- [ ] 3m€ 이상 규모 딜은 EC 프로세스 체크리스트 사전 준비

## 원문 발췌

> "Small pipeline means no visibility! Let's show our BD efforts by registering maximum of opportunities"

> "We need to learn from our failure. Let's be as exhaustive as possible in registering opportunities in Salesforce"
