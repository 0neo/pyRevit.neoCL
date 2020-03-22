#######################################
### XLinst.neoCL ######################
### by neo 		 ######################
### 2019 		 ######################
#######################################
### neoCL | iParameters Editor ########
#######################################

import neo_xl_selected_instances as xli
from neo_xl_functions import rg
from rpw import db

### config ############################
rt = xli.rt 	#Title row
#ct = xli.ct 	#First Column Title
re = xli.re		#First element row
ce = xli.ce		#First Column Element
shName = "neoCL | iParameters Editor"
### ###### ############################

def GetWb():
	import neo_xl_appbuilder as ap
	from inspect import getsourcefile
	import os.path

	ipath = os.path.abspath(getsourcefile(lambda:0))
	objpath = ipath[:ipath.rfind(os.path.sep)] + "\\neoCL.iParametersEditor.xlsm"
	
	XL, wb = ap.getApp(False, objpath, True)
	return XL, wb


def ImportXl():
	with db.Transaction('neoCL | Import from iParameters Editor'):
		XL, wb = GetWb()
		sh = wb.Worksheets(shName)
		sh.Activate
		ImportMain(sh)
		wb.Save
		wb.Close

def ImportMain(sh):
	ri = re
	ci = ce
	atLeastOneImport = False
	while(True):
		r = sh.Range[rg(ri, ci)]
		ri += 1
		rv = r.Text
		if rv:
			strEl = db.Element.from_int(int(rv)).name + " | ID[" + rv + "]"
			print(strEl)
			ImportThisRow(r, sh)
			atLeastOneImport = True
		else:
			if atLeastOneImport:
				print("Import is done!")	    	
			else:
				print("Any to import!")
			return

def ImportThisRow(r, sh):
	ri = r.Row
	ci = r.Column
	eq = db.Element.from_int(int(r.Text))
	
	while(True):
		ci += 1
		rp = sh.Range[rg(rt, ci)]
		rpv = rp.Text
		if rpv:
			rpN = sh.Range[rg(ri, ci)]
			rpNvTxt = rpN.Text
			rpNvVal = rpN.Value2
			try:		
				pm = eq.parameters[rpv]
				try:
					if pm.type is str:
						pm._revit_object.Set(str(rpNvTxt))
					elif pm.type is int:
						pm._revit_object.Set(int(rpNvVal))
					elif pm.type is float:
						pm._revit_object.SetValueString(str(rpNvVal))
					else:
						#if rpNv != pm.AsValueString(): #avoid mess with non modified parameters
						pm._revit_object.SetValueString(rpNvTxt)
				except:
					print("-> Can't set this parameter: " + rpv)
			except:
				print("-> Doesn't have this parameter: " + rpv)
		else:
			return "Done"