# Context — Frontend Developer

> **Role**: Frontend Developer
> **File Path**: `contexts/frontend_dev.md`
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

- [2026-04-03 17:00:00] Svelte 5 Runes 문법만 사용. 레거시 패턴(export let, $:, createEventDispatcher) 절대 금지.
- [2026-04-03 17:00:00] API 통신은 반드시 $lib/fastapi.ts의 api_router 래퍼를 통해 수행. 직접 fetch() 호출 금지.

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

- [2026-04-03 17:00:00] 전역 상태 관리: auth.svelte.ts처럼 Svelte 5 Runes 기반 클래스형 .svelte.ts 파일 사용.

---

## Writing Rules

1. **Format**: `- [YYYY-MM-DD HH:mm:ss] content`
2. **Append only**: Never delete existing entries (invalidate via strikethrough)
3. **Chronological order**: Newest entries at the bottom of each section
4. **Be specific**: "잘 안됨" ❌ → "Flowbite-Svelte v2에서 Sidebar의 activeUrl 속성은 deprecated됨" ✅
5. **Update timing**: Must update this file upon work completion
