# FullOps-Squad
엔드투엔드(E2E) AI 에이전트 개발 플랫폼

## AI 에이전트 하네스 구조 (Agent Harness Structure)

FullOps-Squad는 여러 역할 기반 AI 에이전트(Architect, Backend, Frontend, DevOps, QA)가 자율적으로 협업하고 시스템을 개발 / 유지보수할 수 있도록 **AI 에이전트 하네스(AI Harness)** 구조를 탑재하고 있습니다. 모든 에이전트 관련 지침과 컨텍스트는 프로젝트 루트의 `.agents/` 디렉터리 내에 관리됩니다.

### 🗂 상세 디렉터리 구조도 (Depth-2 Directory Tree)

```text
.agents/
├── AGENTS.md                  # 진입점(Entry Point) 및 내비게이션 트리
├── ARCHITECTURE.md            # 시스템 아키텍처 및 모듈 간 의존성 규칙
├── DESIGN.md                  # 기술적 설계 철학과 방향성
├── PLANS.md                   # 전체 개발 로드맵 및 마일스톤 추적
├── PRODUCT_SENSE.md           # 프로덕트 마인드셋 및 비즈니스 목표 정렬
├── SKILLS.md                  # 에이전트 커스텀 스킬 목록 및 기능 명세
├── QUALITY_SCORE.md           # 전체 품질 평가 체계 및 점수 기준
├── FRONTEND.md                # FE 개별 품질 검증 및 개발 표준
├── BACKEND.md                 # BE 개별 품질 검증 및 개발 표준
├── RELIABILITY.md             # 시스템 안정성과 DevOps 인프라 규칙
├── SECURITY.md                # 보안 체크리스트 및 제약 조건
├── contexts/                  # 각 에이전트 역할별 워크 컨텍스트 관리 (Context State 보존)
│   ├── _TEMPLATE.md           # 상태 문서 양식 템플릿
│   ├── architect.md           # 아키텍트 컨텍스트
│   ├── backend_dev.md         # 백엔드 개발자 컨텍스트
│   ├── frontend_dev.md        # 프론트엔드 개발자 컨텍스트
│   ├── devops.md              # 데브옵스 컨텍스트
│   └── qa_tester.md           # QA 테스터 컨텍스트
├── docs/                      # 프로젝트 통합 문서 지식 공간 (Knowledge Base)
│   ├── design-docs/           # 기술 스택, 구조, UI 등 설계 문서
│   ├── evaluations/           # QA 리포트, 조직 성과 지표 기록
│   ├── exec-plans/            # 스프린트 플랜 체결 문서 및 완료/진행 태스크 목록
│   ├── generated/             # 시스템 자동 생성물 (DB 스키마 등)
│   ├── planning/              # 문제 정의(CPS), 제품 스펙, 회의록 보관
│   └── references/            # 외부 디자인 시스템, 운영 자료 등 레퍼런스
├── handovers/                 # 에이전트 간 역할 전환/작업 이관 시 생성되는 문서함
│   ├── _README.md, _TEMPLATE.md
│   ├── to_architect.md        # 아키텍트 전달 인박스 (이하 동일 구성)
│   ├── to_backend_dev.md      
│   ├── to_frontend_dev.md     
│   ├── to_devops.md           
│   ├── to_qa_tester.md        
│   └── logs/                  # 처리가 완료된 과거 핸드오버 기록 백업 공간
├── rules/                     # 기계적 린터 검증 및 위반 사항 가이드 모음
│   ├── base.md                # 에이전트 글로벌 행동 기반 규칙
│   ├── linter-rules.md        # 코딩 스타일 및 린터 강제 룰 정의서
│   └── correction-guides.md   # 위반 항목 발생 시 해결 지침서
├── skills/                    # 에이전트 스킬 동작 구현체 폴더
└── workflows/                 # 상위 수준 에이전트 슬래시 커맨드 매뉴얼
    ├── _README.md
    ├── master.md              # 제품 초기 명세/기획 워크플로우
    ├── coordinator.md         # 태스크 분배 및 코디네이팅 플로우
    ├── architect.md           # 기술 아키텍처 및 시스템 설계 플로우
    ├── backend.md             # 백엔드 API & 로직 개발 플로우
    ├── frontend.md            # 프론트엔드 UI & 연동 개발 플로우
    ├── devops.md              # 인프라 구성 및 배포 자동화 플로우
    └── qa.md                  # 품질 테스트 및 버그 리포트 생성 플로우
```

### 🤖 에이전트 주요 행동 규칙
이 저장소를 다루는 모든 에이전트들은 다음 규칙을 최우선으로 따르며 동작합니다.
1. 작업 시작 시 `.agents/AGENTS.md`를 우선적으로 읽어 내비게이션 구조를 파악합니다.
2. `ARCHITECTURE.md`에 명시된 아키텍처 디자인 방향 및 의존성 규칙을 절대 위배하지 않습니다.
3. 코드 작성 및 검토 시 `rules/linter-rules.md`를 철저히 확인하고 지킵니다.
4. 작업 완료 후 `contexts/`에 최신 워크 컨텍스트를 커밋하며, 역할 이관 시 `handovers/`에 세부 내용을 기록으로 남깁니다.
5. 코드의 주석을 포함한 모든 문서 답변은 원칙적으로 **한국어**로 작성합니다.

### 🛠️ 에이전트 워크플로우 파이프라인 (Workflow Pipeline)
이 하네스는 다음과 같은 단계를 거쳐 기획부터 설계, 테스트까지 유기적으로 협력하여 작업을 수행합니다.

1. **요구사항 발의 및 기획 (Master)**
   - `/master` 워크플로우를 통해 사용자의 아이디어나 요구사항 접수.
   - 분석 과정을 거쳐 `.agents/docs/planning/product-specs/` 경로에 제품 명세서(Spec) 등으로 구체화 및 문서화.
2. **설계 및 아키텍처 검토 (Architect)** *(프로젝트 초기 혹은 대규모 기능 개발 시)*
   - 확정된 기획안을 바탕으로 `/architect` 워크플로우 진행.
   - 관련 시스템 아키텍처 규칙(`ARCHITECTURE.md`) 현행화 및 개발 방향성 확립.
3. **태스크 분할 및 설계안 배포 (Coordinator)**
   - 기획 및 방향성이 확정되면 `/coordinator` 워크플로우가 이를 개발 단위의 작은 작업(Task)으로 쪼갬.
   - 쪼개진 단위 작업들은 각 직군별 작업 지시서(`.agents/handovers/to_*.md`)로 분산 할당.
4. **실제 작업 수행 및 검증 (Frontend/Backend/DevOps/QA 등)**
   - 개별 개발 에이전트는 할당받은 작업 지시서를 바탕으로 코드를 구현하고 린트 룰에 맞춰 리뷰.
   - `/qa` 워크플로우에 의해 통합 품질 테스트를 수행, 요구 시 피드백과 개선 루프 반복.

### 🔄 자가 개선 파이프라인 (Self-Improvement Pipeline)
이 하네스는 정체되지 않고 스스로의 문서 구조와 룰을 객관적으로 분석/최적화하는 내장형 "자기 개선(Self-Improvement) 루프"를 갖추고 있습니다. 

- **평가 지표 (`harness-metrics.md`)**: 에이전트 작업 간의 핑퐁 반복 횟수, 룰 위반율, 스킬 구동 성공률 등을 수치화하여 하네스의 건강 점수(Health Score) 기준으로 관리합니다.
- **상태 진단 스킬 (`evaluate-harness`)**: 현재 프로젝트의 누적 로그(`.agents/handovers/logs/`)와 컨텍스트 문서들을 읽어들여 낡은 관행이나 문제점을 파악하고, 일정한 포맷(`.agents/docs/evaluations/harness/YYYY-MM-DD_harness-health-report.md`)으로 개선 권고안(Action Items)을 리포트합니다.
- **자가 개선 워크플로우 (`/improve`)**: 스킬을 기동하여 진단을 내린 후, 도출된 Action Items를 바탕으로 낡은 규칙을 폐기하거나 문서를 자체 리팩토링합니다. 개선 결과는 발행된 리포트 하단에 `Before/After` 이력으로 누적 보존됩니다.
