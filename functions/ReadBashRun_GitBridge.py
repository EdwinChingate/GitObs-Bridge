
import os
def ReadBashRun():
    fileLoc = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/functions/Copy-Bridge_GitBridge.sh"
    file=open(fileLoc,'r')
    text=file.read()
    file.close()
    os.system(text)
    fileLoc = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/functions/GitCommit_GitBridge.sh"
    file=open(fileLoc,'r')
    text=file.read()
    file.close()
    os.system(text)    

