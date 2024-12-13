import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    """The main window of the application"""

    def __init__(self):
        # Initialize MainWindow with the properties of QMainWindow
        super().__init__()

        # Set the window title
        self.setWindowTitle("PyQt Widget Showcase")

        # Initialize the main widget and its layout
        self._init_layout()

        # Add the widgets to the main layout
        self.add_widgets()

        # Set the central widget of the Window.
        self.setCentralWidget(self.main_widget)

    def _init_layout(self):
        # Make the main widget
        self.main_widget = QWidget()
        # Make the layout for the main widget
        self.main_layout = QGridLayout()
        # Attach the layout to the widget
        self.main_widget.setLayout(self.main_layout)

    def add_widgets(self):
        """Add a bunch of sample widgets to the main layout"""

        self.main_layout.addWidget(
            QLabel("QCheckBox", alignment=Qt.AlignmentFlag.AlignCenter),
            0,
            0,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QCheckBox(), 1, 0, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QComboBox", alignment=Qt.AlignmentFlag.AlignCenter),
            0,
            1,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QComboBox(), 1, 1, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QDateEdit", alignment=Qt.AlignmentFlag.AlignCenter),
            0,
            2,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QDateEdit(), 1, 2, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QDateTimeEdit", alignment=Qt.AlignmentFlag.AlignCenter),
            0,
            3,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(
            QDateTimeEdit(), 1, 3, 1, 1, alignment=Qt.AlignCenter
        )

        self.main_layout.addWidget(
            QLabel("QDial", alignment=Qt.AlignmentFlag.AlignCenter),
            2,
            0,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QDial(), 3, 0, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QDoubleSpinBox", alignment=Qt.AlignmentFlag.AlignCenter),
            2,
            1,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(
            QDoubleSpinBox(), 3, 1, 1, 1, alignment=Qt.AlignCenter
        )

        self.main_layout.addWidget(
            QLabel("QFontComboBox", alignment=Qt.AlignmentFlag.AlignCenter),
            2,
            2,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(
            QFontComboBox(), 3, 2, 1, 1, alignment=Qt.AlignCenter
        )

        self.main_layout.addWidget(
            QLabel("QLabel", alignment=Qt.AlignmentFlag.AlignCenter),
            2,
            3,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(
            QLabel("This is some text"), 3, 3, 1, 1, alignment=Qt.AlignCenter
        )

        self.main_layout.addWidget(
            QLabel("QLCDNumber", alignment=Qt.AlignmentFlag.AlignCenter),
            4,
            0,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QLCDNumber(), 5, 0, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QLineEdit", alignment=Qt.AlignmentFlag.AlignCenter),
            4,
            1,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QLineEdit(), 5, 1, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QProgressBar", alignment=Qt.AlignmentFlag.AlignCenter),
            4,
            2,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QProgressBar(), 5, 2, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QPushButton", alignment=Qt.AlignmentFlag.AlignCenter),
            4,
            3,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QPushButton("Push me"), 5, 3, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QRadioButton", alignment=Qt.AlignmentFlag.AlignCenter),
            6,
            0,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QRadioButton(), 7, 0, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QSlider", alignment=Qt.AlignmentFlag.AlignCenter),
            6,
            1,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QSlider(), 7, 1, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("QSpinBox", alignment=Qt.AlignmentFlag.AlignCenter),
            6,
            2,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QSpinBox(), 7, 2, 1, 1, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(
            QLabel("TimeEdit", alignment=Qt.AlignmentFlag.AlignCenter),
            6,
            3,
            1,
            1,
            alignment=Qt.AlignCenter,
        )
        self.main_layout.addWidget(QTimeEdit(), 7, 3, 1, 1, alignment=Qt.AlignCenter)


if __name__ == "__main__":
    # Start the app
    app = QApplication(sys.argv)

    # Define an instance of the MainWindow class
    window = MainWindow()

    # Tell the window to show itself
    window.show()

    # Start the event loop
    sys.exit(app.exec())
