
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# Define path to static files
STATIC_ROOT = Path(__file__).parent / "static"

# Start the app
app = QApplication(sys.argv)

# Define an instance of the QMainWindow class
window = QMainWindow()

# Set the window title
window.setWindowTitle("PyQt Knowledge Transfer Example")

# Add an icon
icon_path = STATIC_ROOT / "favicon.ico"
window.setWindowIcon(QIcon(str(icon_path)))

# Tell the window to show itself
window.show()

# Start the event loop
sys.exit(app.exec())

