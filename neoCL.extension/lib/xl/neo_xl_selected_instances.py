######################################
### XLinst.neoCL #####################
### by neo 		 #####################
### 2019 		 #####################
######################################
### neoCL | iParameters Editor #######
######################################

### config ###########################
rt = 1 		#Title row
ct = 1 		#First Column Title
re = rt + 1	#First element row
ce = ct		#First Column Element
### ###### ###########################

def Export():
	import neo_xl_selected_instances_export as exp
	exp.ExportXL()

def Import():
	import neo_xl_selected_instances_import as imp
	imp.ImportXl()