#import clr
import Autodesk
import System
#from Autodesk.Revit.DB import *
from rpw import doc #, ui, db
from neo_print_printer import PrintView

#clr.AddReference("RevitAPI")

#PrintRange Enumeration
#Member name	Description
#Current		A range that represents just the currently active view.
#Visible		Visible portion of current window.
#Select			A range that represents a list of selected views and sheets.

pRange = System.Enum.Parse(Autodesk.Revit.DB.PrintRange, "Current")
combined = True
printerName = "PDF_Revit"
printSetting = "neoCL_Printer"
PrinterFolderPath = r"D:\#DELETE\printer"
RealFolderPath = r"D:\#DELETE\printer\realFolder"

viewSheets = [doc.ActiveView]

def Main():
	for sheet in viewSheets:
		rev = sheet.GetRevisionNumberOnSheet(doc.GetElement(sheet.GetCurrentRevision()).Id)
		FileName = sheet.Name + "_" + rev + ".pdf"
		PrintView(doc, sheet, pRange, printerName, PrinterFolderPath, RealFolderPath, FileName, combined, printSetting)
