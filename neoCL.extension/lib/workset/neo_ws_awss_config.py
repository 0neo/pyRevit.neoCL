#######################################
### neoCL | Auto Workset Set ##########
#######################################

from inspect import getsourcefile
import os.path
import ast
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

awssDB = ""

def WriteThis(section, key, value):
    try:
        config.set(section, key, value)
        WriteConfig()
        return True
    except:
        return False

def WriteConfig():
	with open(npath, 'wb') as conf:
		config.write(conf)

def GetThis(section, key):
	return config.get(section, key)

def UpdateDB(new_awssDB):
    WriteThis('WORKSETS', '_userWorksets', new_awssDB)

# START ### ######################################################################
ipath = os.path.abspath(getsourcefile(lambda:0))
npath = ipath[:ipath.rfind(os.path.sep) + 1] + "neo_ws_awss_config.ini" 
config = ConfigParser()
config.optionxform = str 
config.read(npath)

# Get DB ### #####################################################################
def ReloadDB():
    global awssDB 
    awssDB = GetThis('WORKSETS', '_userWorksets')
    try: awssDB = ast.literal_eval(awssDB)
    except: print("ERROR: There is a problem with the integrity of the config file. Other errors may occur.")

ReloadDB()