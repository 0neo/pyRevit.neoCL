#######################################
### neoCL | Find and Replacer #########
#######################################

from neo_findreplace_funcs_main import *

def ReplaceData(onSelected):

	if g.fm._checkBoxSaveDefaults.Checked: SaveDefaults()

	g.active_repstr = g.fm._comboBoxReplace.Text
	g.AddtoRepalceList(g.active_repstr)
	Set_comboBoxReplaceItems()
		
	count = 0		
		
	g.active_findstr = g.fm._comboBoxFind.Text # allow find something, then replace another thing, without Create selection and then redo the find.
	with db.Transaction(str('neoCL | Replace ' + g.active_findstr + ' by ' + g.active_repstr)):
		if onSelected:
			for i in g.fm._listViewResult.SelectedIndices:
				pam = g.pmfindList[i]
				if pam.ReplaceMe(): count += 1
				#count = len(g.fm._listViewResult.SelectedIndices)
		else:
			for pam in g.pmfindList:
				if pam.ReplaceMe(): count += 1
				#count = len(g.pmfindList)
		
		g.fm._labelFoundLog.Text = "Total replaced : " + str(count)