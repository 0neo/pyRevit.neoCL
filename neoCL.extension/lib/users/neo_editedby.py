import _neo_importer
from lib.xl import neo_xl_appbuilder as ap
from lib.xl.neo_xl_functions import xlFrezzer
from rpw import ui
from rpw.ui.forms import Alert
from pyrevit import revit

def AlertSelection(els):
	if len(els) < 1:		
		Alert('No elements selected!\nSelect elements before run.\nYou can select elements in Project Browser also.',
				title="neoCL | Edited By", header="Any elements found!")
		return False
	else:
		return True

def Editors():	
	els = ui.Selection()
	if AlertSelection(els):
		if revit.doc.IsWorkshared:
			ExportToExcel(els)
		else:
			Alert("Can't get information from a non Workshared document.", title="neoCL | Edited By", header="Warning")
					   
def ExportToExcel(els):
	
	XL, wb = ap.getApp(True)

	sh = wb.Activesheet
	sh.Cells(1, 1).Value = "Exporting... please wait..."
	sh.Columns(1).AutoFit()
	sh.Name = "neoCL | Edited By"
	XL.Caption = "neoCL.Revit"
	xlRestore = xlFrezzer(XL)

	i = 1
	sh.Cells(i, 1).Value = "ID"
	sh.Cells(i, 2).Value = "Creator"
	sh.Cells(i, 3).Value = "Last Changed By"
	sh.Cells(i, 4).Value = "Owner"
	sh.Cells(i, 5).Value = "Category"
	sh.Cells(i, 6).Value = "Family"
	sh.Cells(i, 7).Value = "Type"

	for el in els:
		i += 1
		try:
			try: elhistory = revit.query.get_history(el)
			except: pass
			try: sh.Cells(i, 1).Value = "'" + str(el.Id)
			except: sh.Cells(i, 1).Value = "[N\A?]"
			try: sh.Cells(i, 2).Value = "'" + str(elhistory.creator)
			except: sh.Cells(i, 2).Value = "[N\A?]"
			try: sh.Cells(i, 3).Value = "'" + str(elhistory.last_changed_by)
			except: sh.Cells(i, 3).Value = "[N\A?]"
			try: sh.Cells(i, 4).Value = "'" + str(elhistory.owner)
			except: sh.Cells(i, 4).Value = "[N\A?]"
			try: sh.Cells(i, 5).Value = "'" + str(el.parameters['Category'].AsValueString())
			except: sh.Cells(i, 5).Value = "[N\A?]"
			try: sh.Cells(i, 6).Value = "'" + str(el.parameters["Family"].AsValueString())
			except: sh.Cells(i, 6).Value = "[N\A?]"
			try: sh.Cells(i, 7).Value = "'" + str(el.parameters["Type"].AsValueString())
			except: sh.Cells(i, 7).Value = "[N\A?]"
		except:
			pass
			
	FormatsExcel(sh)
	xlFrezzer(XL, True, xlRestore)


def FormatsExcel(sh):
	sh.Columns.AutoFit()
	sh.Cells.Interior.Color = 12611584
	sh.Cells.Font.Color = 16777215 
	sh.Range("A1:G1").Interior.Color = 16777215 
	sh.Range("1:1").Cells.Font.Color = 0
	sh.Range("1:1").HorizontalAlignment = -4108
	sh.Range("1:1").VerticalAlignment = -4107
	xlCons = [7, 8, 9, 10, 11, 12]
	for xlc in xlCons:
		sh.Range("A:G").Borders(xlc).LineStyle = 1
		sh.Range("A:G").Borders(xlc).Color = 16777215