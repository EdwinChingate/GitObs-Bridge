---
class: code
language: Python
---
## Description

`copy_folder_contents` orchestrates the logic described in this module. It calls `Path`, `ValueError`, `copy2`, `copytree`, `exists`, `is_dir`, `is_file`, `iterdir`, `mkdir` as part of its workflow. The function iterates through runtime collections via `for item in source.iterdir()`.

---
## Code
```Python
from pathlib import Path
import shutil

def copy_folder_contents(source_folder, destination_folder, recursive=False):
    destination = Path(destination_folder)
    source = Path(source_folder)
    if not source.exists():
        raise ValueError(f"Source folder does not exist: {source}")

    destination.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        # Only copy files if recursive=False
        if item.is_dir() and not recursive:
            continue

        if item.is_file():
            shutil.copy2(item, destination / item.name)
        elif item.is_dir() and recursive:
            shutil.copytree(
                item,
                destination / item.name,
                dirs_exist_ok=True,
            )
```

---
## Key operations

- Loops via `for item in source.iterdir()` to process runtime collections.
- Calls `Path` to delegate work.
- Calls `ValueError` to delegate work.
- Calls `copy2` to delegate work.
- Calls `copytree` to delegate work.
- Calls `exists` to delegate work.
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
- `ValueError`: helper function invoked inside the workflow.
- `copy2`: helper function invoked inside the workflow.
- `copytree`: helper function invoked inside the workflow.
- `exists`: helper function invoked inside the workflow.
- `is_dir`: helper function invoked inside the workflow.
- `is_file`: helper function invoked inside the workflow.
- `iterdir`: helper function invoked inside the workflow.
- `mkdir`: helper function invoked inside the workflow.

---
## Called by

- [ReadBashRun_GitBridge](ReadBashRun_GitBridge.md) uses this helper.
- [copy_folder_contents](copy_folder_contents.md) uses this helper.
