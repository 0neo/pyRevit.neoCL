# Create intellisense in the future as on neoCL.AutoCAD 

import neocl__config as g
import neocl__setup as s

def UpdateListBox(firstRun=False):
        
    g.fm._listBoxCmds.Items.Clear()      
    usercmd = g.fm._comboBoxCmds.Text

    if not usercmd:
        # can't clear combobox items without deleting field text
        # now is no text in field, so good time to clear items 
        g.fm._comboBoxCmds.Items.Clear()

    listAll = usercmd == '?'
    if s.easternneocl(usercmd, True): return

    for k, v in g.allcmds.items():
        if firstRun:
            pass
        elif listAll or \
             (usercmd != '' and usercmd.lower() in k.lower()) or \
             (usercmd != '' and usercmd.lower() in v.lower() and g.fm.isFindMode):
            g.fm._listBoxCmds.Items.Add('' + str(k) + '\t: ' + str(v))
            
    s.Resize(firstRun)

def FillComboBox():
    for k, v in g.allcmds.items():
        # prevent doubles :
        if not str(k) in g.fm._comboBoxCmds.Items:
            g.fm._comboBoxCmds.Items.Add(str(k))

    