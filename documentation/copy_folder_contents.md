---
class: code
language: Python
---
## Description

`copy_folder_contents` orchestrates the logic described in this module. It calls `Path`, `WritingDebug`, `copy_dir_basic`, `copy_file_basic`, `is_dir`, `is_file`, `iterdir`, `mkdir` as part of its workflow. The function iterates through runtime collections via `for item in source.iterdir()`.

---
## Code
```Python
from pathlib import Path
import os
from copy_file_basic import *
from copy_dir_basic import *
from WritingDebug import *
def copy_folder_contents(source_folder, destination_folder, recursive=False):
    source = Path(source_folder)
    destination = Path(destination_folder)
    destination.mkdir(parents=True, exist_ok=True)
    WritingDebug(source_folder)
    for item in source.iterdir():
        # Skip directories if not recursive
        if item.is_dir() and not recursive:
            continue

        # Copy file
        if item.is_file():
            target = destination / item.name
            copy_file_basic(item, target)

        # Copy directories (only if recursive)
        elif item.is_dir() and recursive:
            copy_dir_basic(item, destination / item.name)
```

---
## Key operations

- Loops via `for item in source.iterdir()` to process runtime collections.
- Calls `Path` to delegate work.
- Calls `WritingDebug` to delegate work.
- Calls `copy_dir_basic` to delegate work.
- Calls `copy_file_basic` to delegate work.
- Calls `is_dir` to delegate work.
- Calls `is_file` to delegate work.
- Calls `iterdir` to delegate work.
- Calls `mkdir` to delegate work.

---
## Parameters

- `source_folder`: used in expressions such as `Path(source_folder)` to derive runtime paths.
- `destination_folder`: used in expressions such as `Path(destination_folder)` to derive runtime paths.
- `recursive`: user supplied argument consumed directly by `copy_folder_contents`.

---
## Input

- None

---
## Output

- None

---
## Functions

- `Path`: helper function invoked inside the workflow.
- `WritingDebug`: helper function invoked inside the workflow.
- [copy_dir_basic](copy_dir_basic.md): copies an entire directory tree to a destination.
- [copy_file_basic](copy_file_basic.md): performs a direct shutil.copy style file transfer between two paths.
- `is_dir`: helper function invoked inside the workflow.
- `is_file`: helper function invoked inside the workflow.
- `iterdir`: helper function invoked inside the workflow.
- `mkdir`: helper function invoked inside the workflow.

---
## Called by

- [ReadBashRun_GitBridge](ReadBashRun_GitBridge.md) uses this helper.
- [copy_folder_contents_old](copy_folder_contents_old.md) uses this helper.
