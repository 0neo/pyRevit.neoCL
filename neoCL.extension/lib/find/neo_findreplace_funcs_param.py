#######################################
### neoCL | Find and Replacer #########
#######################################

from neo_findreplace_funcs_main import *

class param:

	def __init__(self, el, pm, pval, cat=''):
		
		self.iamTextNote = False
		self.iamRoomTag = False
		if pm:				
		    self.pm = pm
		    self.pmTag = self.pm.Definition.Name
		else: #is Room Tag or Text Note, the value is from TagText not from parameter
			if cat == "Text Notes":
				self.pmTag = "NoteText"
				self.iamTextNote = True
			elif cat == "Room Tags":
				self.pmTag = "TagText"
				self.iamRoomTag = True
		self.el = el
		self.pval = str(pval)
		self.pmap = el.parameters.all
		self.id = el.Id
		self.level = ""
		self.family = ""
		self.category = ""
		try:
			self.family = el.parameters["Family"].AsValueString()
			self.category = el.parameters["Category"].AsValueString()
			self.level = el.parameters["Level"].AsValueString()
		except:
			pass
		
		self.add_pmList()
		self.add_selList()
		self.add_listBox()
		self.add_saveTableVar()

		g.result += ";" + str(pval)

	def add_pmList(self):
		g.pmfindList.append(self)

	def add_selList(self):
		g.selfindList.append(self.el.Id)

	def add_listBox(self):
		self.lvItem = ListViewItem(Array[System.String]([
						str(self.pval),
						str(self.pmTag),
						str(self.el.name),
						str(self.level),
						str(self.category),
						str(self.family),
						str(self.id),
						]))
		g.fm._listViewResult.Items.AddRange(Array[ListViewItem]([self.lvItem]))

	def add_saveTableVar(self):
		row = 	str(self.pval) + "\t" \
			+ str(self.pmTag) + "\t" \
			+ str(self.el.name) + "\t" \
			+ str(self.level) + "\t" \
			+ str(self.category) + "\t" \
			+ str(self.family) + "\t" \
			+ str(self.id) + "\n"
				
		g.savetable += row
		
#	def add_listBox(self):
#		it = "[Id]:["
#		it += str(self.id)
#		it += "]\t"
#		it += str(self.pval)
#		it += "\t[TYPE]:["
#		it += str(self.el.name)
#		it += "]"
#		it += "\t[LEVEL]:["
#		it += str(self.level)
#		it += "]"
#		g.fm._listBoxResult.Items.Add(it)
		# Same position in listBox and selList and pmList (if all add and remove methods at same time), so not needed :
		#self.lbPosition = g.fm._listBoxResult.Items.Count

	def remove_pmList(self):
		g.pmfindList.remove(self)

	def remove_selList(self):
		g.selfindList.remove(self.el)
	
	def SelectMe(self, cancelSelect=False):
		eList = [self.el.Id]
		eids = List[ElementId](eList)
		SetFocus(eids, cancelSelect)

	def ReplaceMe(self):
		
		if self.iamRoomTag or \
           self.pm._revit_object.IsReadOnly:
			return False

		import re
		self.newpval = re.compile(re.escape(g.active_findstr), re.IGNORECASE)
		self.newpval = self.newpval.sub(g.active_repstr, self.pval)

		done = False

		try:
			if self.pm.Definition.Name == "Family":
				self.el.get_family().name = self.newpval
				if self.el.get_family().name == self.newpval: done = True

			elif self.pm.Definition.Name == "Type" or self.pm.Definition.Name == "Type Name":
				self.el.get_symbol().name = self.newpval
				if self.el.get_symbol().name == self.newpval: done = True

			elif self.iamTextNote:
				self.el.Text = self.newpval
				if self.el.Text == self.newpval: done = True

			elif self.pm.type is str:
				if self.pm._revit_object.Set(str(self.newpval)): done = True
				#self.pm._revit_object.Set(str(self.newpval))
				#if self.pm.AsString() == self.newpval: done = True

			elif self.pm.type is int:
				if self.pm._revit_object.Set(int(self.newpval)): done = True
				#self.pm._revit_object.Set(int(self.newpval))
				#if self.pm.value == self.newpval: done = True

			elif self.pm.type is float:
				if self.pm._revit_object.SetValueString(str(self.newpval)): done = True
				#self.pm._revit_object.SetValueString(str(self.newpval))
				#if self.pm.value * 304.8 == self.newpval: done = True

			else:
				if self.pm._revit_object.SetValueString(str(self.newpval)): done = True
				#self.pm._revit_object.SetValueString(str(self.newpval))
				#if self.pm.AsValueString() == self.newpval: done = True

			if  done and str(self.pval) != str(self.newpval):
				self.lvItem.SubItems[0].Text = self.newpval
				self.pval = self.newpval
				return True
			else:
				return False
		except:
			return False
