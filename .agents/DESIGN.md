<!-- AI Harness Rule: Read DESIGN.md purely as high-level architectural constraints (YAGNI, Predictability, Clarity). DO NOT write specific features or implementation details here; they belong in `.agents/docs/design-docs/`. Any UI/UX changes must align with `.agents/docs/design-docs/ui-ux-guidelines.md`. -->
<!-- AI Harness Rule (Mockup ↔ DESIGN.md 동기화):
     `.agents/docs/generated/design-mockup.html`은 이 문서(DESIGN.md)의 모든 규칙을 목업 데이터로 시각화한 "검토용 미러"다.
     소스: `.agents/DESIGN.md` / `docs/design-docs/design.md` / `docs/references/design-system-reference-llms.txt` / `docs/design-docs/ui-ux-guidelines.md`.
     - 목업의 각 섹션은 `[DESIGN.md §x]` 태그로 이 문서의 조항과 1:1 매핑된다.
     - 워크플로우: 사람이 목업을 보고 `[DESIGN.md §x] + 의견` 형태로 피드백 → 그 근거로 이 문서의 해당 조항을 수정한다.
     - 이 문서의 조항을 추가/변경하면 `design-mockup.html`의 대응 섹션도 함께 갱신해 둘을 항상 일치시킨다(둘 중 하나만 바꾸지 말 것). -->
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

## 3. 브랜드 디자인 언어 (Brand Design Language)

> 프로젝트 시작 시 아래 항목을 실제 브랜드 정체성에 맞게 채워넣는다.
> 정확한 색상값(hex/RGB)·중립색·다크모드 토큰은 `docs/references/design-system-reference-llms.txt`에 정의한다.

- **브랜드 무드**: (예: 신뢰·전문성·정돈됨 / 활기·혁신·친근함 등)
- **Primary 컬러**: (메인 브랜드 색상 — 주요 액션·활성 상태에 사용)
- **Accent 컬러**: (강조·경고·중요 신호에 절제하여 사용)
- **레이아웃 기조**: (예: 클린 미니멀 / 정보 밀도 높은 대시보드 / 카드 그리드 등)
- **정보 위계**: (예: 좌측 네비게이션, 일관된 카드 그리드, 헤딩 위계 등)
- **타이포그래피**: (예: 가독성 높은 산세리프, 명확한 헤딩 위계 유지)

## 4. 표준 디자인 소스 세트 (Standard Design Source Set)

이 프로젝트의 디자인 시스템은 아래 **표준 파일 세트**로 단일하게 정의된다.
프론트엔드를 만들 때는 이 세트가 **유일한 기준**이며, 임의 색상·간격·패턴을 도입하지 않는다.

| 파일 | 역할 | 성격 |
|------|------|------|
| `.agents/DESIGN.md` (본 문서) | 디자인 철학·브랜드 언어의 단일 진실 공급원(SSOT) | 프롬프트 |
| `docs/design-docs/design.md` | 시스템 표준 상세 디자인 스펙(컴포넌트·패턴·레이아웃 규칙) | 에이전트 지향 스펙 |
| `docs/references/design-system-reference-llms.txt` | 디자인 토큰(색상·타이포·간격) 평문 — LLM 주입용 | 토큰 SSOT |
| `docs/design-docs/ui-ux-guidelines.md` | UI/UX 평가 루브릭·상태 처리 체크리스트 | 평가 기준 |
| `docs/generated/design-mockup.html` | 위 규칙들을 한 화면에 시각화한 검토용 미러(자동 생성물) | `[DESIGN.md §x]` 1:1 매핑 |

### 프론트엔드 빌드 시 행동 규칙
1. **로드 우선**: UI 구현을 시작하기 전, 프론트엔드 에이전트는 위 세트를 **모두 로드**한다.
2. **토큰 전용**: 모든 색상·타이포·간격은 `design-system-reference-llms.txt`에 정의된 **토큰 값만** 사용한다(하드코딩·임의 값 금지).
3. **패턴 준수**: 새 화면/컴포넌트는 `design.md`의 컴포넌트·레이아웃 패턴과 `ui-ux-guidelines.md`의 상태 처리 체크리스트(로딩/빈/에러/성공)를 충족해야 한다.
4. **동기화 유지**: DESIGN.md 또는 토큰을 변경하면 `design-mockup.html`을 재생성해 둘을 항상 일치시킨다.
5. **검증**: 산출물은 `FRONTEND.md`의 Design Quality 등급(A–F)으로 평가하며, "디자인 시스템 토큰 100% 일치"가 A의 조건이다.

## 5. UI/UX 디자인 원칙
- **일관성 우선**: 디자인 토큰(색상, 간격, 타이포그래피)을 통해 모든 화면에서 동일한 경험을 제공합니다.
- **상태 완전성**: 모든 화면은 로딩/빈 상태/에러/성공 4가지 상태를 반드시 처리합니다.
- **접근성(a11y)**: WCAG AA 수준을 기본으로 준수합니다.
- **모바일 우선**: 반응형 디자인을 기본으로 하되, 데스크탑 사용 경험도 최적화합니다.
- 상세 지침은 `.agents/docs/design-docs/ui-ux-guidelines.md` 문서를 참고하세요.
