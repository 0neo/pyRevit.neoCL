import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

import System.Drawing
import System.Windows.Forms
import neo_increment_funcs as f
import neo_increment_config as g

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
		self.mouseDown = False
		self.lastLocation = Point()
	
	def InitializeComponent(self):
		self._comboBoxPams = System.Windows.Forms.ComboBox()
		self._labelneocl = System.Windows.Forms.Label()
		self._buttonStart = System.Windows.Forms.Button()
		self._labelLog = System.Windows.Forms.Label()
		self._buttonRef = System.Windows.Forms.Button()
		self._buttonClose = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# comboBoxPams
		# 
		self._comboBoxPams.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
		self._comboBoxPams.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._comboBoxPams.ForeColor = System.Drawing.Color.White
		self._comboBoxPams.FormattingEnabled = True
		self._comboBoxPams.Location = System.Drawing.Point(8, 12)
		self._comboBoxPams.Name = "comboBoxPams"
		self._comboBoxPams.Size = System.Drawing.Size(314, 21)
		self._comboBoxPams.TabIndex = 0
		self._comboBoxPams.Text = "Select Parameter..."
		self._comboBoxPams.SelectedIndexChanged  += self._SelectedIndexChanged 
		# 
		# labelneocl
		# 
		self._labelneocl.ForeColor = System.Drawing.Color.Gray
		self._labelneocl.Location = System.Drawing.Point(260, 15)
		self._labelneocl.Name = "labelneocl"
		self._labelneocl.Size = System.Drawing.Size(42, 17)
		self._labelneocl.TabIndex = 1
		self._labelneocl.Text = "neoCL"
		self._labelneocl.MouseDown += self._MouseDown
		self._labelneocl.MouseMove += self._MouseMove
		self._labelneocl.MouseUp += self._MouseUp
		# 
		# buttonStart
		# 
		self._buttonStart.BackColor = System.Drawing.Color.Green
		self._buttonStart.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._buttonStart.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._buttonStart.Location = System.Drawing.Point(8, 39)
		self._buttonStart.Name = "buttonStart"
		self._buttonStart.Size = System.Drawing.Size(100, 23)
		self._buttonStart.TabIndex = 2
		self._buttonStart.Text = "Start"
		self._buttonStart.UseVisualStyleBackColor = False
		self._buttonStart.Click += self._ButtonStartClick
		# 
		# labelLog
		# 
		self._labelLog.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._labelLog.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._labelLog.Location = System.Drawing.Point(8, 70)
		self._labelLog.Name = "labelLog"
		self._labelLog.Size = System.Drawing.Size(314, 38)
		self._labelLog.TabIndex = 1
		self._labelLog.Text = "Select an instance as reference to list its parammeters."
		self._labelLog.MouseDown += self._MouseDown
		self._labelLog.MouseMove += self._MouseMove
		self._labelLog.MouseUp += self._MouseUp
		# 
		# buttonRef
		# 
		self._buttonRef.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._buttonRef.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._buttonRef.Location = System.Drawing.Point(115, 39)
		self._buttonRef.Name = "buttonRef"
		self._buttonRef.Size = System.Drawing.Size(100, 23)
		self._buttonRef.TabIndex = 3
		self._buttonRef.Text = "Select New Ref."
		self._buttonRef.UseVisualStyleBackColor = True
		self._buttonRef.Click += self._ButtonRefClick
		# 
		# buttonClose
		# 
		self._buttonClose.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._buttonClose.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._buttonClose.Location = System.Drawing.Point(222, 39)
		self._buttonClose.Name = "buttonClose"
		self._buttonClose.Size = System.Drawing.Size(100, 23)
		self._buttonClose.TabIndex = 4
		self._buttonClose.Text = "Close"
		self._buttonClose.UseVisualStyleBackColor = True
		self._buttonClose.Click += self._ButtonCloseClick
		# 
		# FormIncPV
		# 
		self.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
		self.CancelButton = self._buttonClose
		self.ClientSize = System.Drawing.Size(330, 115)
		self.Controls.Add(self._buttonClose)
		self.Controls.Add(self._buttonRef)
		self.Controls.Add(self._buttonStart)
		self.Controls.Add(self._labelneocl)
		self.Controls.Add(self._comboBoxPams)
		self.Controls.Add(self._labelLog)
		self.ForeColor = System.Drawing.Color.White
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "FormIncPV"
		self.ShowIcon = False
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent
		self.Text = "neoCL"
		self.TopMost = True
		self.ResumeLayout(False)
		self.MouseDown += self._MouseDown
		self.MouseMove += self._MouseMove
		self.MouseUp += self._MouseUp
		
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

	def _ButtonCloseClick(self, sender, e):
		self.Dispose()

	def _ButtonRefClick(self, sender, e):
		#self.Dispose()
		f.SelectRef()

	def _ButtonStartClick(self, sender, e):
		f.Start()

	def _SelectedIndexChanged(self, sender, e):
		print("Seting pm val:")
		g.pmTag = sender.Text
		g.pmVal = g.elRef.parameters[g.pmTag]
		print(g.pmVal )

def Main():
	g.fm = Form1()
	g.fm.ShowDialog()
	#f.SelectRef()
	print("Done!")