---
description: 하네스(AI 에이전트 환경)의 전반적인 건강 상태를 평가하고 자체 개선(Self-Improvement)을 진행하는 자율 워크플로우
---

## Preconditions
- `.agents/docs/evaluations/harness-metrics.md` 평가 지표 문서가 준비되어 있어야 함.
- 주기적인 점검이 필요하거나, 오류나 병목이 느껴질 때 구동됨.

## Steps

### 1. 상태 정기 점검
- `evaluate-harness` 스킬을 사용하여 최근 작업 및 로그 데이터를 수집하고, 현재 상태에 대한 진단 평가를 자동으로 실행한다.
- (결과물: 매 회차별 `.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md` 이력 생성)

### 2. 리포트 분석 및 즉각 반영
- 생성된 Health Report의 `Action Items` 중 즉각적으로 반영할 수 있는 가이드라인(예: `FRONTEND.md`, `BACKEND.md`) 오류, 또는 업데이트가 안 된 구형 `contexts/` 파일들의 내용 최적화를 수행한다.

### 3. 규칙 및 가이드라인 재편
- 쓸모없거나 반복해서 에이전트의 오작동을 야기하는 지시문을 파악하여, `rules/linter-rules.md` 나 관련 문서에서 삭제하거나 명확히 다시 명세한다.

### 4. 워크플로우 및 스킬 보완 (의사결정 필요 시)
- `manage-skills` 스킬이나 사용자 질의(AskUserQuestion)를 활용하여, 파손된 스킬을 복구하거나 워크플로우 명세의 Process 단계를 불필요한 공정이 남지 않게 리팩토링한다.

### 5. 개선 결과 업데이트 (Before / After 기록)
- 하네스가 성공적으로 자가 최신화를 마쳤다면, 이번 회차에 생성된 `.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md` 파일의 **'5. 적용 결과 (Resolution)'** 섹션에 어떤 부분이 어떻게 개선되었는지(Before / After)를 이어서 작성하고 프로세스를 종료한다. 별도의 관련 로그 파일은 만들지 않는다.

## Outputs
- `Action Items` 결과가 추가로 업데이트된 최종 `.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md` 
- 정비되고 개선된 `.agents/` 하위 문서, 수정된 Role 컨텍스트, 갱신된 워크플로우 스텝들

## Rollback
- 자가 개선 중 핵심 디자인 가이드(`ARCHITECTURE.md` 등)와 같은 문서를 파손하거나 잘못 변경했다면, Git Revert 또는 기존 백업으로 되돌린다.