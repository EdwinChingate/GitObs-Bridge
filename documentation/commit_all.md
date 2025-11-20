---
class: code
language:
---
## Description

`commit_all` orchestrates the logic described in this module. It prepares helper paths such as `repo_path`, `log_path`. It calls `Path`, `Repo`, `add`, `commit`, `isoformat`, `now`, `open`, `print`, `write` as part of its workflow.

---
## Code
```Python
from pathlib import Path
from git import Repo
from datetime import datetime

def commit_all(project_folder: str, message: str, log_file: str | None = None):
    repo_path = Path(project_folder)
    repo = Repo(repo_path)

    repo.git.add(A=True)
    commit = repo.index.commit(message)
    commit_id = commit.hexsha

    print(f"Committed: {commit_id}")

    if log_file:
        log_path = repo_path / log_file
        timestamp = datetime.now().isoformat(timespec="seconds")
        with log_path.open("a", encoding="utf-8") as f:
            f.write(f"{timestamp} {commit_id} {message}\n")

    return commit_id
```

---
## Key operations

- Constructs `repo_path` from `Path(project_folder)`.
- Constructs `log_path` from `repo_path / log_file`.
- Calls `Path` to delegate work.
- Calls `Repo` to delegate work.
- Calls `add` to delegate work.
- Calls `commit` to delegate work.
- Calls `isoformat` to delegate work.
- Calls `now` to delegate work.
- Calls `open` to delegate work.
- Calls `print` to delegate work.
- Calls `write` to delegate work.

---
## Parameters

- `project_folder`: used in expressions such as `Path(project_folder)` to derive runtime paths.
- `message`: used in expressions such as `repo.index.commit(message)` to derive runtime paths.
- `log_file`: used in expressions such as `repo_path / log_file` to derive runtime paths.

---
## Input

- `repo_path`: derived from `Path(project_folder)` to keep track of resources.
- `log_path`: derived from `repo_path / log_file` to keep track of resources.

---
## Output

- `commit_id`

---
## Functions

- `Path`: helper function invoked inside the workflow.
- `Repo`: helper function invoked inside the workflow.
- `add`: helper function invoked inside the workflow.
- `commit`: helper function invoked inside the workflow.
- `isoformat`: helper function invoked inside the workflow.
- `now`: helper function invoked inside the workflow.
- `open`: helper function invoked inside the workflow.
- `print`: helper function invoked inside the workflow.
- `write`: helper function invoked inside the workflow.

---
## Called by

- [ReadBashRun_GitBridge](ReadBashRun_GitBridge.md) uses this helper.
