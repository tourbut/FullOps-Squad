<!-- AI Harness Rule: Read DESIGN.md purely as high-level architectural constraints (YAGNI, Predictability, Clarity). DO NOT write specific features or implementation details here; they belong in `.agents/docs/design-docs/`. Any UI/UX changes must align with `.agents/docs/design-docs/ui-ux-guidelines.md`. -->
# 디자인 철학 및 원칙 (Design Philosophy)

이 문서는 프로젝트 개발 시 준수해야 할 높은 수준의 디자인 철학을 안내합니다. 
구체적인 기능명세 및 설계는 `.agents/docs/design-docs/` 디렉토리에 위치시킵니다.

## 1. 핵심 방향 (Core Beliefs)
- **명확성(Clarity)**: 코드는 작성하기보다 읽기 쉬워야 합니다.
- **예측 가능성(Predictability)**: 시스템은 의도된 일관된 방식으로만 동작해야 합니다.
- **단순성(Simplicity)**: 불필요한 추상화나 과엔지니어링(YAGNI)을 피하십시오.
- **반복 가능성(Repeatability)**: 테스트 및 배포 등 모든 과정은 재현 가능해야 합니다.

## 2. 의사결정 프레임워크 (Decision Framework)
아키텍처 변경이나 새로운 라이브러리 도입시 아래의 기준을 따르세요:
- 이것이 사용자 문제 해결을 위해 반드시 필요한 기능인가?
- 이를 통해 발생하는 부채(Tech Debt)를 어떻게 감당할 것인가?
- 기존의 생태계(`rules/`, `skills/` 등)와의 충돌은 없는가?

## 3. UI/UX 디자인 원칙
- **일관성 우선**: 디자인 토큰(색상, 간격, 타이포그래피)을 통해 모든 화면에서 동일한 경험을 제공합니다.
- **상태 완전성**: 모든 화면은 로딩/빈 상태/에러/성공 4가지 상태를 반드시 처리합니다.
- **접근성(a11y)**: WCAG AA 수준을 기본으로 준수합니다.
- **모바일 우선**: 반응형 디자인을 기본으로 하되, 데스크탑 사용 경험도 최적화합니다.
- 상세 지침은 `.agents/docs/design-docs/ui-ux-guidelines.md` 문서를 참고하세요.
