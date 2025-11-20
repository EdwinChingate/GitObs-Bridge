---
class: code
language: Python
---
## Description

`Bridge_GitBridge` orchestrates the logic described in this module. It prepares helper paths such as `project_root`, `doc_folder`. It calls `ExtractCodeblock_GitBridge`, `FileNotFoundError`, `Path`, `WriteSoftware_GitBridge`, `exists`, `glob`, `lower`, `sorted`, `str` as part of its workflow. The function iterates through runtime collections via `for doc_file in sorted(doc_folder.glob('*.md'))`.

---
## Code
```Python

"""Bridge documentation code blocks with executable files."""

from __future__ import annotations

from pathlib import Path

from .ExtractCodeblock_GitBridge import ExtractCodeblock_GitBridge
from .WriteSoftware_GitBridge import WriteSoftware_GitBridge


def Bridge_GitBridge(
    SoftwareProject: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
) -> None:
    """Sync every documentation code block into the functions directory."""

    project_root = Path(SoftwareProject)
    doc_folder = project_root / docs_subfolder
    if not doc_folder.exists():
        raise FileNotFoundError(f"Documentation folder not found: {doc_folder}")

    for doc_file in sorted(doc_folder.glob("*.md")):
        if doc_file.name.lower() == "documentationtemplate.md":
            continue
        codeblock, language = ExtractCodeblock_GitBridge(FileLoc=str(doc_file))
        WriteSoftware_GitBridge(
            function=doc_file.name,
            SoftwareProject=str(project_root),
            codeblock=codeblock,
            language=language,
            functions_subfolder=functions_subfolder,
        )
```

---
## Key operations

- Constructs `project_root` from `Path(SoftwareProject)`.
- Constructs `doc_folder` from `project_root / docs_subfolder`.
- Loops via `for doc_file in sorted(doc_folder.glob('*.md'))` to process runtime collections.
- Calls `ExtractCodeblock_GitBridge` to delegate work.
- Calls `FileNotFoundError` to delegate work.
- Calls `Path` to delegate work.
- Calls `WriteSoftware_GitBridge` to delegate work.
- Calls `exists` to delegate work.
- Calls `glob` to delegate work.
- Calls `lower` to delegate work.
- Calls `sorted` to delegate work.
- Calls `str` to delegate work.

---
## Parameters

- `SoftwareProject`: used in expressions such as `Path(SoftwareProject)` to derive runtime paths.
- `docs_subfolder`: used in expressions such as `project_root / docs_subfolder` to derive runtime paths.
- `functions_subfolder`: user supplied argument consumed directly by `Bridge_GitBridge`.

---
## Input

- `project_root`: derived from `Path(SoftwareProject)` to keep track of resources.
- `doc_folder`: derived from `project_root / docs_subfolder` to keep track of resources.

---
## Output

- None

---
## Functions

- [ExtractCodeblock_GitBridge](ExtractCodeblock_GitBridge.md): extracts fenced code blocks and metadata from markdown documentation.
- `FileNotFoundError`: helper function invoked inside the workflow.
- `Path`: helper function invoked inside the workflow.
- [WriteSoftware_GitBridge](WriteSoftware_GitBridge.md): writes extracted code to the project's functions directory.
- `exists`: helper function invoked inside the workflow.
- `glob`: helper function invoked inside the workflow.
- `lower`: helper function invoked inside the workflow.
- `sorted`: helper function invoked inside the workflow.
- `str`: helper function invoked inside the workflow.

---
## Called by

- [GitObs-Bridge_GitBridge](GitObs-Bridge_GitBridge.md) uses this helper.
- [GitObs_GitBridge](GitObs_GitBridge.md) uses this helper.
