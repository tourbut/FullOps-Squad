# FRONTEND.md — Frontend Quality Standards & Criteria

<!-- AI Harness Rule: Establish a grading rubric to evaluate the quality required in the corresponding domain (frontend, security, stability, etc.). Include a fundamental capability checklist that the code must pass. -->

> Defines quality grades, coding conventions, and component design principles required for the frontend domain.
> Frontend agents must familiarize themselves with this document before starting work.

---

## Tech Stack Conventions

| Item | Choice | Notes |
|------|--------|-------|
| Framework | Svelte / SvelteKit | Reactive-first |
| Language | TypeScript (strict mode) | `any` type usage forbidden |
| Styling | Tailwind CSS | Minimize inline style attributes |
| UI Library | Flowbite (Tailwind-based) | Prefer custom components; use Flowbite as needed |
| Serving | nginx (reverse proxy) | Static file optimization |

---

## Component Design Principles

### File Structure
```
src/
├── lib/
│   ├── components/    # Reusable UI components
│   │   ├── common/    # Buttons, inputs, modals, etc.
│   │   └── domain/    # Domain-specific components
│   ├── stores/        # Svelte stores (state management)
│   ├── utils/         # Utility functions
│   └── types/         # Frontend-specific type definitions
├── routes/            # SvelteKit routes (pages)
└── app.html           # HTML template
```

### Component Writing Rules

1. **Single Responsibility**: Each component performs only one role
2. **Explicit Props Types**: TypeScript type definitions required for all component props
3. **Event Delegation**: Custom events are delegated upward via `createEventDispatcher`
4. **No Direct Store Access**: Only page (route) level may access stores; components receive data via props
5. **File Size Limit**: A single `.svelte` file must stay under **200 lines**

---

## Quality Grade Criteria

### Design Quality (40%)

| Grade | Criteria |
|-------|----------|
| **A** | Perfect visual consistency; spacing/alignment/colors 100% match the design system |
| **B** | Overall consistent with 1–2 minor spacing/alignment discrepancies |
| **C** | Basic design guide adherence; no discrepancies on key screens |
| **D** | Multiple areas of non-compliance with design guide; clear visual inconsistencies |
| **F** | Design system ignored; arbitrary colors/fonts/spacing used |

### Originality & UX (30%)

| Grade | Criteria |
|-------|----------|
| **A** | Intuitive user flows; loading/error/empty states all handled; micro-interactions implemented |
| **B** | Smooth primary user flows; error state handling complete |
| **C** | Basic flows work; error messages displayed at minimum level |
| **D** | Confusing flows exist; error handling missing |
| **F** | Unusable UX level; primary flows broken |

### Functionality (30%)

| Grade | Criteria |
|-------|----------|
| **A** | All edge cases handled; accessibility (a11y) compliant; keyboard navigation supported |
| **B** | Core features fully functional; basic accessibility compliance |
| **C** | Core features work; 1–2 known edge cases unhandled |
| **D** | Some core features non-functional; accessibility not considered |
| **F** | Core features non-functional; critical bugs present |

---

## Accessibility (a11y) Checklist

- [ ] All images have `alt` attributes
- [ ] Form elements linked to `label`s
- [ ] Color contrast ratio 4.5:1 or above (WCAG AA)
- [ ] All interactions possible via keyboard only
- [ ] Focus indicators are visible
- [ ] Screen reader test passed
- [ ] `aria-*` attributes used appropriately

---

## Performance Criteria

| Item | Threshold | Measurement Tool |
|------|-----------|------------------|
| Lighthouse Performance | ≥ 80 | Chrome DevTools |
| First Contentful Paint | ≤ 1.5s | Lighthouse |
| Cumulative Layout Shift | ≤ 0.1 | Lighthouse |
| Initial Bundle Size (gzip) | ≤ 300KB | webpack-bundle-analyzer |
| Image Optimization | Use WebP/AVIF | Build pipeline |

---

## Testing Requirements

| Test Type | Target | Tool | Minimum Coverage |
|-----------|--------|------|------------------|
| Unit Tests | Utility functions, store logic | Vitest | 80% |
| Component Tests | Key UI components | Testing Library | 100% of core components |
| E2E Tests | User flow scenarios | Playwright | 100% of primary flows |
| Visual Regression Tests | Key page snapshots | Playwright | 100% of key pages |

---

> **Scoring Timing**: During PR review + at sprint end
> **Scorer**: QA agent (UI exploration-based) + code reviewer
> **Results Recorded In**: `docs/evaluations/qa-reports/`
