---
description: 상위 레벨 태스크를 역할별 Handover 파일로 분배·지시
---

## Preconditions
- 설계 산출물·기획안·버그 리포트 등 분할되지 않은 요구사항이 존재해야 함.
- 현행 아키텍처·로드맵 문서를 통해 전체 맥락을 파악할 수 있어야 함.

## Steps

### 1. 현황·컨텍스트 분석
다음 문서를 읽고 현재 프로젝트 상태(완료/진행/예정)를 파악한다.
- `ARCHITECTURE.md`, `PLANS.md`(Phase 인덱스·상태), `docs/design-docs/core-beliefs.md`
- 특정 Phase의 세부 태스크가 필요하면 `PLANS.md` 인덱스의 링크를 따라 `docs/exec-plans/phases/phaseNN.md`만 선택적으로 로드한다 (전체 전수 로드 금지).
- `docs/evaluations/qa-reports/` (미해결 이슈)
- `docs/exec-plans/active/` (진행 중 스프린트 태스크)

### 2. 역할별 태스크 분할·분배
상위 태스크를 각 역할 단위로 쪼개 다음 파일을 **각각** 업데이트한다.
- `handovers/to_architect.md` / `to_backend_dev.md` / `to_frontend_dev.md` / `to_devops.md` / `to_qa_tester.md`

### 3. Handover 포맷
각 파일은 `handovers/_TEMPLATE.md`의 스키마를 그대로 따른다(코드 금지, 지시만 작성). 필수 섹션: 날짜 · 브랜치 · 현재 상황 · 해야 할 일 · 기대 산출물 · 주의사항 · 참고 자료.

### 4. 기존 태스크 아카이빙
이전에 완료된 내용이 남아있으면, 사용자의 명시적 보존 요청이 없는 한 `handovers/logs/YYYY-MM-DD_to_<role>.md`에 append 후 원본을 비운다 (`handover` 스킬과 동일 규칙).

## Outputs
- 역할별로 명확히 나뉜 `handovers/to_*.md`
- 아카이빙된 `handovers/logs/YYYY-MM-DD_to_*.md`

## Rollback
- `logs/..._to_*.md` 내용을 수거하여 원래 `to_*.md`로 복원한다.
