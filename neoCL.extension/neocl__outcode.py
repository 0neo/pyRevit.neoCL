################011011100110010101101111####
### neo Command Line #######################
############################################

#2020 CODE NOT USED YET !

import sys

def getcmdlist():
    cmds = {
            "_pysv"			:"[pyRevit Script] : Auto zoom and center to same 2D coordinates between views.",
            "_pyst"			:"[pyRevit Script] : Sum total of a selected common parameter of selected elements.",
            "_pydh"			:"[pyRevitPlus Script] : Distribute elements horizontally.",
            "_pydv"			:"[pyRevitPlus Script] : Distribute elements vertically.",
            "_pyahc"		:"[pyRevitPlus Script] : Horizontally align elements to center.",
            "_pyahl"		:"[pyRevitPlus Script] : Horizontally align elements to left.",
            "_pyahr"		:"[pyRevitPlus Script] : Horizontally align elements to right.",
            "_pyavc"		:"[pyRevitPlus Script] : Vertically align elements to center.",
            "_pyavb"		:"[pyRevitPlus Script] : Vertically align elements to bottom.",
            "_pyavt"		:"[pyRevitPlus Script] : Vertically align elements to top."
            }
    return cmds

def runcmd(cmd, msg, recallCL=False):
    import imp
    ipath = GetMainDir()
    ipath += r"\neoCL.tab\pyRevit Scripts (non-neoCL).panel"

    if cmd == '_pysv':
        from rpw.ui.forms import Alert
        mg = "Can't call it from neoCL, you need to call this script from ribbon."
        Alert(mg, "non-neoCL Scripts", "pyRevit Sync Views")
    elif cmd == '_pyst':
        ipath += r"\SyncViewSum.stack\Sum.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pydh':
        ipath += r"\smartalign.stack\Distribute.pulldown\Horizontal.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pydv':
        ipath += r"\smartalign.stack\Distribute.pulldown\Vertical.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pyahc':
        ipath += r"\smartalign.stack\Horizontal.pulldown\Align Center.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pyahl':
        ipath += r"\smartalign.stack\Horizontal.pulldown\Align Left.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pyahr':
        ipath += r"\smartalign.stack\Horizontal.pulldown\Align Right.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pyavc':
        ipath += r"\smartalign.stack\Vertical.pulldown\Align Center.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pyavb':
        ipath += r"\smartalign.stack\Vertical.pulldown\Align Bottom.pushbutton\script.py"
        imp.load_source("py", ipath)
    elif cmd == '_pyavt':
        ipath += r"\smartalign.stack\Vertical.pulldown\Align Top.pushbutton\script.py"
        imp.load_source("py", ipath)
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())

def GetMainDir():
	import os.path
	from inspect import getsourcefile
	neodir = "neoCL.extension"                                          # Main folder of neoCL
	ipath = os.path.abspath(getsourcefile(lambda:0))                    # Get this file full path
	npath = ipath[:ipath.rfind(os.path.sep + neodir) + len(neodir) + 1] # Get full path of Main folder of neoCL
	#sys.path.insert(0, npath)                                           # Set Main folder neoCL as current directory
	return npath