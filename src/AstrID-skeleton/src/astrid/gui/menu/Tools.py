from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu


class ToolsMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("Tools", parent)
        self.make_menu()

    def make_menu(self):
        action_EditPlot = QAction(QIcon(None), "Edit Plot...", self)
        action_EditPlot.triggered.connect(self.func_EditPlot)
        self.addAction(action_EditPlot)

        action_Options = QAction(QIcon(None), "Options...", self)
        action_Options.triggered.connect(self.func_Options)
        self.addAction(action_Options)

    def func_EditPlot(self):
        print('Clicked the "Tools > Edit Plot" menu item')

    def func_Options(self):
        print('Clicked the "Tools > Options" menu item')
