#!/usr/bin/env python3
"""
lint_checker.py — linter-rules.md 기반 기계적 린터 규칙 검증 스크립트

linter-rules.md에 정의된 규칙을 Python으로 직접 구현하여
코드 위반을 자동으로 탐지합니다.

에이전트가 custom_rules.json을 통해 규칙을 동적으로 추가/수정할 수 있는
자가 확장(self-evolving) 아키텍처를 지원합니다.

사용법:
    python lint_checker.py                           # 전체 검사
    python lint_checker.py backend/app/              # 특정 디렉토리
    python lint_checker.py --format json             # JSON 출력
    python lint_checker.py --format json backend/app/ # 조합
    python lint_checker.py --list-rules              # 등록된 규칙 목록 출력
"""

import ast
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


# ──────────────────────────────────────────────
# 상수 정의
# ──────────────────────────────────────────────

# 검사 제외 디렉토리
EXCLUDED_DIRS = {
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    ".svelte-kit",
    "build",
    "dist",
    ".git",
    ".agents",
    "alembic",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}

# 검사 제외 파일
EXCLUDED_FILES = {
    "__init__.py",
    "conftest.py",
}

# 파일 유형별 최대 라인 수 (SIZE-001)
MAX_LINES = {
    ".py": 300,
    ".ts": 300,
    ".js": 300,
    ".svelte": 200,
    ".config.py": 100,
    ".config.ts": 100,
    ".config.js": 100,
    ".md": 500,
}

# 테스트 파일 최대 라인 수
TEST_MAX_LINES = 500

# 레이어 매핑 (ARCHITECTURE.md 기준)
# 숫자가 낮을수록 하위 레이어
BACKEND_LAYER_MAP = {
    "app/models":     1,   # Types (L1)
    "app/core":       2,   # Config (L2)
    "app/src/crud":   3,   # Repository (L3)
    "app/src/schemas": 3,  # Repository (L3) — 데이터 검증
    "app/src/engine": 4,   # Service (L4)
    "app/src/utils":  2,   # Config (L2) — 유틸리티
    "app/src/deps":   5,   # Runtime (L5) — 의존성 주입
    "app/src/routes": 5,   # Runtime (L5)
    "app/main":       5,   # Runtime (L5)
}

# 임포트 경로와 레이어 매핑 (Python import → layer)
IMPORT_LAYER_MAP = {
    "app.models":      1,
    "app.core":        2,
    "app.src.crud":    3,
    "app.src.schemas": 3,
    "app.src.engine":  4,
    "app.src.utils":   2,
    "app.src.deps":    5,
    "app.src.routes":  5,
    "app.main":        5,
}

# 프론트엔드 레이어 매핑 (ARCHITECTURE.md 기준)
FRONTEND_LAYER_MAP = {
    "lib/types":       1,   # Types (L1)
    "lib/stores":      2,   # Config (L2)
    "lib/utils":       2,   # Config (L2)
    "lib/apis":        3,   # Repository (L3) — API client
    "lib/services":    4,   # Service (L4)
    "lib/components":  6,   # UI (L6)
    "routes":          5,   # Runtime (L5) / UI (L6)
}

# 프론트엔드 임포트 레이어 매핑
FRONTEND_IMPORT_LAYER_MAP = {
    "$lib/types":      1,
    "$lib/stores":     2,
    "$lib/utils":      2,
    "$lib/apis":       3,
    "$lib/services":   4,
    "$lib/components":  6,
}

# PascalCase가 허용되는 파일 확장자 (프레임워크 컨벤션)
PASCAL_CASE_ALLOWED_EXTENSIONS = {".svelte"}

# ──────────────────────────────────────────────
# Svelte 전용 패턴 (SVELTE-xxx)
# ──────────────────────────────────────────────

# Svelte 5 레거시 문법 탐지 패턴
SVELTE_LEGACY_EXPORT_LET = re.compile(r"^\s*export\s+let\s+")
SVELTE_LEGACY_REACTIVE = re.compile(r"^\s*\$:\s+")
SVELTE_LEGACY_DISPATCHER = re.compile(r"createEventDispatcher")
SVELTE_LEGACY_STORE_SUBSCRIBE = re.compile(r"\$\w+\.subscribe\s*\(")

# Svelte script 태그 검사
SVELTE_SCRIPT_TAG = re.compile(r"<script\b[^>]*>")
SVELTE_SCRIPT_LANG_TS = re.compile(r'<script\b[^>]*\blang\s*=\s*["\']ts["\'][^>]*>')

# Svelte 인라인 스타일 검사
SVELTE_INLINE_STYLE = re.compile(r'<[^>]+style\s*=\s*["\'][^"\']+["\'][^>]*>')

# Svelte 직접 fetch 호출 검사
SVELTE_DIRECT_FETCH = re.compile(r"\bfetch\s*\(")

# 커스텀 규칙 파일 경로 (자가 확장 메커니즘)
CUSTOM_RULES_FILENAME = "custom_rules.json"

# Python 표준 라이브러리 최상위 모듈 (주요 항목)
PYTHON_STDLIB_MODULES = {
    "abc", "aifc", "argparse", "array", "ast", "asynchat", "asyncio",
    "asyncore", "atexit", "base64", "bdb", "binascii", "binhex",
    "bisect", "builtins", "bz2", "calendar", "cgi", "cgitb", "chunk",
    "cmath", "cmd", "code", "codecs", "codeop", "collections",
    "colorsys", "compileall", "concurrent", "configparser", "contextlib",
    "contextvars", "copy", "copyreg", "cProfile", "crypt", "csv",
    "ctypes", "curses", "dataclasses", "datetime", "dbm", "decimal",
    "difflib", "dis", "distutils", "doctest", "email", "encodings",
    "enum", "errno", "faulthandler", "fcntl", "filecmp", "fileinput",
    "fnmatch", "fractions", "ftplib", "functools", "gc", "getopt",
    "getpass", "gettext", "glob", "grp", "gzip", "hashlib", "heapq",
    "hmac", "html", "http", "idlelib", "imaplib", "imghdr", "imp",
    "importlib", "inspect", "io", "ipaddress", "itertools", "json",
    "keyword", "lib2to3", "linecache", "locale", "logging", "lzma",
    "mailbox", "mailcap", "marshal", "math", "mimetypes", "mmap",
    "modulefinder", "multiprocessing", "netrc", "nis", "nntplib",
    "numbers", "operator", "optparse", "os", "ossaudiodev",
    "pathlib", "pdb", "pickle", "pickletools", "pipes", "pkgutil",
    "platform", "plistlib", "poplib", "posix", "posixpath", "pprint",
    "profile", "pstats", "pty", "pwd", "py_compile", "pyclbr",
    "pydoc", "queue", "quopri", "random", "re", "readline", "reprlib",
    "resource", "rlcompleter", "runpy", "sched", "secrets", "select",
    "selectors", "shelve", "shlex", "shutil", "signal", "site",
    "smtpd", "smtplib", "sndhdr", "socket", "socketserver", "sqlite3",
    "ssl", "stat", "statistics", "string", "stringprep", "struct",
    "subprocess", "sunau", "symtable", "sys", "sysconfig", "syslog",
    "tabnanny", "tarfile", "tempfile", "termios", "test", "textwrap",
    "threading", "time", "timeit", "tkinter", "token", "tokenize",
    "tomllib", "trace", "traceback", "tracemalloc", "tty", "turtle",
    "turtledemo", "types", "typing", "unicodedata", "unittest",
    "urllib", "uu", "uuid", "venv", "warnings", "wave", "weakref",
    "webbrowser", "winreg", "winsound", "wsgiref", "xdrlib", "xml",
    "xmlrpc", "zipapp", "zipfile", "zipimport", "zlib",
    "_thread", "__future__",
}

# 하드코딩 시크릿 탐지 패턴 (SEC-001)
SECRET_PATTERNS = [
    re.compile(r"""(?:password|passwd|pwd)\s*=\s*["'][^"']+["']""", re.IGNORECASE),
    re.compile(r"""(?:api_key|apikey|api-key)\s*=\s*["'][^"']+["']""", re.IGNORECASE),
    re.compile(r"""(?:secret|secret_key)\s*=\s*["'][^"']+["']""", re.IGNORECASE),
    re.compile(r"""(?:token|access_token|auth_token)\s*=\s*["'][^"']+["']""", re.IGNORECASE),
    re.compile(r"""(?:db_password|database_password)\s*=\s*["'][^"']+["']""", re.IGNORECASE),
]

# 하드코딩 시크릿 제외 패턴 (테스트용, 예제용)
SECRET_EXCLUDE_PATTERNS = [
    re.compile(r"""=\s*["'](?:test|example|dummy|placeholder|changeme|xxx|your_)""", re.IGNORECASE),
    re.compile(r"""os\.environ"""),
    re.compile(r"""settings\."""),
    re.compile(r"""import\.meta\.env"""),
]

# 하드코딩 URL/포트 탐지 패턴 (ANTI-004)
HARDCODED_URL_PATTERNS = [
    re.compile(r"""["']https?://(?:localhost|127\.0\.0\.1|0\.0\.0\.0):\d+"""),
    re.compile(r"""["']https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"""),
    re.compile(r"""(?:host|HOST)\s*=\s*["']\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}["']"""),
    re.compile(r"""(?:port|PORT)\s*=\s*(?:["'])?\d{4,5}(?:["'])?"""),
]

# 하드코딩 URL 제외 패턴
URL_EXCLUDE_PATTERNS = [
    re.compile(r"""#.*https?://"""),   # 주석 내 URL
    re.compile(r"""["']https?://.*example\.com"""),
    re.compile(r"""\.env"""),          # 환경변수 파일 참조
]


# ──────────────────────────────────────────────
# 데이터 클래스
# ──────────────────────────────────────────────

@dataclass
class LintViolation:
    """린터 위반 정보"""
    code: str            # 위반 코드 (FILE-001, IMP-002 등)
    file: str            # 위반 파일 경로
    line: Optional[int]  # 라인 번호 (해당되는 경우)
    message: str         # 위반 상세 설명
    severity: str        # ERROR 또는 WARNING
    suggestion: str = "" # 수정 제안 (간략)


@dataclass
class LintReport:
    """린터 검증 보고서"""
    violations: list = field(default_factory=list)
    files_checked: int = 0
    skipped_dirs: list = field(default_factory=list)
    skipped_files: list = field(default_factory=list)


# ──────────────────────────────────────────────
# 유틸리티 함수
# ──────────────────────────────────────────────

def is_kebab_case(name: str) -> bool:
    """파일명이 kebab-case인지 확인 (확장자 제외)"""
    # 접미사 패턴(예: .service.py)에서 네이밍 부분만 추출
    stem = name
    # 다중 확장자 처리 (.service.py, .types.ts 등)
    while "." in stem:
        stem = stem.rsplit(".", 1)[0]

    if not stem:
        return True

    # kebab-case: 소문자, 숫자, 하이픈만 허용
    return bool(re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", stem))


def is_test_file(filename: str) -> bool:
    """테스트 파일인지 확인"""
    return (
        filename.startswith("test_")
        or filename.endswith(".test.ts")
        or filename.endswith(".test.js")
        or filename.endswith(".spec.ts")
        or filename.endswith(".spec.js")
    )


def get_file_layer(filepath: str) -> Optional[int]:
    """파일 경로에서 아키텍처 레이어를 결정"""
    # 정규화된 경로로 변환
    normalized = filepath.replace("\\", "/")
    for path_prefix, layer in sorted(
        BACKEND_LAYER_MAP.items(), key=lambda x: len(x[0]), reverse=True
    ):
        if path_prefix in normalized:
            return layer
    return None


def get_import_layer(import_path: str) -> Optional[int]:
    """임포트 경로에서 아키텍처 레이어를 결정"""
    for prefix, layer in sorted(
        IMPORT_LAYER_MAP.items(), key=lambda x: len(x[0]), reverse=True
    ):
        if import_path.startswith(prefix):
            return layer
    return None


def classify_python_import(module_name: str) -> str:
    """Python 임포트를 분류: 'stdlib', 'third_party', 'local'"""
    if not module_name:
        return "local"
    top_level = module_name.split(".")[0]
    if top_level in PYTHON_STDLIB_MODULES:
        return "stdlib"
    if top_level in ("app", "src", "backend", "frontend"):
        return "local"
    return "third_party"


def should_skip_dir(dirname: str) -> bool:
    """디렉토리를 건너뛸지 결정"""
    return dirname in EXCLUDED_DIRS or dirname.startswith(".")


def should_skip_file(filename: str) -> bool:
    """파일을 건너뛸지 결정"""
    return filename in EXCLUDED_FILES


# ──────────────────────────────────────────────
# 린터 검사기 클래스
# ──────────────────────────────────────────────

class LintChecker:
    """linter-rules.md 기반 기계적 린터 규칙 검사기

    자가 확장(self-evolving) 아키텍처:
    - 내장 규칙: 이 클래스에 하드코딩된 검사 메서드
    - 커스텀 규칙: custom_rules.json에서 동적 로드되는 정규식 기반 규칙
    - 에이전트가 새 규칙을 발견하면 custom_rules.json에 추가하고
      이 스크립트가 자동으로 해당 규칙을 적용합니다.
    """

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.report = LintReport()
        self.custom_rules = self._load_custom_rules()

    def _load_custom_rules(self) -> list[dict]:
        """커스텀 규칙을 custom_rules.json에서 동적 로드

        에이전트가 새 패턴을 발견하면 이 파일에 규칙을 추가할 수 있습니다.
        각 규칙은 다음 구조를 가져야 합니다:
        {
            "code": "CUSTOM-001",
            "description": "규칙 설명",
            "pattern": "정규식 패턴",
            "file_extensions": [".py", ".ts"],
            "severity": "ERROR",
            "suggestion": "수정 제안",
            "exclude_patterns": ["제외할 패턴"],
            "enabled": true
        }
        """
        rules_file = (
            self.project_root / ".agents" / "skills"
            / "verify-linter-rules" / CUSTOM_RULES_FILENAME
        )
        if not rules_file.exists():
            return []

        try:
            with open(rules_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [r for r in data.get("rules", []) if r.get("enabled", True)]
        except (json.JSONDecodeError, KeyError):
            return []

    # ────────────────────────────────────────
    # 1. 파일 네이밍 규칙 (FILE-xxx)
    # ────────────────────────────────────────

    def check_file_naming(self, filepath: str) -> list[LintViolation]:
        """파일/디렉토리 네이밍 규칙 검증"""
        violations = []
        path = Path(filepath)
        filename = path.name
        ext = path.suffix

        # Svelte 컴포넌트는 PascalCase 허용
        if ext in PASCAL_CASE_ALLOWED_EXTENSIONS:
            return violations

        # FILE-001: kebab-case 검사
        if ext in (".py", ".ts", ".js"):
            if not is_kebab_case(filename) and not is_test_file(filename):
                # Python test_ 접두사 파일 제외
                if not filename.startswith("test_"):
                    suggested = re.sub(
                        r"([a-z])([A-Z])", r"\1-\2", filename.rsplit(".", 1)[0]
                    ).lower()
                    # 언더스코어를 하이픈으로 변환
                    suggested = suggested.replace("_", "-")
                    suggested += ext
                    violations.append(LintViolation(
                        code="FILE-001",
                        file=filepath,
                        line=None,
                        message=f"파일명이 kebab-case를 위반합니다: {filename}",
                        severity="ERROR",
                        suggestion=f"{filename} → {suggested}",
                    ))

        # FILE-003: 접미사 규칙 검사
        if ext == ".py":
            normalized = filepath.replace("\\", "/")
            # 서비스 파일인데 .service.py가 아닌 경우
            if "/engine/" in normalized and not filename.endswith(".service.py"):
                # engine 디렉토리의 파일은 service 접미사 필요 가능성
                pass  # 현재는 경고 수준으로만 체크

        return violations

    def check_directory_naming(self, dirpath: str) -> list[LintViolation]:
        """디렉토리 네이밍 규칙 검증 (kebab-case + 복수형)"""
        violations = []
        dirname = Path(dirpath).name

        # 숨김 디렉토리, 특수 디렉토리 제외
        if dirname.startswith(".") or dirname.startswith("_"):
            return violations

        # kebab-case 검사 (대문자 또는 언더스코어 포함 시)
        if re.search(r"[A-Z]", dirname):
            violations.append(LintViolation(
                code="FILE-001",
                file=dirpath,
                line=None,
                message=f"디렉토리명이 kebab-case를 위반합니다: {dirname}",
                severity="ERROR",
                suggestion=f"{dirname} → {dirname.lower()}",
            ))

        return violations

    # ────────────────────────────────────────
    # 2. 임포트 규칙 (IMP-xxx) — Python
    # ────────────────────────────────────────

    def check_python_imports(self, filepath: str) -> list[LintViolation]:
        """Python 파일의 임포트 규칙 검증"""
        violations = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
            tree = ast.parse(source)
        except (SyntaxError, UnicodeDecodeError):
            return violations

        imports = []
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append({
                        "type": "import",
                        "module": alias.name,
                        "line": node.lineno,
                        "category": classify_python_import(alias.name),
                        "level": 0,
                    })
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""

                # IMP-002: 상대 경로 임포트 검사
                if node.level > 0:
                    violations.append(LintViolation(
                        code="IMP-002",
                        file=filepath,
                        line=node.lineno,
                        message=f"상대 경로 임포트 사용: from {'.' * node.level}{module} import ...",
                        severity="ERROR",
                        suggestion=f"절대 경로 임포트로 변경하세요 (예: from app.{module} import ...)",
                    ))

                # IMP-004: 와일드카드 임포트 검사
                for alias in node.names:
                    if alias.name == "*":
                        violations.append(LintViolation(
                            code="IMP-004",
                            file=filepath,
                            line=node.lineno,
                            message=f"와일드카드(*) 임포트 사용: from {module} import *",
                            severity="ERROR",
                            suggestion="명시적 임포트로 변경하세요 (예: from module import specific_name)",
                        ))

                imports.append({
                    "type": "from",
                    "module": module,
                    "line": node.lineno,
                    "category": classify_python_import(module),
                    "level": node.level,
                })

        # IMP-001: 임포트 순서 검사
        if len(imports) >= 2:
            category_order = {"stdlib": 0, "third_party": 1, "local": 2}
            prev_category_rank = -1
            prev_line = 0
            blank_line_between_groups = True

            for imp in imports:
                if imp["level"] > 0:
                    continue  # 상대 임포트는 이미 IMP-002로 보고됨
                curr_rank = category_order.get(imp["category"], 2)

                # 그룹 순서가 역전된 경우
                if curr_rank < prev_category_rank:
                    violations.append(LintViolation(
                        code="IMP-001",
                        file=filepath,
                        line=imp["line"],
                        message=(
                            f"임포트 순서 위반: {imp['category']} 임포트가 "
                            f"이전 그룹보다 뒤에 위치해야 합니다"
                        ),
                        severity="WARNING",
                        suggestion="순서: Standard Library → Third-party → Local",
                    ))
                    break  # 첫 위반만 보고

                prev_category_rank = curr_rank
                prev_line = imp["line"]

        return violations

    # ────────────────────────────────────────
    # 2b. 임포트 규칙 (IMP-xxx) — TypeScript
    # ────────────────────────────────────────

    def check_typescript_imports(self, filepath: str) -> list[LintViolation]:
        """TypeScript/JavaScript 파일의 임포트 규칙 검증"""
        violations = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        # type import가 value import 뒤에 오는지 검사
        import_pattern = re.compile(r"""^import\s+""")
        type_import_pattern = re.compile(r"""^import\s+type\s+""")

        last_value_import_line = 0
        first_type_import_line = None

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if import_pattern.match(stripped):
                if type_import_pattern.match(stripped):
                    if first_type_import_line is None:
                        first_type_import_line = i
                else:
                    last_value_import_line = i

        # type import가 value import 보다 앞에 있으면 위반
        if (
            first_type_import_line
            and last_value_import_line
            and first_type_import_line < last_value_import_line
        ):
            violations.append(LintViolation(
                code="IMP-001",
                file=filepath,
                line=first_type_import_line,
                message="type import가 value import보다 앞에 위치합니다",
                severity="WARNING",
                suggestion="type import는 value import 뒤에 배치하세요",
            ))

        return violations

    # ────────────────────────────────────────
    # 3. 파일 크기 제한 (SIZE-xxx)
    # ────────────────────────────────────────

    def check_file_size(self, filepath: str) -> list[LintViolation]:
        """파일 라인 수 제한 검증"""
        violations = []
        path = Path(filepath)
        filename = path.name
        ext = path.suffix

        # 적합한 최대 라인 수 결정
        max_lines = None

        if is_test_file(filename):
            max_lines = TEST_MAX_LINES
        else:
            # 설정 파일 (더 세부적인 확장자 먼저 검사)
            for config_ext in (".config.py", ".config.ts", ".config.js"):
                if filename.endswith(config_ext):
                    max_lines = MAX_LINES[config_ext]
                    break
            if max_lines is None and ext in MAX_LINES:
                max_lines = MAX_LINES[ext]

        if max_lines is None:
            return violations

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                line_count = sum(1 for _ in f)
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        if line_count > max_lines:
            violations.append(LintViolation(
                code="SIZE-001",
                file=filepath,
                line=None,
                message=f"파일 크기 초과: {line_count}라인 (최대 {max_lines}라인)",
                severity="WARNING",
                suggestion="도메인 또는 기능 단위로 파일을 분할하세요",
            ))

        return violations

    # ────────────────────────────────────────
    # 4. 코드 스타일 규칙 (STYLE-xxx)
    # ────────────────────────────────────────

    def check_python_style(self, filepath: str) -> list[LintViolation]:
        """Python 코드 스타일 검증 (타입 힌트, docstring)"""
        violations = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
            tree = ast.parse(source)
        except (SyntaxError, UnicodeDecodeError):
            return violations

        for node in ast.walk(tree):
            # STYLE-002: 함수 타입 힌트 누락
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # private 함수 제외 (언더스코어 시작)
                if node.name.startswith("_"):
                    continue

                # 반환 타입 힌트 누락
                if node.returns is None:
                    violations.append(LintViolation(
                        code="STYLE-002",
                        file=filepath,
                        line=node.lineno,
                        message=f"함수 반환 타입 힌트 누락: def {node.name}(...)",
                        severity="ERROR",
                        suggestion=f"def {node.name}(...) -> ReturnType: 형태로 수정하세요",
                    ))

                # 매개변수 타입 힌트 누락 (self, cls 제외)
                for arg in node.args.args:
                    if arg.arg in ("self", "cls"):
                        continue
                    if arg.annotation is None:
                        violations.append(LintViolation(
                            code="STYLE-002",
                            file=filepath,
                            line=node.lineno,
                            message=f"매개변수 타입 힌트 누락: {node.name}({arg.arg})",
                            severity="ERROR",
                            suggestion=f"{arg.arg}: Type 형태로 타입을 명시하세요",
                        ))
                        break  # 함수당 한 번만 보고

                # STYLE-003: Public 함수 docstring 누락
                docstring = ast.get_docstring(node)
                if docstring is None:
                    violations.append(LintViolation(
                        code="STYLE-003",
                        file=filepath,
                        line=node.lineno,
                        message=f"Public 함수 docstring 누락: {node.name}()",
                        severity="WARNING",
                        suggestion="Google-style docstring을 추가하세요",
                    ))

            # STYLE-003: Public 클래스 docstring 누락
            if isinstance(node, ast.ClassDef):
                if node.name.startswith("_"):
                    continue
                docstring = ast.get_docstring(node)
                if docstring is None:
                    violations.append(LintViolation(
                        code="STYLE-003",
                        file=filepath,
                        line=node.lineno,
                        message=f"Public 클래스 docstring 누락: {node.name}",
                        severity="WARNING",
                        suggestion="클래스에 대한 docstring을 추가하세요",
                    ))

        return violations

    def check_typescript_style(self, filepath: str) -> list[LintViolation]:
        """TypeScript 코드 스타일 검증 (any 타입 금지)"""
        violations = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        # STYLE-001: any 타입 사용 검사
        any_pattern = re.compile(r":\s*any\b|<any>|as\s+any\b")

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            # 주석 라인 제외
            if stripped.startswith("//") or stripped.startswith("*"):
                continue
            if any_pattern.search(line):
                violations.append(LintViolation(
                    code="STYLE-001",
                    file=filepath,
                    line=i,
                    message=f"'any' 타입 사용 금지: {stripped.strip()[:80]}",
                    severity="ERROR",
                    suggestion="'unknown' + type guard 또는 구체적인 타입으로 대체하세요",
                ))

        return violations

    # ────────────────────────────────────────
    # 4b. Svelte 전용 규칙 (SVELTE-xxx)
    # ────────────────────────────────────────

    def check_svelte_style(self, filepath: str) -> list[LintViolation]:
        """Svelte 5 Runes 및 컴포넌트 규칙 검증"""
        violations = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                lines = content.splitlines()
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        filename = Path(filepath).name
        in_script_block = False
        script_block_has_lang_ts = False
        has_script_tag = False

        # 전체 파일에서 script 태그 분석
        for match in SVELTE_SCRIPT_TAG.finditer(content):
            has_script_tag = True
            if SVELTE_SCRIPT_LANG_TS.match(match.group()):
                script_block_has_lang_ts = True

        # SVELTE-001: <script lang="ts"> 미사용
        if has_script_tag and not script_block_has_lang_ts:
            violations.append(LintViolation(
                code="SVELTE-001",
                file=filepath,
                line=None,
                message='<script> 블록에 lang="ts"가 선언되지 않았습니다',
                severity="ERROR",
                suggestion='<script lang="ts">로 변경하세요',
            ))

        # 라인별 검사
        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # script 블록 안인지 추적
            if SVELTE_SCRIPT_TAG.search(line):
                in_script_block = True
            if "</script>" in line:
                in_script_block = False
                continue

            if in_script_block:
                # SVELTE-002: export let (레거시) 사용
                if SVELTE_LEGACY_EXPORT_LET.search(line):
                    violations.append(LintViolation(
                        code="SVELTE-002",
                        file=filepath,
                        line=i,
                        message="'export let' (Svelte 4 레거시) 사용 금지",
                        severity="ERROR",
                        suggestion="$props()를 사용하세요: let { prop } = $props();",
                    ))

                # SVELTE-003: $: 반응형 선언 (레거시) 사용
                if SVELTE_LEGACY_REACTIVE.search(line):
                    violations.append(LintViolation(
                        code="SVELTE-003",
                        file=filepath,
                        line=i,
                        message="'$:' (Svelte 4 레거시) 반응형 선언 사용 금지",
                        severity="ERROR",
                        suggestion="$derived() 또는 $effect()를 사용하세요",
                    ))

                # SVELTE-004: createEventDispatcher 사용
                if SVELTE_LEGACY_DISPATCHER.search(line):
                    violations.append(LintViolation(
                        code="SVELTE-004",
                        file=filepath,
                        line=i,
                        message="createEventDispatcher (Svelte 4 레거시) 사용 금지",
                        severity="ERROR",
                        suggestion="callback props 패턴을 사용하세요 (부모에서 함수를 props로 전달)",
                    ))

                # SVELTE-005: 직접 fetch() 호출 (api_router 미사용)
                if SVELTE_DIRECT_FETCH.search(line):
                    # fastapi.ts나 +server.ts 내부는 제외
                    if not filepath.endswith((
                        "fastapi.ts", "+server.ts", "+server.js",
                        "api-client.ts", "api-client.js",
                    )):
                        violations.append(LintViolation(
                            code="SVELTE-005",
                            file=filepath,
                            line=i,
                            message="직접 fetch() 호출 금지: api_router 래퍼를 사용하세요",
                            severity="ERROR",
                            suggestion="$lib/fastapi의 api_router를 사용하세요",
                        ))

            # SVELTE-006: 인라인 CSS 사용 (script 밖에서도 검사)
            if SVELTE_INLINE_STYLE.search(line):
                violations.append(LintViolation(
                    code="SVELTE-006",
                    file=filepath,
                    line=i,
                    message="인라인 CSS (style=\"...\") 사용 금지",
                    severity="WARNING",
                    suggestion="Tailwind CSS 유틸리티 클래스를 사용하세요",
                ))

        # SVELTE-007: PascalCase 파일명 검증 (Svelte 컴포넌트)
        stem = Path(filepath).stem
        if not re.match(r"^[A-Z][a-zA-Z0-9]*$", stem):
            # SvelteKit 라우팅 파일 (+page, +layout, +error, +server) 제외
            if not stem.startswith("+"):
                violations.append(LintViolation(
                    code="SVELTE-007",
                    file=filepath,
                    line=None,
                    message=f"Svelte 컴포넌트 파일명은 PascalCase이어야 합니다: {filename}",
                    severity="WARNING",
                    suggestion=f"파일명을 PascalCase로 변경하세요 (예: UserCard.svelte)",
                ))

        # SVELTE-008: console.log 사용 (Svelte 파일 내)
        # ANTI-001과 별도로, Svelte 파일 내 script 블록에서도 탐지
        # (ANTI-001에서 이미 .svelte에 대해 검사하므로 여기서는 생략)

        return violations

    # ────────────────────────────────────────
    # 8. 커스텀 규칙 (동적 로드)
    # ────────────────────────────────────────

    def check_custom_rules(self, filepath: str) -> list[LintViolation]:
        """custom_rules.json에서 로드된 커스텀 규칙 검증

        에이전트가 새 위반 패턴을 발견하면 custom_rules.json에 추가하여
        이후 검사에서 자동으로 탐지하도록 합니다.
        """
        violations = []
        if not self.custom_rules:
            return violations

        ext = Path(filepath).suffix

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        for rule in self.custom_rules:
            # 확장자 필터링
            target_exts = rule.get("file_extensions", [])
            if target_exts and ext not in target_exts:
                continue

            try:
                pattern = re.compile(rule["pattern"])
            except re.error:
                continue  # 잘못된 정규식은 무시

            exclude_patterns = []
            for excl in rule.get("exclude_patterns", []):
                try:
                    exclude_patterns.append(re.compile(excl))
                except re.error:
                    pass

            for i, line in enumerate(lines, 1):
                if pattern.search(line):
                    # 제외 패턴 확인
                    is_excluded = any(ep.search(line) for ep in exclude_patterns)
                    if not is_excluded:
                        violations.append(LintViolation(
                            code=rule.get("code", "CUSTOM-000"),
                            file=filepath,
                            line=i,
                            message=rule.get("description", "커스텀 규칙 위반"),
                            severity=rule.get("severity", "WARNING"),
                            suggestion=rule.get("suggestion", ""),
                        ))

        return violations

    # ────────────────────────────────────────
    # 5. 보안 규칙 (SEC-xxx)
    # ────────────────────────────────────────

    def check_security(self, filepath: str) -> list[LintViolation]:
        """보안 규칙 검증 (하드코딩 시크릿)"""
        violations = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # 주석 라인 제외
            if stripped.startswith("#") or stripped.startswith("//"):
                continue

            # SEC-001: 하드코딩 시크릿 탐지
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    # 제외 패턴 확인 (테스트용, 환경변수 참조)
                    is_excluded = any(
                        excl.search(line) for excl in SECRET_EXCLUDE_PATTERNS
                    )
                    if not is_excluded:
                        violations.append(LintViolation(
                            code="SEC-001",
                            file=filepath,
                            line=i,
                            message=f"하드코딩 시크릿 감지: {stripped[:60]}...",
                            severity="ERROR",
                            suggestion="환경변수 또는 Config 레이어를 사용하세요",
                        ))
                    break  # 라인당 한 번만 보고

        return violations

    # ────────────────────────────────────────
    # 6. 아키텍처 규칙 (ARCH-xxx)
    # ────────────────────────────────────────

    def check_architecture(self, filepath: str) -> list[LintViolation]:
        """아키텍처 의존성 방향 규칙 검증"""
        violations = []

        # Python 파일만 검사
        if not filepath.endswith(".py"):
            return violations

        source_layer = get_file_layer(filepath)
        if source_layer is None:
            return violations

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
            tree = ast.parse(source)
        except (SyntaxError, UnicodeDecodeError):
            return violations

        for node in ast.iter_child_nodes(tree):
            import_module = None

            if isinstance(node, ast.Import):
                for alias in node.names:
                    import_module = alias.name
            elif isinstance(node, ast.ImportFrom):
                if node.level > 0:
                    continue  # 상대 임포트는 IMP-002에서 처리
                import_module = node.module or ""

            if import_module is None:
                continue

            target_layer = get_import_layer(import_module)
            if target_layer is None:
                continue

            # ARCH-001: 하위 레이어 → 상위 레이어 참조 금지
            if source_layer < target_layer:
                violations.append(LintViolation(
                    code="ARCH-001",
                    file=filepath,
                    line=node.lineno,
                    message=(
                        f"의존성 방향 위반: Layer {source_layer} → Layer {target_layer} "
                        f"({import_module})"
                    ),
                    severity="ERROR",
                    suggestion=(
                        "하위 레이어는 상위 레이어를 참조할 수 없습니다. "
                        "ARCHITECTURE.md의 규칙을 확인하세요."
                    ),
                ))

            # ARCH-002: UI → Repository 직접 참조 (레이어 6 → 레이어 3)
            if source_layer >= 5 and target_layer == 3:
                # routes에서 crud를 직접 호출하는 경우
                normalized_path = filepath.replace("\\", "/")
                if "routes" in normalized_path and "crud" in import_module:
                    violations.append(LintViolation(
                        code="ARCH-002",
                        file=filepath,
                        line=node.lineno,
                        message=(
                            f"레이어 스킵: Runtime/UI → Repository 직접 참조 "
                            f"({import_module})"
                        ),
                        severity="ERROR",
                        suggestion="Service 레이어(engine)를 통해 접근하세요",
                    ))

        return violations

    # ────────────────────────────────────────
    # 7. 금지 패턴 (ANTI-xxx)
    # ────────────────────────────────────────

    def check_anti_patterns(self, filepath: str) -> list[LintViolation]:
        """금지 패턴(안티패턴) 검증"""
        violations = []
        ext = Path(filepath).suffix

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, FileNotFoundError):
            return violations

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # 주석 라인 제외
            if ext == ".py" and stripped.startswith("#"):
                continue
            if ext in (".ts", ".js", ".svelte") and stripped.startswith("//"):
                continue

            # ANTI-001: print() / console.log 사용
            if ext == ".py":
                # Python print() 탐지 (AST로도 가능하나 라인 기반이 빠름)
                if re.search(r"\bprint\s*\(", line) and not stripped.startswith("#"):
                    violations.append(LintViolation(
                        code="ANTI-001",
                        file=filepath,
                        line=i,
                        message="print() 사용 금지: logging 모듈을 사용하세요",
                        severity="ERROR",
                        suggestion="import logging; logger = logging.getLogger(__name__)",
                    ))

            if ext in (".ts", ".js", ".svelte"):
                if re.search(r"\bconsole\.log\s*\(", line):
                    violations.append(LintViolation(
                        code="ANTI-001",
                        file=filepath,
                        line=i,
                        message="console.log 사용 금지: 구조화된 로거를 사용하세요",
                        severity="ERROR",
                        suggestion="콘솔 로그 대신 구조화된 로깅을 사용하세요",
                    ))

            # ANTI-002: eval() / exec() 사용
            if re.search(r"\b(?:eval|exec)\s*\(", line):
                violations.append(LintViolation(
                    code="ANTI-002",
                    file=filepath,
                    line=i,
                    message="eval()/exec() 사용 금지: 보안 취약점을 유발합니다",
                    severity="ERROR",
                    suggestion="안전한 대안을 사용하세요 (예: ast.literal_eval)",
                ))

            # ANTI-003: type: ignore / @ts-ignore / @ts-expect-error
            if re.search(r"#\s*type:\s*ignore", line):
                violations.append(LintViolation(
                    code="ANTI-003",
                    file=filepath,
                    line=i,
                    message="# type: ignore 사용 금지: 올바른 타입을 정의하세요",
                    severity="ERROR",
                    suggestion="정확한 타입 정의로 대체하세요",
                ))
            if re.search(r"@ts-ignore|@ts-expect-error", line):
                violations.append(LintViolation(
                    code="ANTI-003",
                    file=filepath,
                    line=i,
                    message="@ts-ignore/@ts-expect-error 사용 금지",
                    severity="ERROR",
                    suggestion="정확한 타입 정의로 대체하세요",
                ))

            # ANTI-004: 하드코딩 URL/포트 (주석 제외)
            for url_pattern in HARDCODED_URL_PATTERNS:
                if url_pattern.search(line):
                    is_excluded = any(
                        excl.search(line) for excl in URL_EXCLUDE_PATTERNS
                    )
                    if not is_excluded:
                        violations.append(LintViolation(
                            code="ANTI-004",
                            file=filepath,
                            line=i,
                            message=f"하드코딩 URL/포트 감지: {stripped[:60]}",
                            severity="WARNING",
                            suggestion="환경변수를 사용하세요",
                        ))
                    break  # 라인당 한 번만

        return violations

    # ────────────────────────────────────────
    # 통합 실행
    # ────────────────────────────────────────

    def collect_files(self, target_dirs: list[str]) -> list[str]:
        """검사 대상 파일 수집"""
        files = []
        target_extensions = {".py", ".ts", ".js", ".svelte"}

        for target_dir in target_dirs:
            target_path = Path(target_dir)
            if not target_path.exists():
                self.report.skipped_dirs.append(str(target_path))
                continue

            if target_path.is_file():
                if target_path.suffix in target_extensions:
                    files.append(str(target_path))
                continue

            for root, dirs, filenames in os.walk(target_path):
                # 제외 디렉토리 필터링
                dirs[:] = [d for d in dirs if not should_skip_dir(d)]

                # 디렉토리 네이밍 검사
                for d in dirs:
                    dirpath = os.path.join(root, d)
                    self.report.violations.extend(
                        self.check_directory_naming(dirpath)
                    )

                for filename in filenames:
                    filepath = os.path.join(root, filename)

                    if should_skip_file(filename):
                        self.report.skipped_files.append(filepath)
                        continue

                    ext = Path(filename).suffix
                    if ext not in target_extensions:
                        continue

                    files.append(filepath)

        return files

    def check_file(self, filepath: str) -> list[LintViolation]:
        """단일 파일에 대해 모든 린터 규칙 검사 실행"""
        violations = []
        ext = Path(filepath).suffix

        # 1. 파일 네이밍
        violations.extend(self.check_file_naming(filepath))

        # 2. 파일 크기
        violations.extend(self.check_file_size(filepath))

        # 3. 임포트 규칙
        if ext == ".py":
            violations.extend(self.check_python_imports(filepath))
        elif ext in (".ts", ".js"):
            violations.extend(self.check_typescript_imports(filepath))

        # 4. 코드 스타일
        if ext == ".py":
            violations.extend(self.check_python_style(filepath))
        elif ext in (".ts", ".js"):
            violations.extend(self.check_typescript_style(filepath))
        elif ext == ".svelte":
            violations.extend(self.check_svelte_style(filepath))

        # 5. 보안
        violations.extend(self.check_security(filepath))

        # 6. 아키텍처
        violations.extend(self.check_architecture(filepath))

        # 7. 금지 패턴
        violations.extend(self.check_anti_patterns(filepath))

        # 8. 커스텀 규칙 (동적 로드)
        violations.extend(self.check_custom_rules(filepath))

        return violations

    def run(self, target_dirs: list[str]) -> LintReport:
        """전체 린터 검사 실행"""
        # 기본 대상 디렉토리
        if not target_dirs:
            default_dirs = ["backend/", "frontend/src/"]
            target_dirs = [
                d for d in default_dirs
                if Path(self.project_root / d).exists()
            ]
            if not target_dirs:
                # 프로젝트 루트에서 탐색
                target_dirs = [str(self.project_root)]

        # 절대 경로로 변환
        resolved_dirs = []
        for d in target_dirs:
            p = Path(d)
            if not p.is_absolute():
                p = self.project_root / p
            resolved_dirs.append(str(p))

        # 파일 수집
        files = self.collect_files(resolved_dirs)
        self.report.files_checked = len(files)

        # 각 파일 검사
        for filepath in files:
            file_violations = self.check_file(filepath)
            self.report.violations.extend(file_violations)

        return self.report


# ──────────────────────────────────────────────
# 출력 포매터
# ──────────────────────────────────────────────

def format_text_report(report: LintReport, project_root: str) -> str:
    """텍스트 형식 보고서 생성"""
    lines = []
    lines.append("=" * 50)
    lines.append("  린터 규칙 검증 보고서")
    lines.append("=" * 50)
    lines.append("")

    if report.skipped_dirs:
        lines.append(f"⚠ 존재하지 않는 디렉토리 (스킵됨): {', '.join(report.skipped_dirs)}")
        lines.append("")

    if not report.violations:
        lines.append("✅ PASS: 모든 린터 규칙을 준수합니다!")
        lines.append("")
        lines.append(f"  검사 파일: {report.files_checked}개")
        lines.append("=" * 50)
        return "\n".join(lines)

    # 위반을 코드별로 그룹화
    error_count = sum(1 for v in report.violations if v.severity == "ERROR")
    warning_count = sum(1 for v in report.violations if v.severity == "WARNING")

    for violation in report.violations:
        # 프로젝트 루트 기준 상대 경로로 표시
        rel_path = violation.file
        try:
            rel_path = os.path.relpath(violation.file, project_root)
        except ValueError:
            pass

        line_info = f":{violation.line}" if violation.line else ""
        severity_icon = "❌" if violation.severity == "ERROR" else "⚠️"

        lines.append(f"{severity_icon} [{violation.code}] {rel_path}{line_info}")
        lines.append(f"  → {violation.message}")
        if violation.suggestion:
            lines.append(f"  💡 {violation.suggestion}")
        lines.append("")

    lines.append("-" * 50)
    lines.append(f"  총 검사 파일: {report.files_checked}개")
    lines.append(f"  위반: {len(report.violations)}개 (ERROR: {error_count}, WARNING: {warning_count})")
    lines.append(f"  수정 가이드: .agents/rules/correction-guides.md")
    lines.append("=" * 50)

    return "\n".join(lines)


def format_json_report(report: LintReport) -> str:
    """JSON 형식 보고서 생성"""
    data = {
        "files_checked": report.files_checked,
        "total_violations": len(report.violations),
        "errors": sum(1 for v in report.violations if v.severity == "ERROR"),
        "warnings": sum(1 for v in report.violations if v.severity == "WARNING"),
        "violations": [asdict(v) for v in report.violations],
        "skipped_dirs": report.skipped_dirs,
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


# ──────────────────────────────────────────────
# 규칙 레지스트리
# ──────────────────────────────────────────────

# 내장 규칙 레지스트리 (에이전트가 참조용으로 사용)
BUILTIN_RULES = {
    "FILE-001": "파일명 kebab-case 위반",
    "FILE-003": "파일 접미사 규칙 위반",
    "IMP-001":  "임포트 순서 위반 (stdlib → third-party → local)",
    "IMP-002":  "상대 경로 임포트 사용 (Python)",
    "IMP-004":  "와일드카드(*) 임포트 사용",
    "SIZE-001": "파일 라인 수 초과",
    "STYLE-001": "TypeScript 'any' 타입 사용",
    "STYLE-002": "Python 함수 타입 힌트 누락",
    "STYLE-003": "Public 함수/클래스 docstring 누락",
    "SEC-001":  "하드코딩 시크릿 감지",
    "ARCH-001": "의존성 방향 위반 (하위→상위 레이어)",
    "ARCH-002": "레이어 스킵 (UI→Repository 직접 참조)",
    "ANTI-001": "print()/console.log 사용",
    "ANTI-002": "eval()/exec() 사용",
    "ANTI-003": "type: ignore / @ts-ignore 사용",
    "ANTI-004": "하드코딩 URL/포트 감지",
    "SVELTE-001": 'Svelte <script> 블록 lang="ts" 미선언',
    "SVELTE-002": "Svelte 'export let' (Svelte 4 레거시) 사용",
    "SVELTE-003": "Svelte '$:' (Svelte 4 레거시) 반응형 선언",
    "SVELTE-004": "Svelte createEventDispatcher 사용",
    "SVELTE-005": "직접 fetch() 호출 (api_router 미사용)",
    "SVELTE-006": "인라인 CSS (style=\"...\") 사용",
    "SVELTE-007": "Svelte 컴포넌트 PascalCase 파일명 위반",
}


def print_rule_registry() -> None:
    """등록된 모든 규칙 목록 출력"""
    print("=" * 55)
    print("  Registered Lint Rules")
    print("=" * 55)
    print()
    print("--- Built-in Rules ---")
    for code, desc in sorted(BUILTIN_RULES.items()):
        print(f"  [{code}] {desc}")
    print()

    # 커스텀 규칙 파일 탐색
    script_dir = Path(__file__).resolve().parent
    custom_file = script_dir.parent / CUSTOM_RULES_FILENAME
    if custom_file.exists():
        try:
            with open(custom_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            rules = data.get("rules", [])
            if rules:
                print("--- Custom Rules ---")
                for r in rules:
                    status = "ON" if r.get("enabled", True) else "OFF"
                    print(f"  [{r.get('code', '?')}] {r.get('description', '?')} ({status})")
                print()
        except (json.JSONDecodeError, KeyError):
            pass
    else:
        print("--- Custom Rules ---")
        print("  (custom_rules.json not found - no custom rules loaded)")
        print()

    print("=" * 55)


# ──────────────────────────────────────────────
# 메인 실행
# ──────────────────────────────────────────────

def main() -> int:
    """메인 엔트리포인트"""
    # Windows 환경에서 cp949 인코딩 오류 방지
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)
        sys.stderr = open(sys.stderr.fileno(), mode="w", encoding="utf-8", buffering=1)

    args = sys.argv[1:]
    output_format = "text"
    target_dirs = []

    # 인자 파싱
    i = 0
    while i < len(args):
        if args[i] == "--format":
            if i + 1 < len(args):
                output_format = args[i + 1]
                i += 2
                continue
        elif args[i] == "--help":
            print(__doc__)
            return 0
        elif args[i] == "--list-rules":
            print_rule_registry()
            return 0
        else:
            target_dirs.append(args[i])
        i += 1

    # 프로젝트 루트 결정 (스크립트 위치 기준)
    script_dir = Path(__file__).resolve().parent
    # .agents/skills/verify-linter-rules/scripts/ → 프로젝트 루트
    project_root = script_dir.parent.parent.parent.parent
    if not (project_root / ".agents").exists():
        # 대안: 현재 작업 디렉토리 사용
        project_root = Path.cwd()

    # 린터 실행
    checker = LintChecker(str(project_root))
    report = checker.run(target_dirs)

    # 결과 출력
    if output_format == "json":
        print(format_json_report(report))
    else:
        print(format_text_report(report, str(project_root)))

    # 종료 코드: ERROR가 있으면 1, WARNING만이면 0
    has_errors = any(v.severity == "ERROR" for v in report.violations)
    return 1 if has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
