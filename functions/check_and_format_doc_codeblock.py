"""Format and optionally rewrite documentation code blocks."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Dict, Optional

try:  # pragma: no cover - import optional
    import autopep8  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover
    raise ModuleNotFoundError(
        "autopep8 is required for check_and_format_doc_codeblock; install it first"
    ) from exc

from .extract_code_block import CodeBlock, extract_code_block
from .replace_code_block import replace_code_block


def check_and_format_doc_codeblock(doc_path: str, apply_changes: bool = False) -> Dict[str, object]:
    """Extract, format, and optionally rewrite the code block inside *doc_path*."""

    def _run_subprocess(command: list[str], *, input_text: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            command,
            input=input_text,
            text=True,
            capture_output=True,
            check=False,
        )

    def _format_python(code: str) -> tuple[str, bool, Optional[str]]:
        formatted = autopep8.fix_code(code, options={"aggressive": 2})
        try:
            compile(formatted, "<doc-code>", "exec")
            return formatted, True, None
        except SyntaxError as exc:  # pragma: no cover - depends on doc content
            return formatted, False, f"SyntaxError: {exc}"

    def _fallback_js_formatter(code: str) -> str:
        cleaned_lines = []
        indent_level = 0
        for raw_line in code.splitlines():
            line = raw_line.strip()
            if line.endswith("}"):
                indent_level = max(indent_level - 1, 0)
            cleaned_lines.append("    " * indent_level + line)
            if line.endswith("{"):
                indent_level += 1
        return "\n".join(cleaned_lines) + ("\n" if code.endswith("\n") else "")

    def _format_js(code: str) -> tuple[str, bool, Optional[str]]:
        prettier = shutil.which("prettier")
        if prettier:
            result = _run_subprocess([prettier, "--parser", "babel"], input_text=code)
            if result.returncode == 0:
                formatted = result.stdout
            else:
                return code, False, result.stderr.strip() or "prettier formatting failed"
        else:
            formatted = _fallback_js_formatter(code)

        node = shutil.which("node")
        if node:
            check = _run_subprocess([node, "--check"], input_text=formatted)
            if check.returncode != 0:
                return formatted, False, check.stderr.strip() or check.stdout.strip()
        return formatted, True, None

    path = Path(doc_path)
    block: CodeBlock = extract_code_block(path)
    language = block.language.lower()

    if language in {"python", "py"}:
        formatted, syntax_ok, syntax_error = _format_python(block.code)
        reported_language = "Python"
    elif language in {"javascript", "js"}:
        formatted, syntax_ok, syntax_error = _format_js(block.code)
        reported_language = "JavaScript"
    else:
        formatted, syntax_ok, syntax_error = block.code, True, None
        reported_language = block.language

    if apply_changes and formatted != block.code:
        replace_code_block(path, formatted, language=reported_language)

    return {
        "language": reported_language,
        "formatted_code": formatted,
        "syntax_ok": syntax_ok,
        "syntax_error": syntax_error,
    }
