<!-- AI Harness Rule: Read PRODUCT_SENSE.md to understand the user value and "Why" behind technical decisions. DO NOT put detailed product specs here. Detailed product specifications must ALWAYS be located in `.agents/docs/planning/product-specs/`. -->
# 프로덕트 마인드셋 및 방향 (Product Sense)

이 문서는 기술적 결정 이면에 있는 '왜(Why)'를 제공합니다. 사용자의 문제를 해결하는 제품을 만들기 위한 원칙들입니다.
상세한 기능 스펙은 `.agents/docs/planning/product-specs/` 디렉토리에 정의합니다.

## 1. 핵심 타겟 유저
- AI 에이전트 기반 소프트웨어 개발 자동화가 필요한 개발 팀/개인 개발자
- 기존 개발 생산성 도구(Jira, GitHub Issues 등)로는 에이전트 협업 관리가 어려운 사용자
- Pain Point: 에이전트에게 작업을 위임할 때 일관된 품질과 맥락 유지가 어려움

## 2. 제품 철학 (Product Philosophy)
- **사용자 중심주의**: 모든 기능은 사용자의 가치 창출을 최우선으로 해야 합니다.
- **점진적 가치 제공**: 크고 무거운 릴리스보다, 작고 빠른 이터레이션으로 사용자 피드백을 수집합니다.
- **접근성(Accessibility)**: 누구나 쉽게 사용할 수 있는 UX를 지향합니다.
- **문서 주도(Document-Driven)**: 코드보다 문서가 먼저입니다. 에이전트가 문서를 읽고 작업을 수행하는 것이 핵심 가치입니다.

## 3. 우선순위 판별 기준

### 의사결정 프레임워크

| 우선순위 | 기준 | 설명 |
|----------|------|------|
| P0 | 시스템 장애 | 에이전트 작업 흐름이 완전히 중단되는 문제 |
| P1 | 핵심 가치 손상 | 문서 정합성, 컨텍스트 유지, Handover 신뢰성 관련 |
| P2 | 생산성 저하 | 에이전트 작업 효율을 떨어뜨리는 문제 |
| P3 | 사용 경험 개선 | 추가 기능, UI 개선, 편의성 향상 |

### 중요도 vs 긴급도 매트릭스

```
          높은 긴급도          낮은 긴급도
높은       즉시 실행            일정 확보 후 실행
중요도     (P0, P1)            (P2)

낮은       위임 또는 자동화     백로그 등록
중요도     (P3)                (Tech Debt Tracker)
```

## 4. 성공 지표 (North Star Metrics)
- **에이전트 자율 작업 완료율**: 인간 개입 없이 1 스프린트 완료 가능 여부
- **문서-코드 동기화율**: 문서 변경과 코드 변경이 동시에 이루어지는 비율
- **Handover 완전성**: 다음 역할이 추가 질의 없이 작업 시작 가능한 비율
