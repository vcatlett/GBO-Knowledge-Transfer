from PyQt5.QtWidgets import QGridLayout, QLineEdit, QWidget


class OutputListWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.content = QLineEdit()

        self.main_layout.addWidget(self.content, 0, 0, 1, 1)
