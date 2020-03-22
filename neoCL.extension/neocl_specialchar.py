################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "?"		    :"List all neoCL commands.",
            "@"		    :"Open neoCL website.",
            "#pm.rnc"	:"[OPTION] Recall neoCL after each command."
            }
    return cmds


def runcmd(cmd, msg, recallCL=False):

    if cmd == '?':
        from neocl import AlertAllCmds
        AlertAllCmds()
    elif cmd == '@':
        from webbrowser import open_new_tab 
        open_new_tab(r"https://github.com/0neo/pyRevit.neoCL")
    elif cmd == '#pm.rnc':
        from neocl__user_options import SetOption_RecallneoCL 
        SetOption_RecallneoCL()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())