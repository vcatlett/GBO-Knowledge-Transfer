from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu


class ViewMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("View", parent)
        self.make_menu()

    def make_menu(self):
        action_Toolbar = QAction(QIcon(None), "Toolbar", self)
        action_Toolbar.triggered.connect(self.func_Toolbar)
        self.addAction(action_Toolbar)

        action_StatusBar = QAction(QIcon(None), "Status Bar", self)
        action_StatusBar.triggered.connect(self.func_StatusBar)
        self.addAction(action_StatusBar)

        self.addSeparator()

        action_FullScreen = QAction(QIcon(None), "Full Screen", self)
        action_FullScreen.triggered.connect(self.func_FullScreen)
        self.addAction(action_FullScreen)

    def func_Toolbar(self):
        print('Clicked the "View > Toolbar" menu item')

    def func_StatusBar(self):
        print('Clicked the "View > Status Bar" menu item')

    def func_FullScreen(self):
        print('Clicked the "View > Full Screen" menu item')
