import socket
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QSplitter,
    QTabWidget,
    QWidget,
)

from astrid.gui.gfm import (
    DataDisplayPanel,
    GBTStatusPanel,
    ObservationManagementEditPanel,
    ObservationManagementRunPanel,
    ObservationStatusPanel,
)
from astrid.gui.menu import EditMenu, FileMenu, HelpMenu, ToolsMenu, ViewMenu
from astrid.gui.static import get_path_static
from astrid.gui.windows.VerifyCloseWindow import VerifyCloseWindow


class AstridMainWindow(QMainWindow):
    def __init__(self, mode="OFFLINE"):
        super().__init__()
        self.STATIC_PATH = get_path_static()
        self.setStyleSheet(open(self.STATIC_PATH / "css/styles.qss", "r").read())

        self.hostname = socket.gethostname()
        self.mode = mode

        self.title = f"AstrID ({self.mode}) (on {self.hostname})"
        self.setWindowTitle(self.title)

        self.geo_left = 0
        self.geo_top = 0
        self.geo_width = 1200
        self.geo_height = 750
        self.setGeometry(self.geo_left, self.geo_top, self.geo_width, self.geo_height)

        self.make_menu()
        self.main_layout = QHBoxLayout()

        self.make_main_tabs()
        self.panel_ObservationStatus = ObservationStatusPanel()

        self.splitter_h = QSplitter(Qt.Horizontal)
        self.splitter_h.setStretchFactor(4, 1)

        self.splitter_v = QSplitter(Qt.Vertical)
        self.splitter_v.setStretchFactor(1, 1)

        self.splitter_h.addWidget(self.main_tabs)
        self.splitter_h.addWidget(self.panel_ObservationStatus)

        self.splitter_v.addWidget(self.splitter_h)
        dummy_widget = QWidget()
        self.splitter_v.addWidget(dummy_widget)

        self.main_layout.addWidget(self.splitter_v, 0)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def make_menu(self):
        menu_File = FileMenu(self)
        menu_Edit = EditMenu(self)
        menu_View = ViewMenu(self)
        menu_Tools = ToolsMenu(self)
        menu_Help = HelpMenu(self)

        self.menuBar().addMenu(menu_File)
        self.menuBar().addMenu(menu_Edit)
        self.menuBar().addMenu(menu_View)
        self.menuBar().addMenu(menu_Tools)
        self.menuBar().addMenu(menu_Help)

    def make_main_tabs(self):
        self.main_tabs = QTabWidget()

        self.make_tab_observation_management()
        self.make_tab_data_display()
        self.make_tab_telescope_status()

        self.main_tabs.addTab(self.tab_ObservationManagement, "Observation Management")
        self.main_tabs.addTab(self.tab_DataDisplay, "Data Display")
        self.main_tabs.addTab(self.tab_TelescopeStatus, "GBT Status")

    def make_tab_observation_management(self):
        self.tab_ObservationManagement = QTabWidget()

        self.tab_ObservationManagement_Edit = ObservationManagementEditPanel()
        self.tab_ObservationManagement_Run = ObservationManagementRunPanel()

        self.tab_ObservationManagement.addTab(self.tab_ObservationManagement_Edit, "Edit")
        self.tab_ObservationManagement.addTab(self.tab_ObservationManagement_Run, "Run")

    def make_tab_data_display(self):
        self.tab_DataDisplay = DataDisplayPanel()

    def make_tab_telescope_status(self):
        # [TODO] Add logic for deciding between GBT and 20m
        self.tab_TelescopeStatus = GBTStatusPanel()

    def closeEvent(self, event):
        close_question = VerifyCloseWindow()
        event.ignore()
        if close_question.answer == "Yes":
            event.accept()


def main():
    app = QApplication(sys.argv)
    window = AstridMainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
