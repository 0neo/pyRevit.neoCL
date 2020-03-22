### by neo ### 2019 ##############################################
### PROBLEM ... Can't import modules out of a package.
### SOLUTION .. Use this file path to find the main folder path
###             and set it as current directory to allow import.
### BONUS ..... Get command from file name, so same script to all
###             commands, just file name changes.
### ##############################################################

"""Revisions Editor : Edit project revisions in Excel."""

__title__ = 'Export.xl'
__author__ = 'by neo'

from inspect import getsourcefile
import os.path
import sys

neodir = "neoCL.extension"                                          # Main folder of neoCL

ipath = os.path.abspath(getsourcefile(lambda:0))                    # Get this file full path

cmd = ipath[ipath.rfind(os.path.sep) + 1:-10]                       # Split command to run from file full path

npath = ipath[:ipath.rfind(os.path.sep + neodir) + len(neodir) + 1] # Get full path of Main folder of neoCL
sys.path.insert(0, npath)                                           # Set Main folder neoCL as current directory

import neocl as neo                                                 # Now is possible to import neoCL.py
neo.runcmd(cmd,  "From command caller file.")                       # Call neoCL command 