from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QSplitter, QWidget

from astrid.gui.editor import PyEditorWidget
from astrid.gui.widgets import (
    AvailableSchedulingBlocksWidget,
    ObserverWidget,
    OperatorWidget,
    ProjectWidget,
    RunQueueWidget,
    SessionHistoryWidget,
    SessionWidget,
    ValidationOutputWidget,
)


class ObservationManagementEditPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.widget_Project = ProjectWidget()
        self.widget_AvailableSchedulingBlocks = AvailableSchedulingBlocksWidget()
        self.widget_CodeEditor = PyEditorWidget()
        self.widget_validation = ValidationOutputWidget()

        self.splitter_h = QSplitter(Qt.Horizontal)

        self.left_layout = QGridLayout()
        self.left_layout.addWidget(self.widget_Project, 0, 0, 1, 1)
        self.left_layout.addWidget(self.widget_AvailableSchedulingBlocks, 1, 0, 1, 1)
        self.left_widget = QWidget()
        self.left_widget.setLayout(self.left_layout)

        self.splitter_h.addWidget(self.left_widget)
        self.splitter_h.addWidget(self.widget_CodeEditor)
        self.splitter_h.addWidget(self.widget_validation)

        self.main_layout.addWidget(self.splitter_h, 0, 0)


class ObservationManagementRunPanel(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.widget_Project = ProjectWidget()
        self.widget_Session = SessionWidget()
        self.widget_Observer = ObserverWidget()
        self.widget_Operator = OperatorWidget()
        self.widget_AvailableSchedulingBlocks = AvailableSchedulingBlocksWidget()
        self.widget_SessionHistory = SessionHistoryWidget()
        self.widget_RunQueue = RunQueueWidget()

        self.main_layout.addWidget(self.widget_Project, 0, 0, 1, 1)
        self.main_layout.addWidget(self.widget_Session, 0, 1, 1, 1)
        self.main_layout.addWidget(self.widget_Observer, 0, 2, 1, 1)
        self.main_layout.addWidget(self.widget_Operator, 0, 3, 1, 1)
        self.main_layout.addWidget(self.widget_AvailableSchedulingBlocks, 1, 0, 2, 2)
        self.main_layout.addWidget(self.widget_SessionHistory, 1, 2, 1, 1)
        self.main_layout.addWidget(self.widget_RunQueue, 2, 2, 1, 1)
