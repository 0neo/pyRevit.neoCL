################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "?"		    :"List all neoCL commands.",
            "@"		    :"Open neoCL website."
            }
    return cmds


def runcmd(cmd, msg, recallCL=False):

    if cmd == '?':
        from neocl import AlertAllCmds
        AlertAllCmds()
    elif cmd == '@':
        from webbrowser import open_new_tab 
        open_new_tab(r"https://github.com/0neo/neoCL")
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())