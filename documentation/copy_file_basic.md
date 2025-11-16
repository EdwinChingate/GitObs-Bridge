---
class: code
language: Python
---
## Description


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

- 

## Parameters



---

## Input



---

## Output



---

## Functions



---

## Called by


