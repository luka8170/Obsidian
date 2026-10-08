# Obsidian Daily Journal 설정 가이드

생성일: 2026-01-05
태그: #guide #setup #obsidian

---

## 📚 설치된 플러그인

- ✅ **Calendar** - 달력 뷰
- ✅ **Periodic Notes** - Daily/Weekly/Monthly 노트 자동 생성
- ✅ **Templater** - 동적 템플릿
- ✅ **Dataview** - 데이터 쿼리 및 집계

---

## ⚙️ Periodic Notes 설정

### 1. Settings → Periodic Notes 열기

### 2. Daily Notes 설정
```
Format: YYYY-MM-DD
Template: 3. Resource/템플릿 & 양식/Daily Template.md
Folder: 1. Project (또는 원하는 위치)
```

### 3. Weekly Notes 설정
```
Enabled: ✅
Format: YYYY-[W]WW
Template: 3. Resource/템플릿 & 양식/Weekly Template.md
Folder: 1. Project/Weekly (새로 생성)
```

### 4. Monthly Notes 설정
```
Enabled: ✅
Format: YYYY-MM
Template: 3. Resource/템플릿 & 양식/Monthly Template.md
Folder: 1. Project/Monthly (새로 생성)
```

---


## ⚙️ Templater 설정

### Settings → Templater

1. **Template folder location**
   ```
   3. Resource/템플릿 & 양식
   ```

2. **Trigger Templater on new file creation**
   - ✅ 활성화

3. **Enable Folder Templates** (중요!)
   - ✅ 활성화
   - Add New 클릭하여 폴더별 템플릿 매핑:
   
   | Folder | Template |
   |--------|----------|
   | `1. Project` | `Daily Template.md` |
   | `1. Project/Weekly` | `Weekly Template.md` |
   | `1. Project/Monthly` | `Monthly Template.md` |

---

## 🎨 Calendar 설정

### Settings → Calendar

```
Dot threshold: 0 (모든 노트에 점 표시)
Weekly note format: YYYY-[W]WW
Monthly note format: YYYY-MM
Show week number: ✅ (선택사항)
```

### 오른쪽 사이드바에 Calendar 표시
- 오른쪽 상단 사이드바 아이콘 클릭
- 또는 단축키: `Ctrl/Cmd + Alt + →`

---

## 🚀 사용 방법

### 일일 노트 작성
1. **Calendar에서 날짜 클릭** 또는
2. **단축키**: `Ctrl/Cmd + P` → "Open today's daily note"
3. 자동으로 Daily Template 적용됨
4. Today's Focus에 오늘의 핵심 업무 3가지 작성


### 주간 리뷰 (금요일 또는 월요일)
1. `Ctrl/Cmd + P` → "Periodic Notes: Open Weekly Note"
2. Dataview가 자동으로 이번 주 일일 노트 목록 표시
3. Weekly Goals 달성도 확인
4. 다음 주 계획 작성

### 월간 리뷰 (월말)
1. `Ctrl/Cmd + P` → "Periodic Notes: Open Monthly Note"
2. Dataview가 자동으로 이번 달 통계 표시
3. 주요 성과 정리
4. 다음 달 목표 설정

### 대시보드 활용
1. Dashboard Template으로 새 노트 생성
2. 프로젝트별 진행 상황 한눈에 파악
3. 북마크하여 빠른 접근

---

## 💡 추천 단축키 설정

Settings → Hotkeys에서 설정:

| 기능 | 추천 단축키 |
|------|------------|
| Open today's daily note | `Ctrl/Cmd + D` |
| Open this week's weekly note | `Ctrl/Cmd + W` |
| Templater: Create new note | `Ctrl/Cmd + T` |
| Toggle right sidebar | `Ctrl/Cmd + Alt + →` |

---

## 📌 활용 팁

### 태그 전략
```
#project/hmm - HMM 관련
#project/cybersecurity - 사이버보안
#project/newbuilding - 신조선
#meeting - 미팅 노트
#important - 중요 항목
```

### 링크 활용
- 프로젝트: `[[Project - HMM Container]]`
- 인물: `[[Christophe Vaes]]`
- 회사: `[[Bureau Veritas]]`
- 양방향 링크로 관계 파악


### Dataview 쿼리 예시

**미완료 작업 목록**
\```dataview
TASK
FROM ""
WHERE !completed
GROUP BY file.link
\```

**최근 7일 활동**
\```dataview
LIST
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
\```

**프로젝트별 노트**
\```dataview
TABLE file.ctime as "생성일"
FROM #project
SORT file.mtime DESC
\```

---

## 🔧 트러블슈팅

### Calendar가 보이지 않을 때
1. 오른쪽 사이드바 토글 확인
2. Settings → Community plugins → Calendar 활성화 확인
3. View → Right sidebar → Show calendar

### 템플릿이 자동 적용 안 될 때
1. Templater → Folder Templates 설정 확인
2. "Trigger Templater on new file creation" 활성화 확인
3. 템플릿 파일 경로가 정확한지 확인

### Dataview 쿼리가 작동 안 할 때
1. Settings → Dataview → Enable JavaScript Queries 확인
2. 쿼리 문법 확인 (백틱 3개로 감싸기)
3. FROM 경로가 정확한지 확인

---

## 📚 추가 자료

- [Templater 문서](https://silentvoid13.github.io/Templater/)
- [Dataview 문서](https://blacksmithgu.github.io/obsidian-dataview/)
- [Periodic Notes 문서](https://github.com/liamcain/obsidian-periodic-notes)

---

**작성자**: Claude with Desktop Commander
**최종 수정**: 2026-01-05
