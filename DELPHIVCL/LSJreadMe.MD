pip install delphivcl
結果 PYTHON 要用3.3~3.10的版
所以要裝3.10的PYTHON的PYTHON
python.envManager.create 這會和原來的重覆，因為這只會建立.venv
 用指令
python -m venv virtual_name
c:python -m venv .venv310
使用CMD 到C:\Python310>
D:\LSJ\Python\python_learn\learn>


啟動虛擬環境 (vscode 要記得安裝 Python extension)
接著打開 vscode，輸入 CTRL+SHIFT+P，在 command palette 輸入 Python: Select Interpreter。

看一下在的版本 python -v 是否3.10
然後安裝
pip install delphivcl 可以安裝了

裝完後 執行 python
輸入from delphivcl import *
>>>from delphivcl import *
再輸入 dir()
>>>dir()
會得到以下
['Abort', 'Action', 'ActionList', 'ActivityIndicator', 'Application', 'BaseBindScopeComponent', 'BaseImageList', 'BaseLinkingBindSource', 'BaseObjectBindSource', 'BasicAction', 'BasicBindComponent', 'Bevel', 'BindComponentDelegate', 'BindingsList', 'BitBtn', 'Bitmap', 'BoundLabel', 'BufferedFileStream', 'Button', 'BytesStream', 'Canvas', 'CheckBox',
'Collection', 'ColorBox', 'ComboBox', 'Component', 'ContainedAction', 'ContainedActionList', 'ContainedBindComponent', 'Control', 'ControlBar', 'CreateComponent', 'CustomAction', 'CustomActionList', 'CustomActivityIndicator', 'CustomBindingsList', 'CustomControl', 'CustomDrawGrid', 'CustomEdit', 'CustomForm', 'CustomGrid', 'CustomImageList', 'CustomLinkControlToField', 'CustomLinkLabel', 'CustomLinkListControlToField', 'CustomLinkPropertyToField', 'CustomListControl', 'CustomListView', 'CustomMemo', 'CustomMemoryStream', 'CustomMultiSelectListControl', 'CustomNumberBox', 'CustomPrototypeBindSource', 'CustomStatusBar', 'CustomStyleServices', 'CustomTabControl', 'CustomToggleSwitch', 'CustomTreeView', 'DateTimePicker', 'DelphiDefaultContainer', 'DelphiDefaultIterator', 'DelphiDefaultMapping', 'DelphiMethod', 'DragImageList', 'DrawGrid', 'Edit', 'FileOpenDialog', 'FileStream', 'Form', 'FreeConsole', 'GetProcessDpiAwareness', 'Graphic', 'GroupBox', 'HandleStream', 'Header', 'IDABORT', 'IDCANCEL', 'IDCLOSE', 'IDCONTINUE', 'IDHELP', 'IDIGNORE', 'IDNO', 'IDOK', 'IDRETRY', 'IDTRYAGAIN', 'IDYES', 'Icon', 'Image', 'ImageList', 'IsDpiAware', 'Label', 'LabeledEdit', 'LinkControlDelegate', 'LinkControlToField', 'LinkControlToFieldDelegate', 'LinkLabel', 'LinkListControlToField', 'LinkPropertyToField', 'LinkPropertyToFieldDelegate', 'ListBox', 'ListItem', 'ListView', 'MB_ABORTRETRYIGNORE', 'MB_APPLMODAL', 'MB_DEFBUTTON1', 'MB_DEFBUTTON2', 'MB_DEFBUTTON3', 'MB_DEFBUTTON4', 'MB_HELP', 'MB_ICONASTERISK', 'MB_ICONERROR', 'MB_ICONEXCLAMATION', 'MB_ICONHAND', 'MB_ICONINFORMATION', 'MB_ICONQUESTION', 'MB_ICONSTOP', 'MB_ICONWARNING', 'MB_NOFOCUS', 'MB_OK', 'MB_OKCANCEL', 'MB_RETRYCANCEL', 'MB_SYSTEMMODAL', 'MB_TASKMODAL', 'MB_YESNO', 'MB_YESNOCANCEL',
'MainMenu', 'MediaPlayer', 'Memo', 'MemoryStream', 'Menu', 'MenuItem', 'Metafile', 'Monitor', 'Notebook', 'NumberBox', 'Object', 'OpenDialog', 'Page', 'PageControl', 'PaintBox', 'Panel', 'PascalInterface', 'PascalRecord', 'Persistent', 'Picture', 'Point', 'PopupMenu', 'PrototypeBindSource', 'RadioButton', 'RadioGroup', 'Rect', 'ResourceStream', 'SaveDialog', 'Screen', 'ScrollBar', 'SetHighDpiAware', 'SetProcessDpiAwareness', 'Shape', 'ShowMessage', 'Size', 'SpeedButton', 'SpinButton', 'SpinEdit', 'Splitter', 'StaticText',
'StatusBar', 'Stream', 'StringGrid', 'StringStream', 'Strings', 'StyleInfo', 'StyleManager', 'StyleServices', 'TabControl', 'TabSheet', 'Timer', 'ToggleSwitch', 'ToolBar', 'ToolButton', 'TrackBar', 'TreeNode', 'TreeView', 'VarParameter', 'WinControl', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bkAbort', 'bkAll', 'bkCancel', 'bkClose', 'bkCustom', 'bkHelp', 'bkIgnore', 'bkNo', 'bkOK', 'bkRetry', 'bkYes', 'caFree', 'caHide', 'caMinimize', 'caNone', 'cl3DDkShadow', 'cl3DLight', 'clActiveBorder', 'clActiveCaption', 'clAppWorkSpace', 'clAqua', 'clBackground', 'clBlack', 'clBlue', 'clBtnFace', 'clBtnHighlight', 'clBtnShadow', 'clBtnText', 'clCaptionText', 'clCream', 'clDefault', 'clDkGray', 'clFuchsia', 'clGradientActiveCaption', 'clGradientInactiveCaption', 'clGray', 'clGrayText', 'clGreen', 'clHighlight', 'clHighlightText', 'clHotLight', 'clInactiveBorder', 'clInactiveCaption', 'clInactiveCaptionText', 'clInfoBk', 'clInfoText', 'clLime', 'clLtGray', 'clMaroon', 'clMedGray', 'clMenu', 'clMenuBar', 'clMenuHighlight', 'clMenuText', 'clMoneyGreen', 'clNavy', 'clNone', 'clOlive', 'clPurple', 'clRed', 'clScrollBar', 'clSilver', 'clSkyBlue', 'clTeal', 'clWhite', 'clWindow', 'clWindowFrame', 'clWindowText', 'clYellow', 'crAppStart', 'crArrow', 'crCross',
'crDefault', 'crDrag', 'crHSplit', 'crHandPoint', 'crHelp', 'crHourGlass', 'crIBeam', 'crMultiDrag', 'crNo', 'crNoDrop', 'crNone', 'crSQLWait', 'crSize', 'crSizeAll', 'crSizeNEead', 'fmOpenReadWrite', 'fmOpenWrite', 'fmShareCompat', 'fmShareDenyNone', 'fmShareDenyRead', 'fmShareDenyWrite', 'fmShareExclusive', 'fsBorder', 'fsSurface', 'gdFixed', 'gdFocused', 'gdSelected', 'mdNearest', 'mdNull', 'mdPrimary', 'mrAbort', 'mrAll', 'mrCancel', 'mrIgnore', 'mrNo', 'mrNoToAll', 'mrNone', 'mrOk', 'mrRetry', 'mrYes', 'mrYesToAll', 'ssAlt', 'ssCtrl', 'ssDouble', 'ssLeft', 'ssMiddle', 'ssRight', 'ssShift']
