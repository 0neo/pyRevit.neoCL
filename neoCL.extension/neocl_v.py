################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "ver"		:"neoCL : Version data."
            }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'ver':
        import neocl__config as g
        from neocl__funcs import neoAlert
        version = 'neoCL version\n'
        version += g.version + ' ' + g.beta + '\n' + g.date
        mg = 'Tools :\n\n'
        mg += '' + g.GetAllToolsstr(' : ', '\n', True)
        neoAlert(mg, "neoCL", version)
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())
