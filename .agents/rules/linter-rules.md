# linter-rules.md — Mechanically Enforced Linter Rules

<!-- AI Harness Rule: Specify uniform linter rules strictly enforced by the machine to ensure the agent consistently writes standard code, such as naming conventions (plural nouns), alphabetical import order, and file size limits. -->

> Uniform rules **mechanically enforced** to ensure agents always write consistent code.
> These rules have no exceptions. Violations trigger correction instructions from `correction-guides.md`.
> To guarantee idempotency, applying the same rule repeatedly must yield identical results.

---

## 1. File Naming Rules

### 1.1 General Rules
- **Case**: Use `kebab-case` (lowercase + hyphens)
  - ✅ `user-profile.ts`, `auth-service.py`
  - ❌ `UserProfile.ts`, `auth_service.py`, `authService.py`
- **Plural nouns**: Files dealing with collections/lists must use **plural form**
  - ✅ `users.ts`, `repositories.py`, `components/`
  - ❌ `user.ts` (when a collection), `repository.py` (when defining multiple repos)
- **Singular nouns**: Files defining a single entity/class use **singular form**
  - ✅ `user.model.ts`, `auth.service.py`

### 1.2 Suffix Rules
| File Type | Suffix Pattern | Example |
|-----------|---------------|---------|
| Type Definitions | `.types.ts` | `user.types.ts` |
| Service | `.service.py` / `.service.ts` | `auth.service.py` |
| Repository | `.repository.py` / `.repository.ts` | `user.repository.py` |
| Component (Svelte) | `PascalCase.svelte` | `UserCard.svelte` |
| Test | `.test.ts` / `test_*.py` | `auth.test.ts`, `test_auth.py` |
| Config | `.config.ts` / `.config.py` | `database.config.py` |

### 1.3 Directory Naming
- Always `kebab-case` + **plural**
  - ✅ `components/`, `services/`, `repositories/`
  - ❌ `Component/`, `service/`, `Repository/`
- Exception: SvelteKit `routes/` follows framework conventions

---

## 2. Import Rules (Import Ordering)

### 2.1 Python (Backend)
```python
# 1. Standard Library
import os
import sys
from datetime import datetime

# 2. Third-party Libraries
from fastapi import FastAPI
from sqlalchemy import Column

# 3. Local Modules — absolute paths only
from src.config.settings import Settings
from src.services.auth_service import AuthService
```

**Rules**:
- Each group separated by **1 blank line**
- Sorted **alphabetically** within each group
- `from` imports and simple `import` statements are separated, with `import` first within the same group
- **Relative path imports forbidden**: `from ..models import User` ❌ → `from src.types.user import User` ✅

### 2.2 TypeScript / JavaScript (Frontend)
```typescript
// 1. External Libraries
import { onMount } from 'svelte';
import { writable } from 'svelte/store';

// 2. Internal Modules — absolute paths ($lib, etc.)
import { apiClient } from '$lib/utils/api-client';
import type { User } from '$lib/types/user.types';

// 3. Relative Paths (within current directory)
import UserCard from './UserCard.svelte';
```

**Rules**:
- Each group separated by **1 blank line**
- Sorted **alphabetically** within each group
- `type` imports placed after value imports
- Unused imports forbidden (dead imports)

---

## 3. File Size Limits

| File Type | Max Lines | Action on Exceedance |
|-----------|----------|---------------------|
| Python Module (.py) | 300 lines | Split by domain or function |
| TypeScript Module (.ts) | 300 lines | Split by domain or function |
| Svelte Component (.svelte) | 200 lines | Extract into child components |
| Test Files | 500 lines | Split by test group |
| Config Files | 100 lines | Split by domain |
| Markdown Documents | 500 lines | Split by section |

---

## 4. Code Style Rules

### 4.1 Python
- **Formatter**: `ruff format` (Black-compatible)
- **Linter**: `ruff check`
- **Line length**: Max **88 characters**
- **Indentation**: **4 spaces**
- **Strings**: Prefer double quotes (`"`)
- **Type hints**: Required on all function parameters and return values
- **Docstrings**: Google-style docstrings required on all public functions/classes

### 4.2 TypeScript
- **Formatter**: `prettier`
- **Linter**: `eslint` (TypeScript strict)
- **Line length**: Max **100 characters**
- **Indentation**: **2 spaces**
- **Semicolons**: Always use
- **Strings**: Prefer single quotes (`'`)
- **Types**: `any` usage **absolutely forbidden**; use `unknown` with type guards
- **JSDoc**: Required on all exported functions/components

### 4.3 Common
- **Trailing commas**: Always use (comma after the last item)
- **Blank lines**: **2 lines** between functions/classes, **1 line** between methods
- **Comment language**: Korean (code variable/function names in English)
- **TODO comments**: `TODO(role): description` format — e.g., `TODO(backend): apply caching strategy`

---

## 5. Naming Conventions

### 5.1 Python
| Target | Convention | Example |
|--------|-----------|---------|
| Variables, Functions | `snake_case` | `user_name`, `get_user()` |
| Classes | `PascalCase` | `UserService` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT` |
| Private Members | `_` prefix | `_internal_cache` |

### 5.2 TypeScript
| Target | Convention | Example |
|--------|-----------|---------|
| Variables, Functions | `camelCase` | `userName`, `getUser()` |
| Classes, Interfaces | `PascalCase` | `UserService`, `UserProps` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT` |
| Types | `PascalCase` | `UserResponse` |
| Event Handlers | `handle` prefix | `handleClick`, `handleSubmit` |

---

## 6. Git Commit Message Rules

```
<type>(<scope>): <subject>

<body>
```

### Types
| Type | Meaning |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Refactoring (no behavior change) |
| `docs` | Documentation change |
| `test` | Add/modify tests |
| `chore` | Build, config, and other changes |
| `style` | Code style changes (formatting, etc.) |

### Rules
- **subject**: Under 50 characters, present tense, lowercase first letter
- **body**: 72-character line wrap, explain "why" the change was made
- **scope**: Area of change (e.g., `auth`, `dashboard`, `db`)

Example:
```
feat(auth): add social login functionality

Implemented Kakao/Google OAuth2 authentication flow.
Uses the same session management approach as existing email login.
```

---

## 7. Forbidden Patterns (Anti-patterns)

| Pattern | Violation Reason | Alternative |
|---------|-----------------|-------------|
| `console.log` (production) | Unmanageable logging | Use structured logger |
| `print()` (production) | Unmanageable logging | Use `logging` module |
| `# type: ignore` | Bypasses type safety | Define correct types |
| `@ts-ignore` / `@ts-expect-error` | Bypasses type safety | Define correct types |
| `eval()` / `exec()` | Security vulnerability | Use safe alternatives |
| Hardcoded URLs/ports | Environment dependency | Use environment variables |
| `sleep()` in tests | Non-deterministic tests | Use explicit wait conditions |
| `*` import | Namespace pollution | Use explicit imports |

---

> **These rules are enforced by automation tools (ruff, eslint, prettier).**
> When violations are found, refer to `correction-guides.md` for auto-correction.
> When adding new rules, update both this document and `correction-guides.md` simultaneously.
