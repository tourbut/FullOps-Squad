# Handover — To <Target Role>

> **From**: [현재 역할]
> **To**: [대상 역할]
> **Created**: YYYY-MM-DD HH:mm:ss
> **Urgency**: 🔴 Urgent / 🟡 Normal / 🟢 Low

---

## 날짜
YYYY-MM-DD

## 브랜치 (Version Control)
`develop/*` 또는 `fix/*` 등 가이드라인 참조

## 현재 상황 (Context)
요청 시점의 맥락을 2~4문장으로 작성합니다.

- **완료된 작업**: [지금까지 마친 작업 요약]
- **현재 상태**: [시스템/코드의 현재 상태]
- **관련 파일**: [핵심 파일 경로 목록]

## 해야 할 일 (Tasks)
실행 가능한 단위의 번호 리스트로 작성합니다.

- [ ] **Task 1**: [구체적 작업 설명]
  - 참고 파일: [경로]
  - 비고: [있는 경우]
- [ ] **Task 2**: [구체적 작업 설명]
  - 참고 파일: [경로]
  - 비고: [있는 경우]

## 기대 산출물 (Expected Outputs)
실제 파일 트리명 또는 결과 등을 명확히 작성합니다.

## 주의사항 (Cautions)
- [이 작업 수행 시 특별히 주의할 점]
- [알려진 리스크 또는 엣지 케이스]

## 참고 자료
- 스프린트 계약: `docs/exec-plans/sprint-contracts/[filename]`
- 관련 CPS: `docs/planning/cps/[filename]`
- 관련 컨텍스트: `contexts/[role].md`

---

## 완료 후 처리 절차

모든 태스크가 완료되면:
1. 이 파일의 내용을 `handovers/logs/YYYY-MM-DD_to_<role>.md`에 추가(append)
2. 이 파일(`to_<role>.md`)을 비우거나 새 요청으로 교체
3. 자신의 컨텍스트 파일(`contexts/`) 업데이트
