#######################################
### neoCL | Find and Replacer #########
#######################################

from System import Array, StringSplitOptions
from neo_findreplace_funcs_main import *

def Setup(fromMemory=False):
	
	FillCategoriesSelector()

	if not fromMemory:
		if g.ini: SetupOptions()
	
	els = ui.Selection()
	if len(els) > 0:
		g.fm._radioButtonFindInSel.Checked = True
	
	SearchModeChange()

def SetupOptions():
	g.fm.FreezeEventsMode = True
	#g.fm._buttonClose.XXX = g.v_buttonClose
	#g.fm._buttonFind.XXX = g.v_buttonFind
	#g.fm._buttonReplaceAll.XXX = g.v_buttonReplaceAll
	#g.fm._buttonReplaceSelected.XXX = g.v_buttonReplaceSelected
	#g.fm._buttonSelectionAll.XXX = g.v_buttonSelectionAll
	#g.fm._buttonSelectionSelected.XXX = g.v_buttonSelectionSelected
	g.fm._checkBoxCaseSensitive.Checked = g.v_checkBoxCaseSensitive
	g.fm._checkBoxFullParameter.Checked = g.v_checkBoxFullParameter
	g.fm._checkBoxFullWord.Checked = g.v_checkBoxFullWord
	g.fm._checkBoxIgnoreTags.Checked = g.v_checkBoxIgnoreTags
	g.fm._checkBoxLinks.Checked = g.v_checkBoxLinks
	g.fm._checkBoxMatch.Checked = g.v_checkBoxMatch
	g.fm._checkBoxModal.Checked = g.v_checkBoxModal
	g.fm._checkBoxSaveDefaults.Checked = g.v_checkBoxSaveDefaults
	g.fm._checkBoxKeepSaveDefaults.Checked = g.v_checkBoxKeepSaveDefaults
	g.fm._checkBoxSearchTypes.Checked = g.v_checkBoxSearchTypes
	Set_comboBoxFindItems()
	Set_comboBoxReplaceItems()
	#g.fm._groupBoxOptions.XXX = g.v_groupBoxOptions
	#g.fm._labelbyneo.XXX = g.v_labelbyneo
	#g.fm._labelCreateSelection.XXX = g.v_labelCreateSelection
	#g.fm._labelFindIn.XXX = g.v_labelFindIn
	#g.fm._labelFoundLog.XXX = g.v_labelFoundLog
	#g.fm._labelReplace.XXX = g.v_labelReplace
	#g.fm._labelToFind.XXX = g.v_labelToFind
	#g.fm._listBoxResult.XXX = g.v_listBoxResult
	g.fm._radioButtonFindInProject.Checked = g.v_radioButtonFindInProject
	g.fm._radioButtonFindInSel.Checked = g.v_radioButtonFindInSel
	g.fm._radioButtonFindInView.Checked = g.v_radioButtonFindInView
	g.fm.FreezeEventsMode = False
	Set_CategoriesSelection()

def Set_comboBoxFindItems():
	g.fm._comboBoxFind.Items.Clear()
	g.fm._comboBoxFind.Items.AddRange( \
	g.v_comboBoxFind.Split(Array[str](','), StringSplitOptions.RemoveEmptyEntries))

def Set_comboBoxReplaceItems():
	g.fm._comboBoxReplace.Items.Clear()
	g.fm._comboBoxReplace.Items.AddRange( \
	g.v_comboBoxReplace.Split(Array[str](','), StringSplitOptions.RemoveEmptyEntries))

def Set_CategoriesSelection():
	for i in range(0, g.fmsc._checkedListBoxCatSelector.Items.Count):
		item = "," + g.fmsc._checkedListBoxCatSelector.Items[i] + ","
		if item in g.v_ignoreCategories:
			g.fmsc._checkedListBoxCatSelector.SetItemChecked(i, False)

def SaveDefaults():
	if g.ini:
		SetConfigVars()
		g.WriteDefaults()
		g.SetIgnoreCategoriesList()

def SetConfigVars():
	#g.v_buttonClose = g.fm._buttonClose.XXX
	#g.v_buttonFind = g.fm._buttonFind.XXX
	#g.v_buttonReplaceAll = g.fm._buttonReplaceAll.XXX
	#g.v_buttonReplaceSelected = g.fm._buttonReplaceSelected.XXX
	#g.v_buttonSelectionAll = g.fm._buttonSelectionAll.XXX
	#g.v_buttonSelectionSelected = g.fm._buttonSelectionSelected.XXX
	g.v_checkBoxCaseSensitive = g.fm._checkBoxCaseSensitive.Checked
	g.v_checkBoxFullParameter = g.fm._checkBoxFullParameter.Checked
	g.v_checkBoxFullWord = g.fm._checkBoxFullWord.Checked
	g.v_checkBoxIgnoreTags = g.fm._checkBoxIgnoreTags.Checked
	g.v_checkBoxLinks = g.fm._checkBoxLinks.Checked
	g.v_checkBoxMatch = g.fm._checkBoxMatch.Checked
	g.v_checkBoxModal = g.fm._checkBoxModal.Checked
	g.v_checkBoxSaveDefaults = g.fm._checkBoxSaveDefaults.Checked
	g.v_checkBoxKeepSaveDefaults = g.fm._checkBoxKeepSaveDefaults.Checked
	g.v_checkBoxSearchTypes = g.fm._checkBoxSearchTypes.Checked
	#g.v_comboBoxFind = g.fm._comboBoxFind.Items.AddRange(System.Array[System.Object])
	#g.v_comboBoxReplace = g.fm._comboBoxReplace.Items.AddRange(System.Array[System.Object])
	#g.v_groupBoxOptions = g.fm._groupBoxOptions.XXX
	#g.v_labelbyneo = g.fm._labelbyneo.XXX
	#g.v_labelCreateSelection = g.fm._labelCreateSelection.XXX
	#g.v_labelFindIn = g.fm._labelFindIn.XXX
	#g.v_labelFoundLog = g.fm._labelFoundLog.XXX
	#g.v_labelReplace = g.fm._labelReplace.XXX
	#g.v_labelToFind = g.fm._labelToFind.XXX
	#g.v_listBoxResult = g.fm._listBoxResult.XXX
	g.v_radioButtonFindInProject = g.fm._radioButtonFindInProject.Checked
	g.v_radioButtonFindInSel = g.fm._radioButtonFindInSel.Checked
	g.v_radioButtonFindInView = g.fm._radioButtonFindInView.Checked

def SearchModeChange():
	if g.fm._radioButtonFindInSel.Checked:
		g.fm._labelFoundLog.Text = "Type to search in Active Selection..."
	elif g.fm._radioButtonFindInView.Checked:
		g.fm._labelFoundLog.Text = "Type to search in Active View..."
	elif g.fm._radioButtonFindInProject.Checked:
		g.fm._labelFoundLog.Text = "Type to search in Project...\nIt can be very slow! Highly recommended to use the\nSpecify categories [button] first and maybe save the project."

def BringToFront():
	pass
	# Not needed with g.fm.TopMost = True
	#g.fm.WindowState = System.Windows.Forms.FormWindowState.Maximized
	#g.fm.WindowState = System.Windows.Forms.FormWindowState.Normal

def ChangeModal(FormFind):
	if not g.fm.FreezeEventsMode:
		if g.fm._checkBoxModal.Checked:
			g.fm.Hide()
			g.fm.ShowDialog()
		else:
			SetConfigVars()
			g.fm.Close()
			g.fm = FormFind()
			Setup()			
			g.fm.FreezeReplace()
			g.fm.Show()
			#BringToFront()	# May not work well in this context
	g.fm.UpdateResize(True)

def AutoFitListView():

	def SetLargest(col):
		min = 75
		col.Width = -2
		tt = col.Width
		col.Width = -1
		it = col.Width
		col.Width = max([tt,it,min])

	SetLargest(g.fm._value)
	SetLargest(g.fm._parameter)
	SetLargest(g.fm._type)
	SetLargest(g.fm._family)
	SetLargest(g.fm._id)
	SetLargest(g.fm._level)
	SetLargest(g.fm._category)

def ClearData():
	g.selfindList.Clear()
	g.pmfindList.Clear()
	g.fm._listViewResult.Items.Clear()

def WarningCategories():
	allC = g.fmsc._checkedListBoxCatSelector.Items.Count
	selC = g.fmsc._checkedListBoxCatSelector.CheckedItems.Count

	g.fm._linkLabelWarningCat.Visible = selC < allC

def FillCategoriesSelector():

	cats = []

	for cat in doc.Settings.Categories:
		cats.append(cat.Name)
	
	cats.sort()
	
	for cat in cats:
		i = g.fmsc._checkedListBoxCatSelector.Items.Add(cat)
		g.fmsc._checkedListBoxCatSelector.SetItemChecked(i, True)

	WarningCategories()

def SaveTable():
	from neocl__funcs import CreateFileInDocFolder, Open_neoCLRevitDocFolder, neoAlert

	cFile = CreateFileInDocFolder(g.savetable, "neoCL.Find.Table.")
	filePath = cFile[0]
	created = cFile[1]

	g.fm.MinimizeMe()

	if created:
		Open_neoCLRevitDocFolder()
		mg = "File saved to:\n" + filePath
		neoAlert(mg, 'neoCL Find', header='Save Table', exit=False)
	else:
		mg = "Could not write file to:\n" + filePath
		neoAlert(mg, 'neoCL Find', header='Save Table', exit=False)

	g.fm.NormalizeMe()