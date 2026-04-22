---
description: develop 브랜치의 작업 내역을 main 브랜치로 병합하고 배포를 준비하는 릴리즈 프로세스
---

## Preconditions
- `develop` 브랜치의 모든 기능이 QA 테스트(`/qa`)를 통과하고 병합할 준비가 되어야 함.
- 작업 디렉토리의 상태가 깨끗해야 함 (commit 되지 않은 변경사항 없음).
- `main`과 `develop` 브랜치가 로컬에 존재해야 함.

## Steps
1. 작업 상태를 점검하여 변경사항이 남아있지 않은지 확인합니다 (`git status`).
2. `.agents/skills/git-rules/SKILL.md`을 참고하여 브랜치 전략을 숙지합니다.
3. `develop` 브랜치를 최신 상태로 유지합니다 (`git checkout develop` 후 `git pull origin develop` 등).
4. `main` 브랜치로 전환하고 최신 상태로 업데이트합니다 (`git checkout main` 후 `git pull origin main` 등).
5. `develop` 브랜치를 `main`으로 머지합니다 (`git merge develop --no-ff -m "chore(release): merge develop into main"`).
   - 충돌(Conflict) 발생 시, 작업을 중단하고 사용자에게 충돌 해결을 요청하거나 직접 해결합니다.
6. 머지가 성공하면 원격 저장소에 Push 합니다 (`git push origin main`).
7. 릴리즈 노트가 필요하다면 작성을 지원하고 배포 환경 준비(`/devops`)가 필요한지 확인합니다.

## Outputs
- 원격 저장소의 `main` 브랜치에 `develop` 내용이 반영됨
- 릴리즈 완료 내역을 사용자에게 보고

## Rollback
- 머지 중 충돌이 심하거나 취소해야 할 경우: `git merge --abort`
- 머지 후 Push 전 롤백이 필요한 경우: `git reset --hard ORIG_HEAD`
