---
month: 2026-01
tags: [monthly]
---

# 2026년 01월

## 📈 Monthly Overview

### 월간 목표


### 주요 프로젝트 및 성과


### 핵심 수치 및 지표


## 📊 이번 달 통계

### 일일 노트 작성 현황
```dataview
TABLE WITHOUT ID
  file.link as "날짜",
  choice(file.tags, "✅", "📝") as "상태"
FROM ""
WHERE contains(file.name, "2026-01") 
  AND file.name != this.file.name
SORT file.name ASC
```

### 주요 활동 카테고리별 정리
```dataview
TABLE WITHOUT ID
  rows.file.link as "관련 노트"
FROM ""
WHERE contains(file.name, "2026-01")
  AND (contains(file.content, "HMM") OR contains(file.content, "사이버보안") OR contains(file.content, "신조선"))
GROUP BY 
  choice(contains(file.content, "HMM"), "🚢 HMM", 
  choice(contains(file.content, "사이버보안"), "🔒 사이버보안",
  choice(contains(file.content, "신조선"), "🏗️ 신조선", "📋 기타")))
```


## 💭 Monthly Reflection

### 잘된 점


### 개선이 필요한 점


### 배운 점 및 인사이트


## 🎯 Next Month Goals
- [ ] 

## 📌 중요 문서 및 참고자료


---
**이전 달:** [[<% tp.date.now("YYYY-MM", -1, "month") %>]] | **다음 달:** [[<% tp.date.now("YYYY-MM", 1, "month") %>]]
