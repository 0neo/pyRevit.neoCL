import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from neocl__funcs import neoCLFolderPath

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
		self.BackColor = self._pictureBox.BackColor
		self.TransparencyKey = self._pictureBox.BackColor
	
	def InitializeComponent(self):
		self._pictureBox = System.Windows.Forms.PictureBox()
		self._pictureBox.BeginInit()
		self.SuspendLayout()
		# 
		# pictureBox
		#
		self._pictureBox.ImageLocation = neoCLFolderPath() + r"pic\neoCL.Revit.splash_screen.png"
		self._pictureBox.Location = System.Drawing.Point(1, -1)
		self._pictureBox.Name = "pictureBox"
		self._pictureBox.Size = System.Drawing.Size(800, 400)
		self._pictureBox.TabIndex = 2
		self._pictureBox.TabStop = False
		self._pictureBox.Cursor = Cursors.Hand
		self._pictureBox.Click += self._OpenLink
		# 
		# Form
		# 
		self.ClientSize = System.Drawing.Size(800, 400)
		self.ControlBox = False
		self.Controls.Add(self._pictureBox)
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "Form"
		self.ShowIcon = False
		self.ShowInTaskbar = False
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.TopMost = True
		self.ResumeLayout(False)
		self.KeyDown += self._KeyDown

	def _KeyDown(self, sender, e):
		if e.KeyCode == Keys.Escape:
			self.Close()

	#def _Click(self, sender, e):
	#    self.Close()

	def _OpenLink(self, sender, e):
	    from neocl import runcmd
	    runcmd("@", msg="", recallCL=False)
	    self.Close()

def Main():
    f = Form1()
    f.ShowDialog()
