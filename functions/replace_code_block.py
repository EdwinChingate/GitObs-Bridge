"""Replace the code block inside a documentation file."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from .extract_code_block import extract_code_block


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
