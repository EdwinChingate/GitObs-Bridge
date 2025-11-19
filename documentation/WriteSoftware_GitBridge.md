---
class: code
language: Python
---
## Description

`WriteSoftware_GitBridge` orchestrates the logic described in this module. It prepares helper paths such as `project_root`, `coding_folder`, `filename`, `file_path`. It calls `Path`, `ValueError`, `get`, `lower`, `mkdir`, `with_suffix`, `write_text` as part of its workflow.

---
## Code
```Python

"""Write code that was extracted from documentation into the functions directory."""

from __future__ import annotations

from pathlib import Path
from typing import Dict


LANGUAGE_EXTENSIONS: Dict[str, str] = {
    "python": "py",
    "Python": "py",
    "javascript": "js",
    "JavaScript": "js",
    "bash": "sh",
    "markdown": "md",
}


def WriteSoftware_GitBridge(
    function: str,
    SoftwareProject: str,
    codeblock: str,
    language: str,
    functions_subfolder: str = "functions",
) -> Path | None:
    """Write the provided *codeblock* to the matching file inside *functions_subfolder*."""

    if language.lower() == "markdown":
        return None

    project_root = Path(SoftwareProject)
    coding_folder = project_root / functions_subfolder
    coding_folder.mkdir(parents=True, exist_ok=True)

    extension = LANGUAGE_EXTENSIONS.get(language, LANGUAGE_EXTENSIONS.get(language.lower()))
    if not extension:
        raise ValueError(f"Unsupported language '{language}' in documentation block")

    filename = Path(function).with_suffix(f".{extension}").name
    file_path = coding_folder / filename
    file_path.write_text(codeblock, encoding="utf-8")
    return file_path
```

---
## Key operations

- Constructs `project_root` from `Path(SoftwareProject)`.
- Constructs `coding_folder` from `project_root / functions_subfolder`.
- Constructs `filename` from `Path(function).with_suffix(f'.{extension}').name`.
- Constructs `file_path` from `coding_folder / filename`.
- Calls `Path` to delegate work.
- Calls `ValueError` to delegate work.
- Calls `get` to delegate work.
- Calls `lower` to delegate work.
- Calls `mkdir` to delegate work.
- Calls `with_suffix` to delegate work.
- Calls `write_text` to delegate work.

---
## Parameters

- `function`: used in expressions such as `Path(function).with_suffix(f'.{extension}').name` to derive runtime paths.
- `SoftwareProject`: used in expressions such as `Path(SoftwareProject)` to derive runtime paths.
- `codeblock`: user supplied argument consumed directly by `WriteSoftware_GitBridge`.
- `language`: used in expressions such as `LANGUAGE_EXTENSIONS.get(language, LANGUAGE_EXTENSIONS.get(language.lower()))` to derive runtime paths.
- `functions_subfolder`: used in expressions such as `project_root / functions_subfolder` to derive runtime paths.

---
## Input

- `project_root`: derived from `Path(SoftwareProject)` to keep track of resources.
- `coding_folder`: derived from `project_root / functions_subfolder` to keep track of resources.
- `filename`: derived from `Path(function).with_suffix(f'.{extension}').name` to keep track of resources.
- `file_path`: derived from `coding_folder / filename` to keep track of resources.

---
## Output

- `None`
- `file_path`

---
## Functions

- `Path`: helper function invoked inside the workflow.
- `ValueError`: helper function invoked inside the workflow.
- `get`: helper function invoked inside the workflow.
- `lower`: helper function invoked inside the workflow.
- `mkdir`: helper function invoked inside the workflow.
- `with_suffix`: helper function invoked inside the workflow.
- `write_text`: helper function invoked inside the workflow.

---
## Called by

- [Bridge_GitBridge](Bridge_GitBridge.md) uses this helper.
