################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "os"		:"Open active Schedule View in Excel.",
            "ov"		:"Open selected views in Project Browser."
           }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'os':
        from lib.views import neocl_open_schedule_xl as os
        os.ExportActiveScheduleViewToExcel()
    elif cmd == 'ov':
        from lib.views import neocl_views_open as ov
        ov.OpenSelectedViews()
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())