################011011100110010101101111####
### neo Command Line #######################
############################################

def getcmdlist():
    cmds = {
            "cl"		:"neoCL : neo Command Line.",
            "cl.f"      :"neoCL : neo Command Line, search in commands descriptions."
           }
            # Not listed :
            #"cl.m"		:"neoCL : Unlocked (Modeless). Not recommended, called commands can't do transactions."
    return cmds

def runcmd(cmd, msg, recallCL=False):

    if cmd == 'cl':
        from neocl__main import Main
        Main(True)
    elif cmd == 'cl.f':
        from neocl__main import Main
        Main(False, True)
    elif cmd == 'cl.m':
        # Not listed :
        from neocl__main import Main
        Main(False)
    else:
        from neocl import unknowncmd
        unknowncmd(cmd, recallCL, getcmdlist())