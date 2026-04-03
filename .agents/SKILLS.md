# SKILLS.md — Agent Skills & Tool Specifications

<!-- AI Harness Rule: Document the extended functionalities (skills) available to the agent and provide a specification on when and how to invoke each tool. -->

> 에이전트에게 제공되는 확장 기능(스킬)을 정의하고,
> 각 도구를 언제, 어떻게 호출해야 하는지 명시합니다.
> 새로운 스킬 추가 시 이 문서를 먼저 업데이트한 후 `skills/`에 구현합니다.

---

## 스킬 분류

```
Skills
├── Process Skills         # 에이전트 작업 프로세스 관리
├── Verification Skills    # 코드/문서 품질 검증
├── Development Skills     # 개발 관련 보조 도구
└── Utility Skills         # 범용 유틸리티
```

---

## Process Skills

에이전트의 작업 흐름과 지식 관리를 위한 스킬입니다.

### `role-context`
- **설명**: 에이전트의 역할별 지식 관리 (로드/축적)
- **호출 시점**: 작업 시작 전(지식 로드), 작업 완료 후(지식 기록)
- **경로**: `contexts/<role>.md`

### `handover`
- **설명**: 역할 간 작업 이관(Handover) 완료 처리 및 로그 기록
- **호출 시점**: Handover 문서의 모든 태스크 완료 시
- **경로**: `handovers/to_<role>.md` → `handovers/logs/`

### `git-rules`
- **설명**: Git 커밋 메시지 컨벤션 및 브랜치 전략 검증
- **호출 시점**: 코드 커밋/Push 시, PR 생성 전

### `manage-skills`
- **설명**: 기존 스킬 탐색, 신규 스킬 생성/업데이트, SKILLS.md 관리
- **호출 시점**: 새로운 스킬이 필요하거나 기존 스킬 변경 시

---

## Verification Skills

코드와 문서의 품질을 자동 검증하는 스킬입니다.

### `verify-implementation`
- **설명**: 모든 `verify-*` 스킬을 순차 실행하여 통합 검증 보고서 생성
- **호출 시점**: 기능 구현 후, PR 생성 전, 코드 리뷰 시

### `backend-style`
- **설명**: 백엔드 코드 스타일 검증 (FastAPI + SQLModel)
- **호출 시점**: 백엔드 로직 수정 후
- **검증 대상**: Models, Schemas, CRUD, Routes

### `frontend-style`
- **설명**: 프론트엔드 코드 스타일 검증 (Svelte 5 + FastAPI Client)
- **호출 시점**: 프론트엔드 구현 및 API 연동 후
- **검증 대상**: Runes 문법, 인라인 CSS, API 래퍼 사용

### `qa-tester`
- **설명**: QA 테스트 케이스 작성, 테스트 실행, 버그 리포트 생성
- **호출 시점**: 기능 테스트가 필요할 때

---

## Development Skills

개발 작업을 보조하는 스킬입니다.

### `debug`
- **설명**: 디버깅을 위한 서버 구동 및 로그 확인
- **호출 시점**: 로컬 개발 환경에서 테스트가 필요할 때

### `refactoring`
- **설명**: 코드 스멜 식별 및 안전한 리팩토링 가이드
- **호출 시점**: 코드 품질 개선 작업 시

### `prompt-engineer`
- **설명**: LLM용 프롬프트 및 시스템 프롬프트 설계/최적화
- **호출 시점**: AI 관련 프롬프트 작성 요청 시

---

## Utility Skills

문서 생성 및 범용 도구입니다.

### `docx`
- **설명**: Word 문서(.docx) 생성, 읽기, 편집
- **호출 시점**: Word 문서 관련 작업 시

### `pdf`
- **설명**: PDF 파일 생성, 읽기, 병합, 분할
- **호출 시점**: PDF 파일 관련 작업 시

### `pptx`
- **설명**: PowerPoint 프레젠테이션 생성/편집
- **호출 시점**: 슬라이드/프레젠테이션 관련 작업 시

### `xlsx`
- **설명**: Excel 스프레드시트 생성/편집
- **호출 시점**: 스프레드시트 관련 작업 시

### 기타 유틸리티
| 스킬 | 설명 |
|------|------|
| `skill-creator` | 새 스킬 생성, 기존 스킬 개선, 성능 측정 |
| `frontend-design` | 프로덕션급 프론트엔드 UI 구현 |
| `canvas-design` | 시각적 아트/포스터/디자인 제작 |
| `algorithmic-art` | p5.js 기반 알고리즘 아트 생성 |
| `brand-guidelines` | 브랜드 색상/타이포그래피 적용 |
| `theme-factory` | 아티팩트 테마 스타일링 |
| `web-artifacts-builder` | 복잡한 웹 아티팩트 제작 (React + Tailwind) |
| `webapp-testing` | Playwright 기반 웹앱 테스트 |
| `doc-coauthoring` | 문서 공동 작성 워크플로우 |
| `internal-comms` | 내부 커뮤니케이션 문서 작성 |
| `mcp-builder` | MCP 서버 구축 가이드 |
| `slack-gif-creator` | Slack용 애니메이션 GIF 제작 |

---

## Workflow Skills

슬래시 커맨드로 트리거되는 자동화된 작업 흐름입니다.
구현은 `workflows/` 디렉토리에 위치합니다.

| 커맨드 | 설명 | 실행자 |
|--------|------|--------|
| `/master` | 요구사항 분석 및 제품 명세/기획안 생성 | PM |
| `/coordinator` | 태스크를 역할별 Handover 파일로 분배 | Coordinator |
| `/architect` | 시스템 아키텍처 설계 및 기술 스택 관리 | Architect |
| `/backend` | 백엔드 모듈/API 설계 및 비즈니스 로직 개발 | Backend Dev |
| `/frontend` | 프론트엔드 UI/UX 구현 및 API 연동 | Frontend Dev |
| `/devops` | 인프라 구성, CI/CD 구축 및 배포 자동화 | DevOps |
| `/qa` | 품질 기준에 따른 테스트 및 버그 리포트 생성 | QA |

---

## 스킬 추가 절차

1. 이 문서(`SKILLS.md`)에 스킬 사양을 먼저 추가
2. `skills/` 디렉토리에 구현 코드 작성
3. 해당 역할의 컨텍스트 파일에 신규 스킬 사용 기록
4. 린터 규칙 위반 없음 확인
5. 테스트 코드 작성 후 PR 제출

---

> **참고**: 스킬 호출 시 `ARCHITECTURE.md`의 의존성 규칙을 반드시 확인하세요.
> 레이어 경계를 넘는 스킬 호출은 자동으로 차단됩니다.
