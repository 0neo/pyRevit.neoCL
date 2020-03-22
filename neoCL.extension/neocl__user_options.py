import neocl__config as g
from rpw.ui.forms import CommandLink, TaskDialog

def SetOption_RecallneoCL():

	commands= [CommandLink('Yes', return_value=True),
			   CommandLink('No', return_value=False)]
	
	mg = "Recall neoCL after run a command?"
	dialog = TaskDialog('neoCL | User option',
					title_prefix=False,
					content=mg,
					commands=commands,
					buttons=[],
					show_close=False)

	option_recallneoCL = dialog.show()
	g.WriteVar('USER.OPTIONS', '_recall_neoCL', option_recallneoCL)
	g.op_recallneocl = option_recallneoCL