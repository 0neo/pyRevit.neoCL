################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "ras"		:"Remove annotation from active selection.",
            "rev"		:"Revisions Editor : Edit project revisions in Excel.",
            "revh"		:"Revisions Editor : Information to use revisions editor in Excel.",
            "revi"		:"Revisions Editor : Import updates to revisions from Excel."
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'ras':
        from lib.select import neo_selection_funcs as sel
        sel.RemoveAnnotationFromSelection()
    elif cmd == 'rev':
        from lib.revisions.neo_revisions_main import Export
        Export()
    elif cmd == 'revh':
        from lib.revisions.neo_revisions_main import OpenHowTo
        OpenHowTo()
    elif cmd == 'revi':
        from lib.revisions.neo_revisions_main import Import
        Import()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())