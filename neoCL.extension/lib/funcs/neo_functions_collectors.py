#######################################
### neoCL | Collectors ################
#######################################

from rpw import db, doc, uidoc, ui

def CollectAllElements(where, ignoreTags=False, categoriesFilter=[]):
	els = []
	elsc = []
	for cat in doc.Settings.Categories:
		try:
			#if "tags" in cat.Name.lower() and ignoreTags:
			#	pass
			#else:
			if ValidCategory(cat, ignoreTags, categoriesFilter):
				if where == "ActiveView":
					els = db.Collector(view=doc.ActiveView, of_category=cat.Name)
				elif where == "Project":
					els = db.Collector(of_category=cat.Name)
				else:
					break
				els = els.get_elements(True)
				elsc += els
		except:
			pass
	return elsc

def ValidCategory(cat, ignoreTags=False, categoriesFilter=[]):

	if ignoreTags:
		if "tags" in cat.Name.lower():
			return False
	
	if not categoriesFilter:
		return True
	else:
		for c in categoriesFilter:
			if c == cat.Name:
				return True
	
	return False