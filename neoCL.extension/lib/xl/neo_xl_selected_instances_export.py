#######################################
### XLinst.neoCL ######################
### by neo 		 ######################
### 2019 		 ######################
#######################################
### neoCL | iParameters Editor ########
#######################################

import neo_xl_selected_instances as xli
from rpw import ui, db
from neo_xl_functions import rg

### config ##############################
rt = xli.rt 	#Title row
ct = xli.ct 	#First Column Title
re = xli.re		#First element row
ce = xli.ce		#First Column Element
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

def SetFormatsBefore():
	try:
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
	    sh.Rows(1).AutoFilter()
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

def AddParam(pm):
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
	import _neo_importer
	from neocl__funcs import neoAlert
	mg = "No elements selected, pick elements..."
	print(mg)
	neoAlert(mg, title="neoCL", header="neoCL | iParameters Editor")
	els = []
	ct = len(els)
	go = True

	print("Selecting... ")
	while go:

		try:
		    mg = 'neoCL | Pick Element(s) by order! ESCAPE key when done. Total[' + str(ct) + "]"
		    el = ui.Pick.pick_element(msg=mg, multiple=False)
		    el = db.Element.from_id(el.id)
		    els.append(el)
		    ct = len(els)
		    print("Selecting... Total[" + str(ct) + "]")
		except:
			print("Done! Loading to Excel...")
			go = False
	
	return els

def IsValidParam(pm):
	#pm._revit_object.UserModifiable
	okPm = not pm._revit_object.IsReadOnly
	okPm = okPm and pm.Definition.Name != "Family and Type" #Probably already canceled (if isreadonly)
	return okPm

def GetWb():
	import neo_xl_appbuilder as ap
	from inspect import getsourcefile
	import os.path

	ipath = os.path.abspath(getsourcefile(lambda:0))
	objpath = ipath[:ipath.rfind(os.path.sep)] + "\\neoCL.iParametersEditor.xlsm"
	
	XL, wb = ap.getApp(False, objpath)
	return XL, wb

def ExportXL():
	
    global XL, wb, sh
    global rID, rFa, rTy
    global ar, rt, ct, re, ce

    XL, wb = GetWb()
    sh = wb.ActiveSheet
	
    rID = sh.Range[rg(rt, ct)]
    rFa = sh.Range[rg(rt, ct + 1)]
    rTy = sh.Range[rg(rt, ct + 2)]

    SetFormatsBefore()

    rID.Value2 = "neoCL.iParametersEditor | Loading..."
    XL.ScreenUpdating = True

    XL.ScreenUpdating = False
    XL.Calculation = False

    rFa.Value2 = "Family"
    rTy.Value2 = "Type"

    sel = ui.Selection()
    
    if len(sel) < 1:
        sel = UserSelect()

    print('neoCL.iParametersEditor | Selected Elements :')
    for eq in sel:
        print(eq.name + " | ID[" + str(eq.Id) + "]") 

    for eq in sel:
	    pmap = eq.parameters.all
	    pmap.sort(key=lambda x: x.name, reverse=False)
	    pmap.sort(key=lambda x: x.Definition.ParameterGroup, reverse=False)
	    sh.Range[rg(ar, ce)].Value2 = "'" + str(eq.Id)
	
	    for pm in pmap:
		    if IsValidParam(pm):
			    AddParam(pm)
	    ar += 1

    rID.Value2 = "ID"
    SetFormatsAfter()

    XL.ScreenUpdating = True
    XL.Calculation = True

    print("Excel is ready!")