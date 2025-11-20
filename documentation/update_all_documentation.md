---
class: code
language: Python
---
## Description

`update_all_documentation` walks the documentation folder and rewrites each markdown file using `update_documentation_file`. It prepares helper paths such as `repo_path`, `docs_path`. It calls `Path`, `update_documentation_file` as part of its workflow. The function iterates through runtime collections via `for doc_file in sorted(docs_path.glob('*.md'))`.

---
## Code
```Python
"""Update every documentation file in the repository."""

from __future__ import annotations

from pathlib import Path

from .update_documentation_file import update_documentation_file


def update_all_documentation(
    repo_root: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
) -> None:
    """Update every documentation file under *docs_subfolder*."""

    repo_path = Path(repo_root)
    docs_path = repo_path / docs_subfolder
    for doc_file in sorted(docs_path.glob("*.md")):
        if doc_file.name.lower() == "documentationtemplate.md":
            continue
        update_documentation_file(str(doc_file), repo_root, functions_subfolder=functions_subfolder)
```

---
## Key operations

- Constructs `repo_path` from `Path(repo_root)`.
- Constructs `docs_path` from `repo_path / docs_subfolder`.
- Loops via `for doc_file in sorted(docs_path.glob('*.md'))` to process runtime collections.
- Calls `update_documentation_file` to delegate work.

---
## Parameters

- `repo_root`: user supplied argument consumed directly by `update_all_documentation`.
- `docs_subfolder`: user supplied argument consumed directly by `update_all_documentation`.
- `functions_subfolder`: user supplied argument consumed directly by `update_all_documentation`.

---
## Input

- `repo_path`: derived from `Path(repo_root)` to keep track of resources.
- `docs_path`: derived from `repo_path / docs_subfolder` to keep track of resources.

---
## Output

- None

---
## Functions

- [`update_documentation_file`](update_documentation_file.md): helper function invoked inside the workflow.

---
## Called by

- No direct callers detected in this repository snapshot.
