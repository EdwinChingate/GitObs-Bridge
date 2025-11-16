---
class: code
language:
---
## Description


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


