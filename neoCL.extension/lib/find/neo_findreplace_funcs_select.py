#######################################
### neoCL | Find and Replacer #########
#######################################

from neo_findreplace_funcs_main import *

def SetFocus(eids, cancelSelect=False):
	try:
		if not cancelSelect:
			uidoc.Selection.SetElementIds(eids)
		uidoc.ShowElements(eids)
	except:
		g.fm._labelFoundLog.Text = "Error trying to select the item(s) in model!" 
	BringToFront()

def CreateSelection(sAll):
	try:
		if sAll:
			eids = List[ElementId](g.selfindList)
			SetFocus(eids)
		else:
			sList = []
			for i in g.fm._listViewResult.SelectedIndices:
				pam = g.pmfindList[i]			
				sList.append(pam.el.Id)
			eids = List[ElementId](sList)
			SetFocus(eids)
	except:
		g.fm._labelFoundLog.Text = "Error trying to select the item(s) in model." 