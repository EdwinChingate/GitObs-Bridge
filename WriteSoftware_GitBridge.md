---
class: code
language: Python
---
## Description


---
## Code
```Python
def WriteSoftware_GitBridge(function,SoftwareProject,codeblock,language):
    CodingFolder = SoftwareProject + '/functions'
    if language == 'markdown':
        return 0
    LanguageExtensions = {"Python" : "py",
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


