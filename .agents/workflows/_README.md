# workflows/ — Slash Command Executable Workflows

> 슬래시 커맨드(`/command`)로 트리거되는 자동화 워크플로우 정의.
> 등록된 커맨드 전체 목록은 `../SKILLS.md` §3에서 단일 관리한다.

---

## 공통 전처리 (Common Preamble)

모든 역할 워크플로우(`/architect`, `/backend`, `/frontend`, `/devops`, `/qa`)는 Steps 초두에서 다음 **3단계를 공통 수행**한다. 각 워크플로우 파일에서는 반복 기술하지 않고 "Common Preamble 수행"으로 표기한다.

1. **핸드오버 분석**: `.agents/handovers/to_<role>.md`를 읽고 작업 범위·기대 산출물을 파악한다.
2. **컨텍스트 로드**: `.agents/contexts/<role>.md`의 원칙/이전 결정/학습된 패턴을 동기화한다.
3. **브랜치 생성**: `.agents/skills/git-rules/SKILL.md` 규칙에 따라 `develop/*`, `fix/*` 등 적합한 브랜치를 체크아웃한다.

## 공통 후처리 (Common Postamble)

Steps 말미에서 다음 **2단계를 공통 수행**한다.

1. **컨텍스트 갱신**: 이번 세션에서 얻은 원칙/결정/교훈을 `contexts/<role>.md`에 타임스탬프 형식으로 append.
2. **핸드오버 아카이빙**: `handover` 스킬을 호출하여 `to_<role>.md`를 `logs/YYYY-MM-DD_to_<role>.md`에 append하고 원본은 비운다.

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
