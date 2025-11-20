---
class: code
language: Python
---
## Description

`copy_repo_to_vault` copies code and documentation files from a repository into an Obsidian project. It prepares helper paths such as `repo_root_path`, `vault_root_path`, `docs_repo`, `docs_vault`, `functions_repo`, `functions_vault`, `template`. It calls `Path`, `replace_code_block`, `shutil` as part of its workflow. The function iterates through runtime collections via `for code_file in _iter_files(functions_repo, LANGUAGE_BY_SUFFIX.keys())` and `for doc_file in docs_repo.rglob('*.md')`.

---
## Code
```Python
"""Copy code and documentation files from a repo into an Obsidian vault project."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Iterable

from .replace_code_block import replace_code_block

LANGUAGE_BY_SUFFIX = {
    ".py": "Python",
    ".js": "JavaScript",
}


def copy_repo_to_vault(
    repo_root: str,
    vault_project_root: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
    copy_mode: str = "code",
    template_path: str | None = None,
) -> None:
    """Copy code and/or documentation files from repo_root into the vault project."""

    def _iter_files(root: Path, extensions: Iterable[str]) -> Iterable[Path]:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in extensions:
                yield path

    def _ensure_doc_from_template(doc_path: Path, template: Path, language: str) -> None:
        template_text = template.read_text(encoding="utf-8")
        updated = template_text.replace("```Python", f"```{language}", 1)
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        doc_path.write_text(updated, encoding="utf-8")

    def _update_doc_code(doc_path: Path, code_text: str, language: str, template: Path) -> None:
        if not doc_path.exists():
            _ensure_doc_from_template(doc_path, template, language)
        replace_code_block(doc_path, code_text, language=language)

    repo_root_path = Path(repo_root)
    vault_root_path = Path(vault_project_root)
    docs_repo = repo_root_path / docs_subfolder
    docs_vault = vault_root_path / docs_subfolder
    functions_repo = repo_root_path / functions_subfolder
    functions_vault = vault_root_path / functions_subfolder
    template = Path(template_path) if template_path else repo_root_path / "DocumentationTemplate.md"

    copy_mode = copy_mode.lower()
    copy_code = copy_mode in {"code", "both"}
    copy_docs = copy_mode in {"docs", "both"}

    if copy_code and functions_repo.exists():
        for code_file in _iter_files(functions_repo, LANGUAGE_BY_SUFFIX.keys()):
            relative = code_file.relative_to(functions_repo)
            destination = functions_vault / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(code_file, destination)

            language = LANGUAGE_BY_SUFFIX.get(code_file.suffix, "text")
            doc_name = f"{code_file.stem}.md"
            doc_path = docs_vault / doc_name
            _update_doc_code(doc_path, code_file.read_text(encoding="utf-8"), language, template)

    if copy_docs and docs_repo.exists():
        for doc_file in docs_repo.rglob("*.md"):
            if doc_file.name.lower() == "documentationtemplate.md":
                continue
            relative = doc_file.relative_to(docs_repo)
            destination = docs_vault / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(doc_file, destination)
```

---
## Key operations

- Constructs `repo_root_path` from `Path(repo_root)`.
- Constructs `vault_root_path` from `Path(vault_project_root)`.
- Constructs `docs_repo` from `repo_root_path / docs_subfolder`.
- Constructs `docs_vault` from `vault_root_path / docs_subfolder`.
- Constructs `functions_repo` from `repo_root_path / functions_subfolder`.
- Constructs `functions_vault` from `vault_root_path / functions_subfolder`.
- Constructs `template` from `Path(template_path) if template_path else repo_root_path / "DocumentationTemplate.md"`.
- Loops via `for code_file in _iter_files(functions_repo, LANGUAGE_BY_SUFFIX.keys())` to process runtime collections.
- Loops via `for doc_file in docs_repo.rglob('*.md')` to process runtime collections.
- Calls `replace_code_block` to delegate work.
- Calls `shutil` to delegate work.

---
## Parameters

- `repo_root`: user supplied argument consumed directly by `copy_repo_to_vault`.
- `vault_project_root`: user supplied argument consumed directly by `copy_repo_to_vault`.
- `docs_subfolder`: user supplied argument consumed directly by `copy_repo_to_vault`.
- `functions_subfolder`: user supplied argument consumed directly by `copy_repo_to_vault`.
- `copy_mode`: user supplied argument consumed directly by `copy_repo_to_vault`.
- `template_path`: user supplied argument consumed directly by `copy_repo_to_vault`.

---
## Input

- `repo_root_path`: derived from `Path(repo_root)` to keep track of resources.
- `vault_root_path`: derived from `Path(vault_project_root)` to keep track of resources.
- `docs_repo`: derived from `repo_root_path / docs_subfolder` to keep track of resources.
- `docs_vault`: derived from `vault_root_path / docs_subfolder` to keep track of resources.
- `functions_repo`: derived from `repo_root_path / functions_subfolder` to keep track of resources.
- `functions_vault`: derived from `vault_root_path / functions_subfolder` to keep track of resources.
- `template`: derived from `Path(template_path) if template_path else repo_root_path / "DocumentationTemplate.md"` to keep track of resources.

---
## Output

- None

---
## Functions

- [`replace_code_block`](replace_code_block.md): helper function invoked inside the workflow.
- `shutil`: helper function invoked inside the workflow.

---
## Called by

- No direct callers detected in this repository snapshot.
