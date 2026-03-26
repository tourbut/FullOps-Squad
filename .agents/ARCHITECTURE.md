# 시스템 아키텍처 개요 (Architecture)

이 문서는 FullOps-Squad 프로젝트의 핵심 기술 스택 및 모듈 구성 방식을 설명하는 메타 문서입니다.
세부적인 설계(디자인 문서)는 `docs/design-docs/` 디렉토리를 참조하세요.

## 1. 기술 스택 (Tech Stack)
- **프론트엔드**: Svelte (또는 구체적 프레임워크), `FRONTEND.md` 및 `rules/dev-frontend-svelte.md` 참조
- **백엔드**: FastAPI + SQLModel, `rules/dev-backend-fastapi.md` 참조
- **데이터베이스**: Postgres 등 구체적 DB 명시 필요. 자동 생성 스키마는 `docs/generated/db-schema.md` 참고
- **인프라/DevOps**: (CI/CD 구성), `rules/devops.md` 및 `workflows/devops.md` 참고

## 2. 주요 시스템 컴포넌트
(여기에 주요 서비스 아키텍처 블록 다이어그램이나 모듈 설명을 작성합니다.)

> [!NOTE]
> 에이전트는 기존 모듈을 수정할 때 해당 컴포넌트 간의 의존성을 파악해야 합니다.
> 만약 새로운 시스템이나 서비스를 도입하게 된다면 `AHA` (Avoid Hasty Abstractions) 원칙을 준수하여 이 문서에 반영해 주세요.
