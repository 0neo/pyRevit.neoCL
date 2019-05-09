################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "f"			:"Find And Replace : Find and replace in family parameters.",
            "froxl"		:"Family Replacer : Open Excel file.",
            "frp"		:"Family Replacer : in Project : Replace family and types of instances edited in Excel.",
            "frv"		:"Family Replacer : in ActiveView : Replace family and types of instances edited in Excel."
            }
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'f':
        from lib.find import neo_findreplace_main as find
        find.Main()
    elif cmd == 'froxl':
        from lib.xl import neo_xl_type_replacer as tyrep
        tyrep.GetWb()
    elif cmd == 'frp':
        from lib.xl import neo_xl_type_replacer as tyrep
        tyrep.ImportXl("Project")
    elif cmd == 'frv':
        from lib.xl import neo_xl_type_replacer as tyrep
        tyrep.ImportXl("ActiveView")
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())