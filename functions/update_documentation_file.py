"""Fill documentation sections for a single markdown file."""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List

from .extract_code_block import CodeBlock, extract_code_block


SECTION_ORDER = [
    "Description",
    "Code",
    "Key operations",
    "Parameters",
    "Input",
    "Output",
    "Functions",
    "Called by",
]

KNOWN_FUNCTION_BEHAVIORS = {
    "ExtractCodeblock_GitBridge": "extracts fenced code blocks and metadata from markdown documentation.",
    "WriteSoftware_GitBridge": "writes extracted code to the project's functions directory.",
    "Bridge_GitBridge": "iterates over documentation files and mirrors their code blocks into executable files.",
    "copy_file_basic": "performs a direct shutil.copy style file transfer between two paths.",
    "copy_dir_basic": "copies an entire directory tree to a destination.",
    "copy_folder_contents": "moves every file from a source directory into a destination, creating folders when needed.",
    "ReadBashRun_GitBridge": "opens bash scripts, runs them, and captures their output.",
    "commit_all": "stages repository changes and commits them with a generated message.",
}


@dataclass
class FunctionInfo:
    name: str
    parameters: List[str] = field(default_factory=list)
    called_functions: List[str] = field(default_factory=list)
    loops: List[str] = field(default_factory=list)
    assignments: Dict[str, str] = field(default_factory=dict)
    parameter_usages: Dict[str, List[str]] = field(default_factory=dict)
    return_values: List[str] = field(default_factory=list)


def update_documentation_file(
    doc_path: str,
    repo_root: str,
    functions_subfolder: str = "functions",
) -> Dict[str, str]:
    """Fill documentation sections for a single markdown file."""

    def _contains_name(node: ast.AST, target: str) -> bool:
        return any(isinstance(child, ast.Name) and child.id == target for child in ast.walk(node))

    class _FunctionAnalyzer(ast.NodeVisitor):
        def __init__(self, func: ast.FunctionDef):
            self.info = FunctionInfo(
                name=func.name,
                parameters=[arg.arg for arg in func.args.args],
                parameter_usages={arg.arg: [] for arg in func.args.args},
            )

        # pylint: disable=invalid-name
        def visit_Call(self, node: ast.Call):  # pragma: no cover - AST traversal
            if isinstance(node.func, ast.Name):
                self.info.called_functions.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                self.info.called_functions.append(node.func.attr)
            self.generic_visit(node)

        def visit_For(self, node: ast.For):  # pragma: no cover - AST traversal
            try:
                loop_desc = f"for {ast.unparse(node.target)} in {ast.unparse(node.iter)}"
            except Exception:  # pragma: no cover
                loop_desc = "for <iterable>"
            self.info.loops.append(loop_desc)
            self.generic_visit(node)

        def visit_Assign(self, node: ast.Assign):  # pragma: no cover
            if isinstance(node.targets[0], ast.Name):
                target_name = node.targets[0].id
                target_lower = target_name.lower()
                if any(key in target_lower for key in ("folder", "dir", "path", "file", "root")):
                    try:
                        self.info.assignments[target_name] = ast.unparse(node.value)
                    except Exception:
                        self.info.assignments[target_name] = "expression"
            for param in list(self.info.parameter_usages.keys()):
                if _contains_name(node.value, param):
                    try:
                        expression = ast.unparse(node.value)
                    except Exception:  # pragma: no cover
                        expression = "expression"
                    self.info.parameter_usages[param].append(expression)
            self.generic_visit(node)

        def visit_Return(self, node: ast.Return):  # pragma: no cover
            if node.value is None:
                self.info.return_values.append("None")
            else:
                try:
                    self.info.return_values.append(ast.unparse(node.value))
                except Exception:
                    self.info.return_values.append("value")
            self.generic_visit(node)

    def _parse_first_function(code: str, preferred_name: str | None = None) -> ast.FunctionDef | None:
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return None
        if preferred_name:
            for node in tree.body:
                if isinstance(node, ast.FunctionDef) and node.name == preferred_name:
                    return node
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                return node
        return None

    def _format_description(info: FunctionInfo) -> str:
        parts = [f"`{info.name}` orchestrates the logic described in this module."]
        if info.assignments:
            parts.append(
                "It prepares helper paths such as "
                + ", ".join(f"`{name}`" for name in info.assignments.keys())
                + "."
            )
        if info.called_functions:
            callers = ", ".join(f"`{name}`" for name in sorted(set(info.called_functions)))
            parts.append(f"It calls {callers} as part of its workflow.")
        if info.loops:
            parts.append(
                "The function iterates through runtime collections via "
                + ", ".join(f"`{loop}`" for loop in info.loops)
                + "."
            )
        return " ".join(parts)

    def _format_list_section(items: Iterable[str]) -> str:
        materialized = [item for item in items if item]
        if not materialized:
            return "- None"
        return "\n".join(f"- {item}" for item in materialized)

    def _parameter_lines(info: FunctionInfo) -> List[str]:
        lines = []
        for param in info.parameters:
            usage = info.parameter_usages.get(param)
            if usage:
                lines.append(
                    f"`{param}`: used in expressions such as `{usage[0]}` to derive runtime paths."
                )
            else:
                lines.append(f"`{param}`: user supplied argument consumed directly by `{info.name}`.")
        return lines

    def _input_lines(info: FunctionInfo) -> List[str]:
        lines = []
        for name, expr in info.assignments.items():
            lines.append(f"`{name}`: derived from `{expr}` to keep track of resources.")
        return lines

    def _output_lines(info: FunctionInfo) -> List[str]:
        if not info.return_values:
            return ["None"]
        return [f"`{value}`" for value in info.return_values]

    def _function_lines(info: FunctionInfo) -> List[str]:
        lines = []
        for call in sorted(set(info.called_functions)):
            description = KNOWN_FUNCTION_BEHAVIORS.get(call, "helper function invoked inside the workflow.")
            if call in KNOWN_FUNCTION_BEHAVIORS:
                lines.append(f"[{call}]({call}.md): {description}")
            else:
                lines.append(f"`{call}`: {description}")
        return lines

    def _find_callers(function_name: str, repo_root_path: Path, current_file: Path) -> List[str]:
        pattern = re.compile(rf"\b{re.escape(function_name)}\s*\(")
        callers: List[str] = []
        for py_file in repo_root_path.rglob("*.py"):
            if py_file == current_file:
                continue
            text = py_file.read_text(encoding="utf-8")
            if pattern.search(text):
                callers.append(py_file.stem)
        return sorted(set(callers))

    def _caller_lines(callers: List[str]) -> List[str]:
        if not callers:
            return ["No direct callers detected in this repository snapshot."]
        return [f"[{caller}]({caller}.md) uses this helper." for caller in callers]

    def _build_sections(info: FunctionInfo, repo_root_path: Path, code_path: Path) -> Dict[str, str]:
        callers = _find_callers(info.name, repo_root_path, code_path)
        sections = {
            "Description": _format_description(info),
            "Key operations": _format_list_section(
                [
                    *(f"Constructs `{name}` from `{expr}`." for name, expr in info.assignments.items()),
                    *(f"Loops via `{loop}` to process runtime collections." for loop in info.loops),
                    *(
                        f"Calls `{call}` to delegate work."
                        for call in sorted(set(info.called_functions))
                    ),
                ]
            ),
            "Parameters": _format_list_section(_parameter_lines(info)),
            "Input": _format_list_section(_input_lines(info)),
            "Output": _format_list_section(_output_lines(info)),
            "Functions": _format_list_section(_function_lines(info)),
            "Called by": _format_list_section(_caller_lines(callers)),
        }
        return sections

    def _compose_document(preamble: str, block: CodeBlock, sections: Dict[str, str]) -> str:
        parts: List[str] = []
        if preamble.strip():
            parts.append(preamble.strip())

        def _section(header: str, body: str) -> str:
            return f"## {header}\n\n{body.strip()}\n"

        for header in SECTION_ORDER:
            if header == "Code":
                code_block = "\n".join(
                    ["## Code", f"```{block.language}", block.code.rstrip("\n"), "```", ""]
                )
                parts.append(code_block)
            else:
                parts.append(_section(header, sections.get(header, "- None")))
            if header != "Called by":
                parts.append("---")
        return "\n".join(parts).strip() + "\n"

    path = Path(doc_path)
    repo_path = Path(repo_root)
    code_path = repo_path / functions_subfolder / f"{path.stem}.py"
    if not code_path.exists():
        return {}

    block = extract_code_block(path)
    func = _parse_first_function(block.code, preferred_name=path.stem)
    if func is None:
        return {}
    analyzer = _FunctionAnalyzer(func)
    analyzer.visit(func)
    sections = _build_sections(analyzer.info, repo_path, code_path)

    text = path.read_text(encoding="utf-8")
    first_section_idx = text.find("## ")
    preamble = text[:first_section_idx].strip() if first_section_idx != -1 else text.strip()
    new_doc = _compose_document(preamble, block, sections)
    path.write_text(new_doc, encoding="utf-8")
    return sections
