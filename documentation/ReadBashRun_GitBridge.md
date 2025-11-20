---
class: code
language: Python
---
## Description

`ReadBashRun_GitBridge` orchestrates the logic described in this module. It prepares helper paths such as `SOURCE_FOLDER`, `DESTINATION_FOLDER`, `PROJECT_FOLDER`, `LOG_FILE`. It calls `commit_all`, `copy_folder_contents` as part of its workflow.

---
## Code
```Python

import os
from copy_folder_contents import *
from commit_all import *
def ReadBashRun_GitBridge():
    SOURCE_FOLDER = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/documentation"
    DESTINATION_FOLDER = "/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge/documentation"
    copy_folder_contents(SOURCE_FOLDER, DESTINATION_FOLDER, recursive=False)
    SOURCE_FOLDER = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/functions"
    DESTINATION_FOLDER = "/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge/functions"
    copy_folder_contents(SOURCE_FOLDER, DESTINATION_FOLDER, recursive=False)
    PROJECT_FOLDER = "/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge"
    COMMIT_MESSAGE = "this is a commit, for more details check the log"
    LOG_FILE = "commit_log.txt"
    commit_id = commit_all(PROJECT_FOLDER, COMMIT_MESSAGE, LOG_FILE) 
```

---
## Key operations

- Constructs `SOURCE_FOLDER` from `'/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/functions'`.
- Constructs `DESTINATION_FOLDER` from `'/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge/functions'`.
- Constructs `PROJECT_FOLDER` from `'/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge'`.
- Constructs `LOG_FILE` from `'commit_log.txt'`.
- Calls `commit_all` to delegate work.
- Calls `copy_folder_contents` to delegate work.

---
## Parameters

- None

---
## Input

- `SOURCE_FOLDER`: derived from `'/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/functions'` to keep track of resources.
- `DESTINATION_FOLDER`: derived from `'/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge/functions'` to keep track of resources.
- `PROJECT_FOLDER`: derived from `'/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge'` to keep track of resources.
- `LOG_FILE`: derived from `'commit_log.txt'` to keep track of resources.

---
## Output

- None

---
## Functions

- [commit_all](commit_all.md): stages repository changes and commits them with a generated message.
- [copy_folder_contents](copy_folder_contents.md): moves every file from a source directory into a destination, creating folders when needed.

---
## Called by

- [GitObs-Bridge_GitBridge](GitObs-Bridge_GitBridge.md) uses this helper.
- [GitObs_GitBridge](GitObs_GitBridge.md) uses this helper.
