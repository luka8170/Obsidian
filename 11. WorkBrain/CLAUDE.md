# CLAUDE.md — WorkBrain 시스템 설계도

## 목적
이 vault는 Luka(한상진)의 **해운 영업 업무 지식**을 관리한다.
BV Korea 영업 전략, 고객사 인텔리전스, 업무 관리를 AI가 유지하는 지식 위키.

## 폴더 구조
```
11. WorkBrain/
├── CLAUDE.md          ← 이 파일
├── raw/               ← 원재료. 읽기만 함. 절대 수정 금지.
│   ├── claude-memory/ ← Claude 대화에서 추출한 지식
│   └── 해운-업무/     ← 해운 관련 문서, 보고서
└── wiki/              ← Claude가 생성·관리하는 위키
    ├── _Index.md      ← 전체 페이지 인덱스
    ├── 해운-영업/     ← 고객사, BV 내부, 영업 전략, 업계 동향
    └── 업무-관리/     ← Weekly 노트, 일정 관리
```

## Raw 라우팅 판단 트리

새 파일이 들어오면 ingest 전에 **이 vault 소속인지 먼저 판단**한다.

| 내용 유형 | 소속 | 예시 |
|-----------|------|------|
| 해운 업계 동향, 시장 분석 | ✅ WorkBrain | VLCC 운임, Sinokor 동향 |
| 고객사 인텔리전스, BV 영업 | ✅ WorkBrain | 미팅 메모, 고객 관계 |
| 선박금융, 신조 발주 뉴스 | ✅ WorkBrain | 중국 리스, Pan Ocean |
| 독서, 마인드셋, 자기계발 | ❌ Second Brain | 습관, 몰입, 투자 서적 |
| AI 도구 학습 (개인 목적) | ❌ Second Brain | Claude 활용법 |
| AI를 업무에 적용하는 방법 | **브리지** → 둘 다 | AI로 고객 리서치 자동화 |

**브리지 인사이트 처리**: 두 vault에 모두 해당하는 내용은 각 vault에 요약하고 상호 참조 메모를 남긴다.
- WorkBrain 쪽: `> 🔗 Second Brain 연결: [[페이지명]] 참조`
- Second Brain 쪽: `> 🔗 WorkBrain 연결: [[페이지명]] 참조`

**판단이 모호할 때**: "이 내용이 BV 영업에 직접 쓰이는가?" → Yes면 WorkBrain, No면 Second Brain.

## 핵심 규칙
- **raw/** 폴더는 불변. Claude는 읽기만 하고 절대 수정하지 않는다.
- **wiki/** 폴더는 Claude가 전적으로 소유.
- 모든 위키 페이지는 관련 페이지를 `[[위키링크]]`로 상호 연결한다.
- `_Index.md`는 새 페이지 생성 시 항상 업데이트한다.
- **개인 내용(독서, 자기계발, 커리어 전환)은 이 vault에 기록하지 않는다.**

## 카테고리 정의
- `해운-영업/` — 고객사(Sinokor, HMM, Polaris 등), BV 내부 관계, 영업 전략, 업계 동향
- `업무-관리/` — Weekly 노트, 미팅 기록, 액션 아이템

## 3가지 핵심 작업
- `ingest` — raw/ 새 파일 → wiki/ 페이지 생성
- `query` — wiki 기반 질의응답
- `lint` — wiki 품질 점검
- `sync-calendar` — Google Calendar → Weekly 노트 동기화

## lint 루틴

**실행 시점 (둘 중 하나)**
1. Weekly 노트 생성 시 → 노트 작성 후 자동으로 lint 실행
2. ingest 3회 누적 후 → "raw 파일 N개 처리 완료" 보고 시 lint 권장 알림

**lint 트리거 조건** (자동 감지):
- 마지막 lint 날짜가 7일 이상 경과한 상태에서 ingest가 실행될 경우
  → ingest 완료 후 "⚠️ 마지막 lint: N일 전 — lint 실행을 권장합니다" 안내
