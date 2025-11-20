"""Sync helper that copies repo files into an Obsidian vault project."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Iterable

from .ExtractCodeblock_GitBridge import replace_code_block

LANGUAGE_BY_SUFFIX = {
    ".py": "Python",
    ".js": "JavaScript",
}


def _iter_files(root: Path, extensions: Iterable[str]) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in extensions:
            yield path


def _ensure_doc_from_template(doc_path: Path, template_path: Path, language: str) -> None:
    template_text = template_path.read_text(encoding="utf-8")
    updated = template_text.replace("```Python", f"```{language}", 1)
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(updated, encoding="utf-8")


def _update_doc_code(doc_path: Path, code_text: str, language: str, template_path: Path) -> None:
    if not doc_path.exists():
        _ensure_doc_from_template(doc_path, template_path, language)
    replace_code_block(doc_path, code_text, language=language)


def copy_repo_to_vault(
    repo_root: str,
    vault_project_root: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
    copy_mode: str = "code",
    template_path: str | None = None,
) -> None:
    """Copy code and/or documentation files from repo_root into the vault project."""

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
