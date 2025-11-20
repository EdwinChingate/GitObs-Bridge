---
class: code
language:
---
## Description

`copy_dir_basic` orchestrates the logic described in this module. It prepares helper paths such as `src_dir`, `dst_dir`. It calls `Path`, `copy_dir_basic`, `copy_file_basic`, `is_dir`, `is_file`, `iterdir`, `mkdir` as part of its workflow. The function iterates through runtime collections via `for item in src_dir.iterdir()`.

---
## Code
```Python
from pathlib import Path
import os
def copy_dir_basic(src_dir, dst_dir):
    """Recursively copy a directory without shutil."""
    src_dir = Path(src_dir)
    dst_dir = Path(dst_dir)

    dst_dir.mkdir(parents=True, exist_ok=True)

    for item in src_dir.iterdir():
        target = dst_dir / item.name

        if item.is_file():
            copy_file_basic(item, target)
        elif item.is_dir():
            copy_dir_basic(item, target)
```

---
## Key operations

- Constructs `src_dir` from `Path(src_dir)`.
- Constructs `dst_dir` from `Path(dst_dir)`.
- Loops via `for item in src_dir.iterdir()` to process runtime collections.
- Calls `Path` to delegate work.
- Calls `copy_dir_basic` to delegate work.
- Calls `copy_file_basic` to delegate work.
- Calls `is_dir` to delegate work.
- Calls `is_file` to delegate work.
- Calls `iterdir` to delegate work.
- Calls `mkdir` to delegate work.

---
## Parameters

- `src_dir`: used in expressions such as `Path(src_dir)` to derive runtime paths.
- `dst_dir`: used in expressions such as `Path(dst_dir)` to derive runtime paths.

---
## Input

- `src_dir`: derived from `Path(src_dir)` to keep track of resources.
- `dst_dir`: derived from `Path(dst_dir)` to keep track of resources.

---
## Output

- None

---
## Functions

- `Path`: helper function invoked inside the workflow.
- [copy_dir_basic](copy_dir_basic.md): copies an entire directory tree to a destination.
- [copy_file_basic](copy_file_basic.md): performs a direct shutil.copy style file transfer between two paths.
- `is_dir`: helper function invoked inside the workflow.
- `is_file`: helper function invoked inside the workflow.
- `iterdir`: helper function invoked inside the workflow.
- `mkdir`: helper function invoked inside the workflow.

---
## Called by

- [copy_folder_contents](copy_folder_contents.md) uses this helper.
