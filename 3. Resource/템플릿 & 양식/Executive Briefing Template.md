---
tags:
  - executive-briefing
client: 
meeting_date: <% tp.date.now("YYYY-MM-DD") %>
relationship_owner: 
salesforce_opportunity: 
salesforce_company: 
related: "[[Executive Engagement Briefings Standard]]"
---

# <% tp.file.title %>

## 1. Meeting overview
- **목적:** 
- **일시:** <% tp.date.now("YYYY-MM-DD") %>
- **참석자:** 

## 2. Client leadership
> 사진/직책/약력은 Salesforce Contact 레코드가 원본 — 여기는 이름과 링크만
- 

## 3. 기존 BV 관계 (Salesforce 원본, 재입력 금지)
| 구분 | Salesforce 링크 |
|---|---|
| Company | `[ ]` |
| Opportunity — | `[ ]` |

## 4. 최근 회사/시장 동향
- 

## 5. 이전 미팅 요약 & 미이행 액션
- 

```dataview
LIST
FROM #executive-briefing AND #<% tp.file.title %>
WHERE file.name != this.file.name
SORT meeting_date DESC
```

## 6. 목표 및 기대 성과
- 

## 7. 핵심 메시지 & BV 역량
- 

## 8. Supporting information
- **Fleet summary**: 
- **Org chart**: 
- **Competitor intelligence**: 
- **Project timeline**: 

---

## 하지 말 것
- 

## 확인 필요 (미팅 전)
- [ ] 

## 다녀와서 — Meeting Minutes
| 논의 내용 | 액션 | 담당자 | 기한 | 상태 |
|---|---|---|---|---|
| | | | | ⬜ Open |

- [ ] SharePoint 업로드
- [ ] Salesforce Opportunity 스테이지/Activity 업데이트
