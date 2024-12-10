import sys
from pathlib import Path

from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QGridLayout, 
    QHBoxLayout, 
    QLabel, 
    QFrame, 
    QSizePolicy,
    )
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon

from widgets import AspectWidget
from get_styles import compile_styles
from simulations import FakeDevice
from static.styles.palette import *

class MATBox(AspectWidget):
    """
    Individual box within the MAT widget

    Parameters
    ----------
    btype : `str`
        \"m\", \"a\", or \"t\" (upper or lowercase)

    """
    def __init__(self, device: FakeDevice, min_height_px=50, btype="M"):
        # Initialize MATBox with the properties of QWidget
        super().__init__(ratio=1)

        # Load device
        self._device = device

        # Add dynamic properties
        self._status = None
        self.status = "init"

        # Add static properties
        self.min_height_px = min_height_px
        self.min_width_px = min_height_px
        self.btype = btype

        # Initialize the main layout
        self._init_layout()
        # Add content to the main layout
        self._init_content()
        # Set the styles
        self._init_styles()

    @property
    def status(self):
        """Get the status"""
        return self._status
    
    @status.setter
    def status(self, value):
        """Set the status"""
        allowed_values = ["init", "clear", "warn", "assert"]
        if value not in allowed_values:
            raise ValueError(f"Status must be one of {allowed_values}")
        self._status = value
        self.setProperty("status", self.status)
        
    def get_status(self):
        """Get the current device status"""
        if self.btype.lower() == "m":
            self.status = self._device.manager_status
        elif self.btype.lower() == "a":
            self.status = self._device.accessor_status
        elif self.btype.lower() == "t":
            self.status = self._device.transporter_status
        else:
            raise ValueError("btype must be 'm', 'a', or 't'")
        self.apply_styles()
        
    def _init_styles(self):
        """Initialize the styles of the frame"""
        # Load styles (probably don't want to recompile, but whatever, it works)
        self.styles = compile_styles()
        self.apply_styles()
        # self.frame.setMinimumSize(QSize(self.min_width_px, self.min_height_px))
        # self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    
    def apply_styles(self):
        """Reload the stylesheet"""
        if self.status == "init":
            self.setStyleSheet(f"background-color: {C_STATUS_INIT}")
        if self.status == "clear":
            self.setStyleSheet(f"background-color: {C_STATUS_CLEAR}")
        if self.status == "warn":
            self.setStyleSheet(f"background-color: {C_STATUS_WARN}")
        if self.status == "assert":
            self.setStyleSheet(f"background-color: {C_STATUS_ASSERT}")
        # self.setStyleSheet(self.styles)

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
        self.box_label = QLabel(
            self.btype.upper(),  # Label text
            alignment = Qt.AlignmentFlag.AlignCenter,  # Alignment within parent widget
            )
        

class MATWidget(AspectWidget):
    """The MAT widget"""
    def __init__(self, min_height_px=50, padding=0):
        # Initialize MATWidget with the properties of QWidget
        super().__init__(ratio=3)

        # Add properties
        self.min_height_px = min_height_px
        self.min_width_px = 3 * min_height_px
        self.pad_left = padding
        self.pad_right = padding
        self.pad_top = padding
        self.pad_bottom = padding

        # Start the fake device
        self._init_device()
        
        # Initialize the main layout of the MATWidget
        self._init_layout()
        # Add content to the main layout
        self._init_content()
        # Set the styles of the QFrame
        self._init_styles()

        # Get updates from the fake device
        self._init_status_updates()
    
    def _init_device(self):
        """Connect and start the device simulator"""
        self.device = FakeDevice()
        self.device.runtime = 10
        self.device.run_threaded()

    def _init_status_updates(self):
        """Connect value changes to actions"""
        self.device.managerChanged.connect(self.m_widget.get_status)
        self.device.accessorChanged.connect(self.a_widget.get_status)
        self.device.transporterChanged.connect(self.t_widget.get_status)

    def _init_styles(self):
        """Initialize the styles of the widget"""
        self.setMinimumSize(QSize(self.min_width_px, self.min_height_px))
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)

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
        self.m_widget = MATBox(
            device = self.device, 
            min_height_px = self.min_height_px, 
            btype = "M",
            )

    def _init_a_widget(self):
        """Make the A (accessor) widget"""
        self.a_widget = MATBox(
            device = self.device, 
            min_height_px = self.min_height_px, 
            btype = "A",
            )

    def _init_t_widget(self):
        """Make the T (transporter) widget"""
        self.t_widget = MATBox(
            device = self.device, 
            min_height_px = self.min_height_px, 
            btype = "T",
            )


class MainWindow(QMainWindow):
    """The main window of the application"""
    def __init__(self):
        # Initialize MainWindow with the properties of QMainWindow
        super().__init__()

        # Set the window title
        self.setWindowTitle("PyQt Knowledge Transfer Example")

        # Add an icon
        icon_path = Path(__file__).parent / "static/favicon.ico"
        self.setWindowIcon(QIcon(str(icon_path)))

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

    # Set global stylesheet
    style = compile_styles()
    app.setStyleSheet(style)

    # Define an instance of the MainWindow class
    window = MainWindow()

    # Tell the window to show itself
    window.show()

    # Fake function to show status changing
    # window.MAT_widget.fake_status_change()
    
    # Start the event loop
    sys.exit(app.exec())