---
description: 시스템 아키텍처 설계 및 기술 스택 통합 관리 (기술 설계 도우미)
---

## Preconditions
- `.agents/handovers/to_architect.md` 문서가 존재하고 요구사항(현재 상황, 해야 할 일, 기대 산출물)이 구체적으로 작성되어 있어야 함.

## Steps
1. `.agents/handovers/to_architect.md`를 읽고 요구사항을 분석합니다.
2. 해당 역할의 컨텍스트 파일(`.agents/contexts/`)을 불러옵니다.
3. `git-rules` 스킬(또는 `.agents/skills/git-rules/SKILL.md`)을 참고하여 적절한 브랜치(예: `develop/*`)를 생성하고 체크아웃합니다.
4. 시스템 구조(`.agents/ARCHITECTURE.md`)와 핵심 기술 신념(`.agents/docs/design-docs/core-beliefs.md`)을 목적에 맞게 현행화합니다.
5. 요청된 설계 및 문서화 작업을 수행합니다. (필요 시 `.agents/PLANS.md` 마일스톤 관리)
6. 테스트 및 논리적 검증 결과 이상이 없을 시 `develop` 브랜치에 병합하기 위한 절차를 준비합니다.
7. 특정 마일스톤이 완료되어 릴리즈가 필요한 경우 DevOps 엔지니어에게 배포 및 `main` 병합을 요청합니다.

## Outputs
- 설계 문서 업데이트 (`ARCHITECTURE.md`, `PLANS.md` 등)
- `.agents/contexts/` 아키텍트 지식 업데이트
- `.agents/handovers/logs/YYYY-MM-DD_to_architect.md` (완료 백업)

## Rollback
- `.agents/handovers/logs/...` 백업 파일의 내용을 원래 상태(`to_architect.md`)로 되돌립니다.
- 작업에 사용된 Git 브랜치를 삭제합니다.