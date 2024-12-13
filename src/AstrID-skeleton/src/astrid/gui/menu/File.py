from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu


class FileMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("File", parent)
        self.make_menu()

    def make_menu(self):
        action_NewFile = QAction(QIcon(None), "New File", self)
        action_NewFile.setShortcut("Ctrl+N")
        action_NewFile.triggered.connect(self.func_NewFile)
        self.addAction(action_NewFile)

        action_NewWindow = QAction(QIcon(None), "New Window", self)
        action_NewWindow.setShortcut("Ctrl+Shift+N")
        action_NewWindow.triggered.connect(self.func_NewWindow)
        self.addAction(action_NewWindow)

        action_OpenFile = QAction(QIcon(None), "Open File", self)
        action_OpenFile.setShortcut("Ctrl+O")
        action_OpenFile.triggered.connect(self.func_OpenFile)
        self.addAction(action_OpenFile)

        action_OpenFolder = QAction(QIcon(None), "Open Folder", self)
        action_OpenFolder.setShortcut("Ctrl+K")
        action_OpenFolder.triggered.connect(self.func_OpenFolder)
        self.addAction(action_OpenFolder)

        self.addSeparator()

        action_Save = QAction(QIcon(None), "Save", self)
        action_Save.setShortcut("Ctrl+S")
        action_Save.triggered.connect(self.func_Save)
        self.addAction(action_Save)

        action_SaveAs = QAction(QIcon(None), "Save As...", self)
        action_SaveAs.setShortcut("Ctrl+Shift+S")
        action_SaveAs.triggered.connect(self.func_SaveAs)
        self.addAction(action_SaveAs)

        action_SaveAll = QAction(QIcon(None), "Save All", self)
        action_SaveAll.triggered.connect(self.func_SaveAll)
        self.addAction(action_SaveAll)

        self.addSeparator()

        action_PageSetup = QAction(QIcon(None), "Page Setup...", self)
        action_PageSetup.triggered.connect(self.func_PageSetup)
        self.addAction(action_PageSetup)

        action_PrintPreview = QAction(QIcon(None), "Print Preview...", self)
        action_PrintPreview.triggered.connect(self.func_PrintPreview)
        self.addAction(action_PrintPreview)

        action_Print = QAction(QIcon(None), "Print...", self)
        action_Print.setShortcut("Ctrl+P")
        action_Print.triggered.connect(self.func_Print)
        self.addAction(action_Print)

        self.addSeparator()

        action_ImportFile = QAction(QIcon(None), "Import from File...", self)
        action_ImportFile.triggered.connect(self.func_ImportFile)
        self.addAction(action_ImportFile)

        action_ExportFile = QAction(QIcon(None), "Export to File...", self)
        action_ExportFile.triggered.connect(self.func_ExportFile)
        self.addAction(action_ExportFile)

        self.addSeparator()

        action_Validate = QAction(QIcon(None), "Validate", self)
        action_Validate.triggered.connect(self.func_Validate)
        self.addAction(action_Validate)

        self.addSeparator()

        action_Delete = QAction(QIcon(None), "Delete", self)
        action_Delete.triggered.connect(self.func_Delete)
        self.addAction(action_Delete)

        self.addSeparator()

        action_RealTimeMode = QAction(QIcon(None), "Real time mode...", self)
        action_RealTimeMode.triggered.connect(self.func_RealTimeMode)
        self.addAction(action_RealTimeMode)

        action_CloseWindow = QAction(QIcon(None), "Close Window", self)
        action_CloseWindow.setShortcut("Alt+F4")
        action_CloseWindow.triggered.connect(self.func_CloseWindow)
        self.addAction(action_CloseWindow)

        self.addSeparator()

        action_Exit = QAction(QIcon(None), "Exit", self)
        action_Exit.setShortcut("Ctrl+Q")
        action_Exit.triggered.connect(self.func_Exit)
        self.addAction(action_Exit)

    def func_NewFile(self):
        print('Clicked the "File > New File" menu item')

    def func_NewWindow(self):
        print('Clicked the "File > New Window" menu item')

    def func_OpenFile(self):
        print('Clicked the "File > Open" menu item')

    def func_OpenFolder(self):
        print('Clicked the "File > Open Folder" menu item')

    def func_Save(self):
        print('Clicked the "File > Save" menu item')

    def func_SaveAs(self):
        print('Clicked the "File > Save As" menu item')

    def func_SaveAll(self):
        print('Clicked the "File > Save All" menu item')

    def func_PageSetup(self):
        print('Clicked the "File > Page Setup" menu item')

    def func_PrintPreview(self):
        print('Clicked the "File > Print Preview" menu item')

    def func_Print(self):
        print('Clicked the "File > Print" menu item')

    def func_ImportFile(self):
        print('Clicked the "File > Import File" menu item')

    def func_ExportFile(self):
        print('Clicked the "File > Export File" menu item')

    def func_Validate(self):
        print('Clicked the "File > Validate" menu item')

    def func_Delete(self):
        print('Clicked the "File > Delete" menu item')

    def func_RealTimeMode(self):
        print('Clicked the "File > Real Time Mode" menu item')

    def func_CloseWindow(self):
        print('Clicked the "File > Close Window" menu item')

    def func_Exit(self):
        print('Clicked the "File > Exit" menu item')
