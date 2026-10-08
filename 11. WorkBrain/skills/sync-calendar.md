---
name: second-brain-sync-calendar
description: |
  Google Calendar 일정을 가져와 Daily Note와 Weekly 페이지를 자동 업데이트한다.
  트리거: "캘린더 동기화해줘", "오늘 일정 가져와줘", "이번 주 일정 업데이트해줘"
  Outlook 일정은 수동 입력 또는 별도 연동 필요 (현재 Google Calendar MCP만 지원)
---

# SYNC-CALENDAR — 캘린더 동기화 커맨드

Google Calendar에서 일정을 가져와 Obsidian Daily/Weekly 노트에 반영한다.

## 실행 로직

### Step 1: 캘린더 조회
Google Calendar MCP로 일정 조회:
- **오늘 동기화**: 오늘 00:00 ~ 23:59 (Asia/Seoul)
- **이번 주 동기화**: 이번 주 월요일 ~ 일요일
- **특정 날짜**: 사용자가 지정한 날짜 범위

```
timeZone: Asia/Seoul
orderBy: startTime
```

### Step 2: Daily Note 업데이트
조회 날짜에 해당하는 Daily Note 파일 확인:
- 파일명: `YYYY-MM-DD.md` (vault 루트)
- 없으면 아래 템플릿으로 신규 생성
- 있으면 `## 📅 오늘 일정` 섹션만 업데이트

**Daily Note 템플릿:**
```markdown
---
date: YYYY-MM-DD
type: daily
tags: [daily, 업무관리]
week: "[[11. WorkBrain/wiki/업무-관리/YYYY-WXX-weekly]]"
---

# YYYY-MM-DD (요일)

## 📅 오늘 일정
> Google Calendar 동기화: YYYY-MM-DD 기준
{캘린더 일정 목록}

---

## ✅ To-Do

### 🔴 오늘 반드시
- [ ] 

### 🟡 이번 주 안에
- [ ] 

### 🟢 언제든
- [ ] 

---

## 🧠 오늘의 생각 / 메모
> 여기에 자유롭게 기록. "ingest 해줘"하면 wiki로 연결됨.

---

## 🔗 관련 프로젝트
- [[11. WorkBrain/wiki/해운-영업/key-clients]]
```

**일정 형식:**
- 종일 이벤트: `- 📌 [제목]`
- 시간 이벤트: `- HH:MM–HH:MM [제목]`
- 미팅(참석자 있음): `- HH:MM–HH:MM 👥 [제목]`

### Step 3: Weekly Note 업데이트
해당 주의 Weekly Note 확인:
- 파일명: `11. WorkBrain/wiki/업무-관리/YYYY-WXX-weekly.md`
- 없으면 신규 생성, 있으면 `## 📅 이번 주 캘린더` 테이블만 업데이트

**주차 계산**: ISO 8601 기준 (월요일 시작)

### Step 4: _Index.md 업무-관리 섹션 업데이트
새 Weekly 페이지 생성 시 인덱스에 추가:
```
11. WorkBrain/wiki/_Index.md
```

## 결과 보고
```
📅 캘린더 동기화 완료

이번 주 일정 (W17):
- 수 4/22 16:00 Monthly Tanker Tribunal
- 금 4/24 11:00 MMS Project Update Meeting

업데이트된 파일:
- 2026-04-19.md (Daily Note)
- wiki/업무-관리/2026-W17-weekly.md
```

## 주의사항
- 캘린더 일정은 읽기만 함. 수정/삭제 절대 금지.
- To-Do 섹션은 덮어쓰지 않음 (사용자가 직접 작성한 내용 보존)
- 일정 섹션만 갱신
- Outlook 일정은 현재 자동 연동 불가 → 사용자가 수동으로 Weekly Note에 추가
