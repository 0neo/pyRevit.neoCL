#######################################
### neoCL | Open Views ################
#######################################

import _neo_importer
from neocl__funcs import neoAlert

from rpw import uidoc, ui, db

def OpenView(viewid='', viewname=''):
	col = db.Collector(of_class='View')
	for view in col:
		if view.Id == viewid or \
           view.Name == viewname:
			try:
				uidoc.ActiveView = view
			except:
				pass

def OpenSelectedViews():

    # Future Upgrade : Find a way to activate Project browser before running...
    # OpenView('', "Project View")

    views = []

    for el in ui.Selection():
        try:
            isview = el.parameters["Category"].AsValueString()
            if isview: views.append(el)
        except:
            pass
        
    if len(views) < 1:
        mg = "Any views found, possible causes:\n\n"
        mg += "1) The Project Browser is not active;\n"
        mg += "2) There are any views selected;\n"
        mg += "3) neoCL was called outside of Project Browser. Call neoCL from ribbon instead of key shortcut."
        neoAlert(mg, title="neoCL", header="Error!")
    else:
        for view in views:
            try:
                OpenView(view.Id)
            except:
                pass