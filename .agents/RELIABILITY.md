<!-- AI Harness Rule: Read RELIABILITY.md for system resilience, monitoring, and incident response guidelines. This file defines mandatory reliability standards. For detailed deployment steps, always consult `.agents/rules/devops.md`. Ensure all errors are trackable. -->
# 시스템 안정성 (Reliability)

프로덕션 환경에서 발생할 수 있는 장애를 최소화하고, 신속하게 복구하기 위한 가이드라인입니다.
데브옵스(DevOps) 파이프라인 및 운영 규칙은 `.agents/rules/devops.md`를 참고하세요.

## 1. 장애 대비 및 복원력 (Resilience)
- 모든 외부 서비스 콜에는 타임아웃과 재시도 로직이 포함되어야 합니다.
- Circuit Breaker 패턴 도입 검토

## 2. 모니터링 및 로깅
- **로깅 규칙**: INFO, WARN, ERROR 레벨 분리. 중요한 비즈니스 로직에는 적절한 로깅 추가
- 에러 발생 시 스택 트레이스 및 컨텍스트 정보를 포함할 것

## 3. 무중단 배포 및 백업 전략
- 블루-그린 배포 등 무중단 배포 전략 설계
- 주기적인 데이터베이스 자동 백업 및 복원 테스트

## 4. 장애 대응 프로세스 (Incident Response)
- P1, P2 등급별 장애 정의 및 담당자 알림 체계 구축
