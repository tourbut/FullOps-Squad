---
name: verify-linter-rules
description: linter-rules.md에 정의된 기계적 린터 규칙을 코드로 직접 검증합니다. 코드 변경 후, PR 전, 코드 리뷰 시 사용.
---

# 린터 규칙 검증 (Linter Rules Verification)

## Purpose

`rules/linter-rules.md`에 명시된 기계적 린터 규칙을 Python 스크립트로 직접 구현하여
에이전트가 작성한 코드를 자동으로 검증합니다:

1. **파일 네이밍 규칙** (FILE-xxx): kebab-case, 접미사 컨벤션 검증
2. **임포트 규칙** (IMP-xxx): 그룹 순서, 상대경로 금지, 와일드카드 금지
3. **파일 크기 제한** (SIZE-xxx): 파일 유형별 최대 라인 수 검증
4. **코드 스타일 규칙** (STYLE-xxx): any 타입 금지, 타입 힌트 누락, docstring 누락
5. **보안 규칙** (SEC-xxx): 하드코딩 시크릿 탐지
6. **아키텍처 규칙** (ARCH-xxx): 의존성 방향 위반, 레이어 스킵
7. **금지 패턴** (ANTI-xxx): print(), eval(), type:ignore 등
8. **Svelte 규약** (SVELTE-xxx): Runes 강제(Svelte 5), 레거시 금지, PascalCase 컨벤션, api_router 강제
9. **커스텀 규칙** (CUSTOM-xxx): 에이전트가 `custom_rules.json`을 통해 동적으로 추가한 확장 규칙

## When to Run

- 새로운 코드를 작성하거나 수정한 후
- Pull Request를 생성하기 전
- `verify-implementation`에서 순차 호출될 때
- 코드 품질 감사를 수행할 때

## Related Files

| File | Purpose |
|------|---------|
| `.agents/rules/linter-rules.md` | 린터 규칙 원본 정의서 |
| `.agents/rules/correction-guides.md` | 위반별 자동 수정 가이드 |
| `.agents/ARCHITECTURE.md` | 레이어 계층 및 의존성 방향 규칙 |
| `.agents/SECURITY.md` | 보안 체크리스트 |
| `backend/app/` | 백엔드 Python 소스 코드 |

## Workflow

### Step 1: 린터 검증 스크립트 실행

프로젝트 루트에서 아래 명령어를 실행합니다:

```bash
# 전체 검사
python .agents/skills/verify-linter-rules/scripts/lint_checker.py

# 특정 디렉토리만 검사
python .agents/skills/verify-linter-rules/scripts/lint_checker.py backend/app/

# JSON 형식 출력 (자동화 연동용)
python .agents/skills/verify-linter-rules/scripts/lint_checker.py --format json

# 등록된 규칙 목록 (커스텀 포함) 확인
python .agents/skills/verify-linter-rules/scripts/lint_checker.py --list-rules
```

### Step 2: 위반 분석 및 수정 가이드 연계

스크립트가 출력하는 각 위반에 대해:

1. 위반 코드(예: `FILE-001`, `IMP-002`)를 확인합니다
2. `rules/correction-guides.md`에서 해당 위반 코드의 수정 가이드를 참조합니다
3. 수정 가이드에 따라 코드를 수정합니다

### Step 3: 검사 항목별 세부 검증

스크립트가 자동으로 수행하지만, 수동 확인이 필요한 경우 아래 명령어를 참고하세요:

#### 3a. 파일 네이밍 (FILE-xxx)

```bash
# kebab-case 위반 파일 탐지 (Python)
find backend/app -name "*.py" | grep -E "[A-Z]|_" | grep -v "__" | grep -v ".venv"

# kebab-case 위반 파일 탐지 (TypeScript)
find frontend/src -name "*.ts" -o -name "*.js" | grep -E "[A-Z]" | grep -v node_modules
```

#### 3b. 임포트 규칙 (IMP-xxx)

```bash
# 상대 경로 임포트 탐지 (Python)
grep -rn "from \.\." backend/app/ --include="*.py" | grep -v __pycache__

# 와일드카드 임포트 탐지
grep -rn "import \*" backend/app/ --include="*.py" | grep -v __pycache__
```

#### 3c. 파일 크기 (SIZE-xxx)

```bash
# 300라인 초과 Python 파일
find backend/app -name "*.py" -exec sh -c 'wc -l "$1" | awk "\$1 > 300 {print}"' _ {} \;
```

#### 3d. 금지 패턴 (ANTI-xxx)

```bash
# print() 사용
grep -rn "print(" backend/app/ --include="*.py" | grep -v __pycache__ | grep -v "test_"

# eval()/exec() 사용
grep -rn -E "eval\(|exec\(" backend/app/ --include="*.py" | grep -v __pycache__

# type: ignore 사용
grep -rn "type: ignore" backend/app/ --include="*.py" | grep -v __pycache__
```

### Step 4: 아키텍처 규칙 검증

스크립트가 `ARCHITECTURE.md`의 레이어 매핑을 기반으로 임포트 방향을 분석합니다:

```
Layer 6: UI (routes/, lib/components/)
Layer 5: Runtime (app/main.py, app/src/routes/)
Layer 4: Service (app/src/engine/)
Layer 3: Repository (app/src/crud/)
Layer 2: Config (app/core/)
Layer 1: Types (app/models/)
```

**위반 조건:**
- 하위 레이어 → 상위 레이어 참조 (ARCH-001)
- UI → Repository 직접 참조 (ARCH-002)

## Output Format

검증 결과를 아래 형식의 테이블로 출력합니다:

| 위반 코드 | 파일 | 라인 | 설명 | 심각도 |
|-----------|------|------|------|--------|
| FILE-001 | `backend/app/UserModel.py` | — | 파일명 kebab-case 위반 | ERROR |
| IMP-002 | `backend/app/src/crud/user.py` | 5 | 상대 경로 임포트 사용 | ERROR |
| SIZE-001 | `backend/app/src/routes/auth.py` | — | 350라인 (최대 300) | WARNING |
| ANTI-001 | `backend/app/src/engine/worker.py` | 42 | print() 사용 금지 | ERROR |

**요약:**

```
==========================================
  린터 규칙 검증 보고서
==========================================
  총 검사 파일: N개
  위반: X개 (ERROR: Y, WARNING: Z)
  수정 가이드: .agents/rules/correction-guides.md
==========================================
```

## Self-Evolving Protocol (자가 확장 체계)

본 린터 스킬은 **자가 확장성(Self-Evolving)** 을 지원합니다. 에이전트가 작업 중 지속적으로 발생하는 새로운 위반 패턴을 발견하면, 하드코딩 수정 없이 동적으로 규칙을 추가하여 검증 체계를 강화할 수 있습니다.

### 커스텀 규칙 등록 플로우

1. **위반 인지**: 반복적인 실수나 새로운 규칙 합의 도출
2. **`custom_rules.json` 추가**: `--list-rules`로 등록 현황 파악 후 `.agents/skills/verify-linter-rules/custom_rules.json`에 정규식 플러그인 정의
3. **문서 동기화**: `linter-rules.md`와 `correction-guides.md`에 동일한 규칙을 기록
4. **활성화 및 검증**: `python .../lint_checker.py`에서 `CUSTOM-XXX` 코드로 즉시 탐지 가능하게 연동됨

## Exceptions

다음은 **위반으로 보고하지 않습니다**:

1. **`__init__.py`**: 패키지 초기화 파일은 네이밍/크기/임포트 규칙에서 면제
2. **`__pycache__/`**: 자동 생성된 캐시 디렉토리 제외
3. **`.venv/`, `node_modules/`**: 가상환경 및 외부 패키지 제외
4. **`.svelte-kit/`, `build/`**: 프레임워크 빌드 산출물 제외
5. **테스트 파일 (`test_*.py`, `*.test.ts`)**: SIZE-001 기준이 500라인으로 완화됨
6. **Svelte 컴포넌트 (`*.svelte`)**: 파일명에 PascalCase 허용 (프레임워크 컨벤션)
7. **`alembic/`**: 마이그레이션 스크립트는 자동 생성된 코드이므로 대부분 규칙에서 면제
8. **설정 파일 (`*.config.py`, `*.config.ts`)**: 일부 네이밍 규칙에서 완화
