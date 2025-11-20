---
class: code
language: Python
---
## Description

`WritingDebug` orchestrates the logic described in this module. It prepares helper paths such as `fileLoc`, `file`. It calls `close`, `now`, `open`, `str`, `write` as part of its workflow.

---
## Code
```Python
from datetime import datetime
def WritingDebug(text=''):
	text = str(text)
	current_datetime = str(datetime.now())
	text = ' - ' + current_datetime + ' ; ' + text + '\n'
	fileLoc = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/Test/LogCode.md"
	file = open(fileLoc,'a')
	file.write(text)
	file.close()
```

---
## Key operations

- Constructs `fileLoc` from `'/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/Test/LogCode.md'`.
- Constructs `file` from `open(fileLoc, 'a')`.
- Calls `close` to delegate work.
- Calls `now` to delegate work.
- Calls `open` to delegate work.
- Calls `str` to delegate work.
- Calls `write` to delegate work.

---
## Parameters

- `text`: used in expressions such as `str(text)` to derive runtime paths.

---
## Input

- `fileLoc`: derived from `'/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/Test/LogCode.md'` to keep track of resources.
- `file`: derived from `open(fileLoc, 'a')` to keep track of resources.

---
## Output

- None

---
## Functions

- `close`: helper function invoked inside the workflow.
- `now`: helper function invoked inside the workflow.
- `open`: helper function invoked inside the workflow.
- `str`: helper function invoked inside the workflow.
- `write`: helper function invoked inside the workflow.

---
## Called by

- [copy_folder_contents](copy_folder_contents.md) uses this helper.
