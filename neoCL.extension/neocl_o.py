################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "ov"		:"Open selected views in Project Browser."
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'ov':
        from lib.views import neocl_views_open as ov
        ov.OpenSelectedViews()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())