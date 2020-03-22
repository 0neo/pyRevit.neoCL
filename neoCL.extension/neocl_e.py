################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "edb"		:"List information about who edited selected instances."
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):
	
    if cmd == 'edb':
        from lib.users import neo_editedby as ed
        ed.Editors()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())