---
tags: [dashboard]
created: 2026-01-05
---

# 🎯 Projects Dashboard

## 📅 Quick Navigation
- [[Users/sangjinhan/2026-01-05|오늘]]
- [[2026-W02|이번 주]]
- [[2026-01|이번 달]]

## ⏰ 이번 주 미완료 작업
```dataview
TASK
FROM ""
WHERE !completed 
  AND contains(file.name, "2026-01")
GROUP BY file.link
SORT file.name DESC
```

## 🚢 HMM 관련 최근 노트
```dataview
LIST
FROM #HMM OR [[HMM]]
SORT file.mtime DESC
LIMIT 10
```

## 🔒 사이버보안 프로젝트
```dataview
TABLE file.ctime as "생성일", file.mtime as "수정일"
FROM #cybersecurity OR [[사이버보안]]
SORT file.mtime DESC
LIMIT 10
```

## 📊 최근 7일간 활동
```dataview
TABLE WITHOUT ID
  file.link as "날짜",
  length(file.lists) as "항목 수"
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
  AND contains(file.name, "2026")
SORT file.name DESC
```

## 🏗️ 신조선 프로젝트
```dataview
LIST
FROM #newbuilding OR [[신조선]]
SORT file.mtime DESC
LIMIT 10
```

## 📝 최근 미팅 노트
```dataview
TABLE file.ctime as "날짜"
FROM ""
WHERE contains(file.content, "미팅") OR contains(file.content, "Meeting")
SORT file.ctime DESC
LIMIT 10
```
