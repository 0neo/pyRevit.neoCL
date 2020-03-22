import _neo_importer
import lib.xl.neo_xl_revisions as xl
from Autodesk.Revit import DB
from rpw import doc #, db, uidoc, ui

revDB = {}
revIdsToReorder = []

def UpdateDB():
	revs = DB.Revision.GetAllRevisionIds(doc)
	for r in revs:
		rev = doc.GetElement(r)
		revDB[rev.SequenceNumber] = rev # Test the behavior, check if has this type of  order 1, 10, 11, 13, 2, 3...

def Export():
	UpdateDB()
	xl.Export()
	
def Import():
	xl.Import()

def OpenHowTo():
	xl.OpenHowTo()

def ReorderRevisions():
	import operator
	global revIdsToReorder
	rReorder = sorted(revIdsToReorder, key=operator.itemgetter(0))
	Ids = []
	for rev in rReorder:
		Ids.append(rev[1])
	DB.Revision.ReorderRevisionSequence(doc, Ids)

def DeleteRevision(revId):
	try:
		import System
		from System.Collections.Generic import List
		ElId = DB.ElementId(int(revId))
		doc.Delete(List[DB.ElementId]([ElId]))
		return True
	except:
		return False