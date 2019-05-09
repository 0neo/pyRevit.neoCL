################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "q"			:"Quit neoCL."
            }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'q':
        pass
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())