---
description: 신규 요구사항·기능 요청을 분석하여 기획 산출물(meeting-logs·cps·product-specs)을 현행화하고 다운스트림 분배로 연결
---

## Preconditions
- `prompt` 혹은 외부 사용자로부터 전달된 신규 요구사항/기능 아이디어가 있어야 함.
- 기존 프로젝트 맥락은 `.agents/docs/planning/product-specs/index.md`·`project-context.md`에서 확인 가능해야 함.

## Steps

### 0. 요청 유형 판별
- **신규 프로젝트**(최초 비전 정의) 인지, **기존 프로젝트의 신규 기능/변경**(증분 현행화) 인지 판별한다.
- 판별이 모호하면 `AskUserQuestion`으로 범위(전체 비전 재정의 / 단일 기능 추가 / 기존 기능 변경)를 확인한 뒤 진행한다.

### 1. 원시 요구사항 캡처 (meeting-logs)
- 발산된 아이디어·요구사항 원문을 가공 없이 `.agents/docs/planning/meeting-logs/YYYY-MM-DD_<topic>.md`에 시간순으로 기록한다 (채택안·폐기안 모두 누락 없이).
- 단발성 오타·1줄 문구 수정 등 경미한 변경은 본 단계를 생략할 수 있다.

### 2. 맥락 종합 & 기획 원칙 대조
- 관련 기존 맥락(`meeting-logs/`, `project-context.md`, 관련 `product-specs/*.md`)을 종합하여 중복·충돌·이력을 파악한다.
- `.agents/docs/design-docs/core-beliefs.md` 및 `PRODUCT_SENSE.md`의 기획 원칙과 대조한다. 원칙과 충돌하는 요구사항은 그대로 명세화하지 말고 사용자에게 확인한다.

### 3. CPS 구조화 (cps)
- 요구사항을 **Context(배경)·Problem(현재 한계)·Solution(제안)** 3분할로 `.agents/docs/planning/cps/YYYY-MM-DD_<topic>.md`에 정리한다.

### 4. 제품 명세 현행화 (product-specs) — 핵심 산출물
요청 유형(Step 0)에 따라 대상 문서를 정한다. **코드 레벨 구현은 제외**하고 기능 단위(F-코드)·비즈니스 요구 수준으로 작성한다.
- **신규 기능 / 기능 확장**: `.agents/docs/planning/product-specs/<feature>.md`를 신규 생성하거나, 해당 기능 스펙을 갱신한다.
- **제품 비전·핵심가치·데이터 모델 등 횡단 변경**: `.agents/docs/planning/product-specs/project-context.md`를 갱신한다 (전면 덮어쓰기 금지, 변경분만 반영하여 기존 누적 내용을 보존).
- **[필수] 인덱스 등록**: 신규 스펙 문서를 추가했으면 `.agents/docs/planning/product-specs/index.md`의 "읽는 순서" 목록에 한 줄 등록하고, 관련 문서 간 상호 링크를 기재한다.

### 5. 다운스트림 연결
- 명세로부터 구현 태스크가 도출되면 `/coordinator` 호출을 권고(또는 트리거)하여 역할별 Handover(`handovers/to_*.md`)로 분배되도록 한다.
- 로드맵 갱신은 `/architect` 단계에 위임한다 (master는 기획 산출물까지만 책임). architect는 상세를 `docs/exec-plans/phases/phaseNN.md`에 기록하고 `PLANS.md`는 인덱스(상태·링크)만 갱신한다.

## Outputs
- 캡처된 원시 로그 `planning/meeting-logs/YYYY-MM-DD_<topic>.md` (해당 시)
- CPS 정의 `planning/cps/YYYY-MM-DD_<topic>.md`
- 신규/갱신된 `planning/product-specs/<feature>.md` 또는 `project-context.md` + 등록된 `product-specs/index.md`
- 후속 `/coordinator` 분배를 위해 정돈된 기획 컨텍스트

## Rollback
- 이번 회차에 **신규 생성**한 파일(meeting-logs·cps·신규 spec)은 삭제한다.
- 기존 파일의 **수정분**은 형상 관리 버전에서 체크아웃(`git checkout <file>`)하여 복원한다.
