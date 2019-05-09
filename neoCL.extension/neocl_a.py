################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "about"		:"neoCL : About neoCL.",
            "atte"		:"InsParam Editor : Export family instances parameters to edit in Excel.",
            "atti"		:"InsParam Editor : Import family instances parameters edited in Excel.",
            "attoxl"	:"InsParam Editor : Open Excel file."
            }
    return cmds


def runcmd(cmd, msg, recallCL=False):

    if cmd == 'about':
        #from neocl__funcs import ShowFile
        #ShowFile("about.txt")
        import about
        about.Main()
    elif cmd == 'atte':
        from lib.xl import neo_xl_selected_instances as xlinst
        xlinst.Export()
    elif cmd == 'atti':
        from lib.xl import neo_xl_selected_instances as xlinst
        xlinst.Import()
    elif cmd == 'attoxl':
        from lib.xl import neo_xl_selected_instances_import as xlinst
        xlinst.GetWb()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())