---
description: 시스템 아키텍처 설계 및 기술 스택 통합 관리
---

## Preconditions
- `.agents/handovers/to_architect.md`에 요구사항(현재 상황·해야 할 일·기대 산출물)이 구체적으로 기재되어 있어야 함.

## Steps
1. **Common Preamble** 수행 (`workflows/_README.md` 참조)
2. `ARCHITECTURE.md`·`docs/design-docs/core-beliefs.md`를 요청 목적에 맞춰 현행화한다.
3. 요청된 설계/문서화 작업을 수행한다.
4. **[필수] 로드맵 동기화 (인덱스/상세 분리)**: 구현 태스크가 생기면 분리해 기록한다. (작업 목록 없는 순수 개념/원칙 문서는 예외)
   - **상세 로그 → `docs/exec-plans/phases/phaseNN.md`**: 세부 작업 체크리스트(`- [x]/[ ]`)·구현 노트·완료 기준은 **반드시 해당 Phase 파일에만** append한다. 신규 Phase면 `phaseNN.md`를 새로 만든다. (규약: `docs/exec-plans/phases/_README.md`)
   - **인덱스 → `PLANS.md`**: `PLANS.md`에는 **Phase 인덱스 표의 상태·1줄 목표·상세 링크만** 갱신한다. **세부 체크리스트를 PLANS.md에 직접 쓰지 않는다**(매 세션 로드 비용 일정 유지).
5. 구조 변경이 있으면 `ARCHITECTURE.md`의 레이어 매핑 테이블과 실제 디렉토리 일치 여부를 검증한다.
6. 릴리즈가 필요한 마일스톤이면 DevOps에 `main` 병합을 요청한다 (`/release`).
7. **Common Postamble** 수행.

## Outputs
- 업데이트된 `ARCHITECTURE.md`·관련 design-docs
- 갱신된 `docs/exec-plans/phases/phaseNN.md`(상세 로그) + `PLANS.md` 인덱스 행(상태·링크)
- `handovers/logs/YYYY-MM-DD_to_architect.md`

## Rollback
- `handovers/logs/...` 백업을 `to_architect.md`로 복원하고 Git 브랜치를 파기한다.
