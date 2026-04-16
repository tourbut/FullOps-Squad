---
name: evaluate-harness
description: 하네스의 전체 성능 지표(harness-metrics.md)를 평가하고 상태 보고서(harness-health-report.md)를 생성합니다.
argument-hint: "[선택사항: 특정 집중 평가 영역(예: contexts, workflows)]"
---

# 하네스 상태 정기 측정 스킬 (Evaluate Harness)

## 목적

하네스가 현재 원활하게 동작하고 있는지 객관적인 지표를 통해 평가하여 분석 리포트를 생성합니다. 이 스킬은 `/improve` 워크플로우의 첫 번째 단계로 사용되어 하네스 최적화 로직의 기틀을 마련합니다.

## 실행 시점

- 작업 방식이나 빈번한 에러로 개발 과정(핑퐁 구간 등)에 심각한 병목이 느껴질 때.
- 일정 스프린트 종료 후, 또는 `.agents` 설정을 전반적으로 개선하고 싶을 때 (`/improve` 명령어를 통해).
- 주기적으로 문서들의 노후 상태(Drift)를 파악하고자 할 때.

## 워크플로우

### Step 1: 측정 기준 로드
`docs/evaluations/harness-metrics.md` 파일에 기재된 평가 기준(Handover 효용성, 규칙 준수율, 도구 효율성)을 로드합니다.

### Step 2: 현황 로그 및 패턴 수집
다음의 디렉토리나 파일을 탐색하여 점수 평가에 필요한 데이터를 추출합니다:
1. `handovers/logs/` 위치의 과거 작업 기록 분석(핑퐁 및 반복 작업율 추출)
2. `contexts/` 파일들의 최종 업데이트 내역 (작업 완료 후 업데이트 미준수 여부 추적)
3. `rules/linter-rules.md` 수정 이력 대비 검증 스킬(`verify-implementation`) 보고서 내 이슈 빈도
4. 기타 에러 로그 분석

### Step 3: 점수 도출 및 리포트 작성
추출된 데이터와 기준 지표를 종합하여 100점 만점의 `Harness Health Score`를 도출합니다.
이를 바탕으로 개선이 필요한 영역에 대해서 Action Item을 구성하여 `.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md` (날짜 포함) 파일로 최종 포맷팅 및 생성합니다. (매 진단마다 이력을 남기기 위해 덮어쓰지 않고 날짜를 붙여 새 파일로 생성)

## Output Format (생성 보고서 구조)

`.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md` 생성 시, 반드시 **아래의 마크다운 양식(Template)**을 준수하여 작성해야 합니다.

```markdown
# Harness Health Report
> **Date**: YYYY-MM-DD
> **Evaluator**: evaluate-harness 스킬

## 1. 종합 평가 (Overall Health)
- **Harness Health Score**: [A / B / C / D] (예: 85/100)
- **종합 소견**: (현재 하네스의 상태 및 핵심 문제점에 대한 2~3줄 요약)

## 2. 지표별 상세 분석
### 2.1 Handover(이관) 효용성 
- **결과**: (예: 우수 / 양호 / 주의)
- **관찰 내역**: (수집된 핑퐁 횟수 로그, 태스크 지연 상태 요약)

### 2.2 컨텍스트 및 원칙(Rule) 준수율
- **결과**: (예: 우수 / 양호 / 주의)
- **관찰 내역**: (린터 위반 발생 빈도 관리, 아키텍처 문서의 무시/위반 사례 요약)

### 2.3 도구 및 워크플로우 효율성
- **결과**: (예: 우수 / 양호 / 주의)
- **관찰 내역**: (에이전트 스킬 실패 기록이나 워크플로우 중단/롤백 사례 요약)

## 3. 주요 문제점 (Identified Issues)
- (도출된 핵심 문제점 1: 구체적인 상황)
- (도출된 핵심 문제점 2)

## 4. Action Items (최적화 권고 사항)
- [ ] **(문서 수정/삭제)**: `대상/파일/경로` - (어떤 내용을 추가하거나 지워야 하는지 명시)
- [ ] **(스킬/워크플로우 개선)**: `대상/파일/경로` - (어떻게 개선/리팩토링 해야 하는지 명시)

## 5. 적용 결과 (Resolution) - ※ `/improve` 워크플로우 실행 완료 시 추가 작성됨
### [수정 대상 파일명 1]
- **Before**: (기존 내용 또는 상태)
- **After**: (수정한 상태 및 로그)
```

## Exceptions

- 당장 분석할 만한 과거 `handovers/logs/`가 충분히 쌓여있지 않은 경우 점수 평가는 보류하되, "데이터 부족" 사유와 함께 임시 리포트만 발행합니다.
- 평가 중 자동 스크립트 에러 등의 이슈는 점수 감점이 아니라 스킬 안정성 개선 대상(Action Item)으로 취급합니다.

## Related Files

| File | Purpose |
|------|---------|
| `.agents/docs/evaluations/harness-metrics.md` | 판단 기준 지표 문서 |
| `.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md` | 최종 리포트 및 적용 이력 목적지 |
