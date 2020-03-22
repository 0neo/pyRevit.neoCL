################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "backup"		:"Backup your neoCL user files before update neoCL, these files will be lost after update.",
			"backupr"		:"Restore some or all your neoCL user files after update neoCL."
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):
	
    if cmd == 'backup':
        from neocl__backup import BackupMyUserFiles
        BackupMyUserFiles()
    elif cmd == 'backupr':
        from neocl__backup import RestoreBackups
        RestoreBackups()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())