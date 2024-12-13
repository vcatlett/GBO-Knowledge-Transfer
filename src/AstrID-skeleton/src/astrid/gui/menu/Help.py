from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMenu


class HelpMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__("Help", parent)
        self.make_menu()

    def make_menu(self):
        action_Documentation = QAction(QIcon(None), "Documentation", self)
        action_Documentation.triggered.connect(self.func_Documentation)
        self.addAction(action_Documentation)

        action_SelfTest = QAction(QIcon(None), "Self Test...", self)
        action_SelfTest.triggered.connect(self.func_SelfTest)
        self.addAction(action_SelfTest)

        self.addSeparator()

        action_About = QAction(QIcon(None), "About...", self)
        action_About.triggered.connect(self.func_About)
        self.addAction(action_About)

    def func_Documentation(self):
        print('Clicked the "Help > Documentation" menu item')

    def func_SelfTest(self):
        print('Clicked the "Help > Self Test" menu item')

    def func_About(self):
        print('Clicked the "Help > About" menu item')
