import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

from astrid.gui.static import get_path_static


class VerifyCloseWindow(QMessageBox):
    def __init__(self, parent=None):
        super(VerifyCloseWindow, self).__init__(parent)
        self.answer = None

        self.STATIC_PATH = get_path_static()
        self.setStyleSheet(open(self.STATIC_PATH / "css/styles.qss", "r").read())

        self.setIcon(QMessageBox.Information)
        self.setText("Are you sure you want to close AstrID?")
        self.setWindowTitle("Close AstrID")
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.buttonClicked.connect(self.button_on_click)

        self.exec()

    def button_on_click(self, btn):
        self.answer = btn.text()[1:]
        self.close()


def main():
    app = QApplication(sys.argv)
    window = VerifyCloseWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
