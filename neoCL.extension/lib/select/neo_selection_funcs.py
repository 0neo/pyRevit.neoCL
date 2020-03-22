import _neo_importer
from Autodesk.Revit						import DB
from Autodesk.Revit.DB					import ElementSet, ElementId
from rpw								import ui, uidoc, doc, db
from rpw.utils.dotnet					import List
from rpw.ui.forms						import Alert
from lib.funcs.neo_functions_collectors import CollectAllElements

# SELECT ALL ### ###########################################################################
def SelectAllInView(catTypes=['Model', 'Annotation']):
	els = db.Collector(view=doc.ActiveView)
	els = FilterCategoryType(els, catTypes)
	msg = "Any elements found in Active View."
	if AlertSelection(els, msg):
		SetFocus(els)
	
def SelectAllInProject(catTypes=['Model', 'Annotation']):
	#els = db.Collector(where=lambda x: x.get_category().CategoryType.ToString() == 'Model')
	els = []
	elsc = []
	for cat in doc.Settings.Categories:
		try:
			els = db.Collector(of_category=cat.Name)
			elsc += els
		except:
			pass
	els = FilterCategoryType(elsc, catTypes)
	msg = "Any elements found in Project."
	if AlertSelection(els, msg):
		SetFocus(els)

#def SelectAllInView(ignoreTags=False):
#	els = CollectAllElements("ActiveView", ignoreTags)
#	msg = "Any elements found in Active View."
#	if AlertSelection(els, msg):
#		SetFocus(els)
	
#def SelectAllInProject(ignoreTags=False):
#	els = CollectAllElements("Project", ignoreTags, GetListOfAllCategoriesNamesInDoc())
#	msg = "Any elements found in Project."
#	if AlertSelection(els, msg):
#		SetFocus(els)
		
# SELECT SIMILAR ### #######################################################################
def SelectSimilar(where='ActiveView'):	
	els = ui.Selection()
	elTypes = FilterSelection(els)
	
	colEls = []
	colElsc = []
	
	for pmEnum, pmValues in elTypes.items():
		for elt in pmValues:
			param_id = DB.ElementId(pmEnum)
			parameter_filter = db.ParameterFilter(param_id, equals=elt)
			if where == 'ActiveView':
				colEls = db.Collector(view=doc.ActiveView, parameter_filter=parameter_filter)
			elif where == 'Project':
				colEls = db.Collector(parameter_filter=parameter_filter)
			else:
				return False
			colEls = colEls.get_elements(True)
			colElsc += colEls

	SetFocus(colElsc)

def FilterSelection(els):
	# Try to process as much types of elements in project as possible.
	# From more unique parameters, as type of instance, to more general, as categorie.
	types = []
	families = []
	categories = []

	for el in els:
		try:
			types.append(el.parameters['Family and Type'].AsValueString())
		except:
			try:
				families.append(el.parameters['Family'].AsValueString())
			except:
				try:
					categories.append(el.parameters['Category'].AsValueString())
				except:
					pass

	types = list(set(types))
	families = list(set(families))
	categories = list(set(categories))

	bp = DB.BuiltInParameter

	filterSel = {bp.ELEM_FAMILY_AND_TYPE_PARAM: types, 
				 bp.ELEM_FAMILY_PARAM: families,
				 bp.ELEM_CATEGORY_PARAM: categories}

	return filterSel

# REMOVE ANNOTATION ### ####################################################################
def RemoveAnnotationFromSelection():
	els = ui.Selection()
	catTypes = [x for x in GetAllCatTypes() if (x not in ['Annotation'])]
	els = FilterCategoryType(els, catTypes)
	msg = "Any elements non Annotantion in selection."
	if AlertSelection(els, msg):
		try:
			eids = List[ElementId](GetListOfIds(els))
			uidoc.Selection.SetElementIds(eids)
		except:
			Alert("Can't create new selection!", title="neoCL | Selection", header="Error trying to select...")
# AUX ### ##################################################################################
def AlertSelection(els, msg):
	if len(els) < 1:		
		Alert(msg, title="neoCL | Selection", header="Any elements found!")
		return False
	else:
		return True

def GetAllCatTypes():
	return ['Model', 'Annotation', 'Internal', 'AnalyticalModel', 'Invalid']

def FilterCategoryType(els, catTypes=GetAllCatTypes()):
	ctEls = []
	for el in els:
		try:
			#elCat = el.get_category().CategoryType.ToString()
			elCat = el.Category.CategoryType.ToString()
			if elCat in catTypes:
				ctEls.append(el)
		except:
			pass
	return ctEls

def SetFocus(els, cancelSelect=False):
	try:
		eids = List[ElementId](GetListOfIds(els))
		if not cancelSelect:
			uidoc.Selection.SetElementIds(eids)
		uidoc.ShowElements(eids)
	except:
		Alert("Can't set focus!", title="neoCL | Selection", header="Any elements found!")

def GetListOfIds(els):
	elsid = []
	for el in els:
		elsid.append(el.Id)
	return elsid

def GetListOfAllCategoriesNamesInDoc():
	cats = []
	for cat in doc.Settings.Categories:
		cats.append(cat.Name)
	return cats