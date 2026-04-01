# skills/ — Agent Skill Implementations

> This directory contains the **actual implementation code** for skills specified in `SKILLS.md`.
> Skill specifications (what, when, how) are managed in `SKILLS.md`;
> implementations (actual code/scripts) are managed in this directory.

---

## Directory Structure

```
skills/
├── _README.md              # This file
├── core/                   # Core skill implementations
│   ├── file-read.py        # File read skill
│   ├── file-write.py       # File write skill
│   ├── context-sync.py     # Context sync skill
│   └── handover-dispatch.py # Handover dispatch skill
├── role/                   # Role-specific specialized skills
│   ├── architect/          # Architect/PM only
│   ├── backend/            # Backend only
│   ├── frontend/           # Frontend only
│   ├── qa/                 # QA only
│   └── devops/             # DevOps only
└── util/                   # Utility skills
```

---

## Skill Implementation Principles

1. **Single responsibility**: One skill file performs only one function
2. **Idempotency**: Running multiple times with the same input produces identical results
3. **Error handling**: Return clear error messages on failure
4. **Logging**: Output logs to enable execution tracing
5. **Testing**: Write unit tests for each skill

---

## New Skill Addition Procedure

1. Add skill specification to `SKILLS.md` (specification comes first)
2. Write implementation code in the appropriate location in this directory
3. Write test code
4. Record new skill usage in the relevant role's context file
5. Submit PR and review

---

> **Implementation without specification is not permitted.**
> Always register in `SKILLS.md` first, then implement in this directory.
