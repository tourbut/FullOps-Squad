# Context — QA Tester

> **Role**: QA
> **File Path**: `contexts/qa_tester.md`
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

- [2026-04-03 17:00:00] 테스트 결과는 항상 QUALITY_SCORE.md 기준으로 판정한다. 주관적 판단으로 PASS/FAIL 결정 금지.
- [2026-04-03 17:00:00] 모든 버그 리포트에는 재현 방법(Steps to Reproduce)이 반드시 포함되어야 한다.

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

- [2026-04-03 17:00:00] QA 리포트는 .agents/docs/evaluations/qa-reports/에 저장. 파일명 형식: YYYY-MM-DD_qa-report.md

---

## Writing Rules

1. **Format**: `- [YYYY-MM-DD HH:mm:ss] content`
2. **Append only**: Never delete existing entries (invalidate via strikethrough)
3. **Chronological order**: Newest entries at the bottom of each section
4. **Be specific**: "잘 안됨" ❌ → "Playwright에서 SSE 연결 테스트 시 page.waitForResponse 대신 page.waitForEvent('response')를 사용해야 함" ✅
5. **Update timing**: Must update this file upon work completion
