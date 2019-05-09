################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "backup"		:"Backup your neoCL user files before update neoCL, these files will be lost after update. (overwrites older backups)"
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'backup':
        from neocl__funcs import BackupMyUserFiles
        BackupMyUserFiles()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())