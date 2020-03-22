"""Replace Family and Types of instances
with neoCL.FamilyReplacer.
Config Excel file first.
Sheet named RUN will be precessed. 
"""

#######################################
### XlFaM.neoCL   #####################
### by neo 		  #####################
### 2019 		  #####################
#######################################
#######################################
### neoCL | FamilyReplacer ############
#######################################
import time
import _neo_importer
import lib.type.neo_ty_type_replacer_functions as tyrep
from neo_xl_functions import rg, ClearColumnFrom
from rpw import db, doc

### config ############################
rt1 = 2 	    #Title row 1
rt2 = rt1 + 1 	#Title row 2
ct = 1 	        #First Column Title
re = rt2 + 1	#First element row
ce = ct 		#First Column Element
shName = "RUN"
### ###### ############################

def GetWb():
	import neo_xl_appbuilder as ap
	from inspect import getsourcefile
	import os.path

	ipath = os.path.abspath(getsourcefile(lambda:0))
	objpath = ipath[:ipath.rfind(os.path.sep)] + "\\neoCL.FamilyReplacer.xlsm"
	
	XL, wb = ap.getApp(False, objpath, True)
	return XL, wb

def ImportXl(where="Project"):
	with db.TransactionGroup('neoCL | Import Family Replacer'):
		XL, wb = GetWb()
		XL.DisplayAlerts = False
		sh = wb.Worksheets(shName)
		ImportMain(sh, where)
		XL.DisplayAlerts = True

def ImportMain(sh, where):

    ri = re
    ci = ce
    atLeastOneImport = False

    log = sh.Range[rg(ri - 1, ci + 4)]
    ClearColumnFrom(log.Offset(1, 0))
    log.Value2 = time.ctime() + " | " + doc.PathName
    log.EntireColumn.AutoFit()

    while(True):
        find_familyName = sh.Range[rg(ri, ci)].Text
        find_typeName = sh.Range[rg(ri, ci + 1)].Text
        replace_familyName = sh.Range[rg(ri, ci + 2)].Text
        replace_typeName = sh.Range[rg(ri, ci + 3)].Text
        log = sh.Range[rg(ri, ci + 4)]
        log.Value2 = ""
        ri += 1

        if find_familyName:
            log.Value2 = tyrep.SetNewType(  find_familyName,
                                            find_typeName,
                                            replace_familyName,
                                            replace_typeName,
                                            where)
            log.EntireColumn.AutoFit()
            atLeastOneImport = True
        else:            
            if atLeastOneImport:
                log.Value2 = "^ Import is done!"
                #print("Import is done!")	    	
            else:
                log.Value2 = "^ Any to import!"
                #print("Any to import!")
            return