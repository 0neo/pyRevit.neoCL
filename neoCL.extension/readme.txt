________________________________________________________________________________________________________________________________________
neoCL Manual ________________________________________________________________________________________________________________________

https://github.com/0neo/neoCL

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
________________________________________________________________________________________________________________________________________

Non-neoCL Scripts, check
 . For pyRevit Scripts, in ribbon go to  \pyRevit(tab)\pyRevit(panel)\About(button)
 . https://github.com/gtalarico/pyrevitplus

________________________________________________________________________________________________________________________________________
1. neoCL | neo Command Line ________________________________________________________________________________________________________

Description :
. It's a command line to call neoCL scripts with commands instead of buttons.
  In the future it will give access to scripts or options that are not in the ribbon.
. Run about command to know more.

Body :
. Combobox with all the commands in it's list.
. Listbox will list all the commands compatible with the typed text in combobox field, and it's description.

How to :
. neoCL appears at mouse pointer position.
. To call commands in listbox:
    Type the full command.
    Type ? to view all commands.
    It's not case-sensitive.
    Press Enter or Space bar (as in AutoCAD) to call the typed command in combobox.
. To call commands in listbox:
    Type the full or partial command (or type ? to view all commands).
    Select it with arrows or mouse pointer.
    Enter or double click to call the selected one.
. After run the command you will return to neoCL.
. Escape to exit or command type q and enter.
. To move neoCL, click at any point of it and drag.

Tips :
. cl.f command allow to search also in description of the commands.
. Makes more sense to call neoCL with shortcut keys (SHIFT+N, just my personal preference).
  File -> Options -> User Interface -> Keyboard Shortcuts: Customize...

Warnings :
. Most programs will run after you call the command without ask for confirmation.
. cl.m command Modeless neoCL. Not recommended, called commands can't do transactions, will generate errors.
. myneoclisred command.

Disclaimer :
. Use the neoCL at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________
2. Family Replacer ____________________________________________________________________________________________________________________

Description :
. Replaces types and family instances using lists of names in Excel file to find and replace.

How to :
. Open Excel file first to configuration.
. Set the family name and the type of instances to find to be replaced.
. On each line set the new family name and the type of instances to replace.
. Select where to replace the families, in Project.xl or ActiveView.xl.
. Verify LOG column in Excel.

Tips :
. Its possible to have many sheets with diferent configurations.
  Only the sheet with name RUN will be imported.
  Change the name of the sheet to import to RUN and the other configurantion sheets to any other names.
. Sheet formats can be modified but the position of each cell has to be maintained.
. Excel workbook can be open or closed when Project.xl or ActiveView.xl.

Warnings :
. To understand the behavior of the program, test it first on a test project.
. Some types could not be compatible with replacement.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________
3. iParameters Editor __________________________________________________________________________________________________________________

Description :
. Edit parameters of family instances in Excel.
. Multiple types of instances simultaneous. 

How to :
. First preselect the family instances or :
  You will be requested to select one by one, press Escape when done.
. Export.xl means to export the data of selection to Excel, two options :
  _All : Exports all parameters to Excel.
  _Only Preset : Exports only the parameters that are preseted in Excel, exemple :
                 if you want to edit only the parameter Offset, in cell B1 write Offset, it will export only this parameter, so it's much quicker.
. Wait the end of process, when done, it will log [Excel is ready!] and
  all selected instances will appear listed in Excel.
. Blue cells can't be modified!
. Only Green cells can be modified.
. Import.xl means to import the data from Excel.

Tips :
. Export will be done without any order of selection.
  If order is important, don't select any family instance before Export.xl,
  you will be requested to select one by one, press Escape when done.
. Excel workbook can be open or closed when Import.xl or Export.xl.
. Its possible to export diferent types of families at same time,
  green cells means that this type has this parameter, black cell means the opposite.
. Use Excel filter\sort in title line (even hidden rows will be processed).
. Using Export.xl\All, select only one instance of each type, then in the Excel delete all the columns with parameters that you don't want to edit. And then select all the instances and now use the Export.xl\Only Preset

Warnings :
. To understand the behavior of the program, test it first on a test project.
. Check if all types of parameters are correctly modified, diferent types may have non wanted results.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________
4. Find and Replace ___________________________________________________________________________________________________________________

Description :
. Find and replace in parameters values of family instances.

How to :
. Similar use to any other find\replacer.
. Preselect the family instances to find only in selection.
. General :
    . Find : search history will be stored for future use (up to a limit, the oldest will be deleted).
    . Replace : same as Find.
    . Find button : List found text.
    . Replace Selected button : Replace text in selection of listed.
    . Replace All button : Replace text in all listed.
    . Close button : Close.
    . All button : Select instances of all listed.
    . Selected button : Select instances of selection of listed.
    . Lock checkbox : Change modal. If not checked allow to use Revit and open other windows,
      but replace will be disable until restart (recheck checkbox will not enable replace,
      the connection with Revit allowing changes in project is lost).
    . List of found text :
        . Select items to replace or select. Use CTRL key and\or SHIFT key.
        . Double Click to select and directs to element in project.
          If Find in selection mode, the selection will be kept, so double click only directs to element.
    . save table... : Save table result to a text file.
. Options :
    . Case-sensitive : Case-sensitive.
    . Full word : Only complete words, so XX not found in [YXX], but found in [Y XX YY].
    . Full parameter : Only full content of parameter.
    . Match mode (regex) : Find pattern, google for Python re : Regular expression operations.
    . Don't select Tags : Ignore Tags. It can search in parameters of the tag host (if not RoomTag). Replace will be done in the host.
    . Family, Type Category... : It will search text in this kind of parameter (family name, type...), normally not needed.
    . Find in :
        . Selection : In active selection. All categories.
        . Active View : In active view. Only selected categories in Specify categories...[+].
        . Project : In project. Only selected categories in Specify categories...
        . Specify categories... : Select categories to filter the find. More precision and the fewer selected the faster to process.
    . Save as defaults : Save selected options as defaults (include selected categories!). The options will be saved at next click on Find\Replace\Close buttons.
    . Allways (Save as defaults) : If Save as defaults it's also checked, then it will allways save the defaults.

Tips :
. You can save the result table to a text file, open it with Excel to better visualisation. (the column separator is tab)
. It allows to Find and Replace in family and type name of the instances. Select checkbox Family, Type Category...
. It can find (but not replace) in text of RoomTags of links. (Revit >=2018)
  Unselect checkbox Don't select Tags.
  It will return all the text in fields merged without spaces.
. Window is resizeble.
. Specify categories to speed up process, specially if find in Project mode.
. It can search in schedules, search mode in ActiveView or Selection (selected rows),
  but it will not show where the field with found text is, it will direct to a view with the element.
  The elements in schedules is the same as in a view, it will not process as data in a table.
. It's possible to search for some text, and then replace another part of the text.
  At each time Replace buttons are clicked, the text to replace is the text in find field.
  Exemple :
    Find text = REV
    Found = REVIT
    Change Find text = VIT
    Replace text = NEO
    Replace button = RENEO (not NEOIT)
    You can keep changing find text, replace text and appling it to the listed items.

Warnings :
. To understand the behavior of the program, test it first on a test project.
. Check if all types of parameters are correctly modified, diferent types may have non wanted results.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________
5. Auto Workset Set ___________________________________________________________________________________________________________________

Description :
. Auto activate workset for the active sheet, after user configuration.
. User tells which is the UserWorkset to activate when a specific View is activated.

How to :
. Button Config, then button Open.xl. This will open the Excel file that manages the user configurations.
. In the LOG sheet is listed all the UserWorksets and ViewsWorksets in the active project.
. With the LOG sheet information, the user must fill the columns of CONFIG sheet. For each row, fill :
  _The name of the project, exactly as listed in LOG (sometimes listed with or without .rvt extension) or partially name (read explanation in Tips below) ;
  _The ID of the ViewWorkset (each view has an unique workset, a non modifiable one);
  _The ID of the UserWorkset to activate when this View is activated.
. Button Config, then button UpdateConfig.xl. This will update the configuration file.
. The Excel file can be kept open or closed, it can be saved or not as well.
. Next time Excel is open it will load the user configuration to the CONFIG sheet. Add more or update this sheet as needed and then again button UpdateConfig.xl.

Tips :
. Keep copies of the LOG sheet (renamed, like PROJ01, BUILD04, or any other text) so you can make changes in the future without having to open the projects to relog.
. If your project name keeps changing, for exemple, the suffix like an index or date in file name, you can use a partial file name inside square brackets instead. Like [project2020] instead of neoproject2020-A.rvt.

Warnings :
. The structure of the sheets CONFIG and LOG can not be modified, the program may crash. Yet formats (colors, fonts...) can be modified.
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________
6. Open Selected Views _______________________________________________________________________________________________________________

Description :
. Open all the selected views in the project browser.
. It will open the views at once, so no need to repeat the process of open and wait for each view.

How to :
. Select multiple views or sheets or schedules in the project browser, using the normal keys ([CTRL] or [SHIFT]).
. Run Open Selected Views.

Tips :
. It could be useful to use it with (pyRevit) Sync Views turned on.

Warnings :
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
__________________________________________________________________________________________________________________________________
7. Revisions __________________________________________________________________________________________________________________

Description :
. Edit the revisions of the project in Excel.
. It can modify, create, delete and reorder all the revisions from Excel. 

How to :
. Export.xl will export all the revisions in the project to Excel.
. Wait the end of process, when done, it will show "Export to Excel is done!" in cell A1 of Excel sheet.
. Read the HOW TO sheet to know row to create\delete and reorder.
. Import.xl means to import the data from Excel.
. It will show "Import to Revit is done!" in cell A1 of Excel sheet.

Tips :
. There is no need to always Export the revisions of the project to Excel. If you only want to add a list of revisions, just open the Revisions Workbook, add the new revisions and import to Revit. All the revisions will be added to the end of revisions list by sheet rows order. 

Warnings :
. To understand the behavior of the program, test it first on a test project.
. Check the result in Revit, you can use the Undo to restore.
. Check the log for each revision, after import.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
____________________________________________________________________________________________________________________________________
8. Open Schedule__________________________________________________________________________________________________________________

Description :
. Open active schedule in Excel to analyse or save the data.
. Only export, no import mode available.

How to :
. Open and activate a schedule.
. Run Open Schedule.

Tips :
. None.

Warnings :
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________
9. Edited By__________________________________________________________________________________________________________________

Description :
. See information in Excel about who created, last edited and own the selected elements.

How to :
. Select elements in model.
. Run Edited By.xl

Tips :
. It works with selected views in Project Browser.

Warnings :
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
__________________________________________________________________________________________________________________________________
10. Select All__________________________________________________________________________________________________________________

Description :
. Select all elements in Active View or Project.
. Other mode, same selection except Annotation, only elements of type Model.

How to :
. Choose a option :
  . Select All in Active View;
  . Select All in Project;
  . Select All in Active View, except Annotation (tags, text...);
  . Select All in Project, except Annotation (tags, text...);

Tips :
. After Selecting all apply a selection filter (native from Revit or from other Add-In).

Warnings :
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
_____________________________________________________________________________________________________________________________________
11. Select Similar__________________________________________________________________________________________________________________

Description :
. Select similar elements in Active View or Project.
. Revit has a built-in select similar, but it doesn't work with all categories of elements and doesn't allow various kinds of elements in same selection

How to :
. Select elements in model (one or more, of any kind).
. Run Select Similar, in Active View or Project.

Tips :
. None.

Warnings :
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________
12. Remove Annotation From Selection ______________________________________________________________________________________________

Description :
. Remove from active selection the elements of category type Annotation.

How to :
. Select elements in model.
. Run Remove Annotation using the command [ras] in neoCL. (not available in ribbon)

Tips :
. None.

Warnings :
. Any, this script will not change anything in the project.

Disclaimer :
. Use this at your own risk. I'm not responsible for anything you do with it, or for any damage that comes out of using it.
________________________________________________________________________________________________________________________________________