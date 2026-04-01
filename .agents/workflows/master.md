---
description: 발산된 요구사항 분석 및 초기 제품 명세/기획안(Spec) 생성
---

## Preconditions
- `prompt` 혹은 외부 사용자로부터 전달된 신규 기획 아이디어가 있어야 함.

## Steps
1. 사용자의 신규 작성/요구사항 발산 컨텍스트(`prompt`)의 내용을 꼼꼼하게 분석합니다.
2. 만약 해당 내용과 관련된 기존 맥락 정보가 있다면, `.agents/docs/planning/meeting-logs/`나 이전 `project-context.md`에서 이력을 종합합니다.
3. `.agents/docs/design-docs/core-beliefs.md` 및 `PRODUCT_SENSE.md`의 기획 원칙을 준수하는지 대조합니다.
4. 분석된 제품 목표를 바탕으로, 프로젝트의 구체적 명세를 정의하여 `.agents/docs/planning/product-specs/project-context.md`로 정리 및 저장합니다.

## Outputs
- 구조화된 제품 명세 문서 (`project-context.md`)

## Rollback
- 기존 `project-context.md` 파일 상태를 형상 관리 버전에서 체크아웃(`git checkout`)하여 초기화합니다.