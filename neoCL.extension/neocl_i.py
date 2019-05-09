################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "i++"		:"Keep incrementing values in some parameter of family instances."
            }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'i++':
        from lib.incpv import neo_increment_main as ic
        ic.Main()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())
