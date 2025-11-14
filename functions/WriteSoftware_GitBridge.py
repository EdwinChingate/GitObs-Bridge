
def WriteSoftware_GitBridge(SoftwareProject,codeblock,language):
    CodingFolder = SoftwareProject + '/functions'
    if language == 'markdown':
        return 0
    LanguageExtensions = {"" : "py",
                          "javascript" : "js",
                          "bash" : "sh", 
                          "markdown" : "md"}        
    extension = LanguageExtensions[language]
    fileName = function.replace('.md','') + '.' + extension
    fileLoc = CodingFolder + '/' + fileName
    file = open(fileLoc,'w')
    file.write(codeblock)
    file.close()


