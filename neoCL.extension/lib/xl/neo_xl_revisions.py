#import time
from Autodesk.Revit import DB
from neo_xl_functions import rg, ClearColumnFrom, ActivateSheet, xlFrezzer, SetFiltering
from rpw import db, doc
from rpw.ui.forms import Alert

### config ############################
rt1 = 2 	    #Title row 1
ct = 1 	        #First Column Title
re = rt1 + 1	#First element row
ce = ct 		#First Column Element
shName = "neoCL.Revisions"
### ###### ############################

def GetWb():
	import neo_xl_appbuilder as ap
	from inspect import getsourcefile
	import os.path

	ipath = os.path.abspath(getsourcefile(lambda:0))
	objpath = ipath[:ipath.rfind(os.path.sep)] + "\\neoCL.Revisions.xlsm"
	
	XL, wb = ap.getApp(False, objpath, True)
	return XL, wb

### OPENHOWTO #############################################

def OpenHowTo():
	XL, wb = GetWb()
	xlRestore = xlFrezzer(XL)
	try:
		sh = wb.Worksheets(shName)
		SetFiltering(sh)
	except: pass	
	try: ActivateSheet(sh)
	except: pass	
	xlFrezzer(XL, True, xlRestore)	


### EXPORT #############################################

def Export():
	XL, wb = GetWb()
	try: sh = wb.Worksheets(shName)
	except: pass
	sh.Cells(1, 1).Value = "Exporting to Excel... please wait..."
	xlRestore = xlFrezzer(XL)
	FillData(sh)
	xlFrezzer(XL, True, xlRestore)	
	#print("Excel is ready!")
	   	
def FillData(sh):

    sh.Cells.ClearContents()

    sh.Range[rg(rt1, ce)].Value2 = "'ID"
    sh.Range[rg(rt1, ce + 1)].Value2 = "'Order"
    sh.Range[rg(rt1, ce + 2)].Value2 = "'Numbering"
    sh.Range[rg(rt1, ce + 3)].Value2 = "'Date"
    sh.Range[rg(rt1, ce + 4)].Value2 = "'Description"
    sh.Range[rg(rt1, ce + 5)].Value2 = "'Issued"
    sh.Range[rg(rt1, ce + 6)].Value2 = "'Issued to"
    sh.Range[rg(rt1, ce + 7)].Value2 = "'Issued by"
    sh.Range[rg(rt1, ce + 8)].Value2 = "'Log"
    
    FillData_Rows(sh)

    sh.Range[rg(1, 1)].Value2 = "Export to Excel is done! Read HOW TO sheet!"

    sh.Cells.EntireColumn.AutoFit()   

def FillData_Rows(sh):
    import _neo_importer
    import lib.revisions.neo_revisions_main as mn
    #main.UpdateDB()
    ri = re
    #ci = ce
    for key in mn.revDB:
        rev = mn.revDB[key]
        sh.Range[rg(ri, ce)].Value2 = "'" + str(rev.Id.ToString())
        sh.Range[rg(ri, ce + 1)].Value2 = "'" + str(key)
        sh.Range[rg(ri, ce + 2)].Value2 = "'" + str(rev.NumberType.ToString())
        sh.Range[rg(ri, ce + 3)].Value2 = "'" + str(rev.RevisionDate)
        sh.Range[rg(ri, ce + 4)].Value2 = "'" + str(rev.Description)
        sh.Range[rg(ri, ce + 5)].Value2 = "'" + ('Yes' if rev.Issued else 'No')
        sh.Range[rg(ri, ce + 6)].Value2 = "'" + str(rev.IssuedTo)
        sh.Range[rg(ri, ce + 7)].Value2 = "'" + str(rev.IssuedBy)
        sh.Range[rg(ri, ce + 8)].Value2 = "'Ready..."
        ri += 1

### IMPORT #############################################

def Import():
	import _neo_importer
	import lib.revisions.neo_revisions_main as mn
	with db.Transaction(str('neoCL | Import Revisions')):
		XL, wb = GetWb()
		XL.DisplayAlerts = False
		sh = wb.Worksheets(shName)
		sh.Cells(1, 1).Value = "Importing to Revit... please wait..."

		ri = re
		#ci = ce
	
		while(True):

			newRev = False
			rId = sh.Range[rg(ri, ce)]
			rlog = sh.Range[rg(ri, ce + 8)]
			rDescription = sh.Range[rg(ri, ce + 4)]
			revOrder = sh.Range[rg(ri, ce + 1)].Text
			revOrder = int(revOrder.strip() or 0)

			if rId.Text and not rDescription.Text:
				if mn.DeleteRevision(rId.Text):
					rlog.Value2 = "Revision DELETED!"
				else:
					rlog.Value2 = "Can't delete revision!"
					mn.revIdsToReorder.append([int(revOrder), DB.ElementId(int(rId.Text))])

			elif rDescription.Text:
				try:
					revId = rId.Text
					if revId:
						rev = doc.GetElement(DB.ElementId(int(revId)))
					else:
						rev = DB.Revision.Create(doc)
						revId = rev.Id.ToString()
						sh.Range[rg(ri, ce)].Value2 = "'" + revId
						newRev = True
					mn.revIdsToReorder.append([int(revOrder), DB.ElementId(int(revId))])
					rev.Issued = True if sh.Range[rg(ri, ce + 5)].Text == 'Yes' else False
					if not rev.Issued:
						rev.RevisionDate = sh.Range[rg(ri, ce + 3)].Text
						rev.Description = sh.Range[rg(ri, ce + 4)].Text
						rev.IssuedTo = sh.Range[rg(ri, ce + 6)].Text
						rev.IssuedBy = sh.Range[rg(ri, ce + 7)].Text
						numType = sh.Range[rg(ri, ce + 2)].Text
						if numType == "Numeric":
							rev.NumberType = DB.RevisionNumberType.Numeric 
						elif numType == "Alphanumeric":
							rev.NumberType = DB.RevisionNumberType.Alphanumeric
						elif numType == "None":
							rev.NumberType = DB.RevisionNumberType.None
						rlog.Value2 = "Done."
					else:
						rlog.Value2 = "Can't update data in Issued revisions. Set Issued to No to allow editing."
				except: # OSError as err:
						#print("OS error: {0}".format(err))
						rlog.Value2 = "Error trying to update... Is the Id correct?"
				if newRev:
					rlog.Value2 = "New revision created. " + rlog.Value2

			elif not rId.Text and not rDescription.Text:
				try:
					mn.ReorderRevisions()
					#print("Import is done!")
					sh.Cells(1, 1).Value = "Import to Revit is done!"
				except:
					err = "Process ended. Can't reorder revisions! Are all the revisions listed in Excel? Read HOW TO sheet!"
					#print(err)
					sh.Range[rg(1, 1)].Value2 = err
				sh.Cells.EntireColumn.AutoFit()
				XL.DisplayAlerts = True
				return
			ri += 1