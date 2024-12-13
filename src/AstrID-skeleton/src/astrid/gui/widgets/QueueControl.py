from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget


class QueueControlWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.title = QLabel("Queue Control:")
        self.make_content()

        self.main_layout.addWidget(self.title, 0, 0, 1, 1)
        self.main_layout.addWidget(self.content, 1, 0, 1, 1)

    def make_content(self):
        self.content = QWidget()
        self.content_layout = QGridLayout()
        self.content.setLayout(self.content_layout)

        self.button_halt = QPushButton("Halt Queue")
        self.button_halt.clicked.connect(self.func_button_halt)

        self.content_layout.addWidget(self.button_halt, 0, 0, 1, 1)

    def func_button_halt(self):
        print("Pushed the 'Queue Control > Halt Queue\" button")
