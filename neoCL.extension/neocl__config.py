from neocl__funcs import neoCLFolderPath
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

def ReadVar(sep, var, isbool=False):
    if isbool:
        return config.getboolean(sep, var)
    else:
        return config.get(sep, var)

def WriteVar(sep, var, val):
    config.set(sep, var, val)
    return WriteConfig()

def WriteConfig():
    with open(npath, 'wb') as conf:
        return config.write(conf)

def GetAllToolsList():
    dtools = config.items("TOOLS")
    tools = []
    for toolnr, tool in dtools:
        tools.append(tool.split(','))
    return tools

def GetAllToolsstr(sep, fsep, invert):
    toolsstr = ''
    tools = GetAllToolsList()
    for tool in tools:
        ver = tool[1]
        if ver == 'gversion': ver = version
        if invert:
            toolsstr += ver + ' ' + tool[2] + sep +  tool[0] + fsep
        else:
            toolsstr += tool[0] + sep + ver + ' ' + tool[2] + fsep
    return toolsstr

npath = str(neoCLFolderPath() + 'neocl__config.ini')
config = ConfigParser()
config.optionxform = str
config.read(npath)

fm = None
allcmds = {}
version = ReadVar('DATA', '_version')
beta = ReadVar('DATA', '_beta')
date = ReadVar('DATA', '_date')
isred = ReadVar('E.EGG', '_isred', True)
op_recallneocl = ReadVar('USER.OPTIONS', '_recall_neoCL', True)
