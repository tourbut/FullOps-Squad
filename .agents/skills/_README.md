# skills/ — Agent Skill Implementations

> 스킬 사양(what/when/how)은 `../SKILLS.md`에서 단일 소스로 관리한다.
> 이 디렉토리에는 각 스킬의 **실제 구현**(`<skill>/SKILL.md`)만 둔다.
> 카테고리/설명이 필요하면 항상 `SKILLS.md`를 먼저 참조한다 (이 README에서 테이블을 중복 유지하지 않는다).

---

## 구현 원칙

1. **단일 책임**: 한 SKILL.md는 한 기능만 수행한다.
2. **멱등성**: 동일 입력 → 동일 결과.
3. **실제 경로만**: `Related Files` 테이블에는 `ls`로 존재가 검증된 경로만 등록한다. 플레이스홀더 금지.
4. **에러 처리 · 로깅**: 실패 시 명확한 메시지와 추적 가능한 로그를 남긴다.

## 신규 스킬 추가 절차

1. `SKILLS.md`의 적절한 테이블에 한 줄 등록 (사양이 구현보다 먼저).
2. `skills/<name>/SKILL.md` 작성 — frontmatter(`name`, `description`) + `Purpose / When to Run / Workflow / Related Files` 섹션 준수.
3. 역할 컨텍스트(`contexts/<role>.md`)에 스킬 도입 사실 기록.
4. `verify-linter-rules` 통과 확인 후 PR 제출.

> **사양 없는 구현은 허용되지 않는다.** 항상 `SKILLS.md`에 먼저 등록한다.
