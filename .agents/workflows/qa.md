---
description: 품질 기준(QUALITY_SCORE.md)에 따른 신규 기능 테스트 및 버그 리포트 생성
---

## Preconditions
- `.agents/handovers/to_qa_tester.md` 에 테스트 대상 기능이 명시되어 있어야 함.
- 관련 코드가 타겟 브랜치에 미리 반영(빌드)되어 있어야 함.

## Steps
1. `.agents/handovers/to_qa_tester.md`를 읽고 금번 테스트 대상을 파악합니다.
2. 해당 역할의 컨텍스트 파일(`.agents/contexts/`)을 불러옵니다.
3. `git-rules` 스킬(또는 `.agents/skills/git-rules/SKILL.md`)을 참고하여 적절한 `develop`에 있는 사항을 `main` 브랜치 환경(또는 스테이징)에서 테스트를 수행합니다.
4. QA 대상 목록을 기반으로 기능 확인 및 엣지 케이스 점검을 실행합니다. (요청 범위 밖의 기능 추가 시도는 금지)
5. `QUALITY_SCORE.md` 기준에 맞춰 버그 통과 여부를 판단합니다.
6. 테스트 결과, 이슈 및 재현 방법을 요약하여 `.agents/docs/evaluations/qa-reports/`에 리포트를 작성합니다.

## Outputs
- 버그/QA 리포트 파일 (`.agents/docs/evaluations/qa-reports/`)
- `.agents/handovers/logs/YYYY-MM-DD_to_qa_tester.md` (완료 백업)

## Rollback
- QA 실패로 판정된 경우 해당 리포트를 바탕으로 원래 담당자(Frontend, Backend 등) 측 handover로 문제를 이관합니다.
- QA 로그를 원복합니다.