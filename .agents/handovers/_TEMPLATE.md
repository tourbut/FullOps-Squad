# Handover — To <Target Role>

> **From**: [현재 역할]
> **To**: [대상 역할]
> **Created**: YYYY-MM-DD HH:mm:ss
> **Urgency**: 🔴 Urgent / 🟡 Normal / 🟢 Low

## 날짜
YYYY-MM-DD

## 브랜치 (Version Control)
`develop/*` 또는 `fix/*` 등 `skills/git-rules/SKILL.md` 참조.

## 현재 상황 (Context)
- **완료된 작업**: [지금까지 마친 작업]
- **현재 상태**: [시스템/코드 현재 상태]
- **관련 파일**: [핵심 파일 경로]

## 해야 할 일 (Tasks)
- [ ] **Task 1**: [구체적 작업 설명]
  - 참고 파일: [경로]
- [ ] **Task 2**: [구체적 작업 설명]
  - 참고 파일: [경로]

## 기대 산출물 (Expected Outputs)
실제 파일 트리·API 명세·테스트 결과 등 명확히 기재.

## 주의사항 (Cautions)
- [알려진 리스크·엣지 케이스]

## 참고 자료
- 스프린트 계약: `docs/exec-plans/sprint-contracts/[filename]`
- 관련 CPS: `docs/planning/cps/[filename]`
- 관련 컨텍스트: `contexts/[role].md`

---

## 완료 후 처리 절차 (`handover` 스킬과 동일)

1. 내용을 `handovers/logs/YYYY-MM-DD_to_<role>.md`에 append.
2. 본 파일(`to_<role>.md`)을 비워 다음 롤링 대기 상태로 전환.
3. `contexts/<role>.md` 업데이트.
