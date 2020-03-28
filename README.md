<a href="#"><img src="https://2.bp.blogspot.com/-G8H1IAZuA_Y/XLBNiacnGEI/AAAAAAAABYI/eobITlQtvqoCammld-rVdQulQtZZ6dW9ACPcBGAYYCw/s1600/neoCL.Revit.logo.png" title=""></a>

**An extension for pyRevit in Autodesk Revit.**

A set of tools, mainly to process data, but also other type of tools.
Evely Excel dependent to speed up data process.

There is a core tool, that gives the name to the package (neo Command Line), it can call the scripts with commands instead of buttons and it gives access to more scripts or options that are not in the ribbon.

<a href="#"><img src="https://1.bp.blogspot.com/-bMrQ0KcU8R4/XnZKLrKOlDI/AAAAAAAABgk/cTfqu1umBAQNNU0L3ZpXTjSRYAcEGWUQQCLcBGAsYHQ/s1600/neocl.revit.ribbon.v0.2.4.png" title=""></a>

**Tools :**
 1. neoCL | neo Command Line
 2. Family Replacer
 3. iParameters Editor
 4. Find and Replace
 5. Auto Workset Set
 6. Open Selected Views
 7. Revisions
 8. Open Schedule
 9. Edited By
 10. Select All
 11. Select Similar
 12. Remove Annotation From Selection

**Find and Replace text or numbers in parameters of all categories of the Revit project :**

<a href="#"><img src="https://1.bp.blogspot.com/-SLCiD1_bPcc/XnZ7E7Ari5I/AAAAAAAABhI/eV5AgR5NWwYxYG-Yo457dxZeRJmqtz71ACLcBGAsYHQ/s1600/neoCL.find.png" title=""></a>
<a href="#"><img src="https://1.bp.blogspot.com/-VM_qy6i_Dso/Xn9xb0on5_I/AAAAAAAABhk/NwMK18-hNC0oFns5Dy1DWtB_ekYVbRTcQCLcBGAsYHQ/s1600/neoCL.find.cat.png" title=""></a>

**Update instructions :**

1. If you are updating neoCL, you may want to **save some user files** :  
    Run command *backup* in neoCL, this will save all user files to your documents folder.

2. Now you can delete the old neoCL folder, but I recommend you to save it as a backup.  
(It's really small, and may be useful.)

3. Follow installation instructions.

4. After update use command *backupr* to restore user files if needed.

**Installation instructions :**

1. Download and install pyRevit :  
https://github.com/eirannejad/pyRevit/releases

2. Download and extract neoCL.extension to any folder with write permissions :  
https://github.com/0neo/pyRevit.neoCL

3. Add the path to the parent folder of the neoCL.extension folder :  
If [C:\parent_folder\neoCL.extension], add [C:\parent_folder\].

<div align="center"><a href="#"><img src="https://1.bp.blogspot.com/-gEV7O0PxSCA/XNC5BlyU2zI/AAAAAAAABZ4/re3jJyJJ0VMG7Bds0tfmTbBWa8ZlvqtHQCLcBGAs/s1600/neocl.pyRevit.extension.png" title=""></a></div></br>

4. The help file has **instructions for the tools** : Help button in ribbon or type *help* command in neoCL.

**neoCL Commands added in this version 0.2.4 :**
1. **[awssa]** AWSS : Set workset for active view.
2. **[awssxl]** AWSS : Open Excel file user configuration.
3. **[awssuc]** AWSS : Update config file with data in excel file.
4. **[backupr]** Restore some or all your neoCL user files after update neoCL.
5. **[edb]** List information about who edited selected instances.
6. **[os]** Open active Schedule View in Excel.
7. **[rev]** Revisions Editor : Edit project revisions in Excel.
8. **[revh]** Revisions Editor : Information to use revisions editor in Excel.
9. **[revi]** Revisions Editor : Import updates to revisions from Excel.
10. **[ras]** Remove annotation from active selection.
11. **[sav]** Select all in Active View, Model or Annotation.
12. **[samv]** Select all in Active View, non Annotation.
13. **[ssv]** Select similar in Active View of same kind of selection (multiple types allowed).
14. **[sap]** Select all in Project, Model or Annotation.
15. **[ssp]** Select similar in Project of same kind of selection (multiple types allowed).
16. **[samp]** Select all in Project, non Annotation.
17. **[#pm.rnc]** [OPTION] Recall neoCL after each command.

**Previous neoCL commands in version 0.1.2 :**
1. **[attoxl]** InsParam Editor : Open Excel file.
2. **[attep]** InsParam Editor : Export family instances parameters to edit in Excel (preset parameters mode).
3. **[atte]** InsParam Editor : Export family instances parameters to edit in Excel.
4. **[atti]** InsParam Editor : Import family instances parameters edited in Excel.
5. **[backup]** Backup your neoCL user files before update neoCL, these files will be lost after update.
6. **[f]** Find And Replace : Find and replace in family parameters.
7. **[froxl]** Family Replacer : Open Excel file.
8. **[frv]** Family Replacer : in ActiveView : Replace family and types of instances edited in Excel.
9. **[frp]** Family Replacer : in Project : Replace family and types of instances edited in Excel.
10. **[ov]** Open selected views in Project Browser.
11. **[help]** neoCL : Help.
12. **[about]** neoCL : About neoCL.
13. **[cl]** neoCL : neo Command Line.
14. **[cl.f]** neoCL : neo Command Line, search in commands descriptions.
15. **[ver]** neoCL : Version data.
16. **[@]** Open neoCL website.
17. **[?]** List all neoCL commands.
18. **[q]** Quit neoCL.


**Versions :**
  * 0.0.6 beta : neoCL | neo Command Line
  * 0.0.3 beta : Backup neoCL User Files
  * 0.0.2 beta : Family Replacer
  * 0.1.4 beta : iParameters Editor
  * 0.0.4 beta : Find and Replace
  * 0.0.2 beta : Open Views
  * 0.0.2 beta : Auto Workset Set
  * 0.0.1 beta : Revisions Editor Set
  * 0.0.1 beta : Edited By
  * 0.0.1 beta : Select All
  * 0.0.1 beta : Select Similar
  * 0.0.1 beta : Remove Annotation From Selection
  * 0.0.1 beta : Open Schedule

*Disclaimer : Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.*
