# Context — DevOps Engineer

> **Role**: DevOps
> **File Path**: `contexts/devops.md`
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

- [2026-04-03 17:00:00] 모든 배포는 RELIABILITY.md의 무중단 배포 전략을 따른다. 롤백 계획 없는 배포는 금지.
- [2026-04-03 17:00:00] 환경 변수와 시크릿은 절대 코드에 하드코딩하지 않으며, .env 또는 시크릿 매니저로 관리한다.

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

- [2026-04-03 17:00:00] 인프라: Docker Compose 기반. Backend/Frontend/PostgreSQL/Redis를 컨테이너로 구성.

---

## Writing Rules

1. **Format**: `- [YYYY-MM-DD HH:mm:ss] content`
2. **Append only**: Never delete existing entries (invalidate via strikethrough)
3. **Chronological order**: Newest entries at the bottom of each section
4. **Be specific**: "잘 안됨" ❌ → "nginx 리버스 프록시에서 WebSocket 업그레이드 헤더가 누락되면 SSE 연결 실패" ✅
5. **Update timing**: Must update this file upon work completion
