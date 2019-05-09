#######################################
### neoCL | Find and Replacer #########
#######################################

from neo_findreplace_funcs_main import *

def AlertSelection(els, msg):

	#elsLen = 0
	#for col in collectors:
	#	elsLen += len(col)

	if len(els) < 1:		
		g.fm.TopMost = False
		Alert('No elements in ' + msg + '!', title="neoCL | Find", header="Error!")
		g.fm.TopMost = True
		BringToFront()
		return False
	else:
		return True

def CollectData():
	
	dataok = False
	els = []
	#g.result = ""
	g.savetable = "Value\tParameter\tType Instance\tLevel\tCategory\tFamily Instance\tId\n"
	
	SetCategories()

	if g.fm._radioButtonFindInSel.Checked:

		els = ui.Selection()
		dataok = AlertSelection(els, "Active Selection")

	elif g.fm._radioButtonFindInView.Checked:
		
		els = nfc.CollectAllElements("ActiveView", g.fm._checkBoxIgnoreTags.Checked, g.catselList)				
		dataok = AlertSelection(els, "Active View")

	elif g.fm._radioButtonFindInProject.Checked:
		
		els = nfc.CollectAllElements("Project", g.fm._checkBoxIgnoreTags.Checked, g.catselList)
		dataok = AlertSelection(els, "Active Project")

	if dataok:
		ClearData()
		for elx in els:
			try:
				cat = elx.parameters["Category"].AsValueString()
			except:
				cat = None
			finally:
				CollectData_CheckCat(elx, cat)
		AutoFitListView()
		#g.WriteResult()

def CollectData_CheckCat(elx, cat):

	el = None

	if cat:
		if cat == "Text Notes":
			# After process text note, keep checking tag parameters...
			try:
				pval = elx.Text
				if CheckParamValByUserOptions(pval):
					pam = param(elx, None, pval, cat)
			except:
				return
		elif cat == "Room Tags":
			
			# After process text tag, keep checking tag parameters...
			try:
				pval = elx.TagText
				if CheckParamValByUserOptions(pval):
					pam = param(elx, None, pval, cat)
			except:
				return
		elif "Tags" in str(cat): 
			try:
				# process tag parameters. (elx, elx) not (el, elx)
				CollectData_CheckPmap(elx, elx)
				# try to get host to process its parameters
				el = db.Element.from_id(elx.TaggedElementId.HostElementId)
			except:
				return

	if not el: el = elx

	CollectData_CheckPmap(el, elx)

def CollectData_CheckPmap(el, elx):

    pmap = el.parameters.all

    for pm in pmap:

        if AllowParam(pm):

            if pm.type is str:
                pval = pm.AsString()
            elif pm.type is int:
                pval = pm.value
            elif pm.type is float:
                pval = pm.value * 304.8  # don't know why I have to do this math, only way I have to get a correct value.
            else:
                pval = pm.AsValueString()

            if pval:
                if CheckParamValByUserOptions(pval):
                    pam = param(elx, pm, pval)

def CheckParamValByUserOptions(pval):

	import re

	xval = str(pval)
	fval = g.active_findstr
	ok = True	

	# Case-sensitive #########################
	if not g.fm._checkBoxCaseSensitive.Checked:
		xval = xval.lower()
		fval = fval.lower()

	# Full word ##############################
	if g.fm._checkBoxFullWord.Checked:
		if not g.fm._checkBoxCaseSensitive.Checked:					# if check not needed (Case-sensitive already checked in previous if) but stay not depedent for future changes in code
			pattern = ".*(?:^|\W)(?i)" + fval + "(?i)(?:$|\W).*"	# Full word without letter or numbers left or right, case non-sensitive
		else:
			pattern = ".*(?:^|\W)" + fval + "(?:$|\W).*"			# Full word without letter or numbers left or right
	
		ok = ok and re.match(pattern, xval)
	
	# Full parameter #########################
	if g.fm._checkBoxFullParameter.Checked:
		if xval == fval:
			ok = ok and True
		else:
			ok = ok and False						# same as ok = False, but keep the code pattern
	elif fval in xval:
		ok = ok and True
	else:
		ok = ok and False							# same as ok = False, but keep the code pattern

	# Match mode Regex #######################
	if g.fm._checkBoxMatch.Checked:
		ok = re.match(fval, xval)					# if match mode, regect all checks before as they don't matter
	
	# Done ###################################
	return ok

def AllowParam(pm):
	#ok = not pm._revit_object.IsReadOnly
	ok = True
	ok = ok and pm._revit_object.HasValue
	ok = ok and pm.Definition.Name != "Family and Type"
	ok = ok and AllowParam_CheckUserOptions(pm)
	return ok

def AllowParam_CheckUserOptions(pm):
	
	ok = True

	if pm.Definition.Name == "Family":
		if not g.fm._checkBoxSearchTypes.Checked:
			ok = ok and False	#same as [ok = False] but keep code pattern

	if pm.Definition.Name == "Type":
		if not g.fm._checkBoxSearchTypes.Checked:
			ok = ok and False	#same as [ok = False] but keep code pattern

	if pm.Definition.Name == "Type Name":
		if not g.fm._checkBoxSearchTypes.Checked:
			ok = ok and False	#same as [ok = False] but keep code pattern

	if pm.Definition.Name == "Category":
		if not g.fm._checkBoxSearchTypes.Checked:
			ok = ok and False	#same as [ok = False] but keep code pattern

	return ok

def SetCategories():

	g.catselList = []

	for i in g.fmsc._checkedListBoxCatSelector.CheckedItems:
		g.catselList.append(i)