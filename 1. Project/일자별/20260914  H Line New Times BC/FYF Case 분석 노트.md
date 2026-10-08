---
tags: [FYF, H-Line, Newcastlemax, analysis-note]
status: draft
---

# H-Line Newcastlemax 210K BC — Annual FYF Case 1~4 분석 노트

> 근거 파일: `EC Financial sheet NTS_H-Line_2 x Newcastlemax LNG Case 1~4_20260914.xlsx` (`NS FYF without free` 시트)
> [[H-Line Newcastlemax Annual FYF 승인 요청]] 작성을 위해 진행한 분석 과정 기록

## 1. Case 1~4 기본 비교

Dual class(BV+KR)만 유효 옵션(고객 요건상 Single class 없음) → Case 1·2만 실질 후보, Case 3·4는 Single class 가정이라 참고용.

| | Case 1 | Case 2 | Case 3 | Case 4 |
|---|---|---|---|---|
| Class 가정 | Dual | Dual | Single | Single |
| Total survey points | 110,224 | 110,224 | 76,822 | 76,822 |
| Annual FYF (6년차~, USD/ship/yr) | 40,000 | 25,000 | 30,000 | 20,000 |
| Korea 로컬 man-days(5yr) | 32 | 52 | 32 | 52 |
| 15년 블렌디드 마진 | 19.8% | **29.0%** | 23.4% | 30.8% |
| 15년 누적 이익(척당) | $299,780 | **$308,532** | $284,299 | $281,642 |

## 2. Case 1(FYF $40,000)이 Case 2(FYF $25,000)보다 수익성 낮은 이유

FYF 금액은 Case 1이 더 높지만, **원가 구조 차이가 매출 증가분을 잠식**함.

### International Cost(해외 서베이어 투입 비용)

| | Case 1 | Case 2 | 차이 |
|---|---|---|---|
| Term1 | -$80,483 | -$35,195 | -$45,288 |
| Term2 | -$94,687 | -$48,709 | -$45,978 |
| Term3 | -$120,661 | -$58,455 | -$62,206 |

Case 1은 Korea 로컬 투입(32 man-days)이 적고 해외(China/Australia) 투입 비중이 높은 딜리버리 모델이라 원가가 더 비싸며, 이 격차가 선령이 늘수록(Term3) 더 벌어짐.

### HO Fee(본사 수수료, 매출 연동)

Case 1은 매출 기준(FYF $200,000/term)이 Case 2($125,000/term)보다 커서, 매출의 25.7%로 부과되는 HO Fee도 그만큼 더 나감 (Term1 기준 -$62,433 vs -$43,158).

### Term별 실제 Profit(척당)

| | Case 1 | Case 2 | 차이 |
|---|---|---|---|
| Term1 | $71,184 | $66,652 | Case1 우위 (+$4,532) |
| Term2 | $54,402 | $50,910 | Case1 우위 (+$3,491) |
| Term3 | $24,304 | $36,704 | **Case2 역전 (-$12,399)** |
| 15년 합계 | $149,890 | **$154,266** | Case2가 +$4,376 높음 |

Term1·2까지는 Case1이 절대금액으로 근소 우위지만, Term3에서 International Cost가 급증하며 역전 → 15년 누적으로는 Case2가 마진·절대이익 모두 우위.

## 3. "중국 위주 검사" 조건 재검토 시도 — 확인된 사실 및 한계

사용자 요청: Case별 수치를 중국(China) 위주 검사 조건으로 다시 산출. 시트의 Case별 formula를 대조한 결과, **Case 1~4는 이미 서로 다른 지역 투입 비중을 전제로 설계**되어 있었음이 확인됨.

| | Case 1 | Case 2 | Case 3 | Case 4 |
|---|---|---|---|---|
| 지역 배분 전제(A4 셀) | 35% Korea + 30% China + 35% Aus | 35% Korea + 30% China + 35% Aus (수식상 Aus 항 제거) | 35% Korea + 30% China + 35% Aus | **70% Korea + 30% China** (Aus 없음) |
| International Cost 산식(M10) | China+Aus 모두 반영 | China만 반영 | China+Aus 모두 반영 | **China만 반영** |
| OOS Cost 산식(S10) | China 30% + Aus 35% | China 30%만 | China 30% + Aus 35% | **China 30%만** |

→ Case 2·4가 이미 "호주 제외, Korea+China만" 구조. "중국 위주"로 재산출하려면 Case 2/4의 배분(A4)을 Korea 비중은 낮추고 China 비중을 높이는 방향으로 조정해야 함.

**한계**: International Cost·PSC 등 원가 산식이 외부 연결 워크북 `'[26]GIC back data'`를 참조하고 있으며, 이 파일은 현재 폴더에 없어(끊어진 외부링크) **정확한 재계산 불가**. 캐시된 값(현재 Case별 결과값)만 확인 가능하고, 배분 비율을 바꾼 새 시나리오의 정확한 달러 값은 원본 `GIC back data` 워크북 없이는 산출할 수 없음. NC/NS 담당자에게 해당 외부 파일 확보 요청 필요.

## 4. Next step

- [ ] `[26]GIC back data.xlsx` (또는 해당 외부 링크 파일) 확보 — Bong Seok KANG(NS) 또는 NC팀에 문의
- [ ] 확보 후 "China 위주"(예: Korea 20~30% / China 70~80%) 비중으로 M10/S10 산식 재계산하여 Case 5로 추가 비교
