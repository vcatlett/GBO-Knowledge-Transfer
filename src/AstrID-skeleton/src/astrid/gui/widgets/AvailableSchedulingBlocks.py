from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QWidget


class AvailableSchedulingBlocksWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.title = QLabel("Available Scheduling Blocks:")
        self.content = QLineEdit()
        self.make_buttons()

        self.main_layout.addWidget(self.title, 0, 0, 1, 1)
        self.main_layout.addWidget(self.content, 1, 0, 1, 1)
        self.main_layout.addWidget(self.buttons, 2, 0, 1, 1)

    def make_buttons(self):
        self.buttons = QWidget()
        self.buttons_layout = QGridLayout()
        self.buttons.setLayout(self.buttons_layout)

        self.button_submit = QPushButton("Submit")
        self.button_submit.clicked.connect(self.func_button_submit)

        self.buttons_layout.addWidget(self.button_submit, 0, 0, 1, 1)

    def func_button_submit(self):
        print('Clicked "Submit" button')
