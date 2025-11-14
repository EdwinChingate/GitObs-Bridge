---
class: code
---
## Description


---
## Code
```python
def WriteSoftware_GitBridge(SoftwareProject,codeblock,language):
    CodingFolder = SoftwareProject + '/functions'
    if language == 'markdown':
        return 0
    LanguageExtensions = {"python" : "py",
                          "javascript" : "js",
                          "bash" : "sh", 
                          "markdown" : "md"}        
    extension = LanguageExtensions[language]
    fileName = function.replace('.md','') + '.' + extension
    fileLoc = CodingFolder + '/' + fileName
    file = open(fileLoc,'w')
    file.write(codeblock)
    file.close()
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


