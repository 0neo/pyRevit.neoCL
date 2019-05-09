#######################################
### Find.neoCL   ######################
### by neo 		 ######################
### 2019 		 ######################
#######################################
### neoCL | Find and Replacer #########
#######################################

import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
import neo_findreplace_config as g
import neo_findreplace_funcs_main as f
import neo_findreplace_catsel as fsc

class FormFind(Form):
	def __init__(self):
		self.FreezeEventsMode = False	# To cancel non wanted events when is loading defaults 
		self.ReplaceFreeze = False
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._buttonFind = System.Windows.Forms.Button()
		self._buttonClose = System.Windows.Forms.Button()
		#self._listBoxResult = System.Windows.Forms.ListBox()
		self._labelbyneo = System.Windows.Forms.Label()
		self._labelToFind = System.Windows.Forms.Label()
		self._labelReplace = System.Windows.Forms.Label()
		self._buttonReplaceSelected = System.Windows.Forms.Button()
		self._buttonReplaceAll = System.Windows.Forms.Button()
		self._groupBoxOptions = System.Windows.Forms.GroupBox()
		self._checkBoxCaseSensitive = System.Windows.Forms.CheckBox()
		self._checkBoxFullWord = System.Windows.Forms.CheckBox()
		self._checkBoxFullParameter = System.Windows.Forms.CheckBox()
		self._checkBoxLinks = System.Windows.Forms.CheckBox()
		self._checkBoxIgnoreTags = System.Windows.Forms.CheckBox()
		self._checkBoxMatch = System.Windows.Forms.CheckBox()
		self._MatchModeToolTip = System.Windows.Forms.ToolTip(self._components)
		self._buttonSelectionAll = System.Windows.Forms.Button()
		self._buttonSelectionSelected = System.Windows.Forms.Button()
		self._labelCreateSelection = System.Windows.Forms.Label()
		self._checkBoxSearchTypes = System.Windows.Forms.CheckBox()
		self._labelFoundLog = System.Windows.Forms.Label()
		self._radioButtonFindInProject = System.Windows.Forms.RadioButton()
		self._radioButtonFindInView = System.Windows.Forms.RadioButton()
		self._radioButtonFindInSel = System.Windows.Forms.RadioButton()
		self._labelFindIn = System.Windows.Forms.Label()
		self._checkBoxModal = System.Windows.Forms.CheckBox()
		self._checkBoxSaveDefaults = System.Windows.Forms.CheckBox()
		self._comboBoxFind = System.Windows.Forms.ComboBox()
		self._comboBoxReplace = System.Windows.Forms.ComboBox()
		self._listViewResult = System.Windows.Forms.ListView()
		self._value = System.Windows.Forms.ColumnHeader()
		self._parameter = System.Windows.Forms.ColumnHeader()
		self._type = System.Windows.Forms.ColumnHeader()
		self._family = System.Windows.Forms.ColumnHeader()
		self._level = System.Windows.Forms.ColumnHeader()
		self._category = System.Windows.Forms.ColumnHeader()
		self._id = System.Windows.Forms.ColumnHeader()
		#self._buttonSpecifyCat = System.Windows.Forms.Button()
		self._linkLabelSpecifyCat = System.Windows.Forms.LinkLabel()
		self._linkLabelWarningCat = System.Windows.Forms.LinkLabel()
		self._linkLabelSaveTable = System.Windows.Forms.LinkLabel()
		self._checkBoxKeepSaveDefaults = System.Windows.Forms.CheckBox()
		self._groupBoxOptions.SuspendLayout()
		self.SuspendLayout()
		# 
		# checkBoxKeepSaveDefaults
		# 
		self._checkBoxKeepSaveDefaults.Enabled = True
		self._checkBoxKeepSaveDefaults.ImageAlign = System.Drawing.ContentAlignment.BottomRight
		self._checkBoxKeepSaveDefaults.Location = System.Drawing.Point(612, 121)
		self._checkBoxKeepSaveDefaults.Name = "checkBoxKeepSaveDefaults"
		self._checkBoxKeepSaveDefaults.Size = System.Drawing.Size(60, 18)
		self._checkBoxKeepSaveDefaults.TabIndex = 15
		self._checkBoxKeepSaveDefaults.Text = "Always"
		self._checkBoxKeepSaveDefaults.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._checkBoxKeepSaveDefaults.UseVisualStyleBackColor = True
		# 
		# linkLabelSpecifyCat
		# 
		self._linkLabelSpecifyCat.Cursor = System.Windows.Forms.Cursors.Hand
		self._linkLabelSpecifyCat.LinkBehavior = System.Windows.Forms.LinkBehavior.NeverUnderline
		self._linkLabelSpecifyCat.Location = System.Drawing.Point(319, 88)
		self._linkLabelSpecifyCat.Name = "linkLabelSpecifyCat"
		self._linkLabelSpecifyCat.Size = System.Drawing.Size(126, 18)
		self._linkLabelSpecifyCat.TabIndex = 16
		self._linkLabelSpecifyCat.TabStop = True
		self._linkLabelSpecifyCat.Text = "[+] Specify categories..."
		self._linkLabelSpecifyCat.Click += self.LinkLabelSpecifyCatClick
		# 
		# linkLabelWarningCat
		# 
		self._linkLabelWarningCat.Cursor = System.Windows.Forms.Cursors.Hand
		self._linkLabelWarningCat.LinkBehavior = System.Windows.Forms.LinkBehavior.NeverUnderline
		self._linkLabelWarningCat.LinkColor = System.Drawing.Color.Red
		self._linkLabelWarningCat.Location = System.Drawing.Point(329, 125)
		self._linkLabelWarningCat.Name = "linkLabelWarningCat"
		self._linkLabelWarningCat.Size = System.Drawing.Size(160, 13)
		self._linkLabelWarningCat.TabIndex = 17
		self._linkLabelWarningCat.TabStop = True
		self._linkLabelWarningCat.Text = "Not searching in all categories!"
		self._linkLabelWarningCat.Visible = False
		self._linkLabelWarningCat.Click += self.LinkLabelSpecifyCatClick
		# 
		# linkLabelSaveTable
		# 
		self._linkLabelSaveTable.Cursor = System.Windows.Forms.Cursors.Hand
		self._linkLabelSaveTable.LinkBehavior = System.Windows.Forms.LinkBehavior.NeverUnderline
		self._linkLabelSaveTable.Location = System.Drawing.Point(g.savetableX, g.savetableY)
		self._linkLabelSaveTable.Name = "linkLabelSaveTable"
		self._linkLabelSaveTable.Size = System.Drawing.Size(75, 11)
		#self._linkLabelSaveTable.AutoSize = False
		#self._linkLabelSaveTable.TextAlign = ContentAlignment.MiddleRight
		#self._linkLabelSaveTable.HorizontalContentAlignment = HorizontalAlignment.Right
		self._linkLabelSaveTable.TabIndex = 17
		self._linkLabelSaveTable.TabStop = True
		self._linkLabelSaveTable.Text = "save table..."
		self._linkLabelSaveTable.Click += self.LinkLabelSaveTableClick
		# 
		# buttonSpecifyCat
		# 
		#self._buttonSpecifyCat.BackColor = System.Drawing.SystemColors.Control
		#self._buttonSpecifyCat.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		#self._buttonSpecifyCat.Font = System.Drawing.Font("Microsoft Sans Serif", 6.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		#self._buttonSpecifyCat.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		#self._buttonSpecifyCat.Location = System.Drawing.Point(319, 86)
		#self._buttonSpecifyCat.Margin = System.Windows.Forms.Padding(0)
		#self._buttonSpecifyCat.Name = "buttonSpecifyCat"
		#self._buttonSpecifyCat.Size = System.Drawing.Size(126, 22)
		#self._buttonSpecifyCat.TabIndex = 15
		#self._buttonSpecifyCat.Text = "[+] Specify categories..."
		#self._buttonSpecifyCat.UseVisualStyleBackColor = False
		#self._buttonSpecifyCat.Click += self.ButtonSpecifyCatClick
		# 
		# buttonFind
		# 
		self._buttonFind.Location = System.Drawing.Point(g.btfindX, g.btfindY)
		self._buttonFind.Name = "buttonFind"
		self._buttonFind.Size = System.Drawing.Size(150, 30)
		self._buttonFind.TabIndex = 5
		self._buttonFind.Text = "Find"
		self._buttonFind.UseVisualStyleBackColor = True
		self._buttonFind.Click += self.ButtonFindClick
		# 
		# buttonClose
		# 
		self._buttonClose.DialogResult = System.Windows.Forms.DialogResult.Cancel
		self._buttonClose.Location = System.Drawing.Point(g.btcloseX, g.btcloseY)
		self._buttonClose.Name = "buttonClose"
		self._buttonClose.Size = System.Drawing.Size(150, 30)
		self._buttonClose.TabIndex = 1
		self._buttonClose.Text = "Close"
		self._buttonClose.UseVisualStyleBackColor = True
		self._buttonClose.Click += self.ButtonCloseClick
		# 
		# listBoxResult
		# 
		#self._listBoxResult.FormattingEnabled = True
		#self._listBoxResult.Location = System.Drawing.Point(12, 141)
		#self._listBoxResult.Name = "listBoxResult"
		#self._listBoxResult.Size = System.Drawing.Size(760, 173)
		#self._listBoxResult.TabIndex = 2
		#self._listBoxResult.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended
		#self._listBoxResult.SelectedIndexChanged += self.ListBoxResultSelectedIndexChanged
		#self._listBoxResult.DoubleClick += self.ListBoxResultDoubleClick
		# 
		# labelbyneo
		# 
		self._labelbyneo.ForeColor = System.Drawing.SystemColors.Highlight
		self._labelbyneo.ImageAlign = System.Drawing.ContentAlignment.TopRight
		self._labelbyneo.Location = System.Drawing.Point(397, -1)
		self._labelbyneo.Name = "labelbyneo"
		self._labelbyneo.Size = System.Drawing.Size(52, 24)
		self._labelbyneo.TabIndex = 3
		self._labelbyneo.Text = "by neo"
		self._labelbyneo.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# labelToFind
		# 
		self._labelToFind.Location = System.Drawing.Point(12, 13)
		self._labelToFind.Name = "labelToFind"
		self._labelToFind.Size = System.Drawing.Size(55, 20)
		self._labelToFind.TabIndex = 4
		self._labelToFind.Text = "Find :"
		self._labelToFind.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# labelReplace
		# 
		self._labelReplace.Location = System.Drawing.Point(12, 39)
		self._labelReplace.Name = "labelReplace"
		self._labelReplace.Size = System.Drawing.Size(55, 20)
		self._labelReplace.TabIndex = 4
		self._labelReplace.Text = "Replace :"
		self._labelReplace.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# buttonReplaceSelected
		# 
		self._buttonReplaceSelected.Enabled = False
		self._buttonReplaceSelected.Location = System.Drawing.Point(g.btrslX, g.btrslY)
		self._buttonReplaceSelected.Name = "buttonReplaceSelected"
		self._buttonReplaceSelected.Size = System.Drawing.Size(150, 30)
		self._buttonReplaceSelected.TabIndex = 6
		self._buttonReplaceSelected.Text = "Replace Selected"
		self._buttonReplaceSelected.UseVisualStyleBackColor = True
		self._buttonReplaceSelected.Click += self.ButtonReplaceSelectedClick
		# 
		# buttonReplaceAll
		# 
		self._buttonReplaceAll.Enabled = False
		self._buttonReplaceAll.Location = System.Drawing.Point(g.btrallX, g.btrallY)
		self._buttonReplaceAll.Name = "buttonReplaceAll"
		self._buttonReplaceAll.Size = System.Drawing.Size(150, 30)
		self._buttonReplaceAll.TabIndex = 6
		self._buttonReplaceAll.Text = "Replace All"
		self._buttonReplaceAll.UseVisualStyleBackColor = True
		self._buttonReplaceAll.Click += self.ButtonReplaceAllClick
		# 
		# groupBoxOptions
		# 
		#self._groupBoxOptions.Controls.Add(self._buttonSpecifyCat)
		self._groupBoxOptions.Controls.Add(self._linkLabelSpecifyCat)
		self._groupBoxOptions.Controls.Add(self._labelbyneo)
		self._groupBoxOptions.Controls.Add(self._labelFindIn)
		self._groupBoxOptions.Controls.Add(self._radioButtonFindInSel)
		self._groupBoxOptions.Controls.Add(self._radioButtonFindInView)
		self._groupBoxOptions.Controls.Add(self._radioButtonFindInProject)
		self._groupBoxOptions.Controls.Add(self._checkBoxMatch)
		self._groupBoxOptions.Controls.Add(self._checkBoxFullParameter)
		self._groupBoxOptions.Controls.Add(self._checkBoxSearchTypes)
		self._groupBoxOptions.Controls.Add(self._checkBoxIgnoreTags)
		self._groupBoxOptions.Controls.Add(self._checkBoxFullWord)
		self._groupBoxOptions.Controls.Add(self._checkBoxLinks)
		self._groupBoxOptions.Controls.Add(self._checkBoxCaseSensitive)
		self._groupBoxOptions.Location = System.Drawing.Point(324, 8)
		self._groupBoxOptions.Name = "groupBoxOptions"
		self._groupBoxOptions.Size = System.Drawing.Size(448, 127)
		self._groupBoxOptions.TabIndex = 7
		self._groupBoxOptions.TabStop = False
		self._groupBoxOptions.Text = "Options"
		# 
		# checkBoxCaseSensitive
		# 
		self._checkBoxCaseSensitive.Enabled = True
		self._checkBoxCaseSensitive.Location = System.Drawing.Point(6, 25)
		self._checkBoxCaseSensitive.Name = "checkBoxCaseSensitive"
		self._checkBoxCaseSensitive.Size = System.Drawing.Size(150, 18)
		self._checkBoxCaseSensitive.TabIndex = 0
		self._checkBoxCaseSensitive.Text = "Case-sensitive"
		self._checkBoxCaseSensitive.UseVisualStyleBackColor = True
		# 
		# checkBoxFullWord
		# 
		self._checkBoxFullWord.Enabled = True
		self._checkBoxFullWord.Location = System.Drawing.Point(6, 45)
		self._checkBoxFullWord.Name = "checkBoxFullWord"
		self._checkBoxFullWord.Size = System.Drawing.Size(150, 18)
		self._checkBoxFullWord.TabIndex = 0
		self._checkBoxFullWord.Text = "Full word"
		self._checkBoxFullWord.UseVisualStyleBackColor = True
		# 
		# checkBoxFullParameter
		# 
		self._checkBoxFullParameter.Enabled = True
		self._checkBoxFullParameter.Location = System.Drawing.Point(6, 65)
		self._checkBoxFullParameter.Name = "checkBoxFullParameter"
		self._checkBoxFullParameter.Size = System.Drawing.Size(150, 18)
		self._checkBoxFullParameter.TabIndex = 0
		self._checkBoxFullParameter.Text = "Full parameter"
		self._checkBoxFullParameter.UseVisualStyleBackColor = True
		# 
		# checkBoxLinks
		# 
		self._checkBoxLinks.Enabled = False
		self._checkBoxLinks.Location = System.Drawing.Point(166, 25)
		self._checkBoxLinks.Name = "checkBoxLinks"
		self._checkBoxLinks.Size = System.Drawing.Size(150, 18)
		self._checkBoxLinks.TabIndex = 0
		self._checkBoxLinks.Text = "Links"
		self._checkBoxLinks.UseVisualStyleBackColor = True
		# 
		# checkBoxIgnoreTags
		# 
		self._checkBoxIgnoreTags.Checked = True
		self._checkBoxIgnoreTags.CheckState = System.Windows.Forms.CheckState.Checked
		self._checkBoxIgnoreTags.Enabled = True
		self._checkBoxIgnoreTags.Location = System.Drawing.Point(166, 45)
		self._checkBoxIgnoreTags.Name = "checkBoxIgnoreTags"
		self._checkBoxIgnoreTags.Size = System.Drawing.Size(150, 18)
		self._checkBoxIgnoreTags.TabIndex = 0
		self._checkBoxIgnoreTags.Text = "Don't select Tags"
		self._checkBoxIgnoreTags.UseVisualStyleBackColor = True
		# 
		# checkBoxMatch
		# 
		self._checkBoxMatch.AccessibleDescription = ""
		self._checkBoxMatch.Enabled = True
		self._checkBoxMatch.Location = System.Drawing.Point(6, 86)
		self._checkBoxMatch.Name = "checkBoxMatch"
		self._checkBoxMatch.Size = System.Drawing.Size(150, 18)
		self._checkBoxMatch.TabIndex = 0
		self._checkBoxMatch.Text = "Match mode (regex)"
		self._MatchModeToolTip.SetToolTip(self._checkBoxMatch, "Python: re - Regular expression operations")
		self._checkBoxMatch.UseVisualStyleBackColor = True
		# 
		# MatchModeToolTip
		# 
		self._MatchModeToolTip.AutomaticDelay = 0
		self._MatchModeToolTip.IsBalloon = True
		self._MatchModeToolTip.ToolTipIcon = System.Windows.Forms.ToolTipIcon.Info
		self._MatchModeToolTip.ToolTipTitle = "Search :"
		self._MatchModeToolTip.UseAnimation = False
		# 
		# buttonSelectionAll
		# 
		self._buttonSelectionAll.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._buttonSelectionAll.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._buttonSelectionAll.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._buttonSelectionAll.Location = System.Drawing.Point(12, 116)
		self._buttonSelectionAll.Margin = System.Windows.Forms.Padding(0)
		self._buttonSelectionAll.Name = "buttonSelectionAll"
		self._buttonSelectionAll.Size = System.Drawing.Size(65, 22)
		self._buttonSelectionAll.TabIndex = 8
		self._buttonSelectionAll.Text = "All"
		self._buttonSelectionAll.UseVisualStyleBackColor = False
		self._buttonSelectionAll.Click += self.ButtonSelectionAllClick
		# 
		# buttonSelectionSelected
		# 
		self._buttonSelectionSelected.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._buttonSelectionSelected.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._buttonSelectionSelected.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._buttonSelectionSelected.Location = System.Drawing.Point(77, 116)
		self._buttonSelectionSelected.Margin = System.Windows.Forms.Padding(0)
		self._buttonSelectionSelected.Name = "buttonSelectionSelected"
		self._buttonSelectionSelected.Size = System.Drawing.Size(65, 22)
		self._buttonSelectionSelected.TabIndex = 8
		self._buttonSelectionSelected.Text = "Selected"
		self._buttonSelectionSelected.UseVisualStyleBackColor = False
		self._buttonSelectionSelected.Click += self.ButtonSelectionSelectedClick
		# 
		# labelCreateSelection
		# 
		self._labelCreateSelection.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._labelCreateSelection.Location = System.Drawing.Point(12, 102)
		self._labelCreateSelection.Name = "labelCreateSelection"
		self._labelCreateSelection.Size = System.Drawing.Size(150, 18)
		self._labelCreateSelection.TabIndex = 9
		self._labelCreateSelection.Text = "Create selection from listed :"
		# 
		# checkBoxSearchTypes
		# 
		self._checkBoxSearchTypes.Enabled = True
		self._checkBoxSearchTypes.Location = System.Drawing.Point(166, 65)
		self._checkBoxSearchTypes.Name = "checkBoxSearchTypes"
		self._checkBoxSearchTypes.Size = System.Drawing.Size(150, 18)
		self._checkBoxSearchTypes.TabIndex = 0
		self._checkBoxSearchTypes.Text = "Family, Type, Category..."
		self._checkBoxSearchTypes.UseVisualStyleBackColor = True
		# 
		# labelFoundLog
		# 
		self._labelFoundLog.ForeColor = System.Drawing.SystemColors.HotTrack
		self._labelFoundLog.Location = System.Drawing.Point(12, 63)
		self._labelFoundLog.Name = "labelFoundLog"
		self._labelFoundLog.Size = System.Drawing.Size(306, 43)
		self._labelFoundLog.TabIndex = 10
		self._labelFoundLog.Text = "Type to search in ActiveView..."
		# 
		# radioButtonFindInProject
		# 
		self._radioButtonFindInProject.Location = System.Drawing.Point(322, 63)
		self._radioButtonFindInProject.Name = "radioButtonFindInProject"
		self._radioButtonFindInProject.Size = System.Drawing.Size(104, 24)
		self._radioButtonFindInProject.TabIndex = 1
		self._radioButtonFindInProject.Text = "Project [+]"
		self._radioButtonFindInProject.UseVisualStyleBackColor = True
		self._radioButtonFindInProject.CheckedChanged += self.RadioButtonGroupCheckedChanged
		# 
		# radioButtonFindInView
		# 
		self._radioButtonFindInView.Checked = True
		self._radioButtonFindInView.Location = System.Drawing.Point(322, 43)
		self._radioButtonFindInView.Name = "radioButtonFindInView"
		self._radioButtonFindInView.Size = System.Drawing.Size(104, 24)
		self._radioButtonFindInView.TabIndex = 1
		self._radioButtonFindInView.TabStop = True
		self._radioButtonFindInView.Text = "Active View [+]"
		self._radioButtonFindInView.UseVisualStyleBackColor = True
		self._radioButtonFindInView.CheckedChanged += self.RadioButtonGroupCheckedChanged
		# 
		# radioButtonFindInSel
		# 
		self._radioButtonFindInSel.Location = System.Drawing.Point(322, 23)
		self._radioButtonFindInSel.Name = "radioButtonFindInSel"
		self._radioButtonFindInSel.Size = System.Drawing.Size(104, 24)
		self._radioButtonFindInSel.TabIndex = 1
		self._radioButtonFindInSel.Text = "Selection"
		self._radioButtonFindInSel.UseVisualStyleBackColor = True
		self._radioButtonFindInSel.CheckedChanged += self.RadioButtonGroupCheckedChanged
		# 
		# labelFindIn
		# 
		self._labelFindIn.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._labelFindIn.Location = System.Drawing.Point(319, 11)
		self._labelFindIn.Name = "labelFindIn"
		self._labelFindIn.Size = System.Drawing.Size(65, 15)
		self._labelFindIn.TabIndex = 10
		self._labelFindIn.Text = "Find in :"
		# 
		# checkBoxModal
		# 
		self._checkBoxModal.CheckAlign = System.Drawing.ContentAlignment.MiddleRight
		self._checkBoxModal.Enabled = True
		self._checkBoxModal.Location = System.Drawing.Point(g.modalX, g.modalY)
		self._checkBoxModal.Name = "checkBoxModal"
		self._checkBoxModal.Size = System.Drawing.Size(50, 18)
		self._checkBoxModal.TabIndex = 12
		self._checkBoxModal.Text = "Lock"
		self._checkBoxModal.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._checkBoxModal.UseVisualStyleBackColor = True
		self._checkBoxModal.CheckedChanged += self.CheckBoxModalCheckedChanged
		# 
		# checkBoxSaveDefaults
		# 
		self._checkBoxSaveDefaults.CheckAlign = System.Drawing.ContentAlignment.MiddleRight
		self._checkBoxSaveDefaults.Enabled = True
		self._checkBoxSaveDefaults.ImageAlign = System.Drawing.ContentAlignment.BottomRight
		self._checkBoxSaveDefaults.Location = System.Drawing.Point(661, 121)
		self._checkBoxSaveDefaults.Name = "checkBoxSaveDefaults"
		self._checkBoxSaveDefaults.Size = System.Drawing.Size(111, 18)
		self._checkBoxSaveDefaults.TabIndex = 11
		self._checkBoxSaveDefaults.Text = "Save as defaults"
		self._checkBoxSaveDefaults.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._checkBoxSaveDefaults.UseVisualStyleBackColor = True
		self._checkBoxSaveDefaults.CheckedChanged += self.CheckBoxSaveDefaultsCheckedChanged
		# 
		# comboBoxFind
		# 
		#self._comboBoxFind.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.Suggest
		self._comboBoxFind.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.ListItems
		self._comboBoxFind.FormattingEnabled = True
		self._comboBoxFind.Location = System.Drawing.Point(70, 13)
		self._comboBoxFind.Name = "comboBoxFind"
		self._comboBoxFind.Size = System.Drawing.Size(225, 21)
		self._comboBoxFind.TabIndex = 0
		# 
		# comboBoxReplace
		# 
		#self._comboBoxReplace.AutoCompleteMode = System.Windows.Forms.AutoCompleteMode.Suggest
		self._comboBoxReplace.AutoCompleteSource = System.Windows.Forms.AutoCompleteSource.ListItems
		self._comboBoxReplace.Enabled = True
		self._comboBoxReplace.FormattingEnabled = True
		self._comboBoxReplace.Location = System.Drawing.Point(70, 38)
		self._comboBoxReplace.Name = "comboBoxReplace"
		self._comboBoxReplace.Size = System.Drawing.Size(225, 21)
		self._comboBoxReplace.TabIndex = 1
		self._comboBoxReplace.Text = ""
		# 
		# listViewResult
		# 
		self._listViewResult.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._listViewResult.Columns.AddRange(System.Array[System.Windows.Forms.ColumnHeader]([
			self._value,
			self._parameter,
			self._type,
			self._level,
			self._category,
			self._family,
			self._id
			]))
		self._listViewResult.Location = System.Drawing.Point(g.lvrX, g.lvrY)
		self._listViewResult.Name = "listViewResult"
		self._listViewResult.Size = System.Drawing.Size(g.lvrWidth, g.lvrHeight)
		self._listViewResult.TabIndex = 14
		self._listViewResult.UseCompatibleStateImageBehavior = False
		self._listViewResult.View = System.Windows.Forms.View.Details
		self._listViewResult.AllowColumnReorder = True
		self._listViewResult.CheckBoxes = False
		self._listViewResult.FullRowSelect = True
		self._listViewResult.GridLines = False
		self._listViewResult.HideSelection = False
		#self._listViewResult.HotTracking = True
		#self._listViewResult.HoverSelection = True
		#self._listViewResult.Sorting = System.Windows.Forms.SortOrder.Ascending
		self._listViewResult.SelectedIndexChanged += self.ListViewResultSelectedIndexChanged
		self._listViewResult.DoubleClick += self.ListViewResultDoubleClick
		# 
		# value
		# 
		self._value.Tag = "Value"
		self._value.Text = "Value"
		self._value.Width = -2
		# 
		# parameter
		# 
		self._parameter.Tag = "Parameter"
		self._parameter.Text = "Parameter"
		self._parameter.Width = -2
		# 
		# type
		# 
		self._type.Tag = "Type Instance"
		self._type.Text = "Type Instance"
		self._type.Width = -2
		# 
		# family
		# 
		self._family.Tag = "Family Instance"
		self._family.Text = "Family Instance"
		self._family.Width = -2
		# 
		# id
		# 
		self._id.Tag = "Id"
		self._id.Text = "Id"
		self._id.Width = -2
		# 
		# level
		# 
		self._level.Tag = "Level"
		self._level.Text = "Level"
		self._level.Width = -2
		# 
		# category
		# 
		self._category.Tag = "Category"
		self._category.Text = "Category"
		self._category.Width = -2
		# 
		# FormFind
		# 
		self.AcceptButton = self._buttonFind
		self.CancelButton = self._buttonClose
		self.MaximizeBox = True
		#self.ClientSize = System.Drawing.Size(784, 361)
		self.Controls.Add(self._linkLabelSaveTable)
		self.Controls.Add(self._listViewResult)
		self.Controls.Add(self._linkLabelWarningCat)
		self.Controls.Add(self._comboBoxReplace)
		self.Controls.Add(self._comboBoxFind)
		self.Controls.Add(self._checkBoxKeepSaveDefaults)
		self.Controls.Add(self._checkBoxSaveDefaults)
		self.Controls.Add(self._checkBoxModal)
		self.Controls.Add(self._buttonSelectionSelected)
		self.Controls.Add(self._buttonSelectionAll)
		self.Controls.Add(self._labelCreateSelection)
		self.Controls.Add(self._labelFoundLog)
		self.Controls.Add(self._groupBoxOptions)
		self.Controls.Add(self._buttonClose)
		self.Controls.Add(self._buttonReplaceAll)
		self.Controls.Add(self._buttonReplaceSelected)
		self.Controls.Add(self._labelReplace)
		self.Controls.Add(self._labelToFind)
		#self.Controls.Add(self._listBoxResult)
		self.Controls.Add(self._buttonFind)
		self.MinimumSize = System.Drawing.Size(g.fmWidthmin, g.fmHeightmin)
		self.TopMost = True
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Sizable
		self.Name = "FormFind"
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent
		self.Text = "neoCL | Find and Replace"
		self._groupBoxOptions.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()
		self.ShowIcon = False
		self.Resize += self.FormResize
		
	def FormResize(self, sender, e):
		self.UpdateResize()

	def UpdateResize(self, resizeFormFromMemory=False):

		if resizeFormFromMemory:
			self.Height	= g.fmHeight
			self.Width = g.fmWidth 
			
		g.fmHeight = self.Height
		g.fmWidth = self.Width 

		self._buttonClose.Location = Point(g.btcloseX, g.GetY(g.btcloseYi))
		self._buttonFind.Location = Point(g.btfindX, g.GetY(g.btfindYi))
		self._buttonReplaceAll.Location = Point(g.btrallX, g.GetY(g.btrallYi))
		self._buttonReplaceSelected.Location = Point(g.btrslX, g.GetY(g.btrslYi))
		self._checkBoxModal.Location = Point(g.GetX(g.modalXi), g.GetY(g.modalYi))	
		self._linkLabelSaveTable.Location = Point(g.GetX(g.savetableXi), g.GetY(g.savetableYi))		
		self._listViewResult.Size = Size(g.GetListViewResultW(), g.GetListViewResultH())
		
#	def ListBoxResultSelectedIndexChanged(self, sender, e):
#		pass

#	def ListBoxResultDoubleClick(self, sender, e):
#		pam = g.pmfindList[sender.SelectedIndex]
#		pam.SelectMe(True if self._radioButtonFindInSel.Checked else False)

	def MinimizeMe(self):
		self.WindowState = FormWindowState.Minimized

	def NormalizeMe(self):
		self.WindowState = FormWindowState.Normal

	def ListViewResultSelectedIndexChanged(self, sender, e):
		pass

	def ListViewResultDoubleClick(self, sender, e):
		#pam = g.pmfindList[sender.SelectedIndex]
		#pam = g.pmfindList[sender.Items.IndexOf(sender.SelectedItems[0])]
		pam = g.pmfindList[sender.SelectedIndices[0]]
		pam.SelectMe(True if self._radioButtonFindInSel.Checked else False)

	def ButtonFindClick(self, sender, e):
		if self._checkBoxSaveDefaults.Checked: f.SaveDefaults()
		if self._comboBoxFind.Text:
			g.active_findstr = self._comboBoxFind.Text
			g.AddtoFindList(g.active_findstr)
			f.Set_comboBoxFindItems()
			f.CollectData()
			count = len(g.pmfindList)
			if count > 0:
				self.ReplaceLocker(True)
			else:
				self.ReplaceLocker(False)
			self._labelFoundLog.Text = "Total found : " + str(count)

	def ButtonReplaceSelectedClick(self, sender, e):
		f.ReplaceData(True)

	def ButtonReplaceAllClick(self, sender, e):
		f.ReplaceData(False)

	def ButtonCloseClick(self, sender, e):
		if self._checkBoxSaveDefaults.Checked: f.SaveDefaults()
		self.Dispose()

	def ButtonSelectionAllClick(self, sender, e):
		f.CreateSelection(True)

	def ButtonSelectionSelectedClick(self, sender, e):
		f.CreateSelection(False)

	def RadioButtonGroupCheckedChanged(self, sender, e):
		f.SearchModeChange()

	def CheckBoxModalCheckedChanged(self, sender, e):
		f.ChangeModal(FormFind)

	def CheckBoxSaveDefaultsCheckedChanged(self, sender, e):
		if sender.Checked and not g.ini:
			f.Alert("No configuration file found! Defaults can't be saved.", title="neoCL | Find", header="Error!")
			f.BringToFront()
			self.FreezeEventsMode = True
			sender.Checked = False
			sender.Enabled = False
			self.FreezeEventsMode = False
	
	def FreezeReplace(self):		
		self._comboBoxReplace.Text = "Select lock and save defaults. Restart."
		self._comboBoxReplace.Enabled = False
		self._buttonReplaceSelected.Enabled = False
		self._buttonReplaceAll.Enabled = False
		self.ReplaceFreeze = True

	def ReplaceLocker(self, onOff=False):
		if self.ReplaceFreeze: onOff = False
		self._buttonReplaceSelected.Enabled = onOff
		self._buttonReplaceAll.Enabled = onOff

	def LinkLabelSpecifyCatClick(self, sender, e):
		g.fmsc.ShowDialog()

	def LinkLabelSaveTableClick(self, sender, e):
		f.SaveTable()

def Main():
    g.fm = FormFind()
    g.fmsc = fsc.FormSelCat()
    f.Setup()

    if g.fm._checkBoxModal.Checked:
	    g.fm.ShowDialog()
    else:
	    g.fm.FreezeReplace()
	    g.fm.Show()