---
class: code
language: Python
---
## Description


---
## Code
```Python
import numpy as np
def ExtractCodeblock_GitBridge(FileLoc):
    file = open(FileLoc, 'r')    
    lines = np.array(file.readlines())
    file.close()
    start = int(np.where(lines == "## Code\n")[0][0])+1
    language_clue = lines[start].replace('```','')
    language = language_clue.replace('\n','')
    end = np.where(lines == "## Key operations\n")[0][0]-1
    codeblock = ''.join(list(lines[start:end]))
    codeblock = codeblock.replace('```'+language,'')
    codeblock = codeblock.replace('```\n','')
    return [codeblock,language]
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


