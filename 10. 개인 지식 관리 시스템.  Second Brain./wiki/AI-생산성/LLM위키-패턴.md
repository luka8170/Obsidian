---
updated: 2026-06-10
tags: [LLM위키, 옵시디언, 클로드코드, 지식관리, AI도구]
related: [[second-brain-setup]], [[workflow-stack]], [[PARA-세컨드브레인]]
source: raw/2026-05-17_아티클_Karpathy-LLM위키-패턴.md, raw/2026-05-17_유튜브_옵시디언-클로드코드-결합.md
---

# LLM-Wiki 패턴 (Karpathy)

> 출처: Andrej Karpathy (전 OpenAI/Tesla AI 책임자) | 채널: 태오 유튜브
> 핵심: **"Obsidian = IDE, LLM = 프로그래머, Wiki = 코드베이스"**

## 핵심 비유

| 도서관 비유 | 개발자 비유 |
|------------|------------|
| 도서관 건물 | IDE (Obsidian) |
| 사서 | LLM (Claude Code) |
| 정리된 책꽂이 | Wiki (코드베이스) |
| 책을 사오는 나 | Raw에 정보를 던지는 사람 |

## Raw / Wiki 분리 철학

- **Raw**: 외부에서 들어오는 날것의 정보. 필터링 없이 저장.
- **Wiki**: LLM이 Raw를 읽고 내 기준에 맞는 것만 정제·보관.
- 둘을 섞으면 안 된다 — Raw는 inbox, Wiki는 source of truth.

## 왜 Wiki가 강력해지는가

1. 시간이 쌓일수록 "내 기준을 통과한 것만" 모인다
2. 중복 없이 압축된 나만의 지식베이스 형성
3. LLM이 Wiki를 context로 쓸수록 나를 더 잘 이해한다
4. **1개월 → 3개월 → 6개월: 가치가 기하급수적으로 증가**

> "The wiki becomes more valuable the more you use it — it's a compounding asset."

## 운영 사이클

```
사람이 Raw에 정보를 던진다
       ↓
LLM이 읽고 Wiki 기준에 맞는지 판단
       ↓
통과 → Wiki의 올바른 위치에 분류·압축·저장
       ↓
비슷한 개념끼리 위키링크로 연결
```

## 슬래시 커맨드 체계

| 명령 | 역할 |
|------|------|
| `/ingest` | Raw 소화 → Wiki 정제 박제 |
| `/query` | Wiki 큐레이션 검색 (읽기 전용) |
| `/lint` | Wiki 구조 오류 진단 |

## Luka 적용 포인트

- 이 Second Brain 시스템이 바로 LLM-Wiki 패턴의 구현체
- Raw 폴더에 책/유튜브/뉴스를 던지면 Claude가 사서 역할
- Wiki가 쌓일수록 "나를 아는 AI"가 만들어진다
- **핵심**: 정보를 모으는 것이 아니라 필터링하는 시스템이 경쟁력
