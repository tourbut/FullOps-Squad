# AGENTS.md — Project Navigation Map

<!-- AI Harness Rule: 100줄 이하의 저장소 인덱스 매핑. 상세 기술 구현은 제외하고, 에이전트가 경로만 빠르게 찾아갈 수 있도록 한다 (예: 아키텍처는 ARCHITECTURE.md, 린터 규칙은 rules/). -->

> 에이전트 진입점. 세부 내용은 링크된 문서에 위임한다.
> 이 저장소는 역할 기반 에이전트(Architect/Backend/Frontend/DevOps/QA)가 문서를 매개로 협업하며 컨텍스트·Handover를 관리하는 AI 협업 개발 프로젝트다.

---

## 네비게이션

| 영역 | 문서 |
|------|------|
| 설계 철학·레이어 규칙 | `DESIGN.md` · `ARCHITECTURE.md` |
| 기술 스택·환경 | `docs/design-docs/tech-stack.md` |
| 로드맵·마일스톤(인덱스) | `PLANS.md` |
| Phase별 상세 실행 로그 | `docs/exec-plans/phases/phaseNN.md` |
| 품질 등급·체크리스트 | `QUALITY_SCORE.md` · `BACKEND.md` · `FRONTEND.md` |
| 신뢰성·보안 | `RELIABILITY.md` · `SECURITY.md` |
| 제품 마인드셋 | `PRODUCT_SENSE.md` |
| 스킬·워크플로우 인덱스 | `SKILLS.md` |
| 기획·문제 정의·제품 명세 | `docs/planning/{meeting-logs,cps,product-specs}/` |
| UI/UX 가이드·디자인 시스템 | `docs/design-docs/ui-ux-guidelines.md` · `docs/references/` |
| 스프린트 계약·진행 태스크 | `docs/exec-plans/{sprint-contracts,active,completed}/` · `tech-debt-tracker.md` |
| 평가·QA 리포트·하네스 지표 | `docs/evaluations/{org-metrics.md,harness-metrics.md,qa-reports/}` |
| 자동 생성물·외부 참조 | `docs/generated/` · `docs/references/` |
| 린터 규칙·교정 가이드 | `rules/linter-rules.md` · `rules/correction-guides.md` |
| 역할별 컨텍스트·Handover | `contexts/` · `handovers/` (+`handovers/logs/`) |
| 스킬·워크플로우 구현체 | `skills/` · `workflows/` |

---

## 에이전트 행동 규칙 (요약)

1. 작업 시작 전 이 문서를 먼저 읽고, 관련 경로만 탐색한다 (불필요한 문서 전수 로드 금지).
2. `ARCHITECTURE.md`의 레이어 의존 방향은 **절대 위반 금지**.
3. 모든 코드 변경은 `rules/linter-rules.md` 통과가 필수다. 위반 시 `rules/correction-guides.md`에 따라 교정한다.
4. 작업 완료 후 **반드시** `contexts/<role>.md`에 결정·교훈을 append하고, Handover는 `handovers/logs/`로 아카이빙한다.
5. **언어**: 모든 응답·문서·코드 주석은 **한국어**로 작성한다. 단, 영문 구조 키워드(ARCHITECTURE, Preconditions 등)와 식별자는 유지한다.

> 이 문서는 100줄 이내 인덱스 맵이다. 세부 내용은 반드시 링크된 문서를 따른다.
