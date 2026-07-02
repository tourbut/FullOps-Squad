---
description: 프론트엔드 UI/UX 구현 및 API 연동
---

## Preconditions
- `.agents/handovers/to_frontend_dev.md`에 UI/UX·연동 요구사항이 명확히 기재되어 있어야 함.

## Steps
1. **Common Preamble** 수행.
2. **표준 디자인 소스 세트 로드**: `DESIGN.md §4`에 정의된 세트(`docs/design-docs/design.md`·`design-system-reference-llms.txt`·`ui-ux-guidelines.md`·`design-mockup.html`)를 모두 읽고, 색상·간격·타이포는 토큰만 사용한다.
3. `FRONTEND.md`·`docs/design-docs/ui-ux-guidelines.md` 가이드 내에서 구현한다 (요청 밖 기능 추가 금지).
4. Svelte 5 Runes 문법(`$state`/`$props`/`$derived`/`$effect`, callback props) 사용 여부와 인라인 style 미사용을 자가 점검한다.
5. `frontend-style`·`verify-linter-rules`·`webapp-testing` 스킬을 순차 실행한다 (검증 사다리: `workflows/_README.md`).
6. PR 생성 → 리뷰 통과 시 `develop` 병합.
7. **Common Postamble** 수행.

## Outputs
- 수정/추가 프론트엔드 소스코드·스토리북/E2E 테스트·UI 검증 스크린샷
- 생성된 Pull Request
- `handovers/logs/YYYY-MM-DD_to_frontend_dev.md`

## Rollback
- 브랜치 파기·PR 종료, 백업된 handover 로그 복원.
