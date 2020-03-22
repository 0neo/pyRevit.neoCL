#######################################
### XLinst.neoCL ######################
### by neo 		 ######################
### 2019 		 ######################
#######################################
### neoCL | iParameters Editor ########
#######################################

import neo_xl_selected_instances as xli
import neo_xl_appbuilder as ap
from rpw import ui, db
from neo_xl_functions import rg, FirstEmptyCellInRow, SetFiltering

### config ##############################
rt = xli.rt 	#Title row
ct = xli.ct 	#First Column Title
re = xli.re		#First element row
ce = xli.ce		#First Column Element
shName = "neoCL | iParameters Editor"
### config ##############################
cShc = 1		#ColorIndex Sheet Cell
cSht = 3		#ColorIndex Sheet Text
cLoc = 49		#ColorIndex Locked Cell
cLot = 2		#ColorIndex Locked Text
cEdc = 35		#ColorIndex Editable Cell
cEdt = 18		#ColorIndex Editable Text
cBd = 0			#ColorIndex Borders
colWd = 5		#Non needed columns width
### config ##############################
ar = re			#ActiveRow
### dim #################################
XL = None
wb = None
sh = None
rID = None
rFa = None
rTy = None
### ### #################################

def SetFormatsBefore(presetParams):
	try:
		if presetParams:
			rgAddress = str(sh.Cells(re, ce).Address()) + ":" + str(sh.Cells(sh.Rows.Count, sh.Columns.Count).Address())
			sh.Range(rgAddress).Clear()
		else:
		    sh.Cells.Clear()
		sh.Cells.Interior.ColorIndex = cShc
		sh.Cells.Font.ColorIndex = cSht
		sh.Cells.Borders.ColorIndex = cBd
		sh.Rows(1).Cells.Interior.ColorIndex = cLoc
		sh.Rows(1).Cells.Font.ColorIndex = cLot
		sh.Columns(1).Cells.Interior.ColorIndex = cLoc
		sh.Columns(1).Cells.Font.ColorIndex = cLot
		XL.Caption = "neoCL | iParameters Editor"
		sh.Name = "neoCL | iParameters Editor"
	except:
		print("Error Setting formats before!")
	
def SetFormatsAfter():
	try:
	    SetFiltering(sh)
	    lc = FirstEmptyCellInRow(sh, 1)
	    rngAddress = "A1:" + lc.Offset(0, -1).Address()
	    sh.Range(rngAddress).AutoFilter()
	    sh.Columns.AutoFit()
	    rID.ColumnWidth = colWd
	    rFa.ColumnWidth = colWd
	    #rTy.ColumnWidth = colWd
	except:
		print("Error Setting formats after!")
		
def GetColumnWithParam(param):
	c = ct 
	while(True):
	    c += 1
	    r = sh.Range[rg(rt, c)]
	    rv = r.Text
	    
	    if not rv:
	    	r.Value2 = "'" + param
	    	return c
	    elif rv == param:
	    	return c

def AddParam(pm, c):
	if not c:
		c = GetColumnWithParam(pm.Definition.Name)
	
	pval = ""
	if pm._revit_object.HasValue:
		if pm.type is str:
			pval = pm.AsString()
		elif pm.type is int:
			pval = pm.value
		elif pm.type is float:
			pval = pm.value * 304.8
		else:
			pval = pm.AsValueString()
			
	r = sh.Range[rg(ar, c)]
	r.Value2 = "'" + str(pval)
	r.Interior.ColorIndex = cEdc
	r.Font.ColorIndex = cEdt
	    	
def UserSelect():
	from pyrevit import forms
	from rpw.ui.forms import CommandLink, TaskDialog

	commands= [CommandLink('Pick by order...', return_value=False),
			   CommandLink('Select multiple...', return_value=True)]
	
	mg = "No elements preselected, so select elements now...\nIf listed order in excel matters, pick them by order."
	mg += "\n\nInstructions :\n  1) If pick, when done, press ESCAPE key or in context menu (mouse right click) select Cancel."
	mg += "\n  2) If multiple, when done, press Finish button (on the left, under the ribbon). ESCAPE key will cancel, no elements will be selected."

	dialog = TaskDialog('neoCL | iParameters Editor',
					title_prefix=False,
					content=mg,
					commands=commands,
					buttons=[],
					show_close=False)
	selectMultiple = dialog.show()
	
	els = []
	ct = len(els)
	go = True
	
	if selectMultiple:
		mg = 'neoCL | Select Element(s). Press Finish button (on the left, under the ribbon) when done. ESCAPE key will cancel.'
	else:
		mg = 'neoCL | Pick Element(s) by order! ESCAPE key (or right click and Cancel) when done. Total[' + str(ct) + ']'

	while go:
		try:
			with forms.WarningBar(title=mg):
				if selectMultiple:
					elx = ui.Pick.pick_element(msg=mg, multiple=selectMultiple)
					for el in elx:						
						el = db.Element.from_id(el.id)
						els.append(el)
					go = False
				else:
					el = ui.Pick.pick_element(msg=mg, multiple=selectMultiple)
					el = db.Element.from_id(el.id)
					els.append(el)
					ct = len(els)
					mg = "Selecting... Total[" + str(ct) + "] ESCAPE key when done."
		except:
			go = False
			
	return els

def IsValidParam(pm):
	#pm._revit_object.UserModifiable
	okPm = not pm._revit_object.IsReadOnly
	okPm = okPm and pm.Definition.Name != "Family and Type" #Probably already canceled (if isreadonly)
	return okPm

def GetWb():
	#import neo_xl_appbuilder as ap
	from inspect import getsourcefile
	import os.path

	ipath = os.path.abspath(getsourcefile(lambda:0))
	objpath = ipath[:ipath.rfind(os.path.sep)] + "\\neoCL.iParametersEditor.xlsm"
	
	XL, wb = ap.getApp(False, objpath)
	return XL, wb

def ExportXL(presetParams):
	
    global XL, wb, sh
    global rID, rFa, rTy
    global ar, rt, ct, re, ce

    XL, wb = GetWb()
    try: sh = wb.Worksheets(shName)
    except: pass
    sh.Activate
    XL.DisplayAlerts = False

    rID = sh.Range[rg(rt, ct)]
    rFa = sh.Range[rg(rt, ct + 1)]
    rTy = sh.Range[rg(rt, ct + 2)]

    GetDicOfColumns(sh)

    SetFormatsBefore(presetParams)

    rID.Value2 = "neoCL.iParametersEditor | Loading..."
    XL.ScreenUpdating = True

    XL.ScreenUpdating = False
    XL.Calculation = False

    rFa.Value2 = "Family"
    rTy.Value2 = "Type"

    sel = ui.Selection()
    
    print('[neoCL.iParametersEditor]')

    if len(sel) < 1:
        sel = UserSelect()
        if len(sel) < 1:
            print('No elements selected!\nProcess ended.')
            return False

    print('\n' + str(len(sel)) + ' element(s) selected.\nExporting to Excel... please wait.')
    print('\nSelected Elements : loading...')

    ctEq = 1
    for eq in sel:
        print(str(ctEq) + ') ' + eq.name + " | ID[" + str(eq.Id) + "]")
        ctEq += 1
    
    if presetParams:                # Export only parameters defined in Excel
        dic = GetDicOfColumns(sh)
        for eq in sel:
            sh.Range[rg(ar, ce)].Value2 = "'" + str(eq.Id)
            for col in dic:
                try:		
                    pm = eq.parameters[dic[col]]
                    AddParam(pm, col)
                except:
                    pass
            ar += 1
    else:                           # Export all allowed parameters of elements
        for eq in sel:
            pmap = eq.parameters.all
            pmap.sort(key=lambda x: x.name, reverse=False)
            pmap.sort(key=lambda x: x.Definition.ParameterGroup, reverse=False)
            sh.Range[rg(ar, ce)].Value2 = "'" + str(eq.Id)

            for pm in pmap:
                if IsValidParam(pm):
                    AddParam(pm, None)
            ar += 1

    rID.Value2 = "ID"
    SetFormatsAfter()

    XL.ScreenUpdating = True
    XL.Calculation = True
    XL.DisplayAlerts = True

    #ap.BringExcelToFront(XL)

    print("\nExcel is ready!")

def GetDicOfColumns(sh):
	ri = rt
	ci = ct
	dic = {}
	while(True):
		ci += 1
		rp = sh.Range[rg(ri, ci)]
		rpv = rp.Text
		dic[ci] = rpv
		if rpv == "":
			return dic