---
description: 프론트엔드 UI/UX 구현 및 API 연동 개발
---

## Preconditions
- `.agents/handovers/to_frontend_dev.md` 문서에 UI/UX 및 연동 요구사항이 명확하게 작성되어 있어야 함.

## Steps
1. `.agents/handovers/to_frontend_dev.md`를 분석하여 변경 필요 사항과 기대 산출물을 파악합니다.
2. 해당 역할의 컨텍스트 파일(`.agents/contexts/`)을 불러옵니다.
3. `git-rules` 스킬(또는 `.agents/skills/git-rules/SKILL.md`)을 참고하여 적절한 브랜치(예: `develop/*`)를 생성하고 체크아웃합니다.
4. 프론트엔드 개발 요청사항을 수행하며, 디자인 가이드(`FRONTEND.md` 및 `ui-ux-guidelines.md`)를 준수합니다. (요청 밖의 기능 작업은 제한)
5. 구현한 사항에 대해 브라우저 표시 및 로직 단위 테스트를 추가합니다.
6. 작업 완료 후 GitHub(또는 사용 중인 호스팅 서비스)에서 PR(Pull Request)을 생성합니다.
7. 리뷰 통과 시 `develop` 브랜치에 병합합니다.

## Outputs
- 수정/추가된 프론트엔드 소스코드 및 컴포넌트
- UI 검증 스크린샷 또는 E2E/단위 테스트 코드
- 생성된 Pull Request
- `.agents/handovers/logs/YYYY-MM-DD_to_frontend_dev.md` (완료 백업)

## Rollback
- 적용된 변경 브랜치를 삭제하고 PR을 닫습니다.
- `.agents/handovers/logs/...`에 백업된 내역을 기존 핸드오버 파일로 복원합니다.