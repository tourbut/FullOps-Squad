---
description: 인프라 구성·CI/CD 구축·배포 자동화
---

## Preconditions
- `.agents/handovers/to_devops.md`에 인프라/배포 요구사항이 명시되어 있어야 함.
- (릴리즈 시) `develop` 브랜치가 `main`에 병합 가능한 상태여야 함.

## Steps
1. **Common Preamble** 수행.
2. 배포 스크립트(Dockerfile·docker-compose·CI 파이프라인 등)를 요구사항에 맞게 생성·수정한다.
3. `RELIABILITY.md` 체크리스트(타임아웃·재시도·롤백·헬스체크·백업)를 충족하는지 검증한다.
4. PR 생성 후 스테이징에서 smoke test 수행.
5. 최종 승인 시 `/release` 워크플로우로 `main` 병합을 수행한다.
6. **Common Postamble** 수행.

## Outputs
- 업데이트된 인프라 구성 파일(Dockerfile·compose·CI yaml 등)
- `handovers/logs/YYYY-MM-DD_to_devops.md`

## Rollback
- 인프라 설정을 직전 안정 커밋으로 `git revert`.
- 백업된 handover 로그 복원.
