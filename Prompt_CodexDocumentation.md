## Role & Context

You are working **inside my GitObs-Bridge repository**.

This repo is a **Python library** that I am using to:

- keep an external Git repository and an Obsidian project in sync,  
- read documentation files in `documentation/` that contain code blocks,  
- write/update actual `.py` files from those code blocks,  
- eventually keep everything consistent in both directions.

The repository already contains functions such as:

- `Bridge_GitBridge`
- `WriteSoftware_GitBridge`
- `ExtractCodeblock_GitBridge`
- `ReadBashRun_GitBridge`
- `copy_file_basic`, `copy_dir_basic`, `copy_folder_contents`
- `commit_all`

and several documentation files under `documentation/` (e.g. `copy_folder_contents.md`, `Bridge_GitBridge.md`), each with a `## Code` section and an empty template structure.

You must **refine and extend these existing functions**, not replace the whole design.

---

## What I Want You To Do

### 1. Refine my code-block revision function(s) and add a syntax/formatting check

I already have software that:

- reads documentation files in `documentation/`,
- finds the `## Code` section,
- extracts the code block,
- and writes it as a `.py` file into a `functions/` folder (or similar).

**Task 1a — Refine existing behavior**

- Find the functions that perform this behavior (`Bridge_GitBridge`, `WriteSoftware_GitBridge`, `ExtractCodeblock_GitBridge`, etc.).  
- Keep the same *overall* behavior, but:
  - clean up the code,
  - avoid duplicated logic,
  - improve readability and small bugs (without changing what it does conceptually).

**Task 1b — Add a new syntax/formatting checker**

Add a **new function** whose job is:

- to take a path to a documentation file (e.g. a `.md` file in `documentation/`),
- extract the code from the `## Code` fenced block,
- depending on the language:

  - if the code is Python:
    - use `autopep8` to format the code,
    - optionally check syntax (for example, try `compile()` or `ast.parse()` and report syntax errors),
  - if the code is JavaScript:
    - call a JS formatter if available (e.g. a `prettier` subprocess),
    - or at least apply a simple indentation/brace-normalization strategy,
    - and optionally check syntax in a similar lightweight way (for example, calling `node --check` via subprocess if present).

- return a **result object** or dictionary that includes:
  - `language`
  - `formatted_code`
  - `syntax_ok` (True/False)
  - `syntax_error` (string or `None`)
- optionally, if a flag like `apply_changes=True` is passed, write the formatted code back into the `## Code` block in the doc file.

Design this in terms of Python functions, for example:

```python
def check_and_format_doc_codeblock(
    doc_path: str,
    apply_changes: bool = False,
) -> dict:
    """
    - Extract code + language from '## Code' of doc_path.
    - Format the code using autopep8 (Python) or a JS formatter / fallback.
    - Optionally write the formatted code back into the file.
    - Return a dict with:
        - 'language'
        - 'formatted_code'
        - 'syntax_ok'
        - 'syntax_error'
    """
````

**Important:**  
Do _not_ hard-code any specific absolute path. This function should only operate on `doc_path` and whatever configuration we pass in.

---

### 2. Create a function to copy files from the repo into the Obsidian Vault and update docs

I also want another function that, when I call it, will:

- copy **code files** (e.g. `.py`) or **documentation files** from an external Git repo into my **Obsidian project**,
    
- update or create documentation files in the Obsidian project so that `documentation/*.md` corresponds to the code in the repo.
    

Concretely:

- The function must accept parameters like:
    
    ```python
    repo_root: str              # path to the Git repo
    vault_project_root: str     # path to the project folder inside the Obsidian vault
    docs_subfolder: str = "documentation"
    functions_subfolder: str = "functions"
    copy_mode: str = "code"     # "code", "docs", or "both"
    ```
    
- When `copy_mode` includes `"code"`:
    
    - scan `repo_root/functions_subfolder` (or similar) for `.py` (and later `.js`) files,
        
    - for each code file:
        
        - copy it into the corresponding location inside `vault_project_root`,
            
        - ensure that there is a documentation file for it in `vault_project_root/docs_subfolder`,
            
        - update the `## Code` block of that documentation file to match the code file.
            
- When `copy_mode` includes `"docs"`:
    
    - copy documentation files from the repo’s `documentation/` (or analogous folder) into `vault_project_root/docs_subfolder`,
        
    - keep the structure consistent.
        

You are free to choose the function name(s), but they should be clear. For example:

```python
def copy_repo_to_vault(
    repo_root: str,
    vault_project_root: str,
    docs_subfolder: str = "documentation",
    functions_subfolder: str = "functions",
    copy_mode: str = "code",
) -> None:
    """
    Copy code and/or documentation files from repo_root into vault_project_root,
    and update the documentation files inside the vault accordingly.
    """
```

Internally you can reuse helpers like `copy_folder_contents`, `copy_file_basic`, etc.

---

### 3. Make parameters explicit (no hard-coded paths)

You must:

- remove any hard-coded full paths (like `/home/...`) from the **core** functions,
    
- make sure the key functions take the following **explicit arguments**:
    
    - `repo_root` (path to the Git repo for the project)
        
    - `vault_project_root` (path to the working directory of the project inside the Obsidian vault)
        
    - optional `docs_subfolder` (e.g. `"documentation"`)
        
    - optional `functions_subfolder` (e.g. `"functions"`)
        

I want to be able to import this library and call, from any project:

```python
from gitobs_bridge import check_and_format_doc_codeblock, copy_repo_to_vault

copy_repo_to_vault(
    repo_root="/path/to/some/repo",
    vault_project_root="/path/to/vault/project",
)
```

So please:

- factor out the parameters,
    
- avoid global configuration for paths inside the core functions,
    
- keep behavior the same where possible.
    

---

### 4. Fill the empty sections inside the documentation files according to DocumentationTemplate.md

The folder `documentation/` contains `.md` files with a structure based on `DocumentationTemplate.md`.

Most of them currently have **empty sections**, for example:

- `## Description`
    
- `## Key operations`
    
- `## Parameters`
    
- `## Input`
    
- `## Output`
    
- `## Functions`
    
- `## Called by`
    

I want you to:

1. Read `DocumentationTemplate.md` and treat it as the canonical structure for documentation files.
    
2. Implement **Python functions** in this repo that, when I call them later, will:
    
    - inspect a doc file in `documentation/`,
        
    - check for missing or empty sections,
        
    - fill those sections with concise text that explains:
        
        - what the function does logically,
            
        - what its parameters mean,
            
        - what files/objects it reads or writes,
            
        - which other functions it calls or is called by (when that is visible in the code / repo),
            
    - without inventing unrealistic behavior.
        

For example, for `copy_folder_contents`, the generated description might say things like:

- Copies the contents of a source directory into a destination directory.
    
- Optionally recurses into subdirectories when `recursive=True`.
    
- Uses lower-level helpers like `copy_file_basic` and `copy_dir_basic`.
    

Please:

- keep the explanations **short and implementation-oriented** (this repo is not scientific),
    
- write the code that **generates/updates** these docs; don’t just fill them manually once,
    
- **reuse the existing DocumentationTemplate.md** so the layout stays consistent.
    

---

## General Constraints

- Work _with_ the existing functions (`Bridge_GitBridge`, `WriteSoftware_GitBridge`, `ExtractCodeblock_GitBridge`, etc.), refining and extending them rather than deleting everything.
    
- Do **not** assume any particular OS beyond what’s already used (standard `pathlib`, `os`, etc.).
    
- Keep things as regular Python modules and functions so I can call them from:
    
    - Obsidian (via ExecuteCode),
        
    - small scripts in other repositories.
        

When you change or create functions, add or update docstrings in a way that is compatible with the documentation structure I’m using.

