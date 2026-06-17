# design.md — 시스템 표준 상세 디자인 스펙 (System Standard Design Spec)

<!-- AI Harness Rule: 이 문서는 프론트엔드 에이전트가 UI를 구현할 때 따르는 "에이전트 지향 디자인 스펙"이다.
     상위 철학·브랜드 무드는 `.agents/DESIGN.md`, 토큰 값은 `docs/references/design-system-reference-llms.txt`,
     평가 루브릭은 `ui-ux-guidelines.md`에 있다. 이 문서는 그 사이의 "구현 규칙"을 담당한다.
     (awesome-design-md 스타일: github.com/VoltAgent/awesome-design-md 참조) -->

> `DESIGN.md §4 표준 디자인 소스 세트`의 핵심 구현 스펙.
> 프론트엔드 에이전트는 모든 화면/컴포넌트를 이 문서의 패턴에 맞춰 구현한다.
> 색상·간격·타이포 값은 직접 적지 않고 `design-system-reference-llms.txt`의 **토큰**을 참조한다.

---

## 1. 디자인 원칙 (Design Principles)

> 프로젝트 시작 시 실제 제품 정체성에 맞게 채워넣는다.

- (예: 명료한 정보 위계 — 한 화면에 하나의 주요 행동)
- (예: 토큰 기반 일관성 — 모든 시각 속성은 토큰에서만 파생)
- (예: 접근성 우선 — 명도 대비/키보드 내비게이션을 설계 단계에서 보장)

---

## 2. 레이아웃 (Layout)

- **그리드**: (예: 12-column, 최대 컨테이너 폭 1200px)
- **브레이크포인트**: 모바일 375px / 태블릿 768px / 데스크탑 1440px
- **간격 스케일**: `design-system-reference-llms.txt`의 Spacing 토큰(4px 기준)을 따른다
- **페이지 골격**: (예: 좌측 네비게이션 + 상단 헤더 + 메인 콘텐츠 영역)

---

## 3. 컴포넌트 규칙 (Component Patterns)

각 핵심 컴포넌트의 표준 변형(variant)·상태·사용처를 정의한다.

### Button
- **Variants**: Primary / Secondary / Ghost / Danger
- **States**: default / hover / active / disabled / loading
- **규칙**: 한 화면의 주요 행동에는 Primary 1개만 사용

### Input / Form
- **States**: default / focus / error / disabled
- **규칙**: 모든 입력은 `label` 연결, 에러는 필드 하단 인라인 메시지로 표기

### Card / Surface
- **규칙**: `--color-surface` 배경 + `--color-border` 경계. 카드 간 간격은 Spacing 토큰 사용

### Feedback (Toast / Modal / Empty / Skeleton)
- **규칙**: `ui-ux-guidelines.md §3` 상태 체크리스트(로딩/빈/에러/성공)를 모두 충족

> 컴포넌트별 상세 props·접근성 속성은 구현 시 이 섹션에 추가한다.

---

## 4. 타이포그래피 사용 규칙 (Typography Usage)

- 헤딩 위계(H1–H3)·본문·캡션은 `design-system-reference-llms.txt`의 Typography 표를 따른다
- 한 화면에 H1은 1개만 사용한다
- 강조는 굵기(weight)로 처리하고, 색상 강조는 토큰(`--color-primary`/`--color-accent`)으로 제한한다

---

## 5. 구현 체크리스트 (Implementation Checklist)

새 UI를 추가/수정할 때:

- [ ] 색상·간격·타이포를 토큰으로만 사용했는가 (하드코딩 0)
- [ ] 4가지 상태(로딩/빈/에러/성공)를 처리했는가
- [ ] 3개 브레이크포인트에서 깨지지 않는가
- [ ] WCAG AA 명도 대비(4.5:1)·키보드 내비게이션을 만족하는가
- [ ] `design-mockup.html`의 대응 패턴과 일치하는가
