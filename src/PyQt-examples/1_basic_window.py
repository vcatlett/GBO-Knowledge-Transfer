import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class MainWindow(QMainWindow):
    """The main window of the application"""
    def __init__(self):
        # Initialize MainWindow with the properties of QMainWindow
        super().__init__()

        # Set the window title
        self.setWindowTitle("This is the window title")
        # Initialize the main widget and its layout
        self._init_layout()

        # Set the central widget of the Window.
        self.setCentralWidget(self.main_widget)

    def _init_layout(self):
        # Make the main widget
        self.main_widget = QWidget()
        # Make the layout for the main widget
        self.main_layout = QGridLayout()
        # Attach the layout to the widget
        self.main_widget.setLayout(self.main_layout)

if __name__ == "__main__":
    # Start the app
    app = QApplication(sys.argv)

    # Define an instance of the MainWindow class
    window = MainWindow()

    # Tell the window to show itself
    window.show()

    # Start the event loop
    sys.exit(app.exec())