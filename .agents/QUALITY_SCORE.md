# QUALITY_SCORE.md — Domain/Layer Quality Scoring Criteria

<!-- AI Harness Rule: Establish a grading rubric to evaluate the quality required in the corresponding domain (frontend, security, stability, etc.). Include a fundamental capability checklist that the code must pass. -->

> A criteria table for scoring code and system quality in a **mechanically assessable** manner.
> Defines grades (A–F) per area and specifies the minimum passing threshold (C or above).

---

## Grading System

| Grade | Score | Meaning |
|-------|-------|---------|
| **A** | 90–100 | Exemplary — Can be used as a reference for other projects |
| **B** | 80–89 | Excellent — Sufficient for production deployment |
| **C** | 70–79 | Pass — Meets minimum standards, improvement recommended |
| **D** | 60–69 | Below Standard — Must be improved, resolve before deployment |
| **F** | 0–59 | Fail — Immediate fix or rollback required |

---

## 1. Code Quality

| Item | Weight | Measurement Method | Minimum Threshold |
|------|--------|--------------------|-------------------|
| Test Coverage | 25% | Unit + integration test line coverage | ≥ 80% |
| Linter Violations | 20% | Violation count based on `rules/linter-rules.md` | 0 violations |
| Cyclomatic Complexity | 15% | Cyclomatic Complexity per function | ≤ 10 |
| Code Duplication | 15% | Duplicate block ratio | ≤ 5% |
| Type Safety | 15% | TypeScript strict / Python type hints coverage | ≥ 90% |
| Documentation | 10% | Docstring/JSDoc coverage for public APIs | ≥ 80% |

---

## 2. Architecture Quality

| Item | Weight | Measurement Method | Minimum Threshold |
|------|--------|--------------------|-------------------|
| Dependency Direction Compliance | 30% | Violation count against `ARCHITECTURE.md` rules | 0 violations |
| Domain Separation | 25% | Direct cross-domain reference count | 0 references |
| Single Responsibility Principle | 20% | Exported symbols per file | ≤ 7 |
| Layer Isolation | 15% | Layer-skip count (e.g., UI→Repo direct access) | 0 skips |
| API Consistency | 10% | Response format uniformity, error structure consistency | 100% |

---

## 3. Security Quality

| Item | Weight | Measurement Method | Minimum Threshold |
|------|--------|--------------------|-------------------|
| Authentication/Authorization | 30% | Number of unprotected endpoints | 0 |
| Input Validation | 25% | Unvalidated user input handling count | 0 |
| Secret Management | 20% | Hardcoded credential count | 0 |
| Dependency Vulnerabilities | 15% | Packages with known CVEs | 0 (Critical/High) |
| Log Security | 10% | Log entries containing sensitive information | 0 |

---

## 4. Reliability Quality

| Item | Weight | Measurement Method | Minimum Threshold |
|------|--------|--------------------|-------------------|
| Error Handling | 30% | Unhandled exception count | 0 |
| Retry Logic | 20% | Retry/fallback implementation for external calls | 100% |
| Data Integrity | 20% | Missing transaction handling count | 0 |
| Monitoring | 15% | Health check, metrics endpoint availability | Present |
| Disaster Recovery | 15% | Rollback procedure documentation | Present |

---

## 5. Performance Quality

| Item | Weight | Measurement Method | Minimum Threshold |
|------|--------|--------------------|-------------------|
| API Response Time (P95) | 30% | 95th percentile response time | ≤ 500ms |
| Page Load Time | 25% | Lighthouse Performance Score | ≥ 80 |
| DB Query Efficiency | 20% | N+1 query count, slow query count | 0 |
| Memory Usage | 15% | Container memory utilization | ≤ 80% |
| Bundle Size | 10% | Frontend initial load bundle size | ≤ 300KB (gzip) |

---

## Baseline Checklist

**Minimum requirements** that must be met before code can be reviewed/merged:

- [ ] 0 linter violations
- [ ] All tests pass (unit + integration)
- [ ] 0 dependency rule violations per `ARCHITECTURE.md`
- [ ] No hardcoded secrets
- [ ] Documentation (docstring) written for all new public APIs
- [ ] No external calls with missing error handling
- [ ] DB migration script included (if schema changes)
- [ ] PR description includes change rationale and impact scope

---

> **Scoring Timing**: At sprint end or before major PR merges
> **Scorer**: QA agent or Coordinator agent
> **Results Recorded In**: `docs/evaluations/qa-reports/`
