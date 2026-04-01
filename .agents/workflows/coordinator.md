---
description: 상위 레벨의 태스크를 각 개발 에이전트의 Handover 파일로 분배 및 지시
---

## Preconditions
- 설계 산출물이나 기획안, 버그 리포트 등에 쪼개지지 않은 전체 작업 요구사항이 존재해야 함.
- 현재 시스템 아키텍처 및 로드맵 문서를 통해 전체 맥락 파악이 가능해야 함.

## Steps

### 1. 현황 및 기초 컨텍스트 분석
- 현재 프로젝트의 상태(완료/진행 중/예정)를 파악한다.
- `.agents/ARCHITECTURE.md` (아키텍처 구조 규칙)
- `.agents/docs/design-docs/core-beliefs.md` (시스템 운영 신념)
- `.agents/PLANS.md` (산출물 로드맵)
- `.agents/docs/evaluations/qa-reports/` (현재 이슈 상황 검토)
- `.agents/docs/exec-plans/active/` (현재 진행 상황 검토)

### 2. 구체적인 태스크 분할 (분배형 워크플로우)
- 상위 태스크(예: "Setup Backend Skeleton")를 한 곳에 모아두지 말고, 각 역할별 쪼개진 단위로 다음과 같이 Handover 문서를 업데이트 분배한다.
  - 아키텍트/설계/구조: `.agents/handovers/to_architect.md`
  - 백엔드 구현: `.agents/handovers/to_backend_dev.md`
  - 프론트엔드 구현: `.agents/handovers/to_frontend_dev.md`
  - 품질/테스트: `.agents/handovers/to_qa_tester.md`
  - 배포/인프라: `.agents/handovers/to_devops.md`

### 3. Handovers 기록 포맷팅 
- 분배되는 파일에는 절대 코드를 짜지 않고 지시사항만 쓴다. 형식은 다음과 같다:
  - `## 날짜` (YYYY-MM-DD 형식)
  - `## 브랜치 (Version Control)` (`develop/*` 또는 `fix/*` 등 가이드라인 참조)
  - `## 현재 상황 (Context)` (요청 시점의 맥락을 2~4문장으로)
  - `## 해야 할 일 (Tasks)` (실행 가능한 단위의 번호 리스트. 예: FastAPI 셋업 등)
  - `## 기대 산출물 (Expected Outputs)` (실제 파일 트리명 또는 결과 등 명확히)
  - `## 참고 자료` (디자인 정책 등 링크)

### 4. 기존 완료 태스크 이관 규칙 (Archiving)
- 이미 `to_*.md` 에 완료된 내역이 있을 시 사용자가 명시적으로 남기라 하지 않는 한:
  - 백업 위치: `.agents/handovers/logs/YYYY-MM-DD_to_<role>.md`
  - 파일이 있으면 기존 내용 밑에 추가(`append`)하고 없으면 파일을 복사(이동)한다.
  - 그 후 원본 `to_<role>.md`는 다음 롤링을 위해 비우거나 교체한다.

## Outputs
- 역할별로 명확히 나뉜 `.agents/handovers/to_*.md` 파일들
- 아카이빙 된 `.agents/handovers/logs/YYYY-MM-DD_to_*.md`

## Rollback
- `.agents/handovers/logs/..._to_*.md` 내용을 수거하여 예전 `.agents/handovers/to_*.md` 로 내용을 되돌립니다.