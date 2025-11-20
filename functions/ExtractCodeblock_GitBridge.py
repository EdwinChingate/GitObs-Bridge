"""Wrapper for extracting fenced code blocks from documentation."""

from __future__ import annotations

from pathlib import Path

from .extract_code_block import extract_code_block


def ExtractCodeblock_GitBridge(FileLoc: str, section_header: str = "## Code"):
    """Backward compatible wrapper that returns the code and language as a list."""

    block = extract_code_block(Path(FileLoc), section_header=section_header)
    return [block.code, block.language]
