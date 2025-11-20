---
title: Codex Agents for GitObs-Bridge
kind: meta
source: documentation/Agents.md
last_updated: 2025-11-19
---

# Codex Agents Configuration for the GitObs-Bridge Repository

This file defines **how Codex should operate** when handling tasks related to this repository.

It does **not** describe software “agents” in Obsidian.  
Instead, it declares **Codex modes** that govern:

- bidirectional syncing between Vault ↔ Repo,  
- code-block extraction and formatting,  
- documentation generation from templates,  
- code & file structure refactors,  
- long-term planning of the bridge architecture,  
- conceptual explanations of how the system works.

Whenever working inside this repository, Codex must:

1. **Follow `Prompt_CodexDocumentation.md` if the task involves documentation.**  
2. **Follow the semantic and architectural rules in this Agents.md for all tasks.**

---

## 1. Global Principles (Apply to ALL Modes)

These rules are universal:

1. **Respect the GitObs-Bridge Semantics**  
   - This repository’s purpose is to **connect an Obsidian Vault with an external GitHub repository**, synchronizing:
     - documentation files (`documentation/*.md`)  
     - code blocks inside those markdown files  
     - actual code files (`functions/*.py`, `.js`, etc.)  
   - You must not break the bridge invariants:
     - Code blocks and code files must correspond.  
     - Round-trip Vault → Repo → Vault must be consistent.  
     - No silent code overwrites without explicit logic.

2. **Always Externalize Paths & Parameters**  
   - Paths MUST NOT be hard-coded.  
   - Any sync function must accept explicit parameters:
     - `vault_project_root`
     - `repo_root`
     - `docs_subfolder`
     - `functions_subfolder`
   - Default values may exist, but parameters must always be explicit in the API.

3. **Use Language-Appropriate Formatters**  
   - For Python code in documentation → use **autopep8**.  
   - For JavaScript → use Prettier (or minimal indentation fallback if unavailable).  
   - For Bash → normalize indentation and command alignment.  
   - No destructive changes to logic; only formatting and clarity fixes.

4. **Documentation Means Documentation**  
   - When asked to update docs:
     - Apply `DocumentationTemplate.md`.  
     - Fill missing sections clearly: Description, Parameters, Input, Output, Key Operations.  
     - Explain logic, not scientific meaning (this repo is not scientific).  
     - Link related functions when necessary.

5. **Preserve Behavior Unless Asked Otherwise**  
   - Bridge logic (sync directions, extraction, writing) may be refactored, but:
     - Do NOT change semantics of how sync works unless explicitly authorized.  
     - No silent behavioral changes.

6. **Be Explicit About Modes**  
   - Internally choose the right agent (mode) based on task type.  
   - Do not announce the mode to the user, but obey its rules.
   
   
## 1.x Structural Principles (Function ↔ File ↔ Documentation Mapping)

These constraints apply to *all* modes (DocumentationAgent, BridgeAgent, RefactorAgent):

1. **One Function per File**
   - Every top-level function must live in its own file under `functions/`.
   - The filename must match the function name:
       - `functions/<function_name>.py`
       - `functions/<function_name>.js`
   - No file may contain multiple unrelated top-level functions.
   - If an existing file contains multiple functions, the assistant must propose a split.

2. **One Documentation File per Function**
   - Every function must have exactly one documentation file:
       - `documentation/<function_name>.md`
   - The documentation file must follow the repository’s `DocumentationTemplate.md`.
   - The assistant must create the file if missing.
   - The `## Code` section must contain a fenced code block that exactly matches the current function implementation.

3. **Unbreakable Mapping (Atomic Round-Trip)**
   - Codex must maintain the bijection:
       ```
       documentation/<name>.md  ↔  functions/<name>.py or .js
       ```
   - Whenever code changes, update its documentation.
   - Whenever documentation’s code block changes, update the corresponding code file.
   - No silent drift: both sides must stay consistent.

4. **No God-Files**
   - Codex must not create new multi-function modules.
   - Refactors must preserve the atomic structure unless the user explicitly requests a multi-function design.

5. **Explicit Imports & References**
   - When splitting files, all import paths and call sites must be updated.
   - Codex must ensure the codebase remains executable after reorganizing individual function files.

These structural rules override agent-specific guidance when conflicts appear.
   

---

## 2. DocumentationAgent

**Use this mode when the user asks to:**  
- “document”, “improve docs”, “generate docs”,  
- “fill the empty sections”,  
- “follow DocumentationTemplate.md”,  
- or implicitly requests new `.md` docs for functions or variables.

**Primary references:**  
- `Prompt_CodexDocumentation.md`  
- `DocumentationTemplate.md`  
- existing docs under `documentation/`

**Responsibilities:**  
- Generate Markdown docs for:
  - every function in `functions/`  
  - every script in `GitObs-Bridge/`  
  - templates and meta-docs (`INDEX.md`, `GLOSSARY.md`)  
- Populate:
  - Description  
  - Key operations  
  - Parameters  
  - Input / Output  
  - Functions used  
  - Called by  
- Keep tone and style consistent with the template.

**Guardrails:**  
- Do NOT modify behavior of source code unless user explicitly requests refactor.  
- Document what exists, not imaginary APIs.

---

## 3. BridgeAgent (the core mode)

**Use this when the task involves:**  
- sync Vault → Repo  
- sync Repo → Vault  
- extracting code blocks  
- formatting code inside docs  
- generating or updating documentation from code  
- repairing round-trip consistency

**Primary references:**  
- `GitObs-Bridge.md` notes  
- existing bridge functions (`Bridge_GitBridge`, `WriteSoftware_GitBridge`, etc.)

**Responsibilities:**  

1. **Vault → Repo direction**  
   - Parse documentation files under `documentation/`.  
   - Extract the `## Code` fenced block.  
   - Format according to language.  
   - Write formatted code to `functions/` or user-specified folder.  
   - Ensure deterministic mapping:  
     `documentation/foo.md` ↔ `functions/foo.py` or `.js`.

2. **Repo → Vault direction**  
   - Read code files in `functions/`.  
   - Find or create matching documentation files.  
   - Insert/update the `## Code` block.  
   - Preserve other sections, updating them only when asked.

3. **Parameterizing everything**  
   - All paths, subfolders, formats must be passed explicitly.

4. **Round-trip correctness**  
   - No ambiguous overwrites: the newest version must win, with clear logic.  
   - Preserve user text outside code blocks.

**Guardrails:**  
- No destructive modifications to code behavior.  
- No removal of sections in documentation.  
- No uncontrolled overwrites of user notes.

---

## 4. RefactorAgent

**Use this when the user asks to:**  
- refactor bridge functions,  
- simplify sync logic,  
- modularize,  
- create a clean API,  
- fix architecture.

**Primary references:**  
- all `.py` files in the repo  
- higher-level notes in `GitObs-Bridge.md`

**Responsibilities:**  
- Improve:
  - clarity  
  - modularity  
  - consistency of naming  
  - proper separation: `bridge_core`, `doc_io`, `formatter`, `file_ops`, `git_ops`  
- Ensure every module has:
  - explicit parameters  
  - no absolute paths  
  - minimal side effects

**Guardrails:**  
- Must preserve existing behavior unless explicitly allowed to redesign.  
- Do not silently change sync direction or overwrite precedence rules.

---

## 5. PlanningAgent

**Use this when the user asks for:**  
- a plan,  
- roadmap,  
- next steps,  
- architecture improvements,  
- how to generalize GitObs-Bridge for all software projects.

**Responsibilities:**  
- Propose:
  - improved folder structure  
  - module decomposition  
  - a stable public API  
  - better logging system  
  - improved round-trip detection  
  - options for integrating with Obsidian plugins  
- Cross-reference existing functions by filename.

**Guardrails:**  
- Do not propose destructive rewrites without clearly labeling them as optional.  
- Plans must stay consistent with current design philosophy.

---

## 6. ConceptAgent (Architecture & Explanation)

**Use this when the user asks:**  
- “explain how the bridge works”  
- “what is the architecture?”  
- “how do the sync functions interact?”  
- “how does the round-trip logic work?”

**Responsibilities:**  
- Provide layered explanations:
  - plain-language description of the architecture,  
  - flow diagrams (in ASCII or Markdown),  
  - explanation of round-trip syncing,  
  - explanation of code-block extraction.  
- Explain logic rather than science.

**Guardrails:**  
- Explanations must match the implementation.  
- No invented features that the repo does not support.

---

## 7. Mode Selection Logic

When a request comes:

1. If it involves **documentation** → `DocumentationAgent`.
2. If it involves **sync logic or formatting code blocks** → `BridgeAgent`.
3. If it asks for **refactoring or architectural cleanup** → `RefactorAgent`.
4. If it asks for **roadmaps or next steps** → `PlanningAgent`.
5. If it asks for **architectural / conceptual explanations** → `ConceptAgent`.

Mixed requests:

- If mixing documentation + syncing → let **BridgeAgent** lead,  
  and call DocumentationAgent logic inside doc generation.
- If mixing refactor + bridge logic → let **RefactorAgent** lead,  
  preserving all sync invariants.
- If mixing planning + refactor → use PlanningAgent, calling RefactorAgent rules where needed.

Do NOT announce the mode externally; simply obey its rules.

---

## 8. Interaction with `Prompt_CodexDocumentation.md`

This file is a configuration layer.  
For documentation tasks:

- `DocumentationAgent` MUST follow all rules of `Prompt_CodexDocumentation.md`.

For bridge/refactor tasks:

- Still follow documentation rules for:
  - template structure  
  - cross-linking  
  - consistency of doc filenames  

When documentation rules conflict with bridge logic:

- The **bridge invariants win** for sync behavior.  
- The **documentation template wins** for doc structure.  
- Codex must highlight conflicts rather than silently override.

---

## 9. Example Task Routing

**User:**  
“Format all python code in the docs, update the code files in the repo, and fill the missing sections.”  
→ Mode: `BridgeAgent` (primary) + `DocumentationAgent`

**User:**  
“Create a function that syncs repo → vault with explicit parameters.”  
→ Mode: `BridgeAgent`

**User:**  
“Improve architecture and create a clean API for reusing this bridge in any project.”  
→ Mode: `RefactorAgent` + `PlanningAgent`

**User:**  
“How does the extraction + formatting + writing pipeline work internally?”  
→ Mode: `ConceptAgent`

---

## 10. Philosophy of These Agents

These “agents” are internal operation modes that help Codex keep the GitObs-Bridge:

- **Coherent** (same structure everywhere)  
- **Deterministic** (round-trip correctness)  
- **Reproducible** (formatting + templates)  
- **Transparent** (logic clearly explained)  
- **Scalable** (reusable for any software project)  

They are not isolated programs —  
they are behavioral contracts Codex must follow anytime it works inside this repository.

