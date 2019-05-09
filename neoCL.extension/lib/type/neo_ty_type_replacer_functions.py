#######################################
### neoCL | Type Replacer #############
#######################################

import _neo_importer
import lib.funcs.neo_functions_collectors as nfc
from rpw import db, doc, uidoc
from Autodesk.Revit.DB import FamilySymbol, Element

def GetTypeId(replace_familyName, replace_typeName):

	col = db.Collector(of_class=FamilySymbol)
	alltypes = col.GetElementIdIterator()
	alltypes.Reset()
	
	for el in alltypes:
		fsyb = doc.GetElement(el) 
		if fsyb.Family.Name == replace_familyName:
			tyname = Element.Name.GetValue(fsyb)
			if tyname == replace_typeName:
				return fsyb.Id

def SetNewType(find_familyName, find_typeName, replace_familyName, replace_typeName, where):
	
	tyId = GetTypeId(replace_familyName, replace_typeName)
	#els = db.Collector(view=doc.ActiveView).get_elements(True)
	els = nfc.CollectAllElements(where)
	log = 'Nothing done!'
	errlog = ''

	with db.Transaction('neoCL | Family and Type Replacer'):
		for elx in els:
			try:
				elxFn = elx.parameters["Family"].value_string
				if find_familyName == elxFn:
					if find_typeName == elx.name:
						try:
							elx._revit_object.ChangeTypeId(tyId)
							log = "At least one replaced."
						except:
							errlog = errlog + "\nCouldn't change type of : " + str(elx.name) + " Id[" + str(elx.Id) + "]"
							print("Couldn't change type of : " + str(elx.name) + " Id[" + str(elx.Id) + "]")
			except:
				#print("Can't get Family of : " + str(elx.name))
				pass
	
	return log + errlog