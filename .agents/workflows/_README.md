# workflows/ — Slash Command Executable Workflows

> 이 디렉토리에는 슬래시 커맨드(`/command`)로 트리거되는
> **자동화된 워크플로우** 정의 및 구현이 포함되어 있습니다.

---

## 디렉토리 구조

```
workflows/
├── _README.md               # 이 파일
├── master.md                # /master 워크플로우 정의
├── coordinator.md           # /coordinator 워크플로우 정의
├── architect.md             # /architect 워크플로우 정의
├── backend.md               # /backend 워크플로우 정의
├── frontend.md              # /frontend 워크플로우 정의
├── devops.md                # /devops 워크플로우 정의
└── qa.md                    # /qa 워크플로우 정의
└── improve.md               # /improve 워크플로우 정의
```

---

## 워크플로우 정의 형식

각 워크플로우 파일은 아래 구조를 따릅니다:

```markdown
---
description: [이 워크플로우가 수행하는 작업 설명]
---

## Preconditions
- [실행 전 충족되어야 할 조건]

## Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Outputs
- [워크플로우가 생성하는 파일 또는 결과물]

## Rollback
- [문제 발생 시 되돌리는 방법]
```

---

## 등록된 워크플로우

| 커맨드 | 설명 | 실행자 | 상태 |
|--------|------|--------|------|
| `/master` | 요구사항 분석 및 제품 명세/기획안 생성 | PM | ✅ 구현됨 |
| `/coordinator` | 태스크를 역할별 Handover 파일로 분배 | Coordinator | ✅ 구현됨 |
| `/architect` | 시스템 아키텍처 설계 및 기술 스택 관리 | Architect | ✅ 구현됨 |
| `/backend` | 백엔드 모듈/API 설계 및 비즈니스 로직 개발 | Backend Dev | ✅ 구현됨 |
| `/frontend` | 프론트엔드 UI/UX 구현 및 API 연동 | Frontend Dev | ✅ 구현됨 |
| `/devops` | 인프라 구성, CI/CD 구축 및 배포 자동화 | DevOps | ✅ 구현됨 |
| `/qa` | 품질 기준에 따른 테스트 및 버그 리포트 | QA | ✅ 구현됨 |
| `/improve` | 건강 상태 평가(evaluate-harness) 기반 자가 개선 | Architect | ✅ 구현됨 |

---

## 신규 워크플로우 추가 절차

1. `SKILLS.md`의 "Workflow Skills" 테이블에 항목 추가
2. 이 디렉토리에 `[command-name].md` 파일 생성
3. 필요한 스킬 구현이 없다면 `skills/`에 추가
4. 테스트 후 PR 제출

---

> **워크플로우는 에이전트의 "자동화된 루틴"입니다.**
> 반복적인 작업을 워크플로우로 정의하면
> 단일 커맨드로 일관되게 실행할 수 있습니다.
