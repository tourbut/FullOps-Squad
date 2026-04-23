---
description: 품질 기준(`QUALITY_SCORE.md`)에 따른 기능 테스트 및 버그 리포트 생성
---

## Preconditions
- `.agents/handovers/to_qa_tester.md`에 테스트 대상 기능이 명시되어 있어야 함.
- 대상 코드가 타겟 브랜치/스테이징에 빌드되어 있어야 함.

## Steps
1. **Common Preamble** 수행.
2. 테스트 목록·엣지 케이스를 도출하고 자동/수동 테스트를 실행한다 (요청 범위 밖 기능 추가 검증 금지).
3. `QUALITY_SCORE.md` 기준(A–F)으로 통과 여부를 판정한다.
4. `qa-tester` 스킬을 호출해 `.agents/docs/evaluations/qa-reports/YYYY-MM-DD_qa_report.md`를 작성한다.
5. 실패 판정 시 원 담당자(backend/frontend/devops) handover로 문제를 이관한다.
6. **Common Postamble** 수행.

## Outputs
- QA 리포트 (`docs/evaluations/qa-reports/`)
- `handovers/logs/YYYY-MM-DD_to_qa_tester.md`

## Rollback
- 리포트 철회 및 handover 로그 복원.
