# SKILLS.md — Agent Skills & Workflows Index

<!-- AI Harness Rule: 에이전트가 사용할 수 있는 스킬(확장 기능)과 워크플로우(슬래시 커맨드) 전체 목록과 호출 시점을 한눈에 볼 수 있도록 정리한다. 상세 구현/절차는 각 `skills/<name>/SKILL.md` 또는 `workflows/<name>.md`에 있다. -->

> 새 스킬·워크플로우 추가 시 이 문서에 **먼저 한 줄로 등록**한 뒤 구현 파일을 작성한다.
> 스킬은 `skills/`, 워크플로우는 `workflows/` 디렉토리에 위치한다.

---

## 1. 프로세스 · 품질 스킬

| 스킬 | 호출 시점 | 주요 경로 |
|------|----------|-----------|
| `role-context` | 작업 전(지식 로드)·후(지식 축적) | `contexts/<role>.md` |
| `handover` | `to_<role>.md`의 모든 태스크 완료 시 | `handovers/to_*.md` → `handovers/logs/` |
| `git-rules` | 커밋/Push/PR 생성 직전 | — |
| `manage-skills` | 신규 스킬 생성·기존 스킬 동기화 시 | `skills/verify-*/SKILL.md` |
| `verify-implementation` | 기능 구현 후·PR 전 통합 검증 | `backend-style`·`frontend-style`·`verify-linter-rules` 순차 실행 |
| `verify-linter-rules` | 코드 변경 후 기계적 린터 검증 | `backend/**/*.py`, `frontend/src/**` |
| `backend-style` | 백엔드 로직 수정 후 (Models/Schemas/CRUD/Routes) | `backend/app/...` |
| `frontend-style` | 프론트 구현·API 연동 후 (Runes/API 래퍼/Tailwind) | `frontend/src/...` |
| `qa-tester` | QA 테스트 실행·버그 리포트 생성 시 | `.agents/docs/evaluations/qa-reports/` |

## 2. 개발 보조 스킬

| 스킬 | 호출 시점 |
|------|----------|
| `debug` | 로컬 서버 구동·로그 확인이 필요한 개발 단계 |
| `refactoring` | 코드 스멜 식별 및 안전한 리팩토링 |
| `prompt-engineer` | LLM/시스템 프롬프트 설계·최적화 |
| `skill-creator` | 새 스킬 생성·기존 스킬 개선/평가 |
| `evaluate-harness` | 하네스 건강 지표 측정 및 진단 리포트 생성 |
| `design-mockup` | 구현 전 자체완결 HTML 목업으로 UI/UX 선(先)확정 (산출: `docs/design-docs/mockups/`) |
| `frontend-design` | 프로덕션급 UI 구현 가이드 |
| `web-artifacts-builder` | React + Tailwind 기반 웹 아티팩트 제작 |
| `webapp-testing` | Playwright 기반 웹앱 E2E 테스트 |
| `webwright` | 웹 태스크를 code-as-action으로 자동화·검증 (Playwright/Firefox, 스크린샷 증거 + 재실행 스크립트) |
| `mcp-builder` | 외부 서비스 연동용 MCP 서버 구축 |
| `context7-mcp` | 라이브러리·프레임워크·API 문서를 Context7로 실시간 조회 |

## 3. 워크플로우 (슬래시 커맨드)

> 각 워크플로우는 `Preconditions → Steps → Outputs → Rollback` 형식이며,
> 공통 전처리(핸드오버 읽기 → 컨텍스트 로드 → 브랜치 생성)는 `workflows/_README.md`의 **Common Preamble**에서 1회 정의한다.

| 커맨드 | 설명 | 실행자 |
|--------|------|--------|
| `/master` | 신규 요구사항·기능 분석 및 기획 산출물(meeting-logs·cps·product-specs) 현행화 | PM |
| `/coordinator` | 상위 태스크를 역할별 Handover 파일로 분배 | Coordinator |
| `/architect` | 시스템 아키텍처 설계 및 기술 스택 관리 | Architect |
| `/design` | 구현 전 디자인 목업 작성·UI/UX 확정 (frontend/backend 구현 선행 게이트) | Frontend/Design |
| `/backend` | 백엔드 모듈/API 설계 및 비즈니스 로직 개발 | Backend Dev |
| `/frontend` | 프론트엔드 UI/UX 구현 및 API 연동 | Frontend Dev |
| `/devops` | 인프라 구성·CI/CD 구축·배포 자동화 | DevOps |
| `/qa` | 품질 기준에 따른 테스트 및 버그 리포트 | QA |
| `/release` | `develop` → `main` 병합 및 배포 준비 | DevOps |
| `/improve` | 하네스 평가·자율 개선 루프 | Architect |

---

## 스킬/워크플로우 추가 절차

1. 이 문서의 해당 테이블에 **한 줄 등록** (이름·호출 시점·경로)
2. `skills/<name>/SKILL.md` 또는 `workflows/<name>.md` 구현
3. 역할 컨텍스트(`contexts/<role>.md`)에 사용 기록 시드
4. `verify-linter-rules` 통과 확인 후 PR 제출

> 스킬 호출 시 `ARCHITECTURE.md`의 레이어 의존 방향을 우선 확인한다.
> 레이어 경계 위반 호출은 자동 차단된다.
