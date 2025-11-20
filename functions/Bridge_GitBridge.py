
"""Bridge documentation code blocks with executable files."""

from __future__ import annotations

from pathlib import Path

from .ExtractCodeblock_GitBridge import ExtractCodeblock_GitBridge
from .WriteSoftware_GitBridge import WriteSoftware_GitBridge


def Bridge_GitBridge(
    SoftwareProject: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
) -> None:
    """Sync every documentation code block into the functions directory."""

    project_root = Path(SoftwareProject)
    doc_folder = project_root / docs_subfolder
    if not doc_folder.exists():
        raise FileNotFoundError(f"Documentation folder not found: {doc_folder}")

    for doc_file in sorted(doc_folder.glob("*.md")):
        if doc_file.name.lower() == "documentationtemplate.md":
            continue
        codeblock, language = ExtractCodeblock_GitBridge(FileLoc=str(doc_file))
        WriteSoftware_GitBridge(
            function=doc_file.name,
            SoftwareProject=str(project_root),
            codeblock=codeblock,
            language=language,
            functions_subfolder=functions_subfolder,
        )

