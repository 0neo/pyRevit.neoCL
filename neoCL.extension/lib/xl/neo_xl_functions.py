#######################################
### neoCL | XL.functions ##############
#######################################

def rg(r, c):
	cRange = AA(c,'')
	cRange = cRange + str(r)
	return cRange

def AA(n, s):
	r = n % 26
	r = r if r > 0 else 26
	n = (n - r) / 26
	s = chr(64 + r) + s
	
	if n > 26: 
	    s = AA(n, s)
	elif n > 0:
	    s = chr(64 + n) + s
	
	return s

def uprint(nc):
	for x in range(1, nc + 1):
		print AA(x,'')

def ClearColumnFrom(startR):
    sh = startR.Parent
    endR = sh.Cells(sh.Rows.Count, startR.Column).End(-4162)
    sh.Range(startR, endR).Value2 = ''

def ActivateSheet(sh):
	sh.Activate
	#sh.Activate doesn't seem to be working, so try :
	sh.Visible = 0
	sh.Visible = -1
	sh.Activate

def xlFrezzer(XL, ending=False, xlRestore = {}):
	if bool(xlRestore):
		XL.ScreenUpdating = xlRestore["xlScreenUpdating"]
		XL.Calculation = xlRestore["xlCalculation"]
		XL.DisplayAlerts = xlRestore["xlDisplayAlerts"]
	else:
		xlRestore["xlScreenUpdating"] = XL.ScreenUpdating 
		xlRestore["xlCalculation"] = XL.Calculation
		xlRestore["xlDisplayAlerts"] = XL.DisplayAlerts
		XL.ScreenUpdating = ending
		XL.Calculation = -4105 if ending else -4135
		XL.DisplayAlerts = ending
		return xlRestore

def LastCellWithValues(sh):
	return sh.Cells.Find('*', sh.Cells(1, 1), -4123, 2, 2, 2, False)

def FirstEmptyCellInRow(sh, rNumber):
	for r in sh.Rows(rNumber).Cells:
		if r.Text == "":
			return r

def FirstEmptyCellInColumn(sh, cNumber):
	for r in sh.Column(cNumber).Cells:
		if r.Text == "":
			return r

def RemoveFilteringInSheet(sh):	
	if sh.AutoFilterMode:	  # If filtering is On:
		sh.Cells.AutoFilter() # Remove filter

def SetFiltering(sh):
    #Trying to avoid _FilterDatabase Naming Conflict error when opening Excel
	DeleteNames(sh.Parent)
	RemoveFilteringInSheet(sh)
	RenameFilters(sh.Parent)
	
def RenameFilters(wb):
	from random import randrange, uniform
	for nm in wb.Names:
		nm.Name = "neoCL" + str(randrange(0, 999999))

def DeleteNames(wb):
    for nm in wb.Names:
        nm.Delete