################011011100110010101101111####
### neo Command Line #######################
############################################

import os
import subprocess
import rpw
import neocl
from rpw.ui.forms import Alert
from shutil import copyfile
from time import gmtime, strftime

def ShowFile(file, _Print=False, _Alert=True):
    import os.path
    from inspect import getsourcefile
    ipath = os.path.abspath(getsourcefile(lambda:0))
    ipath = ipath[:ipath.rfind(os.path.sep)]
    ipath = str(ipath) + os.path.sep + file
    f = open(ipath, "r")
    if _Print: print(f.read())
    if _Alert: neoAlert(f.read(), title="File", header="neoCL")

def neoAlert(content, title='Alert', header='', exit=False):
    # replace rpw alert for custom form in the future
    Alert(content, title, header, exit)

def neoCLFolderPath():
    from inspect import getsourcefile
    import os.path
    ipath = os.path.abspath(getsourcefile(lambda:0))
    npath = ipath[:ipath.rfind(os.path.sep)]
    npath = os.path.join(npath, '') # make sure it have \ at the end
    return npath

def CreateFolder(folderPath):

	if not os.path.exists(folderPath):
		try:
			os.makedirs(folderPath)
			return True
		except:
			os.makedirs(folderPath)
			return False
	else:
		return True

def CreateFile(content, fullFileName):

	try:
		thisFile = open(fullFileName, "w")
		thisFile.write(content)
		thisFile.close()
		return True
	except:
		return False

def neoCLRevitDocFolder():

	folderPath = os.path.expanduser(r'~\Documents')
	folderPath = os.path.join(folderPath, "neoCL.Revit", '')

	if CreateFolder(folderPath):
		return folderPath
	else:
		return False

def GenerateDateTimeCode():
    return strftime("%Y%m%d%H%M%S", gmtime())

def OpenExplorer(path):
	subprocess.call("explorer " + path, shell=True)

def Open_neoCLRevitDocFolder():
	OpenExplorer(neoCLRevitDocFolder())

def CreateFileInDocFolder(content, fileName, extension='.txt', addCode=True):

	result = []

	docPath = neoCLRevitDocFolder()
	if not docPath: return False

	if addCode:
		code = GenerateDateTimeCode()
	else:
		code = ''

	filePath = fileName + code + extension
	filePath = os.path.join(docPath, filePath)

	result.append(filePath)
	result.append(CreateFile(content, filePath))

	return result

def BackupUserFiles():
    
	bakFolderPath = UserBackupFolder()
	mainFolder = neoCLFolderPath()

	files = [
                [os.path.join('lib', 'find', ''), 'neo_findreplace_config.ini'],
                [os.path.join('lib', 'xl', ''), 'neoCL.FamilyReplacer.xlsm'],
                [os.path.join('lib', 'xl', ''), 'neoCL.iParametersEditor.xlsm']
            ]

	if bakFolderPath:
		try:
			for file in files:
				src = mainFolder + file[0] + file[1]
				dst = bakFolderPath + file[1]
				copyfile(src, dst)
			return True
		except:
			return False
	else:
		return False

def BackupMyUserFiles():
    
	if BackupUserFiles():
		OpenExplorer(UserBackupFolder())
		mg = "User files backed up to :\n" + str(UserBackupFolder())
	else:
		mg = "Error while backing up user files to to :\n" + str(UserBackupFolder())
		
	neoAlert(mg, 'neoCL', header='Backup User Files', exit=False)

def UserBackupFolder():

	docPath = neoCLRevitDocFolder()
	if not docPath: return False

	bakFolderPath = os.path.join(docPath, '_backupUserData', '')

	if CreateFolder(bakFolderPath):
		return bakFolderPath
	else:
		return False