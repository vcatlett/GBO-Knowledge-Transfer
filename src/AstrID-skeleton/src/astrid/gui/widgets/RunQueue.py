from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QWidget


class RunQueueWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.title = QLabel("Run Queue:")
        self.content = QLineEdit()
        self.make_buttons()

        self.main_layout.addWidget(self.title, 0, 0, 1, 1)
        self.main_layout.addWidget(self.content, 1, 0, 1, 1)
        self.main_layout.addWidget(self.buttons, 2, 0, 1, 1)

    def make_buttons(self):
        self.buttons = QWidget()
        self.buttons_layout = QGridLayout()
        self.buttons.setLayout(self.buttons_layout)

        self.button_move_up = QPushButton("Move Up")
        self.button_move_up.clicked.connect(self.func_button_move_up)

        self.button_move_down = QPushButton("Move Down")
        self.button_move_down.clicked.connect(self.func_button_move_down)

        self.button_remove = QPushButton("Remove")
        self.button_remove.clicked.connect(self.func_button_remove)

        self.buttons_layout.addWidget(self.button_move_up, 0, 0, 1, 1)
        self.buttons_layout.addWidget(self.button_move_down, 0, 1, 1, 1)
        self.buttons_layout.addWidget(self.button_remove, 0, 2, 1, 1)

    def func_button_move_up(self):
        print('Clicked "Move Up" button')

    def func_button_move_down(self):
        print('Clicked "Move Down" button')

    def func_button_remove(self):
        print('Clicked "Remove" button')
