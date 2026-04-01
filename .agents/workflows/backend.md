---
description: 백엔드 모듈, API 설계 및 비즈니스 로직 개발
---

## Preconditions
- `.agents/handovers/to_backend_dev.md` 문서가 존재하고 기능 명세가 명확히 작성되어 있어야 함.

## Steps
1. `.agents/handovers/to_backend_dev.md`를 분석하여 작업 범위와 기대 산출물을 파악합니다.
2. 해당 역할의 컨텍스트 파일(`.agents/contexts/`)을 불러옵니다.
3. `git-rules` 스킬(또는 `.agents/skills/git-rules/SKILL.md`)을 참고하여 적절한 브랜치(예: `develop/*`)를 생성하고 체크아웃합니다.
4. 백엔드 개발 요청사항을 수행하며, 새로운 기능 추가 등 명시되지 않은 작업은 억제합니다.
5. 구현한 코드에 대응하는 단위 테스트(Unit tests)를 추가합니다.
6. `backend-style` 스킬(또는 `.agents/skills/backend-style/SKILL.md`) 및 `BACKEND.md` 관련 규칙을 준수했는지 자체 점검합니다.
7. 작업 완료 후 GitHub(또는 사용 중인 호스팅 서비스)에서 PR(Pull Request)을 생성합니다.
8. 코드 리뷰 후 통과 시 `develop` 브랜치에 병합합니다.

## Outputs
- 백엔드 소스코드 및 구동 환경 (API 등)
- 백엔드 단위 테스트 결과
- 생성 및 승인된 Pull Request
- `.agents/handovers/logs/YYYY-MM-DD_to_backend_dev.md` (완료 백업)

## Rollback
- 백업된 handover 로그를 다시 `to_backend_dev.md`로 원상복구합니다.
- 오류가 포함된 PR을 닫고, Git 브랜치를 파기합니다.