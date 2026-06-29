---
name: design-mockup
description: 구현(프론트/백엔드) 이전에 요구사항을 자체완결 HTML 디자인 목업으로 먼저 시각화해 UI/UX를 확정하는 스킬. "목업", "디자인 시안", "와이어프레임", "화면 먼저 보고", "UI 확정" 등이 언급되거나, 신규 화면·기능 구현에 앞서 시각 검토가 필요할 때 사용.
---

## Purpose

새 화면·컴포넌트를 코드로 구현하기 **전에**, 요구사항을 브라우저에서 바로 열어볼 수 있는 **자체완결 HTML 목업**으로 만들어 UI/UX를 먼저 확정한다. 확정된 목업은 그대로 `/frontend` 구현의 입력(스펙 + 토큰 매핑 + 백엔드 필요 여부)이 된다. 잘못된 방향으로 프론트/백엔드를 구현하는 재작업을 막는 것이 목표다.

## When to Run

- "목업", "디자인 시안", "와이어프레임", "화면 먼저", "UI/UX 확정" 등이 요구될 때
- `/design` 워크플로우 실행 시 (이 스킬이 핵심 산출물 생성기)
- 신규 화면/기능을 `/frontend`로 구현하기 직전, 시각 합의가 필요할 때
- 기존 화면을 크게 개편하기 전 방향을 시각적으로 비교(A/B)하고 싶을 때

## Inputs

- 요구사항: `handovers/to_frontend_dev.md` 또는 `planning/product-specs/<spec>.md`(FD-NN)
- 디자인 권위: `docs/references/design-system-reference-llms.txt`, `frontend/src/app.css`(`@theme`)
- 평가 기준: `docs/design-docs/ui-ux-guidelines.md`, `FRONTEND.md`

## Workflow

1. **요구사항·토큰 동기화**: 위 Inputs를 읽어 화면 목적·대상·상태(로딩/빈/에러/성공)와 디자인 토큰을 파악한다. 기존 유사 화면(`frontend/src/routes`·`lib/components`)이 있으면 패턴을 재사용해 일관성을 유지한다.
2. **목업 폴더 생성**: `docs/design-docs/mockups/_TEMPLATE/`를 `docs/design-docs/mockups/YYYY-MM-DD_<feature-slug>/`로 복사한다. (`cp -r`)
3. **디자인 사고**(`frontend-design` 스킬 참조): 코딩 전 톤·계층·차별점을 정한다. 단, 본 프로젝트는 **NHIS 인스티튜셔널 클린** 무드가 권위이므로 그 안에서 정제한다(임의 브랜드 일탈 금지).
4. **목업 작성**: `index.html`을 편집한다. 템플릿이 주입한 시맨틱 토큰 클래스(`bg-primary`·`text-text-muted`·`border-border` 등 — 프로덕션과 동일)만 사용하고, 임의 hex·인라인 style은 피한다. 상태 4종을 모두 표현한다. 시안이 여러 개면 `option-a.html`/`option-b.html`로 분리한다.
5. **자가 점검**: `_README.md` §4 체크리스트 + 3개 브레이크포인트(375/768/1440px)를 확인한다. 필요 시 `webwright`/`webapp-testing`으로 스크린샷 증거를 남긴다.
6. **README 작성**: 폴더 `README.md`에 요구사항·디자인 근거·체크리스트·구현 노트(특히 **백엔드 필요 여부**: 엔드포인트/스키마)를 채우고 `Status: proposed`로 둔다.
7. **검토·확정**: 사용자/Architect 리뷰를 받는다. 피드백은 `revising`으로 반영하고, 합의되면 `Status: confirmed`로 올린다. **`confirmed` 이전에는 프론트/백엔드 구현에 착수하지 않는다.**
8. **구현 인계**: 확정 시 README의 "구현 노트"를 `handovers/to_frontend_dev.md`(백엔드 필요 시 `to_backend_dev.md`도)에 반영해 `/frontend`(필요 시 `/backend`)로 넘긴다. 구현 완료 후 목업 `Status: implemented`로 갱신한다.

## Output Format

- **HTML**: 자체완결(Tailwind Play CDN + Pretendard CDN + 토큰 인라인). `file://`로 더블클릭해 열린다. 외부 빌드·dev 서버·로컬 에셋 의존 금지.
- **토큰**: `_TEMPLATE/index.html`의 `tailwind.config` 매핑을 유지·확장한다(시맨틱 이름이 `app.css @theme`와 1:1).
- **README**: `_TEMPLATE/README.md` 양식 엄격 준수, Status 라이프사이클 명시.

## Guardrails

- 목업은 **검토용 프로토타입**이다. 실제 Svelte 컴포넌트·API 연동·상태 로직을 여기서 구현하지 않는다.
- `mockups/` 외 디렉토리(`frontend/`·`backend/`)를 이 스킬에서 수정하지 않는다.
- 디자인 시스템 권위(`design-system-reference-llms.txt`)를 벗어난 임의 색·폰트 도입 금지.
- 목업 HTML의 목업 전용 보조물(브레이크포인트 배지 `.bp-badge` 등)은 구현 시 이관하지 않는다.

## Related Files

| File | Purpose |
|------|---------|
| `.agents/docs/design-docs/mockups/_README.md` | 산출물 공간 규칙·Status 라이프사이클 |
| `.agents/docs/design-docs/mockups/_TEMPLATE/` | 신규 목업 시작 스캐폴드(토큰 주입 HTML + README) |
| `.agents/docs/references/design-system-reference-llms.txt` | 디자인 토큰 권위(색·타이포·간격) |
| `.agents/docs/design-docs/ui-ux-guidelines.md` | UI/UX 평가 지침·상태 처리 체크리스트 |
| `.agents/workflows/design.md` | 이 스킬을 오케스트레이션하는 `/design` 워크플로우 |
| `.agents/skills/frontend-design/SKILL.md` | 디자인 사고·미학 가이드(보강 참조) |
