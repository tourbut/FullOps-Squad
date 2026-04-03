# Context — Backend Developer

> **Role**: Backend Developer
> **File Path**: `contexts/backend_dev.md`
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

- [2026-04-03 17:00:00] 모든 CRUD 함수는 async def + 키워드 전용 인자(*) 필수. session: AsyncSession을 반드시 주입받을 것.
- [2026-04-03 17:00:00] DB 쓰기/수정/삭제 로직은 반드시 try-except 블록 내에서 실행하고, 에러 시 await session.rollback() 수행.

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

- [2026-04-03 17:00:00] 실행 환경: uv run 명령어로 backend 디렉토리에서 실행. Import는 app.* 절대 경로 사용.

---

## Writing Rules

1. **Format**: `- [YYYY-MM-DD HH:mm:ss] content`
2. **Append only**: Never delete existing entries (invalidate via strikethrough)
3. **Chronological order**: Newest entries at the bottom of each section
4. **Be specific**: "잘 안됨" ❌ → "Alembic autogenerate는 Enum 타입 변경을 감지하지 못함" ✅
5. **Update timing**: Must update this file upon work completion
