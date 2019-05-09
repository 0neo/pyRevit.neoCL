#######################################
### neoCL | XL.appbuilder #############
#######################################

def getApp(createApp, filepath="", cancelbringtofront=False, canceladdwb=False):
    if createApp:
        import clr
        clr.AddReference("Microsoft.Office.Interop.Excel")
        import Microsoft.Office.Interop.Excel as Excel
        XL = Excel.ApplicationClass()
        XL.Visible = True
    else:
        import System
        try:
            XL = System.Runtime.InteropServices.Marshal.GetActiveObject('Excel.Application')
        except:
            XL, wp = getApp(True, filepath, cancelbringtofront, canceladdwb)
            return XL, wp

    #print XL.Caption

    if filepath and not canceladdwb:     
        #print("is path!")   
        import os.path 
        #print("is path!!!")   
        try:
            wpname = os.path.basename(filepath)
            wp = XL.Workbooks(wpname)
            #print(wpname)  
        except:
            #print("wp is not open!")
            if os.path.isfile(filepath):
                try:
                    wp = XL.Workbooks.Open(filepath)
                except:
                    #print("cant open wp, then add!")
                    wp = XL.Workbooks.Add()
            else:
                #print("wp file does not exists!")
                wp = XL.Workbooks.Add()
                if filepath[len(filepath)-4:]:
                    #print("lets save as!")
                    wp.SaveAs(filepath,52)
                else:
                    try:
                        wp.SaveAs(filepath)
                    except:
                        print("ERROR [neoCL] : Was not possible to save the document!")                
    elif not canceladdwb:
        wp = XL.Workbooks.Add()

    if not cancelbringtofront:
        try:
            XL.WindowState = -4140
            XL.WindowState = -4137
        except:
            print("ERROR [neoCL] : Can't bring Excel to front!")

    try:
        sh = wp.ActiveSheet
    except:
        print("ERROR [neoCL] : No work!")
        wp = XL.ActiveWorkbook

    return XL, wp