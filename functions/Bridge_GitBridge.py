
import os
from ExtractCodeblock_GitBridge import *
from WriteSoftware_GitBridge import *

def Bridge_GitBridge(SoftwareProject):
    DocFolder = SoftwareProject + '/documentation'
    Functions = os.listdir(DocFolder)
    for function in Functions:
        functionLoc = DocFolder + '/' + function
        codeblock,language = ExtractCodeblock_GitBridge(FileLoc=functionLoc)
        WriteSoftware_GitBridge(function=function,
                                SoftwareProject=SoftwareProject,
                                codeblock=codeblock,
                                language=language)  

