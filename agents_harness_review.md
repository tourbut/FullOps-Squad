# `.agents/` AI 하네스 종합 검토 피드백

> **검토 대상**: `/Users/mipd/workspace/FullOps-Squad/.agents/` 전체
> **검토 일시**: 2026-04-03
> **검토 범위**: 구조 설계, 문서 품질, 일관성, 워크플로우, 운영 준비도

---

## 종합 평가

| 카테고리 | 등급 | 요약 |
|----------|------|------|
| 구조 / 아키텍처 | ⭐⭐⭐⭐ | 체계적인 디렉토리 구조와 명확한 네비게이션 맵 |
| 문서 완성도 | ⭐⭐⭐ | 핵심 문서는 양호하나 다수의 스텁(stub) 파일 존재 |
| 일관성 / 정합성 | ⭐⭐⭐ | 전반적으로 일관적이나 경로·네이밍·언어 혼용 이슈 발견 |
| 워크플로우 / 스킬 | ⭐⭐⭐⭐ | 실용적 구조이나 SKILLS.md와 실제 구현 간 괴리 |
| 운영 준비도 | ⭐⭐ | Phase 1 수준, 빈 컨텍스트와 플레이스홀더가 다수 |

---

## 1. 구조 / 아키텍처

### ✅ 잘 된 점
- `AGENTS.md`가 100줄 이하의 명확한 네비게이션 맵 역할 수행
- 레이어 계층(Types → Config → Repo → Service → Runtime → UI) 설계가 체계적
- `docs/` 하위 구조가 기획(planning) → 설계(design-docs) → 실행(exec-plans) → 평가(evaluations) → 참조(references) 순으로 논리적
- Handover 시스템(to_*.md → logs/ 아카이빙)은 에이전트 간 협업에 매우 실용적

### 🔴 문제점 및 수정 제안

#### 1-1. `docs/product-specs/` 경로 중복

> [!WARNING]
> `docs/product-specs/`와 `docs/planning/product-specs/` 두 경로가 모두 존재합니다.

**현황**:
- `docs/product-specs/` — [index.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/product-specs/index.md), [new-user-onboarding.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/product-specs/new-user-onboarding.md) 포함
- `docs/planning/product-specs/` — 빈 디렉토리 (README만 존재할 것으로 추정)
- [AGENTS.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/AGENTS.md) (39행)에서는 `docs/planning/product-specs/`를 가리킴
- [PRODUCT_SENSE.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/PRODUCT_SENSE.md) (5행)에서도 `docs/planning/product-specs/`를 가리킴
- 실제 문서는 `docs/product-specs/`에 존재

**수정 제안**:
- `docs/product-specs/`의 파일들을 `docs/planning/product-specs/`로 이동하여 AGENTS.md의 네비게이션과 일치시키거나
- `docs/product-specs/` 디렉토리를 삭제하고 `docs/planning/product-specs/`에 통합

---

#### 1-2. `ARCHITECTURE.md`의 디렉토리 매핑 vs 실제 백엔드 구조 불일치

**현황**:
- [ARCHITECTURE.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/ARCHITECTURE.md) (64~71행)에서 `src/` 기준 일반적 계층 구조를 정의
- [tech-stack.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/design-docs/tech-stack.md) (17~43행)에서는 `backend/app/src/`라는 실제 프로젝트 구조를 보여주며 `routes/`, `crud/`, `engine/` 등 다른 이름 사용
- 에이전트가 어느 것을 따라야 하는지 모호

**수정 제안**:
- `ARCHITECTURE.md`의 Directory Mapping을 **추상적 원칙**으로 유지하되, "실제 프로젝트 매핑은 `docs/design-docs/tech-stack.md`를 참조"하는 명시적 링크 추가
- 또는 `ARCHITECTURE.md`에 실제 프로젝트 구조와의 매핑 테이블을 추가:
  ```markdown
  | Layer | Abstract | Backend Actual | Frontend Actual |
  |-------|----------|---------------|----------------|
  | Types | types/ | app/models/ | lib/types/ |
  | Config | config/ | app/core/ | lib/stores/ |
  ```

---

#### 1-3. `RELIABILITY.md`에서 참조하는 `rules/devops.md` 미존재

**현황**:
- [RELIABILITY.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/RELIABILITY.md) (5행): "데브옵스(DevOps) 파이프라인 및 운영 규칙은 `.agents/rules/devops.md`를 참고하세요."
- 실제 `rules/` 디렉토리에는 `base.md`, `linter-rules.md`, `correction-guides.md`만 존재

**수정 제안**:
- `rules/devops.md`를 생성하거나
- 해당 참조를 `workflows/devops.md` 또는 다른 적절한 문서로 변경

---

## 2. 문서 완성도

### ✅ 잘 된 점
- [BACKEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/BACKEND.md), [FRONTEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/FRONTEND.md), [QUALITY_SCORE.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/QUALITY_SCORE.md)의 등급 기준이 구체적이고 기계적 평가 가능
- [linter-rules.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/rules/linter-rules.md)와 [correction-guides.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/rules/correction-guides.md)의 위반 코드 ↔ 교정 가이드 1:1 매핑이 체계적
- [contexts/_TEMPLATE.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/contexts/_TEMPLATE.md)의 "미래의 나에게 보내는 브리핑 문서" 관점이 우수

### 🔴 문제점 및 수정 제안

#### 2-1. 다수의 빈 스텁 파일

> [!IMPORTANT]
> 문서 시스템의 신뢰도를 떨어뜨리는 핵심 원인입니다.

| 파일 | 상태 |
|------|------|
| [ui-ux-guidelines.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/design-docs/ui-ux-guidelines.md) | AI Harness Rule 주석 + 1줄 설명만 존재 |
| [org-metrics.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/evaluations/org-metrics.md) | AI Harness Rule 주석 + 1줄 설명만 존재 |
| [db-schema.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/generated/db-schema.md) | 플레이스홀더 텍스트만 존재 |
| [design-system-reference-llms.txt](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/references/design-system-reference-llms.txt) | 플레이스홀더 텍스트만 존재 |
| contexts/ 내 5개 역할 파일 | 모두 빈 파일 (0 bytes) |

**수정 제안**:
- 당장 내용을 채울 수 없는 파일에는 최소한의 초기 구조(섹션 헤더 + TODO 마커)를 넣어서 "작성 예정"임을 명시
- 컨텍스트 파일들은 `_TEMPLATE.md`의 구조를 복사해서 각 역할명만 변경한 초기 상태로 배포 → 에이전트가 첫 작업 시 바로 기록 시작 가능

---

#### 2-2. `PRODUCT_SENSE.md`, `RELIABILITY.md`, `SECURITY.md`가 골격만 존재

**현황**:
- 3개 문서 모두 섹션 제목과 1~2줄 설명만 있고 구체적 기준이 없음
- 예: [SECURITY.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/SECURITY.md)의 OWASP Top 10 섹션에 SQL Injection/XSS/CSRF만 언급, 나머지 7개 항목 미정의

**수정 제안**:
- Phase 1 완료 기준에 맞춰 최소한 **체크리스트 수준**으로 확장 (BACKEND.md의 체크리스트 스타일 참고)
- 또는 명시적으로 "Phase 2에서 확장 예정" 표기를 달아 혼란 방지

---

#### 2-3. `DESIGN.md` 3번 섹션 미작성

**현황**:
- [DESIGN.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/DESIGN.md) (19~21행):
  ```
  ## 3. UI/UX 디자인 원칙
  - (사용자 경험(UX) 및 인터페이스 디자인 시스템 원칙 작성)
  ```
- 괄호 안의 플레이스홀더가 그대로 남아 있음

**수정 제안**:
- 최소한 3~5개의 UI/UX 원칙을 정의하거나
- `ui-ux-guidelines.md`로의 위임을 명확히 하고 본 섹션은 삭제

---

## 3. 일관성 / 정합성

### 🔴 문제점 및 수정 제안

#### 3-1. 경로 표기 불일치 (`.agent/` vs `.agents/`)

> [!CAUTION]
> 에이전트가 잘못된 경로를 참조할 수 있는 심각한 위험입니다.

| 파일 | 표기 | 올바른 경로 |
|------|------|------------|
| [handover/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/handover/SKILL.md) (21, 32~33행) | `.agent/handovers/...` | `.agents/handovers/...` |
| [role-context/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/role-context/SKILL.md) (37행) | `.agent/contexts/*.md` | `.agents/contexts/*.md` |
| [verify-implementation/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/verify-implementation/SKILL.md) (82, 239행) | `.agent/skills/...` | `.agents/skills/...` |
| [Debug/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/Debug/SKILL.md) (26, 43행) | `.agent/project/logs/...` | 경로 자체가 존재하지 않음 |

**수정 제안**: 모든 스킬 파일에서 `.agent/`를 `.agents/`로 일괄 수정

---

#### 3-2. 문서 언어 혼용

**현황**:
- 루트 레벨 문서: `AGENTS.md`, `ARCHITECTURE.md`, `BACKEND.md`, `FRONTEND.md`, `QUALITY_SCORE.md`, `SKILLS.md` → **영어**
- `DESIGN.md`, `PRODUCT_SENSE.md`, `RELIABILITY.md`, `SECURITY.md` → **한국어**
- `docs/` 하위 → 혼용
- `rules/linter-rules.md`, `correction-guides.md` → **영어**
- `rules/base.md` → **영어**
- 워크플로우 → **한국어**
- 스킬 → **한국어**

**수정 제안**:
- 프로젝트 규칙(`base.md`)에서 "항상 한국어로 응답"을 강제하고 있으므로, **문서도 한국어 통일** 또는 **영어 원칙 + AI Harness Comment는 영어** 원칙을 명확히 결정
- 현재 상태가 의도적이라면 AGENTS.md에 "구조 문서는 영어, 기획/운영 문서는 한국어"처럼 언어 전략을 명시

---

#### 3-3. `SKILLS.md`와 실제 `skills/` 디렉토리 간 괴리

> [!WARNING]
> SKILLS.md에 정의된 스킬과 실제 구현된 스킬이 전혀 다릅니다.

**SKILLS.md에 정의된 스킬** (이론적):
- Core: `file-read`, `file-write`, `context-sync`, `handover-dispatch`
- Role: `schema-design`, `adr-record`, `api-scaffold`, `migration-gen`, `component-scaffold`, `route-scaffold`, `e2e-test-gen`, `qa-report-gen`, `docker-compose-update`, `deploy-trigger`

**실제 `skills/` 디렉토리에 존재하는 스킬** (27개):
- `Debug`, `backend-style`, `frontend-style`, `git-rules`, `handover`, `role-context`, `verify-implementation`, `manage-skills`, `qa-tester`, `refactoring`, `prompt-engineer` 등
- SKILLS.md에 정의된 `file-read`, `api-scaffold` 등은 실제 구현 없음

**수정 제안**:
- `SKILLS.md`를 현재 실제 존재하는 스킬에 맞게 전면 재작성
- 또는 SKILLS.md의 Core Skills 섹션을 "에이전트 플랫폼이 제공하는 기본 기능" (별도 구현 불필요)으로 재정의하고, 실제 프로젝트 스킬 목록을 별도 섹션으로 추가

---

#### 3-4. `skills/_README.md`의 디렉토리 구조도 현실과 불일치

**현황**:
- [_README.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/_README.md) (14~26행)에서 `core/`, `role/`, `util/` 하위 구조를 정의
- 실제로는 플랫 구조(27개 디렉토리가 모두 최상위에 나열)

**수정 제안**: `_README.md`의 구조도를 실제 디렉토리 레이아웃에 맞게 업데이트

---

#### 3-5. Workflows `_README.md` 내의 등록 워크플로우 목록 불일치

**현황**:
- [_README.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/workflows/_README.md)의 디렉토리 구조/등록 테이블에는 `sprint-start.md`, `sprint-review.md`, `tech-debt-scan.md`, `context-backup.md`, `handover-cleanup.md`가 명시
- 실제 워크플로우 파일: `architect.md`, `backend.md`, `coordinator.md`, `devops.md`, `frontend.md`, `master.md`, `qa.md`
- 명시된 5개 워크플로우 파일은 실제로 **존재하지 않음**

**수정 제안**: `_README.md`의 구조도와 등록 테이블을 실제 존재하는 워크플로우로 교체

---

#### 3-6. `FRONTEND.md`의 Svelte 5 미반영

**현황**:
- [FRONTEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/FRONTEND.md) (42행): `createEventDispatcher` 언급 → Svelte 4 패턴
- [frontend-style/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/frontend-style/SKILL.md)에서는 Svelte 5 Runes(`$state`, `$props`, `$derived`)를 강제

**수정 제안**:
- FRONTEND.md의 Component Writing Rules를 Svelte 5에 맞게 업데이트
  - 3번 규칙: `createEventDispatcher` → Svelte 5의 callback props 또는 `$props()` 기반으로 변경
  - `export let` → `$props()` 표기로 변경

---

#### 3-7. `linter-rules.md` Import 규칙과 `tech-stack.md` Import 규칙 충돌

**현황**:
- [linter-rules.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/rules/linter-rules.md) (63행): "Relative path imports forbidden: `from ..models import User` ❌ → `from src.types.user import User` ✅"
- [tech-stack.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/design-docs/tech-stack.md) (57~58행): "모든 import는 `app`를 기준으로 한 절대 경로 예: `from app.core.config import settings`"
- 기준이 `src.*`인지 `app.*`인지 불명확

**수정 제안**: `linter-rules.md`의 Python import 예시를 `app.*` 기준으로 통일 (실제 프로젝트 구조에 맞게)

---

#### 3-8. `BACKEND.md` 파일 구조와 `tech-stack.md` 파일 구조 차이

**현황**:
- [BACKEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/BACKEND.md) (26~36행): `api/v1/`, `core/`, `crud/`, `models/`, `schemas/`, `services/`, `tests/`
- [tech-stack.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/docs/design-docs/tech-stack.md) (17~43행): `app/main.py`, `app/core/`, `app/models/`, `app/src/routes/`, `app/src/crud/`, `app/src/schemas/`, `app/src/engine/`
- `services/` vs `engine/`, `api/v1/` vs `src/routes/` 등 구조가 다름

**수정 제안**: `BACKEND.md`의 File Structure를 실제 프로젝트 디렉토리에 맞게 업데이트하거나, 이상적 목표와 현재 구조를 구분 표기

---

## 4. 워크플로우 / 스킬

### ✅ 잘 된 점
- 워크플로우가 일관된 형식 (Preconditions → Steps → Outputs → Rollback) 따름
- [coordinator.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/workflows/coordinator.md)의 태스크 분배 프로세스가 구체적이고 실용적
- [backend-style](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/backend-style/SKILL.md), [frontend-style](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/frontend-style/SKILL.md) 스킬이 AST 파싱까지 포함한 자동 검증 스크립트 제공
- [verify-implementation](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/verify-implementation/SKILL.md)의 다단계 검증 → 보고서 → 사용자 승인 → 자동 수정 → 재검증 흐름이 성숙

### 🔴 문제점 및 수정 제안

#### 4-1. `SKILLS.md`의 Workflow Skills 테이블에 명시된 워크플로우가 미구현

| 명시된 워크플로우 | 실제 존재 여부 |
|------------------|---------------|
| `/sprint-start` | ❌ 미존재 |
| `/sprint-review` | ❌ 미존재 |
| `/tech-debt-scan` | ❌ 미존재 |
| `/context-backup` | ❌ 미존재 |
| `/handover-cleanup` | ❌ 미존재 |

**수정 제안**: `SKILLS.md`의 Workflow Skills 테이블을 실제 존재하는 워크플로우(`/coordinator`, `/master`, `/architect`, `/backend`, `/frontend`, `/devops`, `/qa`)로 교체

---

#### 4-2. `Debug` 스킬 네이밍 규칙 위반

**현황**:
- 디렉토리명이 `Debug/` (PascalCase)
- `linter-rules.md` 1.3절: "디렉토리는 항상 kebab-case + 복수형"
- 다른 모든 스킬 디렉토리는 `kebab-case` 준수

**수정 제안**: `Debug/` → `debug/`로 리네임

---

#### 4-3. `Debug/SKILL.md` 내 보안 위험

> [!CAUTION]
> 테스트 사용자 자격 증명이 버전 관리되는 파일에 평문으로 기록되어 있습니다.

**현황**:
- [Debug/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/Debug/SKILL.md) (52~53행):
  ```
  ## Test User
  - ID: tester@example.com
  - PW: password123
  ```

**수정 제안**:
- `.env` 파일에서 참조하도록 변경: "테스트 계정은 `.env` 파일의 `TEST_ID` / `TEST_PW` 참조"
- 현재 파일에서 직접적인 평문 비밀번호 제거

---

#### 4-4. `Debug/SKILL.md` 내 존재하지 않는 경로 참조

**현황**:
- `.agent/project/logs/backend.log`, `.agent/project/logs/frontend.log` 경로 참조
- 해당 디렉토리는 프로젝트에 존재하지 않으며, `.agent/` 경로명도 잘못됨

**수정 제안**: 로그 출력 경로를 실제 존재하는 경로로 수정하거나, tee 없이 직접 출력으로 변경

---

## 5. 운영 준비도

### 🔴 문제점 및 수정 제안

#### 5-1. 컨텍스트 파일이 모두 빈 상태

**현황**: `contexts/` 디렉토리의 5개 역할 파일(`architect.md`, `backend_dev.md`, `frontend_dev.md`, `devops.md`, `qa_tester.md`)이 모두 0 bytes

**수정 제안**:
- `_TEMPLATE.md`의 기본 구조를 각 역할 파일에 사전 배포
- 최소한 "Core Principles" 섹션에 각 역할의 핵심 원칙 1~2개를 시드(seed) 값으로 기입
  - 예) `architect.md`: "ARCHITECTURE.md의 레이어 의존 방향은 절대 규칙"
  - 예) `backend_dev.md`: "모든 CRUD는 async def + 키워드 전용 인자(*) 필수"

---

#### 5-2. `handovers/to_*.md` 파일들의 포맷이 `_TEMPLATE.md`와 불일치

**현황**:
- [_TEMPLATE.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/handovers/_TEMPLATE.md): Summary, Background, Requested Tasks, Cautions, Reference Documents, Post-Completion Actions 구조
- 실제 `to_*.md` 파일들: 날짜, 현재 상황, 해야 할 일 구조 (coordinator.md 워크플로우 형식)
- 두 포맷이 서로 다름

**수정 제안**:
- `_TEMPLATE.md`와 `coordinator.md` 워크플로우의 포맷 중 하나를 표준으로 확정
- 현재 `to_*.md`의 간소한 형식이 실용적이므로, `_TEMPLATE.md`를 `coordinator.md`의 포맷에 맞추는 것을 권장

---

#### 5-3. `PLANS.md`의 Phase 1 완료 기준과 현재 상태 갭

**현황**:
- Phase 1 완료 기준: "에이전트가 문서를 읽고 독립적으로 작업 시작 가능"
- 현실: 다수의 빈 문서, 경로 불일치, SKILLS.md와 실제 괴리 → 에이전트가 혼란 가능

**수정 제안**: Phase 1 체크리스트 항목별로 현재 진행률을 명시적으로 업데이트
```markdown
- [x] Create `.agents/` directory structure and all convention documents
- [/] Define role-based agent personas — 구조 존재하나 contexts 비어있음
- [x] Establish linter rules and auto-correction guides
- [ ] Configure development environment Docker Compose
- [ ] Set up initial CI/CD pipeline
```

---

## 6. 기타 사소한 수정 사항

| # | 대상 파일 | 수정 내용 |
|---|----------|----------|
| 1 | [FRONTEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/FRONTEND.md) L101 | `webpack-bundle-analyzer` → SvelteKit 프로젝트에서는 `vite-bundle-visualizer` 등으로 변경 |
| 2 | [FRONTEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/FRONTEND.md) L17 | Flowbite 참조 시 "Flowbite-Svelte v2" 등 버전 명시 권장 |
| 3 | [BACKEND.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/BACKEND.md) L16 | `Python 3.10+` → `tech-stack.md`에서는 `Python 3.13` → 통일 필요 |
| 4 | [handover/SKILL.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/skills/handover/SKILL.md) L21 | 로그 파일명 패턴: `YYYY-MM-DD_<role>.md` vs `_TEMPLATE.md`의 `YYYY-MM-DD_to_<role>.md` → 통일 |
| 5 | [SKILLS.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/SKILLS.md) L43 | `contexts/<role>_context.md` → 실제 파일명은 `contexts/<role>.md` (예: `architect.md`, `backend_dev.md`) |
| 6 | [correction-guides.md](file:///Users/mipd/workspace/FullOps-Squad/.agents/rules/correction-guides.md) L121 | `src/types/` → `app/` 기준 경로로 통일 |

---

## 수정 우선순위 제안

> [!IMPORTANT]
> 아래 순서대로 수정하면 하네스의 신뢰성이 체계적으로 개선됩니다.

### 🔴 P0 — 에이전트 오동작 방지 (즉시 수정)
1. **3-1**: `.agent/` → `.agents/` 경로 일괄 수정
2. **3-7**: Import 기준 `src.*` → `app.*` 통일
3. **4-3**: Debug 스킬 내 평문 비밀번호 제거
4. **1-3**: `RELIABILITY.md`의 존재하지 않는 `rules/devops.md` 참조 수정

### 🟡 P1 — 문서 정합성 복원 (1주 내)
5. **3-3**: `SKILLS.md` 전면 재작성 (실제 스킬 반영)
6. **3-5**: `workflows/_README.md` 등록 테이블 실제 워크플로우로 교체
7. **3-4**: `skills/_README.md` 구조도 실제와 일치시킴
8. **1-1**: `docs/product-specs/` 경로 중복 해소
9. **3-8**: `BACKEND.md` 파일 구조를 실제 프로젝트와 동기화
10. **3-6**: `FRONTEND.md`를 Svelte 5 Runes로 업데이트

### 🟢 P2 — 완성도 향상 (Phase 1 마무리)
11. **2-1**: 빈 스텁 파일에 초기 구조 배포
12. **5-1**: 컨텍스트 파일에 템플릿 + 시드 값 배포
13. **5-2**: Handover 포맷 통일
14. **2-2**: PRODUCT_SENSE, RELIABILITY, SECURITY 체크리스트 확장
15. **3-2**: 문서 언어 전략 명시
16. **1-2**: ARCHITECTURE.md ↔ 실제 구조 매핑 추가
