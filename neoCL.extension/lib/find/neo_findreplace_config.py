#######################################
### neoCL | Find and Replacer #########
#######################################

from inspect import getsourcefile
import os.path
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

def WriteDefaults():
	#config.set('FORM', '_buttonClose', v_buttonClose)
	#config.set('FORM', '_buttonFind', v_buttonFind)
	#config.set('FORM', '_buttonReplaceAll', v_buttonReplaceAll)
	#config.set('FORM', '_buttonReplaceSelected', v_buttonReplaceSelected)
	#config.set('FORM', '_buttonSelectionAll', v_buttonSelectionAll)
	#config.set('FORM', '_buttonSelectionSelected', v_buttonSelectionSelected)
	config.set('FORM', '_checkBoxCaseSensitive', v_checkBoxCaseSensitive)
	config.set('FORM', '_checkBoxFullParameter', v_checkBoxFullParameter)
	config.set('FORM', '_checkBoxFullWord', v_checkBoxFullWord)
	config.set('FORM', '_checkBoxIgnoreTags', v_checkBoxIgnoreTags)
	config.set('FORM', '_checkBoxLinks', v_checkBoxLinks)
	config.set('FORM', '_checkBoxMatch', v_checkBoxMatch)
	config.set('FORM', '_checkBoxModal', v_checkBoxModal)
	config.set('FORM', '_checkBoxSaveDefaults', v_checkBoxSaveDefaults)
	config.set('FORM', '_checkBoxKeepSaveDefaults', v_checkBoxKeepSaveDefaults)
	config.set('FORM', '_checkBoxSearchTypes', v_checkBoxSearchTypes)
	#config.set('FORM', '_comboBoxFind', v_comboBoxFind)
	#config.set('FORM', '_comboBoxReplace', v_comboBoxReplace)
	#config.set('FORM', '_groupBoxOptions', v_groupBoxOptions)
	#config.set('FORM', '_labelbyneo', v_labelbyneo)
	#config.set('FORM', '_labelCreateSelection', v_labelCreateSelection)
	#config.set('FORM', '_labelFindIn', v_labelFindIn)
	#config.set('FORM', '_labelFoundLog', v_labelFoundLog)
	#config.set('FORM', '_labelReplace', v_labelReplace)
	#config.set('FORM', '_labelToFind', v_labelToFind)
	#config.set('FORM', '_listBoxResult', v_listBoxResult)
	config.set('FORM', '_radioButtonFindInProject', v_radioButtonFindInProject)
	config.set('FORM', '_radioButtonFindInSel', v_radioButtonFindInSel)
	config.set('FORM', '_radioButtonFindInView', v_radioButtonFindInView)
	WriteConfig()

def WriteResult():
	config.set('FORM', '_Result', result)
	WriteConfig()

def WriteConfig():
	with open(npath, 'wb') as conf:
		config.write(conf)

def SetIgnoreCategoriesList():

	if ini:

		global v_ignoreCategories

		v_ignoreCategories.replace(',', '')

		for i in range(0, fmsc._checkedListBoxCatSelector.Items.Count):
			item = fmsc._checkedListBoxCatSelector.Items[i]
			if not fmsc._checkedListBoxCatSelector.GetItemCheckState(i):
				if not item in v_ignoreCategories:
					v_ignoreCategories += "," + item + ","
		
		for item in fmsc._checkedListBoxCatSelector.CheckedItems:
			v_ignoreCategories = v_ignoreCategories.replace(',' + item + ',', ',')

		while ',,' in v_ignoreCategories:
			v_ignoreCategories = v_ignoreCategories.replace(',,', ',')

		if v_ignoreCategories == ',':
			v_ignoreCategories = ''

		config.set('FORM', '_ignoreCategories', v_ignoreCategories)
		WriteConfig()

def AddtoFindList(fstr):
	if ini:
		global v_comboBoxFind
		v_comboBoxFind = AddToArrayString(v_comboBoxFind, fstr)
		config.set('FORM', '_comboBoxFind', v_comboBoxFind)
		WriteConfig()

def AddtoRepalceList(fstr):
	if ini:
		global v_comboBoxReplace
		v_comboBoxReplace = AddToArrayString(v_comboBoxReplace, fstr)
		config.set('FORM', '_comboBoxReplace', v_comboBoxReplace)
		WriteConfig()

def AddToArrayString(arrstr, astr):

	limit = 99
	arrstr = str(astr) + ',' + arrstr
	sp = arrstr.split(',')
	
	# Clean doubles	
	spx = []
	ss = set()
	for c in range(len(sp)):
		if not sp[c] in ss:
			spx.append(sp[c])
			ss.add(sp[c])
	
	# Set limit
	tt = len(spx)
	if tt >= limit: tt = limit

	arrstr = ''
	for c in range(tt):
		arrstr += ',' + spx[c]

	return arrstr

def GetY(Yi):
	global fmHeight
	global fmBorderH
	return fmHeight - fmBorderH - Yi

def GetX(Xi):
	global fmWidth
	global fmBorderW
	return fmWidth - fmBorderW - Xi

def GetListViewResultH():
	global fmHeight
	global fmBorderH
	global lvrY
	global lvrYo
	return fmHeight - fmBorderH - lvrY - lvrYo

def GetListViewResultW():
	global fmWidth
	global fmBorderW
	global lvrX
	return fmWidth - fmBorderW - (lvrX * 2)

# START ### ######################################################################
ipath = os.path.abspath(getsourcefile(lambda:0))
npath = ipath[:ipath.rfind(os.path.sep) + 1] + "neo_findreplace_config.ini" 
config = ConfigParser()
config.optionxform = str 
config.read(npath)

# RUNNING VARS ### ###############################################################
ini = True
fm = None
fmsc = None
selfindList = []
pmfindList = []
catselList = []
active_findstr = ""
active_repstr = ""
result = ""
savetable = ""

# FORM DESIGN VARS ### ###########################################################
fmHeightmin = 400
fmWidthmin = 800

fmHeight = fmHeightmin
fmWidth = fmWidthmin

fmBorderH = 39
fmBorderW = 16

lvrX = 12
lvrY = 141
lvrYo = 47
lvrHeight = GetListViewResultH()
lvrWidth = GetListViewResultW()

modalXi = 62
modalX = GetX(modalXi) 
modalYi = 18 + 11
modalY = GetY(modalYi) 

savetableXi = modalXi + 12
savetableX = modalX + 12
savetableYi = modalYi + 18
savetableY = modalY + 18

btfindX = 12
btfindYi = 30 + 11
btfindY = GetY(btfindYi)

btrallX = 324
btrallYi = 30 + 11
btrallY = GetY(btrallYi)

btrslX = 168
btrslYi = 30 + 11
btrslY = GetY(btrslYi)

btcloseX = 480
btcloseYi = 30 + 11
btcloseY = GetY(btcloseYi)


# INI ### ########################################################################
try:
	#v_buttonClose = config.get('FORM', '_buttonClose')
	#v_buttonFind = config.get('FORM', '_buttonFind')
	#v_buttonReplaceAll = config.get('FORM', '_buttonReplaceAll')
	#v_buttonReplaceSelected = config.get('FORM', '_buttonReplaceSelected')
	#v_buttonSelectionAll = config.get('FORM', '_buttonSelectionAll')
	#v_buttonSelectionSelected = config.get('FORM', '_buttonSelectionSelected')
	v_checkBoxCaseSensitive = config.getboolean('FORM', '_checkBoxCaseSensitive')
	v_checkBoxFullParameter = config.getboolean('FORM', '_checkBoxFullParameter')
	v_checkBoxFullWord = config.getboolean('FORM', '_checkBoxFullWord')
	v_checkBoxIgnoreTags = config.getboolean('FORM', '_checkBoxIgnoreTags')
	v_checkBoxLinks = config.getboolean('FORM', '_checkBoxLinks')
	v_checkBoxMatch = config.getboolean('FORM', '_checkBoxMatch')
	v_checkBoxModal = config.getboolean('FORM', '_checkBoxModal')
	v_checkBoxKeepSaveDefaults = config.getboolean('FORM', '_checkBoxKeepSaveDefaults')
	v_checkBoxSaveDefaults = config.getboolean('FORM', '_checkBoxSaveDefaults')
	v_checkBoxSaveDefaults = False if not v_checkBoxKeepSaveDefaults else v_checkBoxSaveDefaults
	v_checkBoxSearchTypes = config.getboolean('FORM', '_checkBoxSearchTypes')
	v_comboBoxFind = config.get('FORM', '_comboBoxFind')
	v_comboBoxReplace = config.get('FORM', '_comboBoxReplace')
	#v_groupBoxOptions = config.get('FORM', '_groupBoxOptions')
	#v_labelbyneo = config.get('FORM', '_labelbyneo')
	#v_labelCreateSelection = config.get('FORM', '_labelCreateSelection')
	#v_labelFindIn = config.get('FORM', '_labelFindIn')
	#v_labelFoundLog = config.get('FORM', '_labelFoundLog')
	#v_labelReplace = config.get('FORM', '_labelReplace')
	#v_labelToFind = config.get('FORM', '_labelToFind')
	#v_listBoxResult = config.get('FORM', '_listBoxResult')
	v_radioButtonFindInProject = config.getboolean('FORM', '_radioButtonFindInProject')
	v_radioButtonFindInSel = config.getboolean('FORM', '_radioButtonFindInSel')
	v_radioButtonFindInView = config.getboolean('FORM', '_radioButtonFindInView')
	v_ignoreCategories = config.get('FORM', '_ignoreCategories')
except:
	ini = False
