#######################################
### neoCL | Find and Replacer #########
#######################################

import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from neo_findreplace_funcs_main import WarningCategories

class FormSelCat(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkedListBoxCatSelector = System.Windows.Forms.CheckedListBox()
		self._checkBoxSelectAll = System.Windows.Forms.CheckBox()
		self._buttonInvert = System.Windows.Forms.Button()
		self._buttonClose = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# checkedListBoxCatSelector
		# 
		self._checkedListBoxCatSelector.FormattingEnabled = True
		#self._checkedListBoxCatSelector.Items.AddRange(System.Array[System.Object](["item 1", "item 2"]))
		self._checkedListBoxCatSelector.Location = System.Drawing.Point(0, 29)
		self._checkedListBoxCatSelector.Name = "checkedListBoxCatSelector"
		self._checkedListBoxCatSelector.Size = System.Drawing.Size(283, 439)
		self._checkedListBoxCatSelector.TabIndex = 0
		# 
		# checkBoxSelectAll
		# 
		self._checkBoxSelectAll.Location = System.Drawing.Point(3, 9)
		self._checkBoxSelectAll.Name = "checkBoxSelectAll"
		self._checkBoxSelectAll.Size = System.Drawing.Size(86, 23)
		self._checkBoxSelectAll.TabIndex = 1
		self._checkBoxSelectAll.Text = "Select All"
		self._checkBoxSelectAll.UseVisualStyleBackColor = True
		self._checkBoxSelectAll.Checked = True
		self._checkBoxSelectAll.CheckedChanged += self.CheckBoxSelectAllCheckedChanged
		# 
		# buttonInvert
		# 
		self._buttonInvert.Location = System.Drawing.Point(77, 4)
		self._buttonInvert.Name = "buttonInvert"
		self._buttonInvert.Size = System.Drawing.Size(100, 23)
		self._buttonInvert.TabIndex = 2
		self._buttonInvert.Text = "Invert Selection"
		self._buttonInvert.UseVisualStyleBackColor = True
		self._buttonInvert.Click += self.ButtonInvertClick
		# 
		# buttonClose
		# 
		self._buttonClose.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._buttonClose.Location = System.Drawing.Point(180, 4)
		self._buttonClose.Name = "buttonClose"
		self._buttonClose.Size = System.Drawing.Size(100, 23)
		self._buttonClose.TabIndex = 2
		self._buttonClose.Text = "Close"
		self._buttonClose.UseVisualStyleBackColor = True
		self._buttonClose.Click += self.ButtonCloseClick
		# 
		# FormCatSelector
		# 
		self.AcceptButton = self._buttonClose
		self.CancelButton = self._buttonClose
		self.ClientSize = System.Drawing.Size(284, 469)
		self.Controls.Add(self._checkedListBoxCatSelector)
		self.Controls.Add(self._buttonInvert)
		self.Controls.Add(self._checkBoxSelectAll)
		self.Controls.Add(self._buttonClose)
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
		self.Name = "FormCatSelector"
		self.Text = "neoCL | Find | Category Selector"
		self.ResumeLayout(False)
		self.TopMost = True
		self.ShowIcon = False
		self.Closing += self.FormCatSelectorClosing

	def ButtonCloseClick(self, sender, e):
		self.Hide()

	def CheckBoxSelectAllCheckedChanged(self, sender, e):
		for i in range(0, self._checkedListBoxCatSelector.Items.Count):
			self._checkedListBoxCatSelector.SetItemChecked(i, sender.Checked)

	def ButtonInvertClick(self, sender, e):
		for i in range(0, self._checkedListBoxCatSelector.Items.Count):
			checked = self._checkedListBoxCatSelector.GetItemChecked(i)
			self._checkedListBoxCatSelector.SetItemChecked(i, not checked)

	def FormCatSelectorClosing(self, sender, e):
		WarningCategories()

