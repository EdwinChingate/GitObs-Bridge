
from datetime import datetime
def WritingDebug(text=''):
	text = str(text)
	current_datetime = str(datetime.now())
	text = ' - ' + current_datetime + ' ; ' + text + '\n'
	fileLoc = "/home/edwin/0-GitHubProjects/Codding/SecondBrain/0-Vault/02-Areas/11-Gardening/Planning/Playground/Prototypes/GitObs-Bridge/Test/LogCode.md"
	file = open(fileLoc,'a')
	file.write(text)
	file.close()


