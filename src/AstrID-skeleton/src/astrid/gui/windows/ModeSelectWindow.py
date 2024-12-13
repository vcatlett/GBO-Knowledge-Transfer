import socket
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from astrid.config.config import Config
from astrid.gui.static import get_path_static
from astrid.util.gateway import get_gateway_msg


class ModeSelectWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.STATIC_PATH = get_path_static()
        self.config = Config()

        self.setStyleSheet(open(self.STATIC_PATH / "css/styles.qss", "r").read())

        self.hostname = socket.gethostname()
        self.setWindowTitle(f"Real Time Mode (on {self.hostname})")

        self.main_layout = QVBoxLayout()

        self.make_info_table()
        self.make_radio()
        self.make_buttons()

        self.main_layout.addWidget(self.info_table_widget)
        self.main_layout.addWidget(self.radioSelect)
        self.main_layout.addWidget(self.button_widget)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def make_info_table(self):
        self.info_table_widget = QWidget()
        self.info_table_layout = QGridLayout()
        self.info_table_widget.setLayout(self.info_table_layout)

        self.info_title_user = QLabel("USER:")
        self.info_title_user.setAlignment(Qt.AlignRight)
        self.info_label_user = QLabel(self.config.USERNAME)
        self.info_label_user.setAlignment(Qt.AlignLeft)

        self.info_title_host = QLabel("HOST:")
        self.info_title_host.setAlignment(Qt.AlignRight)
        self.info_label_host = QLabel(self.config.HOSTNAME)
        self.info_label_host.setAlignment(Qt.AlignLeft)

        self.info_title_ygor_telescope = QLabel("YGOR_TELESCOPE:")
        self.info_title_host.setAlignment(Qt.AlignRight)
        self.info_label_ygor_telescope = QLabel(self.config.YGOR_TELESCOPE)
        self.info_label_ygor_telescope.setAlignment(Qt.AlignLeft)

        self.info_title_gateway = QLabel("GATEWAY:")
        self.info_title_gateway.setAlignment(Qt.AlignRight)
        self.info_label_gateway = QLabel(get_gateway_msg())
        self.info_label_gateway.setAlignment(Qt.AlignLeft)

        self.info_table_layout.addWidget(self.info_title_user, 0, 0, 1, 1)
        self.info_table_layout.addWidget(self.info_label_user, 0, 1, 1, 1)
        self.info_table_layout.addWidget(self.info_title_host, 1, 0, 1, 1)
        self.info_table_layout.addWidget(self.info_label_host, 1, 1, 1, 1)
        self.info_table_layout.addWidget(self.info_title_ygor_telescope, 2, 0, 1, 1)
        self.info_table_layout.addWidget(self.info_label_ygor_telescope, 2, 1, 1, 1)
        self.info_table_layout.addWidget(self.info_title_gateway, 3, 0, 1, 1)
        self.info_table_layout.addWidget(self.info_label_gateway, 3, 1, 1, 1)

    def make_radio(self):
        self.radioSelect = QWidget()
        self.radioSelect_layout = QVBoxLayout()
        self.radioSelect.setLayout(self.radioSelect_layout)

        self.radioSelect_offline = QRadioButton("Work offline")
        self.radioSelect_offline.mode = "OFFLINE"
        self.radioSelect_offline.toggled.connect(self.radio_on_click)

        self.radioSelect_monitor = QRadioButton("Work online, but only monitor observations")
        self.radioSelect_monitor.mode = "MONITOR"
        self.radioSelect_monitor.toggled.connect(self.radio_on_click)

        self.radioSelect_control = QRadioButton("Work online with control of the telescope")
        self.radioSelect_control.mode = "CONTROL"
        self.radioSelect_control.toggled.connect(self.radio_on_click)

        self.radioSelect_offline.setChecked(True)

        self.radioSelect_layout.addWidget(self.radioSelect_offline)
        self.radioSelect_layout.addWidget(self.radioSelect_monitor)
        self.radioSelect_layout.addWidget(self.radioSelect_control)

    def make_buttons(self):
        self.button_widget = QWidget()
        self.button_layout = QHBoxLayout()
        self.button_widget.setLayout(self.button_layout)

        self.button_ok = QPushButton("OK")
        self.button_ok.clicked.connect(self.button_ok_on_click)

        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.clicked.connect(self.button_cancel_on_click)

        self.button_layout.addWidget(self.button_ok)
        self.button_layout.addWidget(self.button_cancel)

    def radio_on_click(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.obs_mode = radioButton.mode

    def button_ok_on_click(self):
        self.close()

    def button_cancel_on_click(self):
        self.obs_mode = "CANCEL"
        self.close()

    def closeEvent(self, event):
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = ModeSelectWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
