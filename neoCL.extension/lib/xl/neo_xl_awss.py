#import time
from Autodesk.Revit import DB
import _neo_importer
import lib.workset.neo_ws_awss_config as config
import lib.workset.neo_ws_awss_switch as sw
from neo_xl_functions import rg, ClearColumnFrom
from rpw import db, doc
from rpw.ui.forms import Alert

### config ############################
rt1 = 1 	    #Title row 1
ct = 1 	        #First Column Title
re = rt1 + 1	#First element row
ce = ct 		#First Column Element
### ###### ############################

def GetWb():
	import neo_xl_appbuilder as ap
	from inspect import getsourcefile
	import os.path

	ipath = os.path.abspath(getsourcefile(lambda:0))
	objpath = ipath[:ipath.rfind(os.path.sep)] + "\\neoCL.AutoWorksetSet.Configurator.xlsm"
	
	XL, wb = ap.getApp(False, objpath, True)
	return XL, wb

### LOG #############################################
def LOG_Worksets():
	print("")
	print("neoCL | Auto Workset Set\nLoading Data to Excel, please wait...")

	XL, wb = GetWb()

	#XL.Visible = False
	XL.DisplayAlerts = False
	XL.ScreenUpdating = False
	keepcalcmode = XL.Calculation
	XL.Calculation = -4135      # xlCalculationManual

	sh = wb.Worksheets("LOG")
	LOG_WorksetsMain(sh)

	#XL.Visible = True
	XL.Calculation = keepcalcmode
	XL.ScreenUpdating = True
	XL.DisplayAlerts = True

	print("Excel is ready!")
	#from pyrevit import script
	#output = script.get_output()
	#output.close()
	#Alert("", title="neoCL | Auto Workset Set", header="Excel is ready!")


def LOG_WorksetsMain(sh):

    ri = re
    #ci = ce
    sh.Cells.ClearContents()
    sh.Range[rg(rt1, ce)].Value2 = "'PROJECT NAME"
    sh.Range[rg(rt1, ce + 1)].Value2 = "'TYPE"
    sh.Range[rg(rt1, ce + 2)].Value2 = "'ID"
    sh.Range[rg(rt1, ce + 3)].Value2 = "'NAME"
    
    docname = doc.Title

    collector = DB.FilteredWorksetCollector(doc).OfKind(DB.WorksetKind.ViewWorkset)
    ri = LOG_Collector(sh, ri, docname, collector)
    collector = DB.FilteredWorksetCollector(doc).OfKind(DB.WorksetKind.UserWorkset)
    ri = LOG_Collector(sh, ri, docname, collector)
    
    sh.Cells.EntireColumn.AutoFit()   

def LOG_Collector(sh, ri, docname, collector):
    lastws = ""
    thisws = ""
    for c in collector:
        if Allow_this_workset(c):
            thisws = c.Name.ToString()
            if thisws != lastws:
                sh.Range[rg(ri, ce)].Value2 = "'" + docname
                sh.Range[rg(ri, ce + 1)].Value2 = "'" + c.Kind.ToString()
                sh.Range[rg(ri, ce + 2)].Value2 = "'" + c.Id.ToString()
                sh.Range[rg(ri, ce + 3)].Value2 = "'" + thisws
                ri += 1
            lastws = thisws
    return ri

def Allow_this_workset(ws):
    wsname = ws.Name.ToString()

    wsn = wsname.replace('"', '')           # for some reason there is names without the ending char " (at least in some french projects)
    import unicodedata
    wsn = unicodedata.normalize('NFD', wsn).encode('ascii', 'ignore')
    if wsn == 'View Project Browser' or \
        wsn == 'Vue Arborescence du projet' or \
        wsn == 'Vue Navigateur du systeme' or \
        wsn == 'View System Browser':
        return False

    VIEWTEMPLATE = 'View Template "'
    if wsname[:len(VIEWTEMPLATE)] == VIEWTEMPLATE:
        return False

    return True
### END : LOG #############################################

### LOAD FROM FILE #############################################
def LOAD_Worksets():
	XL, wb = GetWb()
	XL.DisplayAlerts = False
	sh = wb.Worksheets("CONFIG")
	LOAD_WorksetsMain(sh)
	XL.DisplayAlerts = True

def LOAD_WorksetsMain(sh):

    ri = re
    #ci = ce
    sh.Cells.ClearContents()
    sh.Range[rg(rt1, ce)].Value2 = "'PROJECT NAME"
    sh.Range[rg(rt1, ce + 1)].Value2 = "'VIEW WORKSET ID"
    sh.Range[rg(rt1, ce + 2)].Value2 = "'USER WORKSET ID"
    
    config.ReloadDB()
    
    awssDBxl = config.awssDB
    for proj in awssDBxl:
        awssDBxlproj = awssDBxl[proj] 
        for id in awssDBxlproj:
            sh.Range[rg(ri, ce)].Value2 = "'" + proj
            sh.Range[rg(ri, ce + 1)].Value2 = "'" + str(id)
            sh.Range[rg(ri, ce + 2)].Value2 = "'" + str(config.awssDB[proj][id])
            ri += 1

    sh.Cells.EntireColumn.AutoFit()   
### END : LOAD FROM FILE #############################################

### UPLOAD TO FILE #############################################
def UPLOAD_Worksets():
	XL, wb = GetWb()
	XL.DisplayAlerts = False
	sh = wb.Worksheets("CONFIG")
	UPLOAD_WorksetsMain(sh)
	XL.DisplayAlerts = True

def UPLOAD_WorksetsMain(sh):

    ri = re
    #ci = ce
    
    awssDBxl = {}

    while(True):
        r = sh.Range[rg(ri, ce)]
        proj = r.Text
        if proj:
            ids = {int(sh.Range[rg(ri, ce + 1)].Value2): \
                   int(sh.Range[rg(ri, ce + 2)].Value2)}
            if not proj in awssDBxl:
                tmpbdws = {}
                tmpbdpj = {proj:tmpbdws}
                awssDBxl.update(tmpbdpj)
            awssDBxl[proj].update(ids)
        else:
            config.UpdateDB(awssDBxl)
            log = ""
            if sw.isEvenHandlerAdded():
                log = "Attention!\n\nThe tool is or was activated, so must restart Revit to reload new data!\n\n"
                log += "But you can use the ActiveView button, without restarting Revit. "
                log += "(ActiveView button set the workset for the Active View individually.)"
            Alert(log, title="neoCL | Auto Workset Set", header="Update of config file done!")
            return
        ri += 1  
### END : UPLOAD TO FILE #############################################