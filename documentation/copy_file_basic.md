---
class: code
language: Python
---
## Description

`copy_file_basic` orchestrates the logic described in this module. It calls `Path`, `open`, `read`, `write` as part of its workflow.

---
## Code
```Python
from pathlib import Path
import os

def copy_file_basic(src, dst, chunk_size=1024 * 1024):
    """Copy bytes manually without shutil."""
    src = Path(src)
    dst = Path(dst)

    with src.open("rb") as f_src, dst.open("wb") as f_dst:
        while True:
            chunk = f_src.read(chunk_size)
            if not chunk:
                break
            f_dst.write(chunk)
```

---
## Key operations

- Calls `Path` to delegate work.
- Calls `open` to delegate work.
- Calls `read` to delegate work.
- Calls `write` to delegate work.

---
## Parameters

- `src`: used in expressions such as `Path(src)` to derive runtime paths.
- `dst`: used in expressions such as `Path(dst)` to derive runtime paths.
- `chunk_size`: used in expressions such as `f_src.read(chunk_size)` to derive runtime paths.

---
## Input

- None

---
## Output

- None

---
## Functions

- `Path`: helper function invoked inside the workflow.
- `open`: helper function invoked inside the workflow.
- `read`: helper function invoked inside the workflow.
- `write`: helper function invoked inside the workflow.

---
## Called by

- [copy_dir_basic](copy_dir_basic.md) uses this helper.
- [copy_folder_contents](copy_folder_contents.md) uses this helper.
