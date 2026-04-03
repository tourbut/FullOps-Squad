# Context — Architect

> **Role**: Architect
> **File Path**: `contexts/architect.md`
> **Last Updated**: 2026-04-03 17:00:00

---

## Purpose of This File

This file is not a simple notepad.
It is a **briefing document sent to your future self**.

- Before starting work: Read this file and sync the context learned by "your past self."
- After completing work: Record what you learned in this session to this file.

---

## Core Principles

Principles that must never be violated in this role.

- [2026-04-03 17:00:00] ARCHITECTURE.md의 레이어 의존 방향(상→하)은 절대 규칙이다. 예외를 허용하면 기술 부채가 누적된다.
- [2026-04-03 17:00:00] 새로운 기술 도입 시 반드시 DESIGN.md의 의사결정 프레임워크를 통과해야 한다.

> When a principle changes, apply ~~strikethrough~~ to the old entry and add the new one below.

---

## Learned Patterns

Effective methods and reusable patterns discovered during work.

- [YYYY-MM-DD HH:mm:ss] [패턴 설명]

---

## Anti-Patterns

Approaches that were tried but failed — things that must never be repeated.

- [YYYY-MM-DD HH:mm:ss] [설명 + 실패 사유]

---

## Decision History

Timeline of important technical/design decisions.

- [YYYY-MM-DD HH:mm:ss] [결정 + 근거]

> When a past decision changes, apply ~~strikethrough~~ to the old entry and add the new decision below.

---

## Current Knowledge

System/project state that this role must currently be aware of.

- [2026-04-03 17:00:00] 현재 Phase 1 진행 중: .agents/ 하네스 구조 구축 단계

---

## Writing Rules

1. **Format**: `- [YYYY-MM-DD HH:mm:ss] content`
2. **Append only**: Never delete existing entries (invalidate via strikethrough)
3. **Chronological order**: Newest entries at the bottom of each section
4. **Be specific**: "잘 안됨" ❌ → "Alembic autogenerate는 Enum 타입 변경을 감지하지 못함" ✅
5. **Update timing**: Must update this file upon work completion
