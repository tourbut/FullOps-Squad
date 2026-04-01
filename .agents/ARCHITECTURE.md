# ARCHITECTURE.md — Domain/Package Layer Hierarchy & Dependency Rules

<!-- AI Harness Rule: Define the hierarchical structure of domains and packages (e.g., Types -> Config -> Repo -> Service -> Runtime -> UI). Clearly specify the allowed dependency directions between each layer and the strict boundaries that must never be crossed. -->

> Defines the layer hierarchy of domains and packages and the allowed dependency directions between layers.
> The boundaries specified in this document are **absolute** and must never be violated under any circumstances.

---

## Layer Hierarchy

Layers are listed from **top to bottom** below.
Dependencies must flow **strictly downward** only.

```
┌─────────────────────────────────────────────┐
│  Layer 6: UI (Presentation)                 │
│  — User interface, components, pages        │
├─────────────────────────────────────────────┤
│  Layer 5: Runtime (Application)             │
│  — App initialization, middleware, routers  │
├─────────────────────────────────────────────┤
│  Layer 4: Service (Business Logic)          │
│  — Use cases, business rules, orchestration │
├─────────────────────────────────────────────┤
│  Layer 3: Repository (Data Access)          │
│  — DB queries, external API calls, caching  │
├─────────────────────────────────────────────┤
│  Layer 2: Config (Configuration)            │
│  — Environment variables, settings, consts  │
├─────────────────────────────────────────────┤
│  Layer 1: Types (Foundation)                │
│  — Type definitions, interfaces, entities   │
└─────────────────────────────────────────────┘
```

---

## Dependency Rules

### Allowed Dependency Directions (✅)

| Source Layer | May Reference |
|-------------|---------------|
| UI | → Runtime, Service, Types |
| Runtime | → Service, Repository, Config, Types |
| Service | → Repository, Config, Types |
| Repository | → Config, Types |
| Config | → Types |
| Types | → (none — lowest layer) |

### Strictly Forbidden (❌)

- **Lower → Upper references forbidden**: e.g., `Types` importing `Service`
- **Circular dependencies within the same layer forbidden**: e.g., `ServiceA` ↔ `ServiceB`
- **UI → Repository direct access forbidden**: Must go through the Service layer
- **Runtime logic leaking into Service forbidden**: Middleware/init code must not contain business logic

---

## Directory Mapping

```
src/
├── types/          # Layer 1: Types, interfaces, domain entities
├── config/         # Layer 2: Environment variables, settings, constants
├── repositories/   # Layer 3: DB access, external API clients
├── services/       # Layer 4: Business logic, use cases
├── runtime/        # Layer 5: App initialization, middleware, routers
└── ui/             # Layer 6: Frontend components, pages
```

---

## Inter-Package Boundary Rules

### Domain Separation
- Each domain (e.g., `auth`, `portfolio`, `analytics`) is composed as an **independent module**
- Inter-domain communication must only occur through **Service layer interfaces**
- Domain A's Repository being directly called by Domain B's Service is forbidden

### Shared Code
- Code shared across multiple domains is placed in the `shared/` directory
- `shared/` may only contain Layer 1 (Types) or Layer 2 (Config) level code
- Placing business logic (Service) in `shared/` is forbidden

### External Libraries
- External library dependencies are used directly only in **Config** or **Repository** layers
- The Service layer uses them indirectly through **wrapped interfaces**
- UI layer's external component libraries are exceptionally allowed for direct use

---

## Violation Detection

When a dependency violation is found:
1. Check the import rules in `rules/linter-rules.md`
2. Apply the auto-correction instructions from `rules/correction-guides.md`
3. If structural refactoring is needed, register it in `docs/exec-plans/tech-debt-tracker.md`

---

> **The rules in this document are absolute.**
> Exceptions for convenience lead to technical debt, which must be registered in the tracker with a resolution plan.
