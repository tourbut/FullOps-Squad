---
description: 인프라 구성, CI/CD 구축 및 배포 자동화
---

## Preconditions
- `.agents/handovers/to_devops.md` 문서에 배포 아키텍처나 서버 환경 구성 요구사항이 명시되어 있어야 함.
- (릴리즈 시) `develop` 브랜치에 있는 기능이 `main`에 병합 가능하도록 준비되어 있어야 함.

## Steps
1. `.agents/handovers/to_devops.md`를 분석하여 인프라 설정, CI/CD 배포 스크립트 수정 등 요구사항을 파악합니다.
2. 해당 역할의 컨텍스트 파일(`.agents/contexts/`)을 불러옵니다.
3. `git-rules` 스킬(또는 `.agents/skills/git-rules/SKILL.md`)을 참고하여 적절한 브랜치를 생성하고 체크아웃합니다.
4. 배포 스크립트(Docker, Nginx, CI/CD 파이프라인 등) 생성 또는 수정 요청사항을 수행합니다.
5. 시스템 신뢰성 원칙(`.agents/RELIABILITY.md`)에 부합하는지 확인합니다.
6. 완료 시 적합한 PR을 생성하고 환경 구성을 테스트합니다.
7. 테스트 통과 및 최종 검증 완료 시 필요하다면 `main`으로 안정화 버전을 릴리즈(Merge) 처리합니다.

## Outputs
- 배포/인프라 구성 파일 (Dockerfile, docker-compose.yml 등)
- `.agents/handovers/logs/YYYY-MM-DD_to_devops.md` (완료 백업)

## Rollback
- 인프라 설정을 직전 안정된 커밋으로 `revert`합니다.
- 변경된 핸드오버의 백업 내역을 원복합니다.