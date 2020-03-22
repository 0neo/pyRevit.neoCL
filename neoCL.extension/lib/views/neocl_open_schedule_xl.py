import _neo_importer
from lib.xl import neo_xl_appbuilder as ap
from lib.xl.neo_xl_functions import xlFrezzer, rg
from rpw import uidoc
from rpw.ui.forms import Alert
from Autodesk.Revit import DB

def ExportActiveScheduleViewToExcel():
	scView = uidoc.ActiveView
	if scView.ViewType != DB.ViewType.Schedule:
		Alert("Active View is not a Schedule!\nOpen a View Schedule and activate it, before run.", 
				title="neoCL | Open Schedule in Excel", header="Can't Export to Excel!")
		return False
	else:
		ExportThisScheduleViewToExcel(scView)

def ExportThisScheduleViewToExcel(scView):
	tb = scView.GetTableData()
	data = tb.GetSectionData(DB.SectionType.Body)
	fRow = data.FirstRowNumber
	lRow = data.LastRowNumber
	fCol = data.FirstColumnNumber
	lCol = data.LastColumnNumber
	
	XL, wb = ap.getApp(True)

	sh = wb.Activesheet
	sh.Cells(1, 1).Value = "Exporting... please wait..."
	sh.Columns(1).AutoFit()
	try: sh.Name = "neoCL | " + scView.Name
	except: pass	
	XL.Caption = "neoCL.Revit"
	xlRestore = xlFrezzer(XL)

	isError = False

	for rn in range(fRow, lRow + 1):
		for cn in range(fCol, lCol + 1):
			try: sh.Cells(rn + 1, cn + 1).Value = \
				"'" + str(scView.GetCellText(DB.SectionType.Body, rn, cn))
			except:
				isError = True							
	
	FormatsExcel(sh, fRow, lRow, fCol, lCol)
	xlFrezzer(XL, True, xlRestore)

	if isError:
		Alert("Something went wrong!\nCheck the exported data!", 
				title="neoCL | Open Schedule in Excel", header="Error(s) during process!")

def FormatsExcel(sh, fRow, lRow, fCol, lCol):
	titleRng = str(rg(fRow + 1, fCol + 1))
	titleRng += ':'
	titleRng += str(rg(fRow + 1, lCol + 1))
	tableRng = str(rg(fRow + 1, fCol + 1))
	tableRng += ':'
	tableRng += str(rg(lRow + 1, lCol + 1))
	sh.Columns.AutoFit()
	sh.Cells.Interior.Color = 12611584
	sh.Cells.Font.Color = 16777215 
	sh.Range(titleRng).Interior.Color = 16777215 
	sh.Range("1:1").Cells.Font.Color = 0
	sh.Range("1:1").HorizontalAlignment = -4108
	sh.Range("1:1").VerticalAlignment = -4107
	xlCons = [7, 8, 9, 10, 11, 12]
	for xlc in xlCons:
		sh.Range(tableRng).Borders(xlc).LineStyle = 1
		sh.Range(tableRng).Borders(xlc).Color = 16777215