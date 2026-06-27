# phases/ — Per-Phase Detailed Execution Logs (Roadmap Phase Logs)

<!-- AI Harness Rule: Keep each roadmap Phase's detailed task checklists, implementation notes, and completion criteria in a per-phase file. The top-level index (vision, status, duration, links) is managed solely in the root PLANS.md. -->

> This directory holds the **detailed work logs** for each Phase (`phaseNN.md`).
> The root [`PLANS.md`](../../../PLANS.md) keeps only **guide-level content (vision · phase index · status · milestones)** so its per-session load cost stays constant.

## Conventions
- **Filename**: `phaseNN.md` (2-digit zero-padded, e.g. `phase02.md`).
- **Content**: the phase's goal, detailed task checklist (`- [x]/[ ]`), implementation notes, and completion criteria.
- **Owner**: the `/architect` workflow. As work progresses, **append detail to this file** and sync **only the status, one-line goal, and link** into `PLANS.md` (never write detail directly into `PLANS.md`).
- **New phase**: create a new `phaseNN.md` and add one row to the `PLANS.md` index table.

## Relation to sprint-level docs
- `phases/phaseNN.md` = **roadmap-phase-level** cumulative log (long-lived).
- `active/` · `completed/` = **sprint/task-level** execution contracts (short-lived). Cross-link from the phase log to the relevant sprint docs and QA reports.
