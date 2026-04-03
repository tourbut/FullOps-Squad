# skills/ — Agent Skill Implementations

> 이 디렉토리에는 `SKILLS.md`에 정의된 스킬의 **실제 구현**이 포함되어 있습니다.
> 스킬 사양(what, when, how)은 `SKILLS.md`에서 관리하며,
> 구현(실제 코드/스크립트)은 이 디렉토리에서 관리합니다.

---

## 디렉토리 구조

```
skills/
├── _README.md              # 이 파일
│
│  # 프로세스 관리
├── role-context/           # 역할별 지식 관리
├── handover/               # Handover 완료 처리
├── git-rules/              # Git 커밋/브랜치 규칙 검증
├── manage-skills/          # 스킬 동적 관리
│
│  # 코드 검증
├── verify-implementation/  # 통합 검증 오케스트레이터
├── backend-style/          # 백엔드 코드 스타일 검증
├── frontend-style/         # 프론트엔드 코드 스타일 검증
├── qa-tester/              # QA 테스트 실행
│
│  # 개발 보조
├── debug/                  # 디버깅/서버 구동
├── refactoring/            # 코드 리팩토링
├── prompt-engineer/        # AI 프롬프트 설계
│
│  # 유틸리티
├── docx/                   # Word 문서 처리
├── pdf/                    # PDF 파일 처리
├── pptx/                   # PowerPoint 처리
├── xlsx/                   # Excel 처리
├── skill-creator/          # 스킬 생성/개선
├── frontend-design/        # 프론트엔드 UI 구현
├── canvas-design/          # 시각적 디자인 제작
├── algorithmic-art/        # 알고리즘 아트
├── brand-guidelines/       # 브랜드 가이드라인
├── theme-factory/          # 테마 스타일링
├── web-artifacts-builder/  # 웹 아티팩트 제작
├── webapp-testing/         # 웹앱 테스트
├── doc-coauthoring/        # 문서 공동 작성
├── internal-comms/         # 내부 커뮤니케이션
├── mcp-builder/            # MCP 서버 구축
└── slack-gif-creator/      # Slack GIF 제작
```

---

## 스킬 구현 원칙

1. **단일 책임**: 하나의 스킬 파일은 하나의 기능만 수행
2. **멱등성**: 동일 입력에 대해 동일한 결과 보장
3. **에러 처리**: 실패 시 명확한 에러 메시지 반환
4. **로깅**: 실행 추적이 가능한 로그 출력
5. **테스트**: 각 스킬에 대한 단위 테스트 작성

---

## 신규 스킬 추가 절차

1. `SKILLS.md`에 스킬 사양 추가 (사양이 먼저)
2. 이 디렉토리의 적절한 위치에 구현 코드 작성
3. 테스트 코드 작성
4. 해당 역할의 컨텍스트 파일에 신규 스킬 사용 기록
5. PR 제출 및 리뷰

---

> **사양 없는 구현은 허용되지 않습니다.**
> 항상 `SKILLS.md`에 먼저 등록한 후, 이 디렉토리에서 구현하세요.
