---
class: code
language: Python
---
## Description


---
## Code
```Python
import os
from copy_folder_contents import *
from commit_all import *
def ReadBashRun_GitBridge():
	SOURCE_FOLDER = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/documentation"
	DESTINATION_FOLDER = "/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge"
	copy_folder_contents(SOURCE_FOLDER, DESTINATION_FOLDER, recursive=False)
	SOURCE_FOLDER = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02 Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/functions"
	DESTINATION_FOLDER = "/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge"
	copy_folder_contents(SOURCE_FOLDER, DESTINATION_FOLDER, recursive=False)
	PROJECT_FOLDER = "/home/edwin/0-GitHubProjects/Codding/GitObs-Bridge"
	COMMIT_MESSAGE = "this is a commit, for more details check the log"
	LOG_FILE = "commit_log.txt"
	commit_id = commit_all(PROJECT_FOLDER, COMMIT_MESSAGE, LOG_FILE) 
```

---
## Key operations

- 

## Parameters



---

## Input



---

## Output



---

## Functions



---

## Called by


