# Context — <Role Name>

> **Role**: [Architect / Backend / Frontend / DevOps / QA / Coordinator]
> **File Path**: `contexts/<role>.md` (e.g., `architect.md`, `backend_dev.md`)
> **Last Updated**: YYYY-MM-DD HH:mm:ss

---

## Purpose of This File

This file is not a simple notepad.
It is a **briefing document sent to your future self**.

- Before starting work: Read this file and sync the context learned by "your past self."
- After completing work: Record what you learned in this session to this file.

---

## Core Principles

Principles that must never be violated in this role.

- [YYYY-MM-DD HH:mm:ss] [Principle 1]
- [YYYY-MM-DD HH:mm:ss] [Principle 2]

> When a principle changes, apply ~~strikethrough~~ to the old entry and add the new one below.

---

## Learned Patterns

Effective methods and reusable patterns discovered during work.

- [YYYY-MM-DD HH:mm:ss] [Pattern description]
- [YYYY-MM-DD HH:mm:ss] [Pattern description]

---

## Anti-Patterns

Approaches that were tried but failed — things that must never be repeated.

- [YYYY-MM-DD HH:mm:ss] [Description + reason for failure]
- [YYYY-MM-DD HH:mm:ss] [Description + reason for failure]

---

## Decision History

Timeline of important technical/design decisions.

- [YYYY-MM-DD HH:mm:ss] [Decision + rationale]
- [YYYY-MM-DD HH:mm:ss] [Decision + rationale]

> When a past decision changes, apply ~~strikethrough~~ to the old entry and add the new decision below.

---

## Current Knowledge

System/project state that this role must currently be aware of.

- [YYYY-MM-DD HH:mm:ss] [Current state description]

---

## Writing Rules

1. **Format**: `- [YYYY-MM-DD HH:mm:ss] content` (압축된 요약 항목은 `[YYYY-MM-DD]` 날짜만 허용)
2. **분량**: 한 항목은 **3줄 이내**로 요약한다. 구현 상세·체크리스트는 `docs/exec-plans/phases/phaseNN.md` 등 원 문서에 쓰고 여기에는 링크만 남긴다.
3. **Chronological order**: Newest entries at the bottom of each section
4. **Be specific**: "Didn't work well" ❌ → "Alembic autogenerate fails to detect Enum type changes" ✅
5. **Current Knowledge는 스냅샷**: 이 섹션만은 누적이 아니라 "현재 유효한 상태"로 유지한다 — 구식 항목은 ~~취소선~~ 처리하고 다음 압축 때 제거한다.
6. **삭제 대신 아카이브**: 활성 파일에서 항목을 지울 때는 반드시 `contexts/archive/<role>_YYYY-MM.md`에 원문이 보존되어 있어야 한다 (압축 절차는 `skills/role-context/SKILL.md` 참조).
7. **파일 예산**: 본문이 **150줄 또는 10KB**를 초과하면 `role-context` 스킬의 압축(Compact) 절차를 수행한다.
8. **Update timing**: 작업 완료 시 반드시 갱신 (Common Postamble)
