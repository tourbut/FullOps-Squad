## Skills

커스텀 검증 및 유지보수 스킬은 `.agent/skills/`에 정의되어 있습니다.

| Skill | Purpose |
|-------|---------|
| `Debug` | 디버깅을 위한 서버 구동 스크립트 모음 |
| `handover` | 각 역할별 Handovers(업무 이관) 완료 처리 규칙 |
| `manage-skills` | 세션 변경사항을 분석하고, 검증 스킬을 생성/업데이트 관리합니다 |
| `qa-tester` | QA 테스터 역할 지침 (테스트 케이스 작성, 실행, 버그 리포트 작성 등) |
| `role-context` | 에이전트의 지식(Context) 로드 및 축적(학습) 방법 |
| `verify-backend-style` | 백엔드 코드 스타일 검증 (FastAPI + SQLModel) |
| `verify-frontend-style` | 프론트엔드 API 호출 양식 검증 (Svelte + FastAPI Client) |
| `verify-implementation` | 프로젝트의 모든 verify 스킬을 순차 실행하여 통합 검증 보고서를 생성합니다 |