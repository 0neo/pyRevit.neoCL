import neo_increment_config as g
import neo_increment_main as m
from rpw import ui, db, doc

def UserSelect(onlyOne=False):
	#import _neo_importer
	#from neocl__funcs import neoAlert
	#mg = "No elements selected, pick elements..."
	#print(mg)
	#neoAlert(mg, title="neoCL", header="neoCL | iParameters Editor")
	els = []
	ct = 0
	go = True

	#print("Selecting... ")
	while go:

		try:
			print("Selecting")
			mg = 'neoCL | Pick Element(s) by order! ESCAPE key when done. Total[' + str(ct) + "]"
			el = ui.Pick.pick_element(msg=mg, multiple=False)
			el = db.Element.from_id(el.id)
			if onlyOne:
				return el
			else:
				els.append(el)
				ct = len(els)
				print("Selecting... Total[" + str(ct) + "]")
		except:
			print("Done! Loading to Excel...")
			go = False
			if onlyOne:
				return None	
	return els

def SelectRef():
    g.fm.Visible = False
    g.fm.Close()
    #el = UserSelect(True)
    el = ui.Pick.pick_element(msg="select", multiple=False)
    el = db.Element.from_id(el.id)
    #g.fm = m.Form1() 
    if el:
        print(el.name)
        g.elRef = el
        g.fm._comboBoxPams.Items.Clear()
        pmap = el.parameters.all
        pmap.sort(key=lambda x: x.name, reverse=False)
        pmap.sort(key=lambda x: x.Definition.ParameterGroup, reverse=False)
        for pm in pmap:
            if IsValidParam(pm):
                g.fm._comboBoxPams.Items.Add(pm.Definition.Name)
    g.fm.Visible = True
    g.fm.Show()
    #Start()

def IsValidParam(pm):
	#pm._revit_object.UserModifiable
	okPm = not pm._revit_object.IsReadOnly
	okPm = okPm and pm.Definition.Name != "Family and Type" #Probably already canceled (if isreadonly)
	okPm = okPm and pm.Definition.Name != "Family"
	okPm = okPm and pm.Definition.Name != "Type"
	return okPm

def Start():
    with db.Transaction('neoCL | Import from iParameters Editor'):
        go = True
        val = g.pmVal
        print("Val " + str(val))
        while go:
            el = UserSelect(True)
            if el:
                pm = el.parameters[g.pmTag]
                try:
                    if pm.type is str:
                        pm._revit_object.Set(str(val))
                    elif pm.type is int:
                        pm._revit_object.Set(int(val))
                    elif pm.type is float:
                        pm._revit_object.SetValueString(str(val))
                    else:
                        pm._revit_object.SetValueString(val)
                except:
                    print("-> Can't set this parameter: " + val)
            else:
                go = False
