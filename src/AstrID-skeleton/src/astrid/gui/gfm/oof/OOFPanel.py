from PyQt5.QtWidgets import QGridLayout, QWidget


class OOFPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()