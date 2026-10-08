---
week: <% tp.date.now("YYYY-[W]WW") %>
start: <% tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY-[W]WW") %>
tags: [weekly]
---

# Week <% tp.date.now("WW, YYYY") %>

## 🎯 Weekly Goals
- [ ] 

## 📊 Weekly Summary

### 주요 성과


### 진행 중인 프로젝트
- 

### 주요 미팅 및 활동


## 📈 이번 주 일일 노트
```dataview
TABLE WITHOUT ID
  file.link as "날짜",
  join(filter(file.lists.text, (x) => contains(x, "✅")), ", ") as "완료 항목"
FROM "1. Project"
WHERE contains(file.name, "<% tp.date.now("YYYY-MM") %>")
SORT file.name ASC
```


## 💡 Key Insights


## 🔄 Next Week Planning
- [ ] 

## 📌 Important Links & References


---
**이전 주:** [[<% tp.date.now("YYYY-[W]WW", -7, tp.file.title, "YYYY-[W]WW") %>]] | **다음 주:** [[<% tp.date.now("YYYY-[W]WW", 7, tp.file.title, "YYYY-[W]WW") %>]]
