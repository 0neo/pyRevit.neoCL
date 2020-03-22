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
            XL.Visible = True
        except:
            XL, wp = getApp(True, filepath, cancelbringtofront, canceladdwb)
            XL.Visible = True
            if not cancelbringtofront:
                BringExcelToFront(XL)
            return XL, wp

    #print XL.Caption

    if filepath and not canceladdwb:    
        import os.path 
        try:
            wpname = os.path.basename(filepath)
            wp = XL.Workbooks(wpname)
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

    try:
        sh = wp.ActiveSheet
    except:
        print("ERROR [neoCL] : No work!")
        wp = XL.ActiveWorkbook

    if not cancelbringtofront:
        BringExcelToFront(XL)

    return XL, wp

def BringExcelToFront(XL):
    try:
        XL.WindowState = -4140
        XL.WindowState = -4137
    except:
        print("ERROR [neoCL] : Can't bring Excel to front!")