
import sys
import os
home=os.getcwd()
sys.path.append(home)
from Bridge_GitBridge import *
from ReadBashRun_GitBridge import *
from WritingDebug import *
SoftwareProject = '/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge'
Bridge_GitBridge(SoftwareProject=SoftwareProject)  
ReadBashRun_GitBridge()


