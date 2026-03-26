# `.agents` 사용 가이드 및 구조

본 문서는 하네스 엔지니어링 구조를 적용한 `FullOps-Squad/.agents` 환경의 메타 지식 저장소를 설명합니다. 
AI 에이전트가 이 폴더의 내용을 참조하여 코드 작성, 기획, 테스트, 배포 등의 역할을 보다 체계적으로 수행할 수 있도록 돕습니다.

## 기본 디렉토리 구조
```text
.agents/
├── AGENTS.md             # 에이전트 시스템 가이드 (현재 문서)
├── ARCHITECTURE.md       # 시스템 아키텍처 개요
├── DESIGN.md             # 디자인 철학 및 원칙
├── FRONTEND.md           # 프론트엔드 가이드
├── PLANS.md              # 로드맵 및 실행 계획
├── PRODUCT_SENSE.md      # 프로덕트 방향성
├── QUALITY_SCORE.md      # 개발 품질 기준
├── RELIABILITY.md        # 시스템 안정성
├── SECURITY.md           # 보안 수칙
│
├── docs/                 # 기획, 설계, 자동 생성된 지식 저장소
│   ├── design-docs/      # 기술 세부 설계 문서
│   ├── exec-plans/       # 마일스톤, 진행 상황 및 기술 부채
│   ├── generated/        # 자동 생성 문서 (DB 스키마 등)
│   ├── product-specs/    # 제품 기능 스펙
│   └── references/       # LLM 참조용 레퍼런스 링크/텍스트
│
├── contexts/             # 각 에이전트 역할별 컨텍스트
├── handovers/            # 에이전트 작업 이관 규칙
├── project/              # 프로젝트 메타 데이터 및 임시 아티팩트
├── rules/                # 기술 스택별 코딩 스타일 및 기본 규칙
├── skills/               # 개별 검증 스크립트 및 유지보수 스킬
└── workflows/            # 복합 자동화 워크플로우
```

## AI 에이전트 가이드 (How to use)
- 새로운 기능을 구현할 땐, `docs/product-specs/`의 스펙 문서와 `ARCHITECTURE.md`, `DESIGN.md`를 우선 확인하세요.
- 코드 작성 전에는 `rules/` 디렉토리와 `FRONTEND.md`(혹은 백엔드 가이드)를 읽고 코딩 스타일을 준수하세요.
- 각 에이전트는 역할을 시작할 때 `contexts/`의 해당 역할 문서를 참조하고, 작업 완료 후 `handovers/`를 참고하여 로그를 남깁니다.
