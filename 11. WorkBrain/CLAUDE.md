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

## Raw 라우팅 판단

새 파일이 들어오면 ingest 전에 **이 vault 소속인지 먼저 판단**한다. 판단 기준·예시·브리지 처리 방법은
`.claude/rules/routing.md`를 따른다 (두 vault 공통 규칙, 여기서 중복 유지하지 않음).

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
실행 시점·트리거 조건은 `.claude/rules/lint-routine.md` 참조.

## 변경 로그
- 2026-10-21: 라우팅표·lint 루틴을 `.claude/rules/`로 통일(중복 제거). `raw-classifier`(분류)·`wiki-reviewer`(검증) 서브에이전트를 ingest 파이프라인에 연결.
- 2026-10-22: `wiki-writer`(작성 전담) 서브에이전트 추가 — ingest가 판단(raw-classifier)·작성(wiki-writer)·검증(wiki-reviewer) 3단계로 완전 분리됨.
