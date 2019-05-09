###         ###   ____    ____    ____   ###
#0# neoCL   #0#  /    \ _/ __ \  /  _ \  #0# 
### by neo  ### |  |   \\  ___/ (  <_> ) ###
#0# 2019    #0# |__|   / \___  > \____/  #0#
###         ###      \/      \/          ###
################011011100110010101101111####
### neo Command Line #######################
############################################

# Add new letter : 1\4
import neocl_specialchar as _sc       
import neocl_a as _a  
import neocl_b as _b
import neocl_c as _c
import neocl_f as _f
import neocl_h as _h 
#import neocl_i as _i  
import neocl_o as _o          
import neocl_q as _q          
import neocl_v as _v            
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.UI import UIApplication
from neocl__funcs import neoAlert

def runcmd(cmd, msg="", recallCL=False):

    cmd = cmd.lower()
    cmd0 = cmd[0]

    # Add new letter : 2\4
    if cmd0 == 'a':
        _a.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'b':
        _b.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'c':
        _c.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'f':
        _f.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'h':
        _h.runcmd(cmd, msg, recallCL)
    #elif cmd0 == 'i':
    #    _i.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'o':
        _o.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'q':
        _q.runcmd(cmd, msg, recallCL)
    elif cmd0 == 'v':
        _v.runcmd(cmd, msg, recallCL)
    else:
        _sc.runcmd(cmd, msg, recallCL)

def unknowncmd(cmd, recallCL, cmdlist):    
    from neocl__funcs import neoAlert
    mg = "Command [" + cmd + "] does not exists!"
    mg += "\n\n" + Getcmdstr(cmdlist) 
    neoAlert(mg, title="ERROR", header="neoCL")
    if recallCL:
	#print("done runing schedul")
        #import sched, time
        #s = sched.scheduler(time.time, time.sleep)
        #s.enter(5, 1, _c.runcmd, ('cl', msg, False))
        #s.run()
	#print("done runing schedul")
        _c.runcmd('cl', msg, False)
	#(delay, priority, action, argument)

def Printcmdlist(cmds):
    for k, v in cmds.items():
        print('[' + str(k) + '] ' + str(v))

def PrintAllcmdlist():
    Printcmdlist(GetAllcmdlist())

def GetAllcmdlist():
	cmds = {}
    # Add new letter : 3\4
	cmds.update(_a.getcmdlist())
	cmds.update(_b.getcmdlist())
	cmds.update(_c.getcmdlist())
	cmds.update(_f.getcmdlist())
	cmds.update(_h.getcmdlist())
	#cmds.update(_i.getcmdlist())
	cmds.update(_o.getcmdlist())
	cmds.update(_q.getcmdlist())
	cmds.update(_v.getcmdlist())
	cmds.update(_sc.getcmdlist())
	return cmds

def GetAllcmdstr():
	cmds = ""
    # Add new letter : 4\4
	cmds += Getcmdstr(_a.getcmdlist())
	cmds += Getcmdstr(_b.getcmdlist())
	cmds += Getcmdstr(_c.getcmdlist())
	cmds += Getcmdstr(_f.getcmdlist())
	cmds += Getcmdstr(_h.getcmdlist())
	#cmds += Getcmdstr(_i.getcmdlist())
	cmds += Getcmdstr(_o.getcmdlist())
	cmds += Getcmdstr(_q.getcmdlist())
	cmds += Getcmdstr(_v.getcmdlist())
	cmds += Getcmdstr(_sc.getcmdlist())
	return cmds

def Getcmdstr(cmds):
    cmdstr = ""
    for k, v in cmds.items():
        cmdstr += '[' + str(k) + '] ' + str(v) + '\n'
    return cmdstr

def AlertAllCmds():    
    from neocl__funcs import neoAlert
    neoAlert(GetAllcmdstr(), title="neoCL", header="All neoCL commands :")

def CanRecallneoCL(cmd):
    if cmd == 'cl' or \
       cmd == 'cl.m':      
        return False
    return True
    # 'cl'        neoCL itself
    # 'cl.m'      neoCL itself