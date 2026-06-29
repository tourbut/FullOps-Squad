---
description: 구현 이전 디자인 목업 작성 및 UI/UX 확정 (frontend/backend 구현 선행 게이트)
---

## Preconditions
- `.agents/handovers/to_frontend_dev.md` 또는 `planning/product-specs/<spec>.md`에 화면/기능 요구사항이 기재되어 있어야 함.
- 디자인 권위 문서(`docs/references/design-system-reference-llms.txt`, `frontend/src/app.css @theme`)가 최신이어야 함.

## Steps
1. **Common Preamble** 수행 (역할: `frontend_dev`).
2. 요구사항·디자인 토큰·`docs/design-docs/ui-ux-guidelines.md`를 동기화하고, 기존 유사 화면(`frontend/src/routes`·`lib/components`) 패턴을 확인한다.
3. **`design-mockup` 스킬**을 실행해 `docs/design-docs/mockups/YYYY-MM-DD_<feature-slug>/`에 자체완결 HTML 목업 + README(`Status: proposed`)를 생성한다.
4. 목업을 브라우저에서 검토하고, `_README.md` §4 체크리스트 + 3개 브레이크포인트(375/768/1440px)를 자가 점검한다 (필요 시 `webwright`로 스크린샷 증거).
5. **검토·확정 게이트**: 사용자/Architect 피드백을 받아 `revising`으로 반영하고, 합의되면 README `Status: confirmed`로 올린다.
6. 확정된 목업의 "구현 노트"(신규 컴포넌트·토큰 매핑·**백엔드 필요 여부**)를 `handovers/to_frontend_dev.md`(백엔드 필요 시 `to_backend_dev.md`)에 반영한다.
7. **Common Postamble** 수행.

## Outputs
- `docs/design-docs/mockups/YYYY-MM-DD_<feature-slug>/{index.html, README.md, ...}`
- 확정 시 갱신된 `handovers/to_frontend_dev.md`(필요 시 `to_backend_dev.md`)
- `handovers/logs/YYYY-MM-DD_to_frontend_dev.md`

## Rollback
- 목업은 `mockups/` 한정 산출물이라 코드 영향 없음. 방향 폐기 시 폴더 `Status: superseded`로 표기하거나 삭제하고, handover 로그를 복원한다.

> **게이트 규칙**: `/frontend`(및 필요 시 `/backend`)는 대상 기능 목업이 `confirmed`일 때만 구현에 진입한다. `proposed`/`revising` 상태에서는 구현 착수 금지.
