---
source: "Luka와의 대화로 직접 작성 (원본 raw 파일 없음, Second Brain 구축 과정 자체가 소스)"
updated: 2026-04-19
tags: [AI, second-brain, 구축기록, Obsidian]
related: [[AI-생산성/workflow-stack]], [[나-자신/luka-identity]]
---

# Second Brain 구축 기록

## 구축 동기
- 2026-04-19: YouTube 영상 "AI로 나를 복제했습니다 | 클로드 코드 × 옵시디언 × LLM Wiki" 시청
- Andrej Karpathy의 LLM Wiki 개념에서 영감
- 핵심 통찰: RAG(매번 검색) → Compile(AI가 위키 직접 관리)로 패러다임 전환

## 설계 결정
| 결정 | 선택 | 이유 |
|------|------|------|
| 저장소 | 기존 vault 통합 | PARA 구조 유지, 기존 워크플로와 연속성 |
| 폴더명 | `6. Second Brain/` | 기존 5.x 개인 시리즈와 구분 |
| 주제 범위 | 나 자신 + 해운/영업 + AI/생산성 + 커리어 전환 | 가장 가치 있는 개인 데이터 |
| Raw 원재료 | Claude 대화 메모리 우선 | 이미 가장 풍부한 개인 지식 보유 |

## 초기 구축 (2026-04-19)
- [x] `CLAUDE.md` 시스템 설계도 작성
- [x] `raw/claude-memory/luka-profile.md` 시드 데이터 생성
- [x] `wiki/_Index.md` 인덱스 생성
- [x] `wiki/나-자신/luka-identity.md`
- [x] `wiki/나-자신/career-history.md`
- [x] `wiki/해운-영업/key-clients.md`
- [x] `wiki/해운-영업/bv-internal.md`
- [x] `wiki/AI-생산성/workflow-stack.md`
- [x] `wiki/AI-생산성/second-brain-setup.md` (이 파일)
- [x] `wiki/커리어-전환/customs-broker.md`

## 다음 단계
- [ ] Claude Code Skills에 `ingest`, `query`, `lint` 커맨드 등록
- [ ] 첫 번째 query 테스트: "내 의사결정 패턴은?"
- [ ] 첫 번째 lint 실행
- [ ] 새 raw 원재료 추가: 업무 이메일, 기존 Obsidian 메모

## 관련 페이지
- [[workflow-stack]] — 전체 AI 스택
- [[luka-identity]] — 구축 동기
