# AGENTS.md — Project Navigation Map

<!-- AI Harness Rule: Create an index mapping of this repository within 100 lines. Exclude detailed technical implementations. Only guide the paths for the agent to navigate, for instance, pointing to ARCHITECTURE.md for architecture and rules/ for linter rules. -->

> This document serves as the **entry point** for agents to understand and navigate the project.
> Specific technical details are delegated to their respective reference documents.

---

## Project Overview

This repository is an **AI agent collaboration-based software development project**.
Multiple role-based agents (Architect, Backend, Frontend, DevOps, QA) collaborate through documents,
maintain their own contexts, and transfer tasks via handovers.

---

## Navigation Guide

### Architecture & Structure
- **Technical Design Philosophy** → `DESIGN.md`
- **System Architecture & Dependency Rules** → `ARCHITECTURE.md`
- **Tech Stack & Environment Setup** → `docs/design-docs/tech-stack.md`
- **Overall Roadmap & Milestones** → `PLANS.md`

### Quality Standards & Governance
- **Overall Quality Scoring Criteria** → `QUALITY_SCORE.md`
- **Frontend Quality Standards** → `FRONTEND.md`
- **Backend Quality Standards** → `BACKEND.md`
- **System Reliability & Devops Rules** → `RELIABILITY.md`
- **Security Checklists & Constraints** → `SECURITY.md`

### Agent Tools
- **Skills & Tool Specifications** → `SKILLS.md`

### Product Sense & Planning
- **Product Mindset & Goal Alignment** → `PRODUCT_SENSE.md`
- **Meeting Notes & Ideas** → `docs/planning/meeting-logs/`
- **Problem Definitions (CPS)** → `docs/planning/cps/`
- **Product Specifications** → `docs/planning/product-specs/`

### Design Principles
- **Core Operating Beliefs** → `docs/design-docs/core-beliefs.md`
- **UI/UX Evaluation Criteria** → `docs/design-docs/ui-ux-guidelines.md`

### Execution Plans
- **Sprint Contracts** → `docs/exec-plans/sprint-contracts/`
- **Active Tasks** → `docs/exec-plans/active/`
- **Completed Tasks** → `docs/exec-plans/completed/`
- **Technical Debt Tracking** → `docs/exec-plans/tech-debt-tracker.md`

### Performance Evaluation
- **Organization-Specific Quality Metrics** → `docs/evaluations/org-metrics.md`
- **QA Bug Reports** → `docs/evaluations/qa-reports/`

### Auto-Generated & References
- **Auto-Generated Files (DB Schema, etc.)** → `docs/generated/`
- **External Reference Materials (Design System, etc.)** → `docs/references/`

### Mechanical Controls
- **Linter Rules** → `rules/linter-rules.md`
- **Linter Violation Correction Guides** → `rules/correction-guides.md`

### Agent Work Context
- **Role-Specific Contexts (Knowledge)** → `contexts/`
- **Task Handover Documents** → `handovers/`

### Ecosystem Management
- **Agent Skill Implementations** → `skills/`
- **Workflows (Slash Commands)** → `workflows/`

---

## Agent Behavior Rules (Summary)

1. **Before starting work**: Always read this document first, then explore relevant paths.
2. **No architecture violations**: Never violate the dependency directions in `ARCHITECTURE.md`.
3. **Follow linter rules**: Always comply with the mechanical constraints in `rules/linter-rules.md`.
4. **Maintain context**: Update your file in `contexts/` after completing work.
5. **Record handovers**: Leave records in `handovers/` when transferring tasks.
6. **Language rule**: 모든 응답과 문서 작성은 **한국어**로 합니다. 코드 주석도 한국어로 작성합니다. (구조 문서의 영어 제목/키워드는 유지)

---

> **Note**: This document is a concise map of under 100 lines.
> Refer to linked documents for details on each item.
