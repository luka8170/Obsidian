---
tags:
  - standard
  - executive-briefing
  - kam
type: standard
source: "FW: Executive Engagement Briefings Standard — Jeffrey Guo, 2026-08-02"
related: "[[Executive Briefing Template]]"
---

# Executive Engagement Briefings Standard

## 왜
APA 지역 임원 미팅이 늘면서, Jeffrey Guo(APA)가 미팅 준비/사후관리를 표준화하자고 지시 (2026-08-02). HOMT가 만들고 있는 KAM 프레임워크를 대체하는 게 아니라, 그게 나오기 전까지 APA가 쓸 실무 방식. 브리핑팩·회의록·서포팅자료는 SharePoint에 올려서 팀 간 중복작업을 막는 것이 핵심.

## 실무 적용: 무엇을 어디서 채우나
원문이 요구하는 8개 브리핑 항목은 전부 채운다 — 다만 **이미 Salesforce에 있는 데이터는 링크만 걸고, 텍스트로 재입력하지 않는다**. 이중입력을 막는 게 핵심이지, 항목을 줄이는 게 핵심이 아니다.

| 원문 요구 항목 | 출처 | 노트에서 할 일 |
|---|---|---|
| 1. Meeting overview (목적/일시/참석자) | 직접 작성 | frontmatter `meeting_date` + 본문 목적/일시/참석자 |
| 2. Client leadership (사진/직책/약력) | Salesforce Contact 레코드 | 이름만 적고 상세(사진/약력)는 Contact 링크로 대체 |
| 3. 기존 BV 관계 (fleet in class, 계약, JDP/AIP, 파이프라인) | Salesforce Opportunity/Company | **Salesforce 링크 표**만 채운다 — fleet 수치·계약 내역을 텍스트로 재서술 금지 |
| 4. 최근 회사/시장 동향 | 직접 작성 | 1~3줄 |
| 5. 이전 미팅 요약 & 미이행 액션 | 과거 Executive Briefing 노트 | 같은 고객사 태그의 이전 노트에서 요약만, 아래 Dataview 인덱스가 목록은 자동으로 모아줌 |
| 6. 목표/기대 성과 | 직접 작성 | |
| 7. 핵심 메시지 & BV 역량 | 직접 작성 | |
| 8. Supporting info (org chart, fleet summary, timeline, competitor intel) | 기존 자료 있으면 링크, 없으면 직접 작성 | |

## 노트 작성 규칙
- 새 브리핑은 [[Executive Briefing Template]]로 생성 (Templater) — 8개 섹션 + Salesforce 링크 표 + Meeting Minutes 표 포함
- 파일 위치는 기존 `1. Project/일자별/YYYYMMDD ...` 폴더 규칙 그대로 — 폴더 재구조화 없음
- 태그는 `executive-briefing` + 고객사 태그(소문자, 예: `polaris`) 필수 — 검색과 아래 인덱스가 이 태그로만 찾는다
- **3번(기존 관계) 섹션은 Salesforce 링크만** — 여기가 이중입력이 가장 자주 생기는 지점이라 별도로 강조

## 사후관리
- [ ] 미팅 직후 "다녀와서" 섹션 채우기 (논의/액션/담당자/기한)
- [ ] SharePoint 업로드, 액션 완료 전까지 오픈 상태 유지
- [ ] Relationship Owner가 분기 1회 Salesforce Opportunity 스테이지 확인

## Executive Briefing 노트 인덱스 (자동)
```dataview
TABLE WITHOUT ID
  file.link as "노트",
  client as "고객사",
  meeting_date as "미팅일",
  relationship_owner as "담당자",
  salesforce_opportunity as "Salesforce"
FROM #executive-briefing
SORT meeting_date DESC
```

## 원문 (Jeffrey Guo, 2026-08-02)
> Dear Team,
>
> As our engagement with senior executives across Asia Pacific continues to increase, I'd like us to adopt a more consistent way of preparing for these meetings and capturing what we learn afterwards. This is not intended to replace the Key Account Management (KAM) framework that HOMT is developing. Rather, it gives APA a practical way of working now, and will make it much easier to align once the global framework is introduced.
>
> We already have a lot of good material from previous engagements with shipowners, shipyards, government, ports and other key customers. Instead of recreating information every time, let's consolidate it, keep it updated and build a common knowledge base for the region. Going forward, I'd like every executive engagement to include:
>
> - A short executive briefing before the meeting covering: meeting overview (purpose, date, attendees); client leadership (photos, positions, brief biographies); existing relationship with BV (fleet in class, vessels contracted/delivered/on order, JDPs, AIPs, strategic collaborations, commercial pipeline); recent company and market developments; summary of previous engagements and outstanding commitments; objectives of the visit and desired outcomes; key messages and relevant BV capabilities; supporting information where appropriate.
> - After the meeting, concise meeting minutes with key discussion points, agreed actions, action owner and target completion date. Actions should remain open until completed.
> - Each strategic account should have a Relationship Owner responsible for keeping the account profile up to date, coordinating executive briefings and following up outstanding actions.
> - All briefing packs, meeting minutes, presentations and supporting materials should be uploaded to the SharePoint repository so that future teams can easily understand the relationship history and avoid duplicating work.
>
> Let's treat this as our APA standard going forward. We can continue improving it and align it with the HOMT KAM framework when it is rolled out.
>
> Thanks everyone for your support.
>
> Jeffrey
