
"""Write code that was extracted from documentation into the functions directory."""

from __future__ import annotations

from pathlib import Path
from typing import Dict


LANGUAGE_EXTENSIONS: Dict[str, str] = {
    "python": "py",
    "Python": "py",
    "javascript": "js",
    "JavaScript": "js",
    "bash": "sh",
    "markdown": "md",
}


def WriteSoftware_GitBridge(
    function: str,
    SoftwareProject: str,
    codeblock: str,
    language: str,
    functions_subfolder: str = "functions",
) -> Path | None:
    """Write the provided *codeblock* to the matching file inside *functions_subfolder*."""

    if language.lower() == "markdown":
        return None

    project_root = Path(SoftwareProject)
    coding_folder = project_root / functions_subfolder
    coding_folder.mkdir(parents=True, exist_ok=True)

    extension = LANGUAGE_EXTENSIONS.get(language, LANGUAGE_EXTENSIONS.get(language.lower()))
    if not extension:
        raise ValueError(f"Unsupported language '{language}' in documentation block")

    filename = Path(function).with_suffix(f".{extension}").name
    file_path = coding_folder / filename
    file_path.write_text(codeblock, encoding="utf-8")
    return file_path

