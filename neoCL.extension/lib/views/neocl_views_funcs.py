from Autodesk.Revit import DB
from rpw import doc, uidoc

def ActivateView(viewid='', viewname=''):
	try:
		if viewid:
			uidoc.ActiveView = doc.GetElement(viewid)
		elif viewname:
			uidoc.ActiveView = GetViewIdByName(viewname)
	except:
		pass


def GetViewIdByName(viewname):
	col = DB.FilteredElementCollector(doc).OfClass(View)
	for v in col:
		if v.Name == viewname:
			