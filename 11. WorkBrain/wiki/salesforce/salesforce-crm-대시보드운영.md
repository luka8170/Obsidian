---
source: "Salesforce 2nd coffee (2021-10) + 16th coffee (2023)"
date: 2026-06-30
tags: [#비즈니스, #시스템]
related: "[[bv-internal]], [[salesforce-mo-세일즈프로시저-2025]]"
---

# Salesforce CRM 대시보드 운영 원칙

## 핵심 인사이트

- **Report → Dashboard 순서 필수**: Report를 먼저 만들어야 Dashboard를 만들 수 있음. Dashboard는 Summary/Matrix 리포트 타입의 시각적 표현
- **4가지 리포트 타입 구분**: Tabular(단순 목록, 대시보드 불가) / Summary(소계+차트 가능, 대시보드 적합) / Joined(최대 5블록) / Matrix(행+열 교차 집계)
- **대시보드 그래픽 4종**: Gauge(목표 대비 진척) / Table(Top5 등 순위) / Metric(단일 숫자) / Chart(비교) — 대시보드당 최대 20 컴포넌트
- **계층별 파이프라인 추적**: 개인(Sales Rep Dashboard) → 팀(Team Selling Pipeline) → 로컬팀(Local Team Pipeline) → 글로벌(Excom/Zone Dashboard) 4단계로 분리 운영
- **주간 리뷰 3대 지표**: ① Close date 갱신 여부 ② Overdue + 14일 내 만기 Opp 정리 ③ 리드 전환율(New lead current year)
- **즐겨찾기 활용**: 자주 보는 Report/Dashboard를 Favorite 등록 → 주간/월간 리뷰 시 원클릭 접근

## 내 사업 적용 액션

- [ ] 현재 파이프라인 추적을 위한 Summary Report 생성 (Stage별 Opp 분포 시각화)
- [ ] Sales Rep Dashboard를 매주 월요일 루틴으로 확인하는 습관 세팅
- [ ] Overdue Opp 정리 기준 14일을 내 영업 캘린더에 알림 설정
- [ ] 주간 리뷰에 쓸 리포트/대시보드 3개 Favorite 등록

## 원문 발췌

> "Make Salesforce your unique daily tool to track your projects, associate deals and commercial actions"

> "No need to use excel file to be updated regularly, reports and dashboard are updated in a real time — you have all your sales history in a single place"
