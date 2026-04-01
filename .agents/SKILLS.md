# SKILLS.md — Agent Skills & Tool Specifications

<!-- AI Harness Rule: Document the extended functionalities (skills) available to the agent and provide a specification on when and how to invoke each tool. -->

> Defines the extension capabilities (skills) available to agents,
> and specifies when and how each tool should be invoked.
> When adding a new skill, update this document first, then implement in `skills/`.

---

## Skill Classification

```
Skills
├── Core Skills           # Basic capabilities available to all agents
├── Role-Specific Skills  # Specialized capabilities restricted to certain roles
├── Workflow Skills        # Automated flows triggered via slash commands
└── Utility Skills         # Helper tools and auxiliary functions
```

---

## Core Skills

Skills available to all agents by default.

### `file-read`
- **Description**: Reads a file from the project and returns its content
- **When to invoke**: Before starting work to understand context; when referencing documents
- **Input**: `{ path: string }`
- **Output**: File content (string)

### `file-write`
- **Description**: Creates or modifies a file
- **When to invoke**: Writing code, updating documents, creating config files
- **Input**: `{ path: string, content: string }`
- **Output**: Success/failure status
- **Note**: Verify compliance with linter rules (`rules/linter-rules.md`) before saving

### `context-sync`
- **Description**: Reads and updates the agent's own context file
- **When to invoke**: At work start (read), at work completion (write)
- **Path**: `contexts/<role>_context.md`
- **Format**: `- [YYYY-MM-DD HH:mm:ss] content`

### `handover-dispatch`
- **Description**: Creates a handover document to transfer work to another role
- **When to invoke**: When a task outside the current role's scope is discovered
- **Path**: `handovers/to_<target_role>.md`
- **Note**: Record transfer log in `handovers/logs/`

---

## Role-Specific Skills

### Architect / PM Only

#### `schema-design`
- **Description**: Designs DB schema and generates ERD based on domain models
- **When to invoke**: When adding a new domain or requesting schema changes
- **Output**: SQL DDL + ERD diagram (Mermaid)

#### `adr-record`
- **Description**: Creates an Architecture Decision Record
- **When to invoke**: When a significant technical decision is made
- **Path**: `docs/exec-plans/active/ADR-<number>.md`

### Backend Developer Only

#### `api-scaffold`
- **Description**: Generates FastAPI endpoint boilerplate
- **When to invoke**: When adding a new API endpoint
- **Input**: `{ domain: string, resource: string, methods: string[] }`
- **Note**: Must comply with `ARCHITECTURE.md` layer structure

#### `migration-gen`
- **Description**: Auto-generates Alembic DB migration scripts
- **When to invoke**: When domain models change
- **Command**: `uv run alembic revision --autogenerate -m "<description>"`

### Frontend Developer Only

#### `component-scaffold`
- **Description**: Generates Svelte component boilerplate
- **When to invoke**: When adding a new UI component
- **Input**: `{ name: string, props: object, domain: string }`
- **Note**: Must comply with `FRONTEND.md` component writing rules

#### `route-scaffold`
- **Description**: Generates SvelteKit route page boilerplate
- **When to invoke**: When adding a new page
- **Output**: `+page.svelte`, `+page.ts`, `+page.server.ts`

### QA Engineer Only

#### `e2e-test-gen`
- **Description**: Generates Playwright-based E2E test scenarios
- **When to invoke**: When verifying test criteria from sprint contracts
- **Input**: `{ scenario: string, steps: string[] }`
- **Reference**: `docs/exec-plans/sprint-contracts/`

#### `qa-report-gen`
- **Description**: Auto-generates QA test result reports
- **When to invoke**: After test execution completes
- **Path**: `docs/evaluations/qa-reports/YYYY-MM-DD_qa-report.md`

### DevOps Engineer Only

#### `docker-compose-update`
- **Description**: Updates Docker Compose configuration
- **When to invoke**: When adding new services or changing environment variables

#### `deploy-trigger`
- **Description**: Executes the deployment pipeline
- **When to invoke**: After QA pass + coordinator approval
- **Note**: Verify rollback plan before deployment

---

## Workflow Skills

Automated task flows triggered via slash commands.
Implementations are located in the `workflows/` directory.

| Command | Description | Executor |
|---------|-------------|----------|
| `/sprint-start` | Create sprint contract and distribute tasks | Coordinator |
| `/sprint-review` | Generate sprint-end QA report | QA |
| `/tech-debt-scan` | Scan tech debt and update tracker | DevOps |
| `/context-backup` | Snapshot backup of all context files | Coordinator |
| `/handover-cleanup` | Migrate completed handovers to logs/ | Coordinator |

---

## Skill Addition Procedure

1. Add the skill specification to this document (`SKILLS.md`) first
2. Write implementation code in the `skills/` directory
3. Record new skill usage in the relevant role's context file
4. Verify no linter rule violations
5. Write test code and submit PR

---

> **Note**: Always check `ARCHITECTURE.md` dependency rules when invoking skills.
> Skill invocations that cross layer boundaries are automatically blocked.
