################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "sav"		:"Select all in Active View, Model or Annotation.",
            "samv"		:"Select all in Active View, non Annotation.",
            "ssv"		:"Select similar in Active View of same kind of selection (multiple types allowed).",
            "sap"		:"Select all in Project, Model or Annotation.",
            "samp"		:"Select all in Project, non Annotation.",
            "ssp"		:"Select similar in Project of same kind of selection (multiple types allowed)."
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'sav':
        from lib.select import neo_selection_funcs as sel
        sel.SelectAllInView(['Model', 'Annotation'])
    elif cmd == 'samv':
        from lib.select import neo_selection_funcs as sel
        sel.SelectAllInView(['Model'])
    elif cmd == 'ssv':
        from lib.select import neo_selection_funcs as sel
        sel.SelectSimilar('ActiveView')
    elif cmd == 'sap':
        from lib.select import neo_selection_funcs as sel
        sel.SelectAllInProject(['Model', 'Annotation'])
    elif cmd == 'samp':
        from lib.select import neo_selection_funcs as sel
        sel.SelectAllInProject(['Model'])
    elif cmd == 'ssp':
        from lib.select import neo_selection_funcs as sel
        sel.SelectSimilar('Project')
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())