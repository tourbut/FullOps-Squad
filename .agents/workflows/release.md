---
description: main 브랜치의 작업 내역을 원격 저장소에 반영하고 배포를 준비하는 릴리즈 프로세스
---

## Preconditions
- `main` 브랜치의 모든 기능이 QA 테스트(`/qa`)를 통과하고 배포할 준비가 되어야 함.
- 작업 디렉토리의 상태가 깨끗해야 함 (commit 되지 않은 변경사항 없음).
- 로컬 `main` 브랜치가 존재해야 함 (이 프로젝트는 `main` 단일 브랜치만 사용한다).

## Steps
1. 작업 상태를 점검하여 변경사항이 남아있지 않은지 확인합니다 (`git status`).
2. `.agents/skills/git-rules/SKILL.md`을 참고하여 브랜치 전략(단일 `main` 브랜치)을 숙지합니다.
3. 현재 `main` 브랜치에 위치해 있는지 확인합니다 (`git checkout main`).
4. 원격 저장소의 최신 변경사항을 반영합니다 (`git pull origin main`).
   - 충돌(Conflict) 발생 시, 작업을 중단하고 사용자에게 충돌 해결을 요청하거나 직접 해결합니다.
5. 로컬 `main`을 원격 저장소에 Push 합니다 (`git push origin main`).
6. 릴리즈 노트가 필요하다면 작성을 지원하고 배포 환경 준비(`/devops`)가 필요한지 확인합니다.

## Outputs
- 원격 저장소의 `main` 브랜치에 최신 작업 내역이 반영됨
- 릴리즈 완료 내역을 사용자에게 보고

## Rollback
- Push 전 롤백이 필요한 경우: `git reset --hard origin/main`
- Push 후 되돌려야 하는 경우: `git revert <commit>`로 문제 커밋을 되돌린 뒤 다시 Push
