<!-- AI Harness Rule: Read SECURITY.md for non-negotiable security requirements (Secrets, OWASP constraints). Any new infrastructure or API additions MUST be validated against these checkpoints before reaching `main`. -->
# 보안 수칙 및 체크리스트 (Security)

이 문서는 프로젝트 개발 시 준수해야 할 최소한의 보안 요구사항을 정의합니다.

## 1. 코드 보안 기본 수칙

### 비밀키 관리
- [ ] 토큰, 비밀번호, API 키 등은 절대 코드에 하드코딩하지 않는다
- [ ] 모든 시크릿은 `.env` 파일 또는 시크릿 매니저를 통해 관리한다
- [ ] `.env` 파일은 `.gitignore`에 등록되어 있어야 한다
- [ ] `.env.example` 파일에 키 이름만 정의하고, 실제 값은 비워둔다

### 의존성(Dependency) 검사
- [ ] 사용 중인 라이브러리의 취약점을 주기적으로 검사한다 (`pip audit`, `npm audit`)
- [ ] Critical/High 수준 CVE가 발견된 패키지는 즉시 업데이트한다
- [ ] 사용하지 않는 의존성은 제거한다

## 2. 데이터 보호 정책

### 저장 데이터
- [ ] PII(개인 식별 정보)는 적절히 암호화하여 저장한다
- [ ] 비밀번호는 반드시 해싱하여 저장한다 (`bcrypt` / `passlib`)
- [ ] 데이터베이스 접근 권한은 최소 권한 원칙(Least Privilege)을 따른다

### 전송 데이터
- [ ] 모든 API 통신은 HTTPS 프로토콜을 사용한다
- [ ] 민감한 데이터는 응답 로그에 포함하지 않는다
- [ ] CORS 설정은 허용된 도메인만 명시적으로 등록한다

## 3. 취약점 방어 (OWASP Top 10)

| # | 취약점 | 방어 방법 | 체크 |
|---|--------|-----------|------|
| A01 | Broken Access Control | 모든 엔드포인트에 인증/인가 적용, 역할 기반 접근 제어 | [ ] |
| A02 | Cryptographic Failures | TLS 1.2+ 강제, 적절한 해싱 알고리즘 사용 | [ ] |
| A03 | Injection | ORM 사용 필수, 파라미터 바인딩, 사용자 입력 검증 | [ ] |
| A04 | Insecure Design | 위협 모델링, 비즈니스 로직 검증 | [ ] |
| A05 | Security Misconfiguration | 디버그 모드 프로덕션 비활성화, 기본 계정 제거 | [ ] |
| A06 | Vulnerable Components | 의존성 스캔, 취약 패키지 즉시 업데이트 | [ ] |
| A07 | Auth Failures | 강력한 비밀번호 정책, 세션 타임아웃, MFA 검토 | [ ] |
| A08 | Data Integrity Failures | 서명된 데이터, CI/CD 파이프라인 무결성 검증 | [ ] |
| A09 | Security Logging | 보안 이벤트 로깅, 로그에 민감 정보 미포함 | [ ] |
| A10 | SSRF | 내부 네트워크 접근 차단, URL 화이트리스트 | [ ] |

## 4. API 보안 체크리스트

- [ ] Rate Limiting 적용 (Brute Force 방어)
- [ ] 입력 데이터 크기 제한 (Request Body Size Limit)
- [ ] JWT 토큰 만료 시간 설정 및 갱신 메커니즘
- [ ] SQL Injection 방어: ORM 전용, raw query 금지
- [ ] XSS 방어: 사용자 입력 이스케이프 처리
- [ ] CSRF 방어: SameSite 쿠키 또는 CSRF 토큰 사용

## 5. 보안 리뷰 타이밍

- 모든 API 엔드포인트 추가/변경 시
- 인프라/배포 설정 변경 시
- 외부 라이브러리 신규 도입 시
- `main` 브랜치 병합 전 필수 검증
