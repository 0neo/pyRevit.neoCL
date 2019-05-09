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