from PyQt5.QtWidgets import QGridLayout, QTabWidget, QWidget

from astrid.gui.widgets import OutputListWidget

from .Continuum import ContinuumPanel
from .Focus import FocusPanel
from .oof.OOFPanel import OOFPanel
from .Pointing import PointingPanel
from .SpectralLine import SpectralLinePanel


class DataDisplayPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.widget_OutputList = OutputListWidget()
        self.make_tabs()

        self.main_layout.addWidget(self.widget_OutputList, 0, 0, 1, 1)
        self.main_layout.addWidget(self.main_tabs, 0, 1, 1, 1)

    def make_tabs(self):
        self.main_tabs = QTabWidget()

        self.tab_Pointing = PointingPanel()
        self.tab_Focus = FocusPanel()
        self.tab_OOF = OOFPanel()
        self.tab_Continuum = ContinuumPanel()
        self.tab_SpectralLine = SpectralLinePanel()

        self.main_tabs.addTab(self.tab_Pointing, "Pointing")
        self.main_tabs.addTab(self.tab_Focus, "Focus")
        self.main_tabs.addTab(self.tab_OOF, "OOF")
        self.main_tabs.addTab(self.tab_Continuum, "Continuum")
        self.main_tabs.addTab(self.tab_SpectralLine, "Spectral Line")
