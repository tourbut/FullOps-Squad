# PLANS.md — Project Roadmap & Milestones

<!-- AI Harness Rule: Summarize the macroscopic goals and milestones the project aims to achieve, either chronologically or by phases. -->

> Summarizes the macro-level goals and milestones the project aims to achieve in chronological/phase order.
> Detailed execution plans for each phase are managed in `docs/exec-plans/` subdocuments.

---

## Project Vision

Build a development system where AI agents **autonomously collaborate through documents**,
producing software of **consistent quality** with minimal human intervention.

---

## Phase 1: Foundation

**Goal**: Establish project structure, agent conventions, and basic infrastructure

- [ ] Create `.agents/` directory structure and all convention documents
- [ ] Define role-based agent personas (Architect, Backend, Frontend, DevOps, QA)
- [ ] Establish linter rules and auto-correction guides
- [ ] Configure development environment Docker Compose
- [ ] Set up initial CI/CD pipeline

**Completion Criteria**: Agents can read documents and begin work independently

---

## Phase 2: Core Domain Implementation

**Goal**: Build core business logic and data models

- [ ] Design domain models and finalize DB schema
- [ ] Implement core API endpoints (CRUD + business logic)
- [ ] Implement frontend base layout and key screens
- [ ] Achieve unit test coverage of 80% or above
- [ ] Auto-generate API documentation (OpenAPI/Swagger)

**Completion Criteria**: Core use cases work end-to-end

---

## Phase 3: Agent Autonomy

**Goal**: Stabilize inter-agent handover and autonomous execution systems

- [ ] Automate coordinator agent task distribution
- [ ] Validate creator-evaluator workflow based on sprint contracts
- [ ] Build QA agent's Playwright-based automated testing system
- [ ] Set up technical debt auto-detection and refactoring pipeline
- [ ] Stabilize context file auto-update workflows

**Completion Criteria**: Agents can autonomously complete 1 sprint without human intervention

---

## Phase 4: Quality Hardening

**Goal**: Achieve production-level stability and performance

- [ ] Load testing and performance optimization
- [ ] Security audit and vulnerability patching
- [ ] Build monitoring & alerting system
- [ ] UX improvements based on user feedback
- [ ] Achieve 90%+ compliance with org-specific quality metrics (`org-metrics.md`)

**Completion Criteria**: Ready for production deployment

---

## Phase 5: Scale & Operate

**Goal**: Ensure sustainable operations and scalability

- [ ] Generalize agent structure for multi-project support
- [ ] Standardize agent onboarding process for new domains/features
- [ ] Build operations dashboard and metrics visualization
- [ ] Establish automated document sync system (code changes → document sync)
- [ ] Write guides for team or community sharing

**Completion Criteria**: This system can be applied to a new project within 1 day

---

## Milestone Timeline (Example)

| Phase | Estimated Duration | Status |
|-------|-------------------|--------|
| Phase 1: Foundation | 2 weeks | 🔄 In Progress |
| Phase 2: Core Domain | 4 weeks | ⏳ Pending |
| Phase 3: Agent Autonomy | 3 weeks | ⏳ Pending |
| Phase 4: Quality Hardening | 3 weeks | ⏳ Pending |
| Phase 5: Scale & Operate | Ongoing | ⏳ Pending |

---

> **Note**: Detailed tasks and decision logs for each Phase are managed
> in `docs/exec-plans/active/` and `docs/exec-plans/completed/`.
