# 프론트엔드 가이드 (Frontend Guide)

이 문서는 FullOps-Squad 프로젝트의 프론트엔드 아키텍처 및 개발 패턴을 안내합니다. 
구체적인 프레임워크별 가이드는 `rules/dev-frontend-svelte.md` 및 `rules/frontend-code-style.md` 문서를 반드시 참조하십시오.

## 1. 컴포넌트 설계 원칙
- 모든 UI 컴포넌트는 단일 책임 원칙(SRP)을 따르도록 작게 나눕니다.
- `AHA` (Avoid Hasty Abstractions) 원칙: 너무 빠른 추상화보다는 코드의 중복을 잠시 허용하는 편이 나을 때가 있습니다.

## 2. 상태 관리 (State Management)
- 전역 상태는 최소한으로 유지합니다.
- (사용 중인 상태 관리 라이브러리/기법에 대한 구체적 안내 추가 필요)

## 3. 스타일링 가이드
- 일관된 디자인 시스템 적용 (CSS 변수 활용 등)
- 반응형 웹 원칙(Mobile First 등) 준수
