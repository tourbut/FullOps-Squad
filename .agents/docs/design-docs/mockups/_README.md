# mockups/ — 디자인 목업 산출물 공간

<!-- AI Harness Rule: 구현(프론트/백엔드) 이전에 요구사항을 시각적 목업으로 먼저 확정(UI/UX 확정)하기 위한 산출물 공간. 목업은 자체완결 HTML로 브라우저에서 즉시 검토 가능해야 하며, 확정 결과가 곧 프론트 구현의 입력이 된다. -->

> **목적**: 요구사항 → **디자인 목업(시각 검토)** → **UI/UX 확정** → 프론트(필요시 백엔드) 구현으로 이어지는 *구현-선행 검토* 단계의 산출물을 보관한다.
> 목업 생성은 `skills/design-mockup/SKILL.md` 스킬이, 전체 흐름은 `/design` 워크플로우(`workflows/design.md`)가 담당한다.

---

## 1. 디렉토리 규칙

각 기능 단위로 폴더 하나를 만든다.

```
mockups/
├── _README.md                  ← 이 문서 (규칙)
├── _TEMPLATE/                  ← 신규 목업 시작 스캐폴드 (복사해서 사용)
│   ├── index.html              ← 토큰 주입된 자체완결 HTML 시작점
│   └── README.md               ← 스펙·결정·상태 기록 템플릿
└── YYYY-MM-DD_<feature-slug>/  ← 기능별 목업
    ├── index.html              ← 목업 (단일 또는 상태/화면별 분리)
    ├── <variant>.html          ← (선택) A/B 시안·상태별 화면
    └── README.md               ← 스펙 링크·디자인 근거·UI/UX 결정·상태
```

- 폴더명: `YYYY-MM-DD_<feature-slug>` (kebab-case). 예: `2026-06-28_mcp-server-panel`.
- HTML은 **자체완결**(Tailwind CDN + Pretendard CDN + 디자인 토큰 인라인)이어야 하며, `file://`로 더블클릭해 바로 열린다. 외부 빌드·dev 서버 불요.
- 시안이 여러 개면 `index.html`(대표) + `option-a.html`/`option-b.html` 등으로 분리하고 README에 비교표를 둔다.

## 2. 상태(Status) 라이프사이클

각 목업 폴더의 `README.md` 상단에 상태를 명시한다.

| 상태 | 의미 | 다음 단계 |
|------|------|-----------|
| `proposed` | 목업 작성 완료, 검토 대기 | 사용자/Architect 리뷰 |
| `confirmed` | UI/UX 확정 — 구현 착수 가능 | `/frontend` 구현 진입 |
| `revising` | 피드백 반영 중 | 재검토 |
| `implemented` | 구현 완료 (목업과 실제 화면 정합) | 보존(레퍼런스) |
| `superseded` | 후속 목업으로 대체됨 | 보존(이력) |

> **핵심 게이트**: `/frontend` 워크플로우는 해당 기능 목업이 `confirmed` 상태일 때만 구현에 진입한다.

## 3. 디자인 토큰 (권위)

색상·타이포·간격 토큰의 단일 출처는 `docs/references/design-system-reference-llms.txt`이며,
프론트 실제 정의는 `frontend/src/app.css`의 `@theme` 블록이다.
목업 HTML은 `_TEMPLATE/index.html`이 주입하는 동일 시맨틱 토큰(`primary`/`accent`/`surface`/`text` 등)을 사용해
**확정 → 구현 시 클래스 매핑이 1:1로 이어지도록** 한다.

## 4. UI/UX 확정 체크리스트

목업을 `confirmed`로 올리기 전 `docs/design-docs/ui-ux-guidelines.md` §3 상태 처리와 아래를 확인한다.

- [ ] 로딩·빈·에러·성공 상태가 목업에 표현되었는가
- [ ] 3개 브레이크포인트(375 / 768 / 1440px)에서 레이아웃이 깨지지 않는가
- [ ] 디자인 토큰만 사용했는가 (임의 hex·인라인 스타일 최소화)
- [ ] 기존 화면과 일관성(네비·헤더·카드 패턴)이 유지되는가
- [ ] 관련 스펙(`planning/product-specs/*`)의 요구사항을 모두 시각화했는가
