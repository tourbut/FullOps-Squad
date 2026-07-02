# workflows/ — Slash Command Executable Workflows

> 슬래시 커맨드(`/command`)로 트리거되는 자동화 워크플로우 정의.
> 등록된 커맨드 전체 목록은 `../SKILLS.md` §3에서 단일 관리한다.

---

## 공통 전처리 (Common Preamble)

모든 역할 워크플로우(`/architect`, `/design`, `/backend`, `/frontend`, `/devops`, `/qa`)는 Steps 초두에서 다음 **3단계를 공통 수행**한다. 각 워크플로우 파일에서는 반복 기술하지 않고 "Common Preamble 수행"으로 표기한다. (`/master`·`/coordinator`·`/release`·`/improve`는 역할 컨텍스트가 없으므로 자체 Steps만 따른다.)

1. **핸드오버 분석**: `.agents/handovers/to_<role>.md`를 읽고 작업 범위·기대 산출물을 파악한다. **파일이 없거나 비어 있으면 작업을 임의로 만들지 말고** 사용자 지시 또는 `/coordinator` 재분배를 요청하고 중단한다 (사용자가 prompt로 직접 지시한 경우는 그 지시가 handover를 대신한다).
2. **컨텍스트 로드**: `.agents/contexts/<role>.md`를 읽고 Core Principles·Anti-Patterns·Current Knowledge를 현재 작업의 제약조건으로 동기화한다.
3. **브랜치 생성**: `.agents/skills/git-rules/SKILL.md` 규칙에 따라 `develop/*`, `fix/*` 등 적합한 브랜치를 체크아웃한다.

## 공통 후처리 (Common Postamble)

Steps 말미에서 다음 **2단계를 공통 수행**한다.

1. **컨텍스트 갱신**: 이번 세션에서 얻은 원칙/결정/교훈을 `contexts/<role>.md`에 타임스탬프 형식으로 append. **항목당 3줄 이내**로 요약하고 상세는 `docs/exec-plans/phases/phaseNN.md`에 쓰고 링크한다. Current Knowledge는 스냅샷으로 갱신(구식 항목 취소선). 파일이 예산(본문 150줄 또는 10KB)을 초과하면 `role-context` 스킬의 **압축(Compact)** 절차를 수행한다.
2. **핸드오버 아카이빙**: `handover` 스킬을 호출하여 `to_<role>.md`를 `logs/YYYY-MM-DD_to_<role>.md`에 append하고 원본은 비운다.

## 검증 사다리 (Verification Ladder)

모든 워크플로우의 "검증" 단계는 아래 순서로 수행하고, **어느 단계로 검증했는지**를 산출물(커밋 메시지·handover·QA 리포트)에 명시한다.

1. **도구 실행**: ruff/pytest/svelte-check/eslint/build 등 실제 도구가 실행 가능하면 반드시 실행하고 결과 수치(통과 건수·에러 0 등)를 기록한다.
2. **정적 대체**: 도구 실행이 불가하면(폐쇄망·PyPI 차단·서버 미기동) `python -m compileall`·grep 기반 참조 검사·`lint_checker.py` 등으로 대체하고 **"⚠ 실행 불가: <사유>, CI/스테이징에서 실행 필요"**를 명시한다.
3. **위장 금지**: 실행하지 않은 테스트를 통과로 보고하거나 측정하지 않은 지표를 수치로 기재하는 것은 금지. 측정 불가 항목은 **N/A + 사유**로 표기한다.

---

## 워크플로우 정의 형식

```markdown
---
description: [이 워크플로우가 수행하는 작업]
---

## Preconditions
- [실행 전 충족되어야 할 조건]

## Steps
1. Common Preamble 수행
2. …(해당 역할 고유 단계)
N. Common Postamble 수행

## Outputs
- [생성되는 파일·결과물]

## Rollback
- [문제 발생 시 되돌리는 방법]
```

## 신규 워크플로우 추가 절차

1. `../SKILLS.md` §3 테이블에 한 줄 등록.
2. 이 디렉토리에 `<command>.md` 생성 (위 형식 준수).
3. 필요한 신규 스킬은 `../skills/`에 추가한다.
4. `/qa` 통과 후 PR 제출.

> **워크플로우는 에이전트의 자동화 루틴**이다. 반복 작업을 워크플로우로 정의하면 단일 커맨드로 일관되게 실행할 수 있다.
