# correction-guides.md — Linter Violation Auto-Correction Guides

> When violations from `linter-rules.md` occur, use these instructions to fix them.

## File/Directory Violations (FILE-xxx)
- **FILE-001**: Rename file/dir to `kebab-case` and update imports.
- **FILE-002**: Rename files handling collections to plural.
- **FILE-003**: Fix missing/wrong suffix (e.g., `.service.ts`, `.types.ts`).

## Import Violations (IMP-xxx)
- **IMP-001**: Reorder: Standard → Third-Party → Local.
- **IMP-002**: Use absolute paths in Python (`from app.types.user import X`).
- **IMP-003**: Remove unused (dead) imports.
- **IMP-004**: Replace wildcard `*` with explicit module imports.

## Size Violations (SIZE-001)
- **SIZE-001**: Extract groups by domain/function into new files to reduce file length.

## Style Violations (STYLE-xxx)
- **STYLE-001**: Replace TS `any` with specific types or `unknown` + type guard.
- **STYLE-002**: Add explicit Python type hints (param types and `-> ReturnType`). (Enforced by `Ruff ANN`)
- **STYLE-003**: Add Google-style docstrings or JSDoc for public functions/classes. (Enforced by `Ruff D`)

## Security Violations (SEC-xxx)
- **SEC-001**: Move hardcoded secrets to `.env` or `os.environ` / Config layer.
- **SEC-002**: Use Pydantic/Zod/Valibot to validate all user inputs.

## Architecture Violations (ARCH-xxx)
- **ARCH-001**: Lower layers cannot depend on upper layers. Use Dependency Inversion.
- **ARCH-002**: UI must fetch through the Service layer, not directly from Repositories.

## Git Violations (GIT-001)
- **GIT-001**: Use `git commit --amend` to match `<type>(<scope>): <subject>` format.

## Svelte Violations (SVELTE-xxx)
- **SVELTE-001**: Change `<script>` to `<script lang="ts">`.
- **SVELTE-002**: Replace `export let` with Svelte 5 `let { prop } = $props()`.
- **SVELTE-003**: Replace `$:` with `$derived()` or `$effect()`.
- **SVELTE-004**: Replace `createEventDispatcher` with callback `onSubmit={func}` props.
- **SVELTE-005**: Replace `fetch()` with `api_router` from `$lib/fastapi`.
- **SVELTE-006**: Replace `<div style="...">` with equivalent Tailwind CSS utility classes.
- **SVELTE-007**: Rename `.svelte` component to `PascalCase.svelte`.

- **Other**: Check `suggestion` in `custom_rules.json` or `lint_checker.py --list-rules`.

---

## Appendix: Frontend Setup Template (ESLint & Prettier)

프론트엔드(`frontend/`) 디렉터리 구축 시, 다음 설정을 적용하여 `linter-rules.md`를 기계적으로 강제할 수 있습니다.

### 1. `eslint.config.js` (Flat Config)
```javascript
import svelte from "eslint-plugin-svelte";
import ts from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";
import svelteParser from "svelte-eslint-parser";

export default [
  {
    files: ["**/*.ts", "**/*.js", "**/*.svelte"],
    languageOptions: {
      parser: tsParser,
      extraFileExtensions: [".svelte"],
    },
    plugins: {
      "@typescript-eslint": ts,
      svelte: svelte,
    },
    rules: {
      "@typescript-eslint/no-explicit-any": "error", // STYLE-001
      "svelte/no-at-html-tags": "warn",
      "svelte/no-inner-declarations": "error",
      // Svelte 5 Runes 강제 및 레거시 문법 금지 설정 필요
    },
  },
  {
    files: ["**/*.svelte"],
    languageOptions: {
      parser: svelteParser,
      parserOptions: {
        parser: tsParser,
      },
    },
  },
];
```

### 2. `.prettierrc`
```json
{
  "useTabs": false,
  "singleQuote": false,
  "trailingComma": "all",
  "printWidth": 100,
  "plugins": ["prettier-plugin-svelte"],
  "overrides": [{ "files": "*.svelte", "options": { "parser": "svelte" } }]
}
```
