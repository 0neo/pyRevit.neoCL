################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "help"		:"neoCL : Help."
            }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'help':
        from neocl__funcs import ShowFile
        ShowFile("readme.txt")
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())
