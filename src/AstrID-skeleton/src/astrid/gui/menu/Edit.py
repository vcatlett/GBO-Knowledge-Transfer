from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu


class EditMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("Edit", parent)
        self.make_menu()

    def make_menu(self):
        action_Undo = QAction(QIcon(None), "Undo", self)
        action_Undo.setShortcut("Ctrl+Z")
        action_Undo.triggered.connect(self.func_Undo)
        self.addAction(action_Undo)

        action_Redo = QAction(QIcon(None), "Redo", self)
        action_Redo.triggered.connect(self.func_Redo)
        self.addAction(action_Redo)

        self.addSeparator()

        action_Cut = QAction(QIcon(None), "Cut", self)
        action_Cut.setShortcut("Ctrl+X")
        action_Cut.triggered.connect(self.func_Cut)
        self.addAction(action_Cut)

        action_Copy = QAction(QIcon(None), "Copy", self)
        action_Copy.setShortcut("Ctrl+C")
        action_Copy.triggered.connect(self.func_Copy)
        self.addAction(action_Copy)

        action_Paste = QAction(QIcon(None), "Paste", self)
        action_Paste.setShortcut("Ctrl+V")
        action_Paste.triggered.connect(self.func_Paste)
        self.addAction(action_Paste)

        action_Delete = QAction(QIcon(None), "Delete", self)
        action_Delete.triggered.connect(self.func_Delete)
        self.addAction(action_Delete)

        self.addSeparator()

        action_SelectAll = QAction(QIcon(None), "Select All", self)
        action_SelectAll.setShortcut("Ctrl+A")
        action_SelectAll.triggered.connect(self.func_SelectAll)
        self.addAction(action_SelectAll)

        action_Clear = QAction(QIcon(None), "Clear", self)
        action_Clear.triggered.connect(self.func_Clear)
        self.addAction(action_Clear)

    def func_Undo(self):
        print('Clicked the "Edit > Undo" menu item')

    def func_Redo(self):
        print('Clicked the "Edit > Redo" menu item')

    def func_Cut(self):
        print('Clicked the "Edit > Cut" menu item')

    def func_Copy(self):
        print('Clicked the "Edit > Copy" menu item')

    def func_Paste(self):
        print('Clicked the "Edit > Paste" menu item')

    def func_Delete(self):
        print('Clicked the "Edit > Delete" menu item')

    def func_SelectAll(self):
        print('Clicked the "Edit > Select All" menu item')

    def func_Clear(self):
        print('Clicked the "Edit > Clear" menu item')
