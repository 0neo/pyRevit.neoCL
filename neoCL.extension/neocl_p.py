################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "p"		:"Print : Print to PDF."
            }
    return cmds


def runcmd(cmd, msg, recallCL=False):

    if cmd == 'p':
        from rpw.ui.forms import Alert
        Alert('Check next versions.', title="neoCL | Printer", header="Not available yet...")
        #from lib.printer import neo_print_main as printer
        #printer.Main()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())