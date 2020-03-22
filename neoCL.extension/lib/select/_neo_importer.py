### by neo ### 2019 ################################################
### Set main folder to import from parent folders, out of a package.
### ################################################################

from inspect import getsourcefile
import os.path
import sys

neodir = "neoCL.extension"                                          # Main folder of neoCL
ipath = os.path.abspath(getsourcefile(lambda:0))                    # Get this file full path
npath = ipath[:ipath.rfind(os.path.sep + neodir) + len(neodir) + 1] # Get full path of Main folder of neoCL
sys.path.insert(0, npath)                                           # Set Main folder neoCL as current directory