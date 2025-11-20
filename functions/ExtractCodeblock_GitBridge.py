
"""Utilities for extracting and updating fenced code blocks inside documentation files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple


@dataclass
class CodeBlock:
    """Represents a fenced code block inside a documentation file."""

    code: str
    language: str
    code_start: int
    code_end: int
    fence_start: int


def _normalize_language(header_line: str) -> str:
    cleaned = header_line.replace("`", "").strip()
    return cleaned or "text"


def _locate_code_block_lines(lines: list[str], section_header: str) -> Tuple[int, int, int, str]:
    """Return indices for code/fence boundaries along with the detected language."""

    section_idx = None
    for idx, line in enumerate(lines):
        if line.strip() == section_header.strip():
            section_idx = idx
            break
    if section_idx is None:
        raise ValueError(f"Section '{section_header}' not found in document")

    language_line_idx = None
    for idx in range(section_idx + 1, len(lines)):
        stripped = lines[idx].strip()
        if stripped.startswith("```"):
            language_line_idx = idx
            language = _normalize_language(stripped)
            break
    if language_line_idx is None:
        raise ValueError("Unable to locate fenced code block after '## Code'")

    code_start = language_line_idx + 1
    code_end = None
    for idx in range(code_start, len(lines)):
        if lines[idx].strip().startswith("```"):
            code_end = idx
            break
    if code_end is None:
        raise ValueError("Code fence not properly terminated in documentation file")

    return code_start, code_end, language_line_idx, language


def extract_code_block(doc_path: Path, section_header: str = "## Code") -> CodeBlock:
    """Extract the fenced code block from *section_header* within *doc_path*."""

    lines = doc_path.read_text(encoding="utf-8").splitlines()
    code_start, code_end, fence_start, language = _locate_code_block_lines(
        lines, section_header
    )
    code = "\n".join(lines[code_start:code_end])
    return CodeBlock(
        code=code,
        language=language,
        code_start=code_start,
        code_end=code_end,
        fence_start=fence_start,
    )


def replace_code_block(doc_path: Path, new_code: str, language: Optional[str] = None) -> None:
    """Replace the `## Code` block inside *doc_path* with *new_code*."""

    text_lines = doc_path.read_text(encoding="utf-8").splitlines()
    block = extract_code_block(doc_path)
    language = language or block.language
    fence_line = f"```{language}" if language else "```"
    new_block_lines = [fence_line, *new_code.rstrip("\n").splitlines(), "```"]
    updated_lines = (
        text_lines[: block.fence_start]
        + new_block_lines
        + text_lines[block.code_end + 1 :]
    )
    doc_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")


def ExtractCodeblock_GitBridge(FileLoc: str, section_header: str = "## Code"):
    """Backward compatible wrapper that returns the code and language as a list."""

    block = extract_code_block(Path(FileLoc), section_header=section_header)
    return [block.code, block.language]


