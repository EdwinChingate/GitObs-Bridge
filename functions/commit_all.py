
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


