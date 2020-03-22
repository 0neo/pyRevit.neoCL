import System
import collections
import neocl__main
import neocl__config as g
import neocl__intel as i
from neocl import GetAllcmdlist, runcmd, CanRecallneoCL
from neocl__funcs import neoCLFolderPath, neoAlert

def GenerateFalsecmdstr(cmds, nr):
    # Programmer only
	for c in range(0, nr):
		cm = 'cmd{n:03d}'.format(n=c)
		ds = 'False command to test neoCL form behavior cmd{n:03d}'.format(n=c)
		cmds.update({cm:ds})
	return cmds

g.allcmds = GetAllcmdlist()
#g.allcmds = GenerateFalsecmdstr(g.allcmds, 999)
g.allcmds = collections.OrderedDict(sorted(g.allcmds.items()))

def Setup(FirstRun=False, setCMD=''):
    if g.isred: easternneocl('myneoclisred')
    if g.fm.isFindMode: FindMode(FirstRun)
    if setCMD: g.fm._comboBoxCmds.Text = setCMD  
    #i.UpdateListBox(True)

def Resize(firstRun=False):
    
    if not firstRun:
        
        # Refresh AutoSize
        g.fm._listBoxCmds.Width = 0
        g.fm._listBoxCmds.AutoSize = True
        
        g.fm.MaximumSize = System.Drawing.Size(0, 0)
        g.fm.MinimumSize = System.Drawing.Size(0, 0)
        
        #nItems = min(g.fm._listBoxCmds.Items.Count, 10)
        g.fm._listBoxCmds.Height = g.fm._listBoxCmds.Items.Count * 11
        g.fm._listBoxCmds.Width = g.fm._listBoxCmds.Width + 10
        
        w = g.fm._listBoxCmds.Width + 5
        h = g.fm._listBoxCmds.Height + 3

        g.fm._listBoxCmds.Width = w
        
        if g.fm._listBoxCmds.Items.Count > 0:
            h += g.fm._comboBoxCmds.Height
        else:
            h = 23
            w = g.fm.iWidth
        
        g.fm.Width = w + 2
        g.fm.Height = h 
        g.fm._panelBorder.Width = w + 3
        g.fm._panelBorder.Height = h
        g.fm._comboBoxCmds.Width = w
        g.fm.UpdateneoCLlabelPosition()

        neoCLRunningColors()
        UpdateDrawing()

def UpdateDrawing():
    # To solve a graphical problem at the right of the form
    # while resizing the dropbox is not correctly updated
    # Force update of the drawing :
    g.fm._comboBoxCmds.Focus()
    g.fm._comboBoxCmds.SelectionStart = len(g.fm._comboBoxCmds.Text)
    g.fm._comboBoxCmds.SelectionLength = 0
    g.fm.Update()

def neoCLRunningColors():
    g.fm._comboBoxCmds.BackColor = g.fm.rColor
    g.fm._comboBoxCmds.ForeColor = g.fm.rColorF
    g.fm._listBoxCmds.BackColor = g.fm.rColor
    g.fm._listBoxCmds.ForeColor = g.fm.rColorF
        
def runcmdComboBox():
    runcmdneoCL(g.fm._comboBoxCmds.Text)

def runcmdListBox():
    cmd = g.fm._listBoxCmds.SelectedItems[0]
    cmd = cmd[:cmd.find('\t')]
    runcmdneoCL(cmd)

def runcmdneoCL(cmd):
    if cmd == 'q':
        g.fm.Dispose()
    elif cmd != '':
        modal = g.fm.modal
        #g.fm.Visible = False
        #g.fm.TopMost = False
        g.fm.Dispose()
        runcmd(cmd, 'neoCL Form', False)
        if g.op_recallneocl:
            if CanRecallneoCL(cmd):
                g.fm.ShowMe(modal, not modal)
                #g.fm.ShowMe(modal, not modal, '?')

def ShowneoCL(isModal=False, isModeless=False, isFindMode=False, setCMD=''):
    ForceMode = isModal or isModeless
    g.fm.Dispose()
    if isModal or (not ForceMode and g.fm.modal):
        g.fm = neocl__main.Formneocl(True)
        g.fm.isFindMode = isFindMode
        Setup(False, setCMD)
        g.fm.ShowDialog()
    elif isModeless or (not ForceMode and not g.fm.modal):
        g.fm = neocl__main.Formneocl(False)
        g.fm.isFindMode = isFindMode
        Setup(False, setCMD)
        g.fm.Show()

def FindMode(FirstRun=False):
    #forc = System.Drawing.Color.FromArgb(255, 93, 0)
    forc = System.Drawing.Color.FromArgb(224, 63, 0)
    g.fm.rColorF = forc
    g.fm._comboBoxCmds.ForeColor = forc
    g.fm._listBoxCmds.ForeColor = forc
    g.fm._panelBorder.BackColor = forc
    g.fm._labelneoCL.ForeColor = forc
    g.fm._comboBoxCmds.Text = 'Search in description mode:'
    g.fm.nouserinput = True

# E.Egg ### ################################################
def easternneocl(usercmd, FirstRun=False):
    
    iseEgg = False
    isred = usercmd.lower() == 'myneoclisred'
    isalwred = usercmd.lower() == 'myneoclisalwaysred'
    isnotalwred = usercmd.lower() == 'myneoclisnotalwaysred'
    
    if isred or isalwred:
        eEgg_isred(isred, isalwred, FirstRun)
        iseEgg = True
    elif isnotalwred:
        eEgg_isnotred()
        iseEgg = True
        
    return iseEgg

def eEgg_isnotred():
    g.WriteVar('E.EGG', '_isred', False)
    g.isred = False
    g.fm.iColor = System.Drawing.Color.FromArgb(0, 120, 215)
    g.fm.iColorF = System.Drawing.Color.White
    g.fm.rColor = System.Drawing.Color.White
    g.fm.rColorF = System.Drawing.Color.FromArgb(0, 46, 114)
    g.fm._comboBoxCmds.BackColor = g.fm.iColor
    g.fm._comboBoxCmds.ForeColor = g.fm.iColorF
    g.fm._listBoxCmds.BackColor = g.fm.iColor
    g.fm._listBoxCmds.ForeColor = g.fm.iColorF
    g.fm._labelneoCL.BackColor = g.fm.rColor
    g.fm._labelneoCL.ForeColor = g.fm.iColor
    g.fm._panelBorder.BackColor = g.fm.iColor
    neoCLRunningColors()
    g.fm._comboBoxCmds.Text = '?'
    i.UpdateListBox(False)
    if g.fm.isFindMode: FindMode(False)

def eEgg_isred(isred, isalwred, FirstRun):
    g.isred = True
    forc = System.Drawing.Color.Red
    bacc = System.Drawing.Color.Black
    g.fm.rColor = bacc
    g.fm.rColorF = forc
    g.fm._comboBoxCmds.BackColor = bacc
    g.fm._comboBoxCmds.ForeColor = forc
    g.fm._listBoxCmds.BackColor = bacc
    g.fm._listBoxCmds.ForeColor = forc
    g.fm._panelBorder.BackColor = forc
    g.fm._labelneoCL.BackColor = bacc
    g.fm._labelneoCL.ForeColor = forc
    if FirstRun:
        g.fm._comboBoxCmds.Text = '?'
        g.fm._listBoxCmds.MaximumSize = System.Drawing.Size(0, 600)
        i.UpdateListBox(False)
        g.fm._comboBoxCmds.Text = '[Easter Egg] All commands in red :'
        if isred:
            neoAlert("Your neoCL is now black/red!\nTo keep it always red type: " + \
                     "myneoclisalwaysred\n(my neoCL is always red)", \
                     title="Easter Egg", header="neoCL")
            g.fm.TopMost = True
        g.fm.nouserinput = True
    if isalwred:
        g.WriteVar('E.EGG', '_isred', True)
        g.fm._comboBoxCmds.Text = '?'
        i.UpdateListBox(False)
        g.fm._comboBoxCmds.Text = 'To revert : myneoclisnotalwaysred'
        g.fm.nouserinput = False
        neoAlert("Your neoCL is now always black/red!\nTo revert it remember to type: " + \
                 "myneoclisnotalwaysred\n(my neoCL is not always red)", \
                 title="Easter Egg", header="neoCL")
        g.fm.TopMost = True

#def Processcmds():
#    p = 1
#    for k, v in g.allcmds.items():
#        cmd(str(k), str(v), p)
#        p += 1

#def FillComboBox():
#	for k, v in g.allcmds.items():
#		g.fm._comboBoxCmds.Items.Add(str(k))

#def FillListBox():
#	for k, v in g.allcmds.items():
#		g.fm._listBoxCmds.Items.Add('[' + str(k) + ']\t' + str(v))


#class cmd:
#    
#    def __init__(self, k, v, p):
#        self.k = k
#        self.v = v
#        self.p = p
#        self.dic = {k : v}
#        self.AddMeToComboBox()
#        self.AddMeToListBox()
#        self.AddMeToActivecmds()
#
#    def AddMeToComboBox(self):
#        g.fm._comboBoxCmds.Items.Add(str(self.k))
#
#    def AddMeToListBox(self):
#        g.fm._listBoxCmds.Items.Add('[' + str(self.k) + ']\t' + str(self.v))
#
#    def AddMeToAllcmdslist(self):
#        g.allcmdslist.append(self)
#
#    def RemoveMeFromComboBox(self):
        # not compatible usabel
        # listbox is updated to user input
        # but combobox has allways all commands
        # so diferent positions
#        g.fm._comboBoxCmds.Items.RemoveAt(self.p)
        #g.fm.Update()

#    def RemoveMeFromListBox(self):
#        g.fm._listBoxCmds.Items.RemoveAt(self.p)
        #g.fm.Update()

#    def RemoveMeFromAllcmdslist(self):
#        g.allcmdslist.remove(self)
        #g.fm.Update()

#    def killme(self):
#        RemoveMeFromComboBox()
#        RemoveMeFromListBox()
#        RemoveMeFromActivecmds()
#       del self