# 데이터베이스 스키마 (자동 생성)

> **자동 생성 파일 — 직접 편집 금지.**
> 이 문서는 `alembic` 마이그레이션 또는 ORM 반영 스크립트를 통해 갱신됩니다.
> 스키마 설계 의사결정(근거·트레이드오프)은 `docs/design-docs/`에, 실 변경은 `backend/alembic/versions/`에 기록합니다.

## 생성 규칙
- 생성 시점: Alembic revision 적용 후(`alembic upgrade head`)
- 생성 스크립트: `backend/scripts/dump_schema.py` (예정)
- 섹션 순서: 테이블 → 인덱스 → 제약조건 → 관계 다이어그램

## 현재 스키마

> _아직 생성되지 않았습니다. 최초 마이그레이션 반영 후 자동 채워집니다._

<!-- TODO(devops): dump_schema 스크립트를 CI 파이프라인에 연결한다. -->

