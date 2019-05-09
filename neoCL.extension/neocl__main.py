import clr
from neocl__setup import runcmdListBox
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
import System.Drawing
import System.Windows.Forms
import neocl__config as g
import neocl__setup as s
import neocl__intel as i
from System.Drawing import *
from System.Windows.Forms import *

class Formneocl(Form):
    def __init__(self, Modal=True):
        self.isFindMode = False
        self.modal = Modal
        self.mouseDown = False
        self.nouserinput = True
        self.lastLocation = Point()
        self.iWidth = 170
        self.iHeight = 23
        self.iColor = System.Drawing.Color.FromArgb(0, 120, 215)
        self.iColorF = System.Drawing.Color.White
        self.rColor = System.Drawing.Color.White
        self.rColorF = System.Drawing.Color.FromArgb(0, 46, 114)
        self.SelectedComoboxItem = ''
        self.InitializeComponent()
	    #self._labelneoCL.Parent = self._comboBoxCmds
        #self._labelneoCL.BackColor = System.Drawing.Color.Transparent

    def InitializeComponent(self):
        self._comboBoxCmds = System.Windows.Forms.ComboBox()
        self._listBoxCmds = System.Windows.Forms.ListBox()
        self._panelBorder = System.Windows.Forms.Panel()
        self._labelneoCL = System.Windows.Forms.Label()
        self.SuspendLayout()
	# 
	# panelBorder
	# 
        self._panelBorder.BackColor = self.iColor
        self._panelBorder.Location = System.Drawing.Point(0, 0)
        self._panelBorder.Name = "panelBorder"
        self._panelBorder.Size = System.Drawing.Size(self.iWidth, self.iHeight)
        self._panelBorder.TabIndex = 2
        self._panelBorder.MouseDown += self._MouseDown
        self._panelBorder.MouseMove += self._MouseMove
        self._panelBorder.MouseUp += self._MouseUp
        # 
        # comboBoxCmds
        # 
        self._comboBoxCmds.FormattingEnabled = False
        self._comboBoxCmds.CausesValidation = False
        self._comboBoxCmds.ImeMode = System.Windows.Forms.ImeMode.Off
        self._comboBoxCmds.BackColor = self.iColor
        self._comboBoxCmds.ForeColor = self.iColorF
        self._comboBoxCmds.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        self._comboBoxCmds.Location = System.Drawing.Point(1, 1)
        self._comboBoxCmds.Name = "comboBoxCmds"
        #self._comboBoxCmds.SelectedIndex = -1
        self._comboBoxCmds.Sorted = True
        self._comboBoxCmds.Size = System.Drawing.Size(self.iWidth - 2, self.iHeight - 2)
        self._comboBoxCmds.TabIndex = 0
        self._comboBoxCmds.Text = "neoCL"    
        self._comboBoxCmds.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.None
        self._comboBoxCmds.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.None
        self._comboBoxCmds.MouseDown += self._MouseDown
        self._comboBoxCmds.MouseMove += self._MouseMove
        self._comboBoxCmds.MouseUp += self._MouseUp
        self._comboBoxCmds.KeyDown += self._KeyDown
        self._comboBoxCmds.KeyPress += self._KeyPress
        self._comboBoxCmds.TextUpdate += self._comboBoxCmdsTextUpdate
        self._comboBoxCmds.SelectedIndexChanged += self._comboBoxCmdsTextUpdate
        self._comboBoxCmds.DropDown += self._DropDown
        self._comboBoxCmds.DropDownClosed += self._DropDownClosed
        self._comboBoxCmds.SelectionChangeCommitted += self._SelectionChangeCommitted
        self._comboBoxCmds.SelectedIndexChanged += self._SelectedIndexChanged
        self._comboBoxCmds.TextChanged += self._TextChanged
	# 
	# labelneoCL
	# 
        self._labelneoCL.Visible = False
        self._labelneoCL.BackColor = self.rColor
        self._labelneoCL.ForeColor = self.iColor
        self._labelneoCL.Name = "labelneoCL"
        self._labelneoCL.Text = "neoCL"
        self._labelneoCL.Size = System.Drawing.Size(38, 14)
        self._labelneoCL.TabIndex = 3
        self._labelneoCL.MouseDown += self._MouseDown
        self._labelneoCL.MouseMove += self._MouseMove
        self._labelneoCL.MouseUp += self._MouseUp
        # 
        # listBoxCmds
        # 
        self._listBoxCmds.BackColor = self.iColor
        self._listBoxCmds.ForeColor = self.iColorF
        self._listBoxCmds.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._listBoxCmds.FormattingEnabled = True
        self._listBoxCmds.Location = System.Drawing.Point(1, 23)
        self._listBoxCmds.Name = "listBoxCmds"
        #self._listBoxCmds.Size = System.Drawing.Size(20, 20)
        self._listBoxCmds.MaximumSize = System.Drawing.Size(0, 300)
        self._listBoxCmds.TabIndex = 1
        self._listBoxCmds.IntegralHeight = False
        self._listBoxCmds.MouseDown += self._MouseDown
        self._listBoxCmds.MouseMove += self._MouseMove
        self._listBoxCmds.MouseUp += self._MouseUp
        self._listBoxCmds.KeyDown += self._KeyDown
        self._listBoxCmds.KeyPress += self._KeyPress
        self._listBoxCmds.DoubleClick += self._DoubleClick
        self._listBoxCmds.MouseWheel += self._MouseWheel
        self._listBoxCmds.Resize += self._Resize
        # 
        # Formneocl
        # 
        self.StartPosition = System.Windows.Forms.FormStartPosition.Manual
        self.Location = Point(Cursor.Position.X, Cursor.Position.Y)
        self.BackColor = System.Drawing.Color.White
        self.AutoScale = True
        #self.ClientSize = System.Drawing.Size(20, 20)
        #self.Size = System.Drawing.Size(20, 50)
        self.MaximumSize = System.Drawing.Size(self.iWidth, self.iHeight)
        self.MinimumSize = System.Drawing.Size(self.iWidth, self.iHeight)
        self.Controls.Add(self._labelneoCL)
        self.Controls.Add(self._comboBoxCmds)
        self.Controls.Add(self._listBoxCmds)
        self.Controls.Add(self._panelBorder)
        #self.ForeColor = System.Drawing.SystemColors.Highlight
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None
        self.MouseDown += self._MouseDown
        self.MouseMove += self._MouseMove
        self.MouseUp += self._MouseUp
        self.KeyDown += self._KeyDown
        self.KeyPress += self._KeyPress
        self.Name = "FormneoCL"
        self.ShowIcon = False
        self.TopMost = True
        self.Text = "neoCL | neo Command Line"
        self.ResumeLayout(False)

    def UpdateneoCLlabelPosition(self):        
        self._labelneoCL.Location = System.Drawing.Point(self._comboBoxCmds.Width - 55, 5)
        self._labelneoCL.Visible = True

    def ShowMe(self, isModal=False, isModeless=False):
        s.ShowneoCL(isModal, isModeless, self.isFindMode)

    def _MouseDown(self, sender, e):
        self.mouseDown = True
        self.lastLocation = e.Location

    def _MouseMove(self, sender, e):
        if self.mouseDown:
            self.Location = Point(
                (self.Location.X - self.lastLocation.X) + e.X,
                (self.Location.Y - self.lastLocation.Y) + e.Y)
            self.Update()

    def _MouseUp(self, sender, e):
        self.mouseDown = False

    def GotoMouse(self):
        self.Location = Point(Cursor.Position.X, Cursor.Position.Y)
        self.Update()

    def _MouseWheel(self, sender, e):
        #sender.Visible = False
        #sender.Visible = True
        e.Handled = True    # ignore pressed key
        if sender.Items.Count > 0:
            rows = e.Delta / 120
            rows = rows * -1
            rows += sender.SelectedIndex
            if rows > sender.Items.Count - 1:
                rows = sender.Items.Count - 1
            elif rows < 0:
                rows = 0
            sender.SetSelected(rows, True)

    def _KeyDown(self, sender, e):
        # make sure that the inicial text (neoCL) in combobox is deleted:
        if self.nouserinput:
            self.nouserinput = False
            self._comboBoxCmds.Text = ''
        if e.KeyCode == Keys.Escape:
            self.Close()
        elif e.KeyCode == Keys.Enter or e.KeyCode == Keys.Space:
            if sender.Name == self._comboBoxCmds.Name and not self.isFindMode:
                s.runcmdComboBox()
            elif sender.Name == self._listBoxCmds.Name:
                s.runcmdListBox()
            #e.Handle = True        <---------------------------------------------------------
        elif e.KeyCode == Keys.Down:
            if sender.Name == self._comboBoxCmds.Name:
                e.Handled = True    # ignore pressed key
                #self._listBoxCmds.SelectedIndex = 0
                #self._listBoxCmds.UpdateLayout()
                self._listBoxCmds.Focus()
                SendKeys.SendWait("{DOWN}")
        #elif sender.Name == self._listBoxCmds.Name:
        #    if not e.KeyCode == Keys.Down and not e.KeyCode == Keys.Up:
        #        self._comboBoxCmds.Focus()
        #        if not e.KeyCode == Keys.Left and not e.KeyCode == Keys.Right:
        #            SendKeys.SendWait(str(e.KeyCode))

    def _KeyPress(self, sender, e):
        #if sender.Name == self._comboBoxCmds.Name:
        #    if sender.Text: sender.Items.Clear()
        if sender.Name == self._listBoxCmds.Name:
            self._comboBoxCmds.Focus()
            if not e.KeyChar != " ":
                SendKeys.SendWait(str(e.KeyChar))
        #g.fm._comboBoxCmds.SelectionStart = len(g.fm._comboBoxCmds.Text)
        
    def _DoubleClick(self, sender, e):
        if sender.Name == self._listBoxCmds.Name:
            s.runcmdListBox()

    def _comboBoxCmdsTextUpdate(self, sender, e):
        #self.SelectedComoboxItem = sender.Text
        i.UpdateListBox()
        #self._comboBoxCmds.Refresh()
        #self._comboBoxCmds.Items.Clear()
        #s.UpdateDrawing()
        #self._comboBoxCmds.Refresh()
        #self.Text = self.SelectedComoboxItem
        pass

    def _Resize(self, sender, e):
        pass

    def _DropDown(self, sender, e):
        # for some reason can't cancel autocomplete, so fill and delete items when user demand it
        i.FillComboBox()
        pass

    def _DropDownClosed(self, sender, e):
        # for some reason can't cancel autocomplete, so fill and delete items when user demand it
        #val = sender.Items[sender.SelectedIndex]
        #g.tmp = sender.Text
        #print g.tmp
        #sender.Items.Clear()
        #sender.Text = val    
        #g.fm._comboBoxCmds.SelectedIndex = -1
        #g.fm._comboBoxCmds.Items.Clear()
        #self._comboBoxCmds.ResetText()
        #self.SelectedComoboxItem = sender.SelectedItem
        #self._comboBoxCmds.Items.Clear()
        #self._comboBoxCmds.Items.Add(self.SelectedComoboxItem)
        #self._comboBoxCmds.DataSource = None
        #self._comboBoxCmds.Items.Clear()
        pass

    def _SelectionChangeCommitted(self, sender, e):
        pass
        #print("selec change")
        #self.SelectedComoboxItem = sender.Text
        #self._listBoxCmds.Focus()
        #g.fm._comboBoxCmds.Items.Clear()
        #sender.Text = self.SelectedComoboxItem    

    def _SelectedIndexChanged(self, sender, e):
        #self.SelectedComoboxItem = sender.Text
        #sender.SelectedIndex = -1
        #self._listBoxCmds.Focus()
        #g.fm._comboBoxCmds.Items.Clear()
        #sender.Text = self.SelectedComoboxItem         
        #return
        for i in range(sender.Items.Count - 1, 0, -1):
            #print sender.Items[i] + ' | ' + sender.Text
            if sender.Items[i] != sender.Text:
                sender.Items.RemoveAt(i)  
        return
        print(self.SelectedComoboxItem)
        s.UpdateDrawing()
        self._comboBoxCmds.Text = self.SelectedComoboxItem
        pass

    def _TextChanged(self, sender, e):
        #val = sender.Text
        #sender.Items.Clear()
        #sender.Text = val
        pass

def Main(isModal=True, isFindMode=False):
    g.fm = Formneocl(isModal)
    g.fm.isFindMode = isFindMode
    s.Setup()
    g.fm.ShowMe()