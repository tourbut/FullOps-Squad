# workflows/ — Slash Command Executable Workflows

> This directory contains definitions and implementations of
> **automated workflows** triggered via slash commands (`/command`).

---

## Directory Structure

```
workflows/
├── _README.md               # This file
├── sprint-start.md          # /sprint-start workflow definition
├── sprint-review.md         # /sprint-review workflow definition
├── tech-debt-scan.md        # /tech-debt-scan workflow definition
├── context-backup.md        # /context-backup workflow definition
└── handover-cleanup.md      # /handover-cleanup workflow definition
```

---

## Workflow Definition Format

Each workflow file follows the structure below:

```markdown
# /[command-name]

> Description: [What this workflow does]
> Executor: [Which agent role runs it]
> Trigger: [Manual / Automatic / Scheduled]

## Preconditions
- [Conditions that must be met before execution]

## Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Outputs
- [Files or results produced by the workflow]

## Rollback
- [How to revert if something goes wrong]
```

---

## Registered Workflows

| Command | Description | Executor | Status |
|---------|-------------|----------|--------|
| `/sprint-start` | Create sprint contract + distribute tasks | Coordinator | 📝 Defined |
| `/sprint-review` | Generate sprint-end QA report | QA | 📝 Defined |
| `/tech-debt-scan` | Scan tech debt + update tracker | DevOps | 📝 Defined |
| `/context-backup` | Snapshot backup of all context files | Coordinator | 📝 Defined |
| `/handover-cleanup` | Migrate completed handovers → logs/ | Coordinator | 📝 Defined |

---

## New Workflow Addition Procedure

1. Add an entry to the "Workflow Skills" table in `SKILLS.md`
2. Create a `[command-name].md` file in this directory
3. If required skill implementations don't exist, add them to `skills/`
4. Run tests and submit PR

---

> **Workflows are the "automated routines" of agents.**
> By defining repetitive tasks as workflows,
> they can be consistently executed with a single command.
