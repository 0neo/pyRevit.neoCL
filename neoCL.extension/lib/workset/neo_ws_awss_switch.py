import neo_ws_awss_funcs as f
from System import EventHandler, Uri
from Autodesk.Revit.UI.Events import ViewActivatedEventArgs, ViewActivatingEventArgs
from rpw.ui.forms import Alert
from pyrevit import script

AUTO_WORKSET_SET = 'AUTO_WORKSET_SET'
AUTO_WORKSET_SET_EVENTADDED = 'AUTO_WORKSET_SET_EVENTADDED'

def awss(sender, args):
    f.AutoSetWorkset()

def isOn():
    return script.get_envvar(AUTO_WORKSET_SET)

def setOnOff(onoff):
    script.set_envvar(AUTO_WORKSET_SET, onoff)

def isEvenHandlerAdded():
    return script.get_envvar(AUTO_WORKSET_SET_EVENTADDED)
        
def switch():
    onoff = not isOn()
    setOnOff(onoff)
    script.toggle_icon(onoff)
    if onoff:
        #prevent multiple additions to eventhandler while switching on\off (remove if else (delete handler) works...)
        if not isEvenHandlerAdded():
            __revit__.ViewActivated += EventHandler[ViewActivatedEventArgs](awss)
            script.set_envvar(AUTO_WORKSET_SET_EVENTADDED, True)        
        f.AutoSetWorkset()
        Alert('Auto Workset Set is activated!', title="neoCL | Auto Workset Set", header="neoCL")
    else:
        #does this line unloads eventhandler?
        __revit__.ViewActivated -= EventHandler[ViewActivatedEventArgs](awss)
        __revit__.ViewActivated -= awss