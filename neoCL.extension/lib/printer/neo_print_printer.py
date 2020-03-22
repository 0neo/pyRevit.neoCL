import Autodesk
from Autodesk.Revit.DB import *
from rpw import db
import os
import shutil

#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

def PrintView(doc, sheet, pRange, printerName, PrinterFolderPath, RealFolderPath, FileName, combined, printSetting):
	
	viewSet = ViewSet()
	viewSet.Insert(sheet)
	
	tempFullName = PrinterFolderPath + "\\" + FileName
	realFullName = RealFolderPath + "\\" + FileName

	pm = doc.PrintManager
	pm.PrintRange = pRange
	pm.PrintRange = PrintRange.Select
	pm.ViewSheetSetting.CurrentViewSheetSet.Views = viewSet
	pm.SelectNewPrintDriver(printerName)
	pm.PrintToFile = True
	pm.PrintToFileName = realFullName
	pm.Apply()
	try:
		printSetup = pm.PrintSetup
		printSetup.CurrentPrintSetting = printSetting
		pm.Apply()
	except:
		pass

	with db.Transaction('neoCL | Print'):
		pm.SubmitPrint()
		shutil.move(tempFullName, realFullName)


#def DeleteViewSet(doc, ViewSetName):
#	viewSets = FilteredElementCollector(doc).OfClass(ViewSheetSet)
#	for vs in viewSets:
#		if vs.Name == ViewSetName:
#			with db.Transaction('neoCL | Printer'):
#			    doc.Delete(i.Id)


	#pm.CombinedFile = combined
	#pm.PrintToFile = pm.IsVirtual

	#ViewSetName = "neoCL_PDF_Printer"
	#DeleteViewSet(doc, ViewSetName)

	#printManager.PrintToFile = True

	# set file path
	#pm.PrintToFileName = FullFileName
	#pm.Apply()
	# apply print setting

		#try:
		#	pm.ViewSheetSetting.SaveAs(ViewSetName)
		#	pm.Apply()
		#except:
		#	pass
		#pm.ViewSheetSetting.Delete()