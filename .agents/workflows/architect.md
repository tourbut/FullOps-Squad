---
description: 시스템 아키텍처 설계 및 기술 스택 통합 관리
---

## Preconditions
- `.agents/handovers/to_architect.md`에 요구사항(현재 상황·해야 할 일·기대 산출물)이 구체적으로 기재되어 있어야 함.

## Steps
1. **Common Preamble** 수행 (`workflows/_README.md` 참조)
2. `ARCHITECTURE.md`·`docs/design-docs/core-beliefs.md`를 요청 목적에 맞춰 현행화한다.
3. 요청된 설계/문서화 작업을 수행한다. 필요 시 `PLANS.md` 마일스톤을 업데이트한다.
4. 구조 변경이 있으면 `ARCHITECTURE.md`의 레이어 매핑 테이블과 실제 디렉토리 일치 여부를 검증한다.
5. 릴리즈가 필요한 마일스톤이면 DevOps에 `main` 병합을 요청한다 (`/release`).
6. **Common Postamble** 수행.

## Outputs
- 업데이트된 `ARCHITECTURE.md`·`PLANS.md`·관련 design-docs
- `handovers/logs/YYYY-MM-DD_to_architect.md`

## Rollback
- `handovers/logs/...` 백업을 `to_architect.md`로 복원하고 Git 브랜치를 파기한다.
