################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "about"		:"neoCL : About neoCL.",
            "atte"		:"InsParam Editor : Export family instances parameters to edit in Excel.",
            "attep"		:"InsParam Editor : Export family instances parameters to edit in Excel (preset parameters mode).",
            "atti"		:"InsParam Editor : Import family instances parameters edited in Excel.",
            "attoxl"	:"InsParam Editor : Open Excel file.",
            "awssa"	    :"AWSS : Set workset for active view.",
            "awssuc"	:"AWSS : Update config file with data in excel file.",
            "awssxl"	:"AWSS : Open Excel file user configuration."
            }
			# Ribbon toogle icon icompability :
            #"awss"	    :"AWSS : Auto set workset by name view (user configuration file needed).", 
    return cmds


def runcmd(cmd, msg, recallCL=False):

    if cmd == 'about':
        #from neocl__funcs import ShowFile
        #ShowFile("about.txt")
        import about
        about.Main()
    elif cmd == 'atte':
        from lib.xl import neo_xl_selected_instances as xlinst
        xlinst.Export(False)
    elif cmd == 'attep':
        from lib.xl import neo_xl_selected_instances as xlinst
        xlinst.Export(True)
    elif cmd == 'atti':
        from lib.xl import neo_xl_selected_instances as xlinst
        xlinst.Import()
    elif cmd == 'attoxl':
        from lib.xl import neo_xl_selected_instances_export as xlinst
        xlinst.GetWb()
    elif cmd == 'awss':
        from lib.workset import neo_ws_awss_main
    elif cmd == 'awssxl':
        from lib.xl import neo_xl_awss as awss
        awss.LOG_Worksets()
        awss.LOAD_Worksets()
    elif cmd == 'awssuc':
        from lib.xl import neo_xl_awss as awss
        awss.UPLOAD_Worksets()
    elif cmd == 'awssa':                           
        from lib.workset import neo_ws_awss_testmode
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())