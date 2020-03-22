import neo_ws_awss_switch as sw
from neo_ws_awss_config import awssDB
#import neo_ws_awss_config as conf
from Autodesk.Revit import DB
from rpw import doc, db
from pyrevit import script

#awssDB = []

def AutoSetWorkset():
    #from rpw.ui.forms import Alert
    #Alert('Auto Workset Setting!', title="neoCL | awss", header="neoCL")
    
    if not script.get_envvar(sw.AUTO_WORKSET_SET) or \
        doc.ActiveView.ViewType == "ProjectBrowser":
        return False

    ws = GetActiveViewWsInt()
    if ws != False :
        ActivateThisWorkset(ws)

def GetActiveViewWsInt():
    viewWsInt = int(doc.ActiveView.WorksetId.ToString())
    try:
        return awssDB[doc.Title][viewWsInt]
    except:
		# Full project name doesn't exist in DB, so try to find a partial name
		# like [project2020] instead of neoproject2020-A.rvt 
        if UpdatePartialProjectName():
            try:
                return awssDB[doc.Title][viewWsInt]
            except:
                return False
        else:
            return False

def ActivateThisWorkset(worksetIdInt):
    worksetId = DB.WorksetId(worksetIdInt)
    worksetTable = doc.GetWorksetTable()
    try:
        worksetTable.SetActiveWorksetId(worksetId)
        return True
    except:
        return False

def UpdatePartialProjectName():
	# Find the partial project name in DB, then update the current DB (not the config file)
	# so it doesn't need to refind the project name, each time a new View is activated. 
	pNames = list(set(awssDB))
	dName = doc.Title
	for pn in pNames:
		if pn[:1] == "[":
			p = pn.replace("[","") 
			p = p.replace("]","") 
			if p in dName:
				awssDB[dName] = awssDB.pop(pn)
				return True
	return False