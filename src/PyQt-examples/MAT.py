import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QHBoxLayout, QLabel, QFrame, QSizePolicy
from PyQt5.QtCore import QSize, QFile

class MATBox(QWidget):
    """
    Individual box within the MAT widget

    Parameters
    ----------
    btype : `str`
        \"m\", \"a\", or \"t\" (upper or lowercase)

    """
    def __init__(self, min_height_px=50, btype=None):
        # Initialize MATBox with the properties of QWidget
        super().__init__()

        # Add properties
        self.min_height_px = min_height_px
        self.min_width_px = min_height_px
        self.btype = btype

        # Initialize the main layout
        self._init_layout()
        # Add content to the main layout
        self._init_content()
        # Set the styles
        self._init_styles()

    def _init_styles(self):
        """Initialize the styles of the frame"""

        style_path = "styles/main.css"
        # Set stylesheet
        self.setStyleSheet(style_path)
        self.frame.setMinimumSize(QSize(self.min_width_px, self.min_height_px))
        self.frame.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.set_status()
        
    def _init_layout(self):
        """Initialize the layout of the frame"""
        # Make the layout for the main widget
        self.main_layout = QHBoxLayout()
        # Set the spacing between widgets in the layout
        self.main_layout.setSpacing(0)
        # Set the margins of the layout
        self.main_layout.setContentsMargins(0, 0, 0, 0) 
        # Attach the layout to the widget
        self.setLayout(self.main_layout)

    def _init_content(self):
        # Make the individual content widgets
        self._init_frame()
        self._init_label()

        # Add the individual content widgets to the main layout
        self.main_layout.addWidget(self.box_label, 0)
    
    def _init_frame(self):
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.Box) 

    def _init_label(self):
        self.box_label = QLabel(self.btype.upper())

    def set_status(self, status="init"):
        if status == "init":
            self.frame.setStyleSheet("background-color: rgb(80, 80, 80);")
        elif status == "clear":
            self.frame.setStyleSheet("background-color: rgb(0, 255, 0);")
        elif status == "warn":
            self.frame.setStyleSheet("background-color: rgb(255, 255, 0);")
        elif status == "assert":
            self.frame.setStyleSheet("background-color: rgb(255, 0, 0);")

class MATWidget(QWidget):
    """The MAT widget"""
    def __init__(self, min_height_px=50, padding=10):
        # Initialize MATWidget with the properties of QWidget
        super().__init__()

        # Add properties
        self.min_height_px = min_height_px
        self.min_width_px = 3 * min_height_px
        self.pad_left = padding
        self.pad_right = padding
        self.pad_top = padding
        self.pad_bottom = padding

        # Initialize the main layout of the MATWidget
        self._init_layout()
        # Add content to the main layout
        self._init_content()
        # Set the styles of the QFrame
        self._init_styles()

    def _init_styles(self):
        """Initialize the styles of the frame"""
        self.setMinimumSize(QSize(self.min_width_px, self.min_height_px))
        self.setSizePolicy(
            QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        
    def _init_layout(self):
        """Initialize the layout of the widget"""
        # Make the layout for the main widget
        self.main_layout = QHBoxLayout()
        # Set the spacing between widgets in the layout
        self.main_layout.setSpacing(0)
        # Set the margins of the layout
        self.main_layout.setContentsMargins(
            self.pad_left, 
            self.pad_top, 
            self.pad_right, 
            self.pad_bottom
            ) 
        # Attach the layout to the widget
        self.setLayout(self.main_layout)

    def _init_content(self):
        # Make the individual content widgets
        self._init_m_widget()
        self._init_a_widget()
        self._init_t_widget()

        # Add the individual content widgets to the main layout
        self.main_layout.addWidget(self.m_widget)
        self.main_layout.addWidget(self.a_widget)
        self.main_layout.addWidget(self.t_widget)

    def _init_m_widget(self):
        """Make the M (manager) widget"""
        self.m_widget = MATBox(min_height_px=self.min_height_px, btype="M")

    def _init_a_widget(self):
        """Make the A (accessor) widget"""
        self.a_widget = MATBox(min_height_px=self.min_height_px, btype="A")

    def _init_t_widget(self):
        """Make the T (transporter) widget"""
        self.t_widget = MATBox(min_height_px=self.min_height_px, btype="T")

class MainWindow(QMainWindow):
    """The main window of the application"""
    def __init__(self):
        # Initialize MainWindow with the properties of QMainWindow
        super().__init__()

        # Set the window title
        self.setWindowTitle("MAT Example")
        # Initialize the main widget and its layout
        self._init_layout()
        # Add content to the main widget
        self._init_content()

        # Set the central widget of the Window.
        self.setCentralWidget(self.main_widget)

    def _init_layout(self):
        # Make the main widget
        self.main_widget = QWidget()
        # Make the layout for the main widget
        self.main_layout = QGridLayout()
        # Attach the layout to the widget
        self.main_widget.setLayout(self.main_layout)

    def _init_content(self):
        # Make the individual content widgets
        self._init_MAT_widget()

        # Add the individual content widgets to the main layout
        self.main_layout.addWidget(self.MAT_widget, 0, 0)

    def _init_MAT_widget(self):
        self.MAT_widget = MATWidget()

if __name__ == "__main__":
    # Start the app
    app = QApplication(sys.argv)

    # Define an instance of the MainWindow class
    window = MainWindow()

    # Tell the window to show itself
    window.show()

    # Start the event loop
    sys.exit(app.exec())