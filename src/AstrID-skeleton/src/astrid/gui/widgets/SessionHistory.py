from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QWidget


class SessionHistoryWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.title = QLabel("Session History:")
        self.content = QLineEdit()

        self.main_layout.addWidget(self.title, 0, 0, 1, 1)
        self.main_layout.addWidget(self.content, 1, 0, 1, 1)
