# BACKEND.md — Backend Quality Standards & Criteria

<!-- AI Harness Rule: Establish a grading rubric to evaluate the quality required in the corresponding domain (backend, security, stability, etc.). Include a fundamental capability checklist that the code must pass. -->

> Defines quality grades, coding conventions, and architectural design principles required for the backend domain.
> Backend agents must familiarize themselves with this document before starting work.

---

## Tech Stack Conventions

| Item | Choice | Notes |
|------|--------|-------|
| Framework | FastAPI | High-performance async API |
| Language | Python 3.13+ | Strict type hints required (`typing`) |
| ORM | SQLModel / SQLAlchemy | Declarative models, Pydantic integration |
| Database | PostgreSQL | Relational data standard |
| Task Queue | Celery / Redis | Background processing |

---

## Architectural Design Principles

### File Structure
```
backend/
├── app/                 # 메인 애플리케이션 코드
│   ├── main.py          # FastAPI 앱 엔트리포인트 (앱 실행, 미들웨어)
│   ├── core/            # 핵심 설정 및 유틸리티 (Config, Redis 등)
│   ├── models/          # 데이터베이스 모델 (SQLModel)
│   └── src/             # 비즈니스 로직 및 API 구현
│       ├── api.py       # API 라우터 통합
│       ├── routes/      # API 엔드포인트 핸들러
│       ├── crud/        # 데이터베이스 CRUD 함수
│       ├── schemas/     # Pydantic 데이터 검증 스키마
│       ├── engine/      # 핵심 엔진 로직 (AI, 백그라운드 작업)
│       ├── deps.py      # 의존성 주입 (DB 세션, 인증 등)
│       └── utils/       # 기타 유틸리티 함수
├── alembic/             # DB 마이그레이션 스크립트
└── tests/               # Pytest 테스트 스위트
```

### Component Writing Rules

1. **Separation of Concerns**: Routers handle requests/responses. Services handle business logic. CRUD handles database interactions.
2. **Explicit Dependency Injection**: Use FastAPI `Depends()` for database sessions, current user authentication, etc.
3. **Strict Type Hinting**: All functions, parameters, and return signatures MUST have accurate Python type hints.
4. **Centralized Error Handling**: Use structured exception raising (e.g., specific HTTPExceptions defined globally).
5. **File Size Limit**: A single `.py` file must aim to stay under **300 lines**. Refactor into smaller modules if it grows larger.

---

## Quality Grade Criteria

### Architecture & Modularity (40%)

| Grade | Criteria |
|-------|----------|
| **A** | Perfect separation of concerns; no business logic in routers or DB queries in schemas. |
| **B** | Great architecture; 1-2 minor logic bleeds across layers. |
| **C** | Basic layer separation; some noticeable coupling between routers and database calls. |
| **D** | High coupling; thick router functions directly manipulating the database. |
| **F** | Monolithic "God functions"; no clear boundary between HTTP, logic, and data layers. |

### Reliability & Error Handling (30%)

| Grade | Criteria |
|-------|----------|
| **A** | All exceptions are caught, logged, and translated into standardized HTTP error responses. |
| **B** | Standard HTTP errors are returned, but some internal exceptions might leak stack traces or missing logs. |
| **C** | Basic error handling is present, but inconsistent across different endpoints. |
| **D** | Poor error handling; 500 Internal Server Errors are common for predictable edge cases. |
| **F** | No error handling; uncaught exceptions crash background tasks or expose sensitive data. |

### Functionality & Performance (30%)

| Grade | Criteria |
|-------|----------|
| **A** | Perfect execution; zero N+1 database queries; efficient async/await usage everywhere. |
| **B** | Works flawlessly; maybe 1-2 minor synchronous blocking calls in async routes. |
| **C** | Core features work; noticeable N+1 query patterns or inefficient loops exist. |
| **D** | Features work but cause performance bottlenecks or timeout risks under load. |
| **F** | Core business logic fails or generates corrupted data states. |

---

## Security & Performance Checklist

- [ ] All sensitive environment variables are loaded via Pydantic `BaseSettings`.
- [ ] Passwords and secrets are hashed (e.g., using `passlib`/`bcrypt`).
- [ ] SQL Injection prevented (ORM exclusively used, no raw string concatenation).
- [ ] Proper pagination implemented on all list endpoints.
- [ ] Expensive I/O or computations are offloaded to background tasks (Celery/FastAPI BackgroundTasks).
- [ ] No N+1 query issues (Used `joinedload`, `selectinload`, or specific `JOIN`s).

---

## Testing Requirements

| Test Type | Target | Tool | Minimum Coverage |
|-----------|--------|------|------------------|
| Unit Tests | Schemas, Utilities, Services | Pytest | 80% |
| Integration Tests | DB access (CRUD layer) | Pytest + Test DB | 90% |
| API (E2E) Tests | FastAPI Routers | Pytest + HTTPX | 100% of critical endpoints |
| Load Tests | High-traffic endpoints | Locust / k6 | Required before production launch |

---

> **Scoring Timing**: During PR review + at sprint end
> **Scorer**: QA agent & automated CI tools
> **Results Recorded In**: `.agents/docs/evaluations/qa-reports/`
