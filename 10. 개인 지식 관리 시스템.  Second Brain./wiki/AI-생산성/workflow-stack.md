---
source: "Luka와의 대화로 직접 작성 (원본 raw 파일 없음, 현재 쓰는 도구 스택 자체가 소스)"
updated: 2026-04-19
tags: [AI, 생산성, 워크플로, Claude, Obsidian]
related: [[AI-생산성/second-brain-setup]], [[나-자신/luka-identity]]
---

# 현재 AI 워크플로 스택

## 핵심 도구
| 도구 | 역할 | 상태 |
|------|------|------|
| Claude (claude.ai) | 주력 AI 어시스턴트 | 매일 사용 |
| Claude Code | 자동화 에이전트 (Obsidian 조작, 파일 생성) | 활발히 사용 |
| Obsidian | 지식 저장소 (iCloud 동기화) | 메인 PKM |
| Desktop Commander | 파일시스템 자동화 MCP | 사용 중 |
| NotebookLM | 문서 기반 AI Q&A | CLI 설치 실험 중 |

## Obsidian Vault 구조
- 경로: `/Users/sangjinhan/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/`
- PARA 구조: 1.Project / 2.Area / 3.Resource / 4.Archive / 5.x 개인 시리즈
- **6. Second Brain** ← 현재 구축 중 (이 위키)

## 주요 자동화 워크플로
### 미팅 후 세일즈 인텔리전스 자동화
- 미팅 메모 → Claude Code → Obsidian 구조화 저장
- `1. Project/0. Sales Call/` 경로에 고객별 기록
- korean-shipping-intelligence Skill 활용

### Second Brain Ingest (신규)
- Raw 파일 추가 → Claude Code ingest → Wiki 자동 업데이트
- 이 파일이 바로 그 결과물

## 배운 것 / 인사이트
- RAG(매번 검색)보다 **LLM Wiki(컴파일)**가 개인 지식 관리에 더 적합
- AI는 유지보수를 귀찮아하지 않음 → 유지보수 비용 ≈ 0
- 가장 대체 불가능한 데이터는 '나에 대한 데이터'

## 관련 페이지
- [[second-brain-setup]] — Second Brain 구축 상세 기록
- [[luka-identity]] — 왜 이런 시스템을 만드는가
