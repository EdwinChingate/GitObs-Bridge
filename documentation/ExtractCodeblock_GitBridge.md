---
class: code
language: Python
---
## Description

`ExtractCodeblock_GitBridge` reads a documentation file and returns the code block contents with its language. It prepares helper paths such as `Path(FileLoc)`. It calls `Path`, `extract_code_block` as part of its workflow.

---
## Code
```Python
"""Wrapper for extracting fenced code blocks from documentation."""

from __future__ import annotations

from pathlib import Path

from .extract_code_block import extract_code_block


def ExtractCodeblock_GitBridge(FileLoc: str, section_header: str = "## Code"):
    """Backward compatible wrapper that returns the code and language as a list."""

    block = extract_code_block(Path(FileLoc), section_header=section_header)
    return [block.code, block.language]
```

---
## Key operations

- Calls `extract_code_block` to delegate work.
- Calls `Path` to delegate work.

---
## Parameters

- `FileLoc`: user supplied argument consumed directly by `ExtractCodeblock_GitBridge`.
- `section_header`: user supplied argument consumed directly by `ExtractCodeblock_GitBridge`.

---
## Input

- `Path(FileLoc)`: derived from `Path(FileLoc)` to keep track of resources.

---
## Output

- `[block.code, block.language]`

---
## Functions

- [`extract_code_block`](extract_code_block.md): helper function invoked inside the workflow.

---
## Called by

- [`Bridge_GitBridge`](Bridge_GitBridge.md) uses this helper.
