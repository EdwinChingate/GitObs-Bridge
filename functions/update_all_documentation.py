"""Update every documentation file in the repository."""

from __future__ import annotations

from pathlib import Path

from .update_documentation_file import update_documentation_file


def update_all_documentation(
    repo_root: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
) -> None:
    """Update every documentation file under *docs_subfolder*."""

    repo_path = Path(repo_root)
    docs_path = repo_path / docs_subfolder
    for doc_file in sorted(docs_path.glob("*.md")):
        if doc_file.name.lower() == "documentationtemplate.md":
            continue
        update_documentation_file(str(doc_file), repo_root, functions_subfolder=functions_subfolder)
