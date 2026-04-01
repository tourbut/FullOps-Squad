# BACKEND.md — Backend Quality Standards & Criteria

<!-- AI Harness Rule: Establish a grading rubric to evaluate the quality required in the corresponding domain (backend, security, stability, etc.). Include a fundamental capability checklist that the code must pass. -->

> Defines quality grades, coding conventions, and architectural design principles required for the backend domain.
> Backend agents must familiarize themselves with this document before starting work.

---

## Tech Stack Conventions

| Item | Choice | Notes |
|------|--------|-------|
| Framework | FastAPI | High-performance async API |
| Language | Python 3.10+ | Strict type hints required (`typing`) |
| ORM | SQLModel / SQLAlchemy | Declarative models, Pydantic integration |
| Database | PostgreSQL | Relational data standard |
| Task Queue | Celery / Redis | Background processing |

---

## Architectural Design Principles

### File Structure
```
backend/
├── api/             # API Routers (FastAPI endpoints)
│   ├── v1/          # API versioning
│   └── deps.py      # FastAPI Dependency Injection
├── core/            # Config, security, and global settings
├── crud/            # CRUD operations and database repositories
├── models/          # Database models (SQLModel/SQLAlchemy)
├── schemas/         # Pydantic schemas (Validation & Serialization)
├── services/        # Core business logic
└── tests/           # Pytest test suite
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
