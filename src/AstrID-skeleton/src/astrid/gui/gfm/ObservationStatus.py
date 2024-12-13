from PyQt5.QtWidgets import QGridLayout, QWidget

from astrid.gui.widgets import (
    GBTStateWidget,
    GBTStatusWidget,
    ObservationControlWidget,
    ObservationStateWidget,
    QueueControlWidget,
)


class ObservationStatusPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.widget_ObservationState = ObservationStateWidget()
        self.widget_QueueControl = QueueControlWidget()
        self.widget_ObservationControl = ObservationControlWidget()

        # [TODO] Add logic to decide if GBT or 20m
        self.widget_TelescopeState = GBTStateWidget()
        self.widget_TelescopeStatus = GBTStatusWidget()

        self.main_layout.addWidget(self.widget_ObservationState, 0, 0, 1, 1)
        self.main_layout.addWidget(self.widget_TelescopeState, 1, 0, 1, 1)
        self.main_layout.addWidget(self.widget_TelescopeStatus, 2, 0, 1, 1)
        self.main_layout.addWidget(self.widget_QueueControl, 3, 0, 1, 1)
        self.main_layout.addWidget(self.widget_ObservationControl, 4, 0, 1, 1)
