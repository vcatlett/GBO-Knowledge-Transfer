import sys
import warnings

from PyQt5.QtWidgets import QApplication

from astrid.gui.windows import AstridMainWindow, ModeSelectWindow
from astrid.util.gateway import get_gateway


def launch():
    in_gateway, perms = get_gateway()
    app = QApplication(sys.argv)
    window_ModeSelect = ModeSelectWindow()
    window_ModeSelect.show()
    app.exec()

    selected_mode = window_ModeSelect.obs_mode

    if selected_mode != "CANCEL":
        if selected_mode == "CONTROL":
            if not in_gateway:
                selected_mode = "MONITOR"
                warnings.warn("You are not in the gateway. Launching in MONITOR mode.")
        window_AstridMain = AstridMainWindow(selected_mode)
        window_AstridMain.show()
        sys.exit(app.exec())
    else:
        sys.exit()


if __name__ == "__main__":
    launch()
