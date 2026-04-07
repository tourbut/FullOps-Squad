# linter-rules.md — Mechanically Enforced Linter Rules

> Uniform rules **mechanically enforced** to ensure consistent code. No exceptions.
> Violations must be corrected using `correction-guides.md`.

## 1. File Naming Rules
- **kebab-case**: Use `kebab-case` (`user-profile.ts`). Svelte components use `PascalCase.svelte`.
- **Collections**: Plural form (`users.ts`, `repositories/`).
- **Entities**: Singular form (`user.model.ts`, `auth.service.py`).
- **Suffixes**: `.types.ts`, `.service.py/ts`, `.test.ts`, `.config.py/ts`.

## 2. Import Rules
- **Order**: Standard/External Libraries → Third-party/Internal → Local Modules. 1 blank line between. Sort alphabetically.
- **Python**: Absolute paths only (no `from .. import X`). No wildcard imports (`import *`).

## 3. Size Limits
- **Max Lines**: Mod(.py/.ts)=300, Svelte=200, Test/MD=500, Config=100.

## 4. Code Style & Naming
- **Python**: `ruff format/check`, 88 chars max, 4 spaces. Type hints & Google docstrings required. `snake_case` (vars/funcs) / `PascalCase` (classes) / `UPPER_SNAKE` (constants).
- **TypeScript**: `prettier/eslint`, 100 chars max, 2 spaces. No `any` type (use `unknown`). JSDoc required. `camelCase` (vars/funcs) / `PascalCase` (classes/types).

## 5. Git Commit Messages
- **Format**: `<type>(<scope>): <subject>` (e.g., `feat(auth): add google login`).
- Subject < 50 chars, present tense, lowercase start.

## 6. Forbidden Patterns (ANTI-xxx)
- **No**: `console.log()` / `print()` (use loggers).
- **No**: `eval()` / `exec()` / `# type: ignore` / `@ts-ignore`.
- **No**: Hardcoded secrets/URLs, `sleep()` in tests.

## 7. Svelte 5 Component Rules (SVELTE-xxx)
- **Script Block**: `<script lang="ts">` is mandatory (SVELTE-001).
- **Runes Only**: Svelte 4 legacy is forbidden. Use `$props()`, `$derived()`, `$effect()`, and callback props (SVELTE-002~004).
- **API**: Use `$lib/fastapi` `api_router` (No direct `fetch()`) (SVELTE-005).
- **Style**: Use Tailwind classes. Inline `style="..."` is forbidden (SVELTE-006).

## 8. Self-Evolving Protocol (CUSTOM-xxx)
- **Custom Rules**: Agents map recurring issues to regex rules in `custom_rules.json`.
- Must stay synced with `-rules.md` and `-guides.md`. Disable vs Delete. Run `python lint_checker.py --list-rules`.
