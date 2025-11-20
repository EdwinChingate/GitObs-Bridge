---
class: code
language: Python
---
## Description

`replace_code_block` overwrites the code fence inside a documentation file with new content. It prepares helper paths such as `text_lines`. It calls `Path`, `extract_code_block` as part of its workflow.

---
## Code
```Python
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
```

---
## Key operations

- Constructs `text_lines` from `doc_path.read_text(encoding="utf-8").splitlines()`.
- Calls `extract_code_block` to delegate work.
- Calls `Path` to delegate work.

---
## Parameters

- `doc_path`: user supplied argument consumed directly by `replace_code_block`.
- `new_code`: user supplied argument consumed directly by `replace_code_block`.
- `language`: user supplied argument consumed directly by `replace_code_block`.

---
## Input

- `text_lines`: derived from `doc_path.read_text(encoding="utf-8").splitlines()` to keep track of resources.

---
## Output

- None

---
## Functions

- [`extract_code_block`](extract_code_block.md): helper function invoked inside the workflow.

---
## Called by

- [`copy_repo_to_vault`](copy_repo_to_vault.md) uses this helper.
- [`check_and_format_doc_codeblock`](check_and_format_doc_codeblock.md) uses this helper.
