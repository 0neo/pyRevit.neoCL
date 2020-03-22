import os
import neocl__funcs as f
from shutil import copyfile

def BackupUserFilesList():	
	files = [
                [os.path.join('lib', 'find', ''), 'neo_findreplace_config.ini'],
                [os.path.join('lib', 'workset', ''), 'neo_ws_awss_config.ini'],
                [os.path.join('lib', 'xl', ''), 'neoCL.FamilyReplacer.xlsm'],
                [os.path.join('lib', 'xl', ''), 'neoCL.iParametersEditor.xlsm'],
                [os.path.join('lib', 'xl', ''), 'neoCL.AutoWorksetSet.Configurator.xlsm'],
                [os.path.join('lib', 'xl', ''), 'neoCL.Revisions.xlsm']
            ]

	return files

def BackupUserFilesDic(invert=False):		
	filesList = BackupUserFilesList()
	filesDic = {}
	for file in filesList:
		if invert:
			filesDic[file[1]] = file[0]
		else:
			filesDic[file[0]] = file[1]
	return filesDic

def BackupUserFiles(bakFolder):    
	#bakFolderPath = UserBackupFolder()
	mainFolder = f.neoCLFolderPath()

	files = BackupUserFilesList()
	
	f.CreateFolder(bakFolder)

	if os.path.isdir(bakFolder):
		try:
			for file in files:
				src = mainFolder + file[0] + file[1]
				dst = bakFolder + file[1]
				copyfile(src, dst)
			return True
		except:
			return False
	else:
		return False

def BackupMyUserFiles(cancelAlert=False):    
	mainBakFolder = UserBackupFolder()
	subBakFolder = f.GenerateUniqueDateFolder()
	bakFolder = os.path.join(mainBakFolder, subBakFolder, '')

	if BackupUserFiles(bakFolder):
		f.OpenExplorer(bakFolder)
		mg = "User files backed up to :\n" + str(bakFolder)
	else:
		mg = "Error while backing up user files to to :\n" + str(bakFolder)
	
	if cancelAlert:
		print(mg)
	else:
		f.neoAlert(mg, 'neoCL', header='Backup User Files', exit=False)

def UserBackupFolder():
	docPath = f.neoCLRevitDocFolder()
	if not docPath: return False
	
	bakFolderPath = os.path.join(docPath, '_backupUserData', '')

	if f.CreateFolder(bakFolderPath):
		return bakFolderPath
	else:
		return False

def RestoreBackups():
	WarningMsg = "Warning:\n\nSelect only the files that you really want to keep, " \
				"these files could be updated (new functionalities, fixed errors...).\n\n" \
				"A new backup of the user files will be created before the replace, so if there are " \
				"errors with some tools due an obsolete file, you should restore the newer file!"
	f.neoAlert(WarningMsg, 'neoCL', header='Restore Backed up User Files', exit=False)

	from rpw.ui.forms import select_file
	filespath = select_file(GetFilterBackedupFiles(), title='Select backup files to Restore!', multiple=True, restore_directory=True)
	
	if filespath:
		BackupMyUserFiles(True) # Backup before replace
		log = ''
		logOk = ''
		logError = ''
		mainFolder = f.neoCLFolderPath()
		files = BackupUserFilesDic(True)
		for src in filespath:
			fileName = os.path.basename(src)
			dst = os.path.join(mainFolder, files[fileName], fileName)
			try:
				copyfile(src, dst)
				logOk += ' -> ' + fileName + '\n'
			except:
				logError += ' -> ' + fileName + '\n'

		if logOk:
			log += "Files restored to neoCL folder :\n" + logOk

		if logError:
			log += "Error restoring these files to neoCL folder :\n" + logError

		log += '\nA new backup of the user files was created before the replace.'
		f.neoAlert(log, 'neoCL', header='Restore Backed up User Files', exit=False)

def GetFilterBackedupFiles():
	files = BackupUserFilesList()
	filterStrS = 'neoCL files ('
	filterStrV = ''

	for file in files:
		filterStrS += file[1] + ';'
		filterStrV += file[1] + ';'

	filterStrS = filterStrS[:-1]
	filterStrV = filterStrV[:-1]

	filterStr = filterStrS + ')|' + filterStrV

	return filterStr