---
description: 백엔드 모듈·API 설계 및 비즈니스 로직 개발
---

## Preconditions
- `.agents/handovers/to_backend_dev.md`에 기능 명세와 기대 산출물이 명확히 기재되어 있어야 함.

## Steps
1. **Common Preamble** 수행.
2. 요청 범위 내에서만 백엔드 구현을 수행한다 (요청 밖 기능 추가 금지).
3. 신규·수정 모듈에 대응하는 단위 테스트를 추가한다.
4. `backend-style`·`verify-linter-rules` 스킬을 실행하고 `BACKEND.md` 체크리스트를 자가 점검한다 (검증 사다리: `workflows/_README.md`).
5. PR 생성 → 리뷰 통과 시 `develop` 병합.
6. **Common Postamble** 수행.

## Outputs
- 백엔드 소스코드·단위 테스트·OpenAPI 스키마 갱신
- 생성/승인된 Pull Request
- `handovers/logs/YYYY-MM-DD_to_backend_dev.md`

## Rollback
- PR 종료 및 브랜치 파기, 백업된 handover 로그를 복원한다.
