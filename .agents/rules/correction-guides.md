# correction-guides.md — Linter Violation Auto-Correction Guides

<!-- AI Harness Rule: Map out specific correction guides to be provided to the AI along with error messages when the aforementioned linter rules are violated, instructing it on how to self-correct the code. -->

> When violations from `linter-rules.md` occur,
> these correction guides are delivered to the AI along with the error message
> so it can **fix the code on its own**.
> Each violation type maps an error pattern to a correction method.

---

## How to Use

1. A linter/build error occurs
2. Identify the **violation code** from the error message
3. Find the correction instructions for that violation code in this document
4. Deliver the correction instructions to the AI agent along with the error message
5. The agent auto-corrects the code

---

## File Naming Violations (FILE-xxx)

### FILE-001: Filename is not kebab-case

**Error Pattern**:
```
[FILE-001] Filename violates kebab-case convention: UserProfile.ts
```

**Correction Instructions**:
```
Rename the file to kebab-case.
- Current: UserProfile.ts
- Fix: user-profile.ts

Also update all files that import this file with the new path.
Search the entire project with grep for the old filename to ensure no references are missed.
```

### FILE-002: Collection file named with singular form

**Error Pattern**:
```
[FILE-002] Files handling collections/lists must use plural form: repository.py
```

**Correction Instructions**:
```
If the file defines multiple items or handles collections, rename it to plural form.
- Current: repository.py
- Fix: repositories.py

Update all related import paths.
Note: Files defining a single entity/class (e.g., user.model.ts) should correctly remain singular.
```

### FILE-003: Suffix convention violation

**Error Pattern**:
```
[FILE-003] Service file suffix is incorrect: auth-handler.py
```

**Correction Instructions**:
```
Use the appropriate suffix for the file type:
- Service → .service.py / .service.ts
- Repository → .repository.py / .repository.ts
- Type Definition → .types.ts
- Config → .config.py / .config.ts

Current: auth-handler.py (contains service logic)
Fix: auth.service.py

Refer to the 'Suffix Rules' table in linter-rules.md.
```

---

## Import Violations (IMP-xxx)

### IMP-001: Import order violation

**Error Pattern**:
```
[IMP-001] Import order is incorrect. Group order: Standard → Third-party → Local
```

**Correction Instructions**:
```
Reorder import statements in the following order:

Python:
1. Standard library (os, sys, datetime, etc.)
2. Third-party libraries (fastapi, sqlalchemy, etc.)
3. Local modules (src.*, etc.)

TypeScript:
1. External libraries (svelte, sveltekit, etc.)
2. Internal absolute paths ($lib/*, etc.)
3. Relative paths (./, etc.)

Separate each group with 1 blank line and sort alphabetically within each group.
```

### IMP-002: Relative path import used (Python)

**Error Pattern**:
```
[IMP-002] Relative path imports are not allowed in Python: from ..models import User
```

**Correction Instructions**:
```
Convert the relative path import to an absolute path.
- Current: from ..models import User
- Fix: from src.types.user import User

Use absolute paths starting from the project root (src/).
In the uv run environment, src is automatically included in PYTHONPATH.
```

### IMP-003: Unused import (Dead Import)

**Error Pattern**:
```
[IMP-003] Unused import found: import os (line 3)
```

**Correction Instructions**:
```
Remove the unused import statement.
- Remove: import os (line 3)

Verification: Search the file to confirm the module/variable is not referenced anywhere.
If you anticipate using it later, do not import it now — add it when needed.
```

### IMP-004: Wildcard import used

**Error Pattern**:
```
[IMP-004] Wildcard (*) imports are forbidden: from utils import *
```

**Correction Instructions**:
```
Convert the wildcard import to explicit imports.
- Current: from utils import *
- Fix: from utils import specific_function, SpecificClass

Import only the symbols you actually use.
This prevents namespace pollution and enables dependency tracking.
```

---

## File Size Violations (SIZE-xxx)

### SIZE-001: File size exceeded

**Error Pattern**:
```
[SIZE-001] File exceeds maximum line count: auth.service.py (350 lines, max 300)
```

**Correction Instructions**:
```
Split the file into logical units:

1. Group the file contents by function/domain.
2. Extract each group into a separate file.
3. In the original file, re-export from the split files if necessary.

Example:
- auth.service.py (350 lines)
  → auth-login.service.py (login-related logic)
  → auth-token.service.py (token management logic)
  → auth.service.py (retain only combined exports or common logic)

Split thresholds:
- Python module: 300 lines
- TypeScript module: 300 lines
- Svelte component: 200 lines
```

---

## Code Style Violations (STYLE-xxx)

### STYLE-001: `any` type used

**Error Pattern**:
```
[STYLE-001] Usage of 'any' type is forbidden in TypeScript: const data: any = ...
```

**Correction Instructions**:
```
Replace 'any' with a specific type or 'unknown'.

Method 1: Specific type definition
- Current: const data: any = await fetchUser();
- Fix: const data: UserResponse = await fetchUser();

Method 2: unknown + type guard
- Current: function process(data: any) { ... }
- Fix: function process(data: unknown) {
    if (isUserData(data)) { ... }
  }

If a type definition is needed, create a .types.ts file under $lib/types/.
```

### STYLE-002: Missing type hints (Python)

**Error Pattern**:
```
[STYLE-002] Function is missing type hints: def get_user(user_id):
```

**Correction Instructions**:
```
Add type hints to function parameters and return values.
- Current: def get_user(user_id):
- Fix: def get_user(user_id: int) -> User | None:

For complex types, define custom types in the src/types/ directory.
```

### STYLE-003: Missing docstring/JSDoc

**Error Pattern**:
```
[STYLE-003] Public function is missing a docstring: def create_user(...)
```

**Correction Instructions**:
```
Add a Google-style docstring:

def create_user(name: str, email: str) -> User:
    """Creates and returns a user.

    Args:
        name: User name
        email: User email address

    Returns:
        The created User object

    Raises:
        ValueError: If the email format is invalid
    """

For TypeScript, use JSDoc:

/**
 * Creates and returns a user.
 * @param name - User name
 * @param email - User email address
 * @returns The created User object
 */
```

---

## Security Violations (SEC-xxx)

### SEC-001: Hardcoded secret

**Error Pattern**:
```
[SEC-001] Hardcoded credential found: password = "admin123"
```

**Correction Instructions**:
```
Replace the hardcoded secret with an environment variable.

Python:
- Current: password = "admin123"
- Fix: password = os.environ["DB_PASSWORD"]
  or: password = settings.db_password  # Using Config layer

TypeScript:
- Current: const apiKey = "sk-abc123";
- Fix: const apiKey = import.meta.env.VITE_API_KEY;

Add the environment variable to .env.example but leave the actual value empty.
```

### SEC-002: Unvalidated user input

**Error Pattern**:
```
[SEC-002] User input is being used without validation
```

**Correction Instructions**:
```
Validate all user inputs before use.

Python (FastAPI):
- Use Pydantic models to validate request body
- Specify type + constraints for Query/Path parameters
  e.g.: user_id: int = Path(..., gt=0)

TypeScript:
- Use zod or valibot for runtime validation
- Types alone are insufficient — runtime validation is essential

SQL injection prevention: Use query parameter binding (never assemble raw SQL directly)
```

---

## Architecture Violations (ARCH-xxx)

### ARCH-001: Dependency direction violation

**Error Pattern**:
```
[ARCH-001] Lower layer references upper layer: types/ → services/
```

**Correction Instructions**:
```
Check the dependency rules in ARCHITECTURE.md.
Allowed direction: UI → Runtime → Service → Repository → Config → Types

Resolution approach:
1. Define the required interface in the lower layer (Types)
2. Implement that interface in the upper layer (Service)
3. The lower layer references only the interface (Dependency Inversion Principle)

If this pattern doesn't resolve the issue,
the design itself may need re-examination.
Hand over to the Architect role.
```

### ARCH-002: Layer skip (UI → Repository direct access)

**Error Pattern**:
```
[ARCH-002] UI layer directly references Repository layer
```

**Correction Instructions**:
```
When data is needed from UI, always go through the Service layer.

Current (violation):
UI → Repository.getUsers()

Fix:
UI → Service.getUsers() → Repository.getUsers()

If the Service layer doesn't have the relevant method, create it.
Service is the sole intermediary between business logic and data access.
```

---

## Git Commit Message Violations (GIT-xxx)

### GIT-001: Commit message format violation

**Error Pattern**:
```
[GIT-001] Commit message does not match the required format
```

**Correction Instructions**:
```
Modify the commit message to the following format:

<type>(<scope>): <subject>

Allowed types: feat, fix, refactor, docs, test, chore, style
subject: Under 50 characters, present tense, lowercase first letter

Examples:
- feat(auth): add social login functionality
- fix(dashboard): resolve chart rendering error
- refactor(user): extract service layer

Use git commit --amend to modify the last commit message.
```

---

> **When a new violation type is discovered, add it to this document immediately.**
> Violation code format: `[CATEGORY]-[3-digit sequential number]` (e.g., FILE-001, IMP-002)
> This document and `linter-rules.md` must always remain in sync.
