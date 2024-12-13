from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QWidget


class ValidationOutputWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.title = QLabel("Validation Output:")
        self.content = QLineEdit()
        self.make_buttons()

        self.main_layout.addWidget(self.title, 0, 0, 1, 1)
        self.main_layout.addWidget(self.content, 1, 0, 1, 1)
        self.main_layout.addWidget(self.buttons, 2, 0, 1, 1)

    def make_buttons(self):
        self.buttons = QWidget()
        self.buttons_layout = QGridLayout()
        self.buttons.setLayout(self.buttons_layout)

        self.button_validate = QPushButton("Validate")
        self.button_validate.clicked.connect(self.func_button_validate)

        self.button_export = QPushButton("Export")
        self.button_export.clicked.connect(self.func_button_export)

        self.buttons_layout.addWidget(self.button_validate, 0, 0, 1, 1)
        self.buttons_layout.addWidget(self.button_export, 0, 1, 1, 1)

    def func_button_validate(self):
        print('Clicked "Validate" button')

    def func_button_export(self):
        print('Clicked "Export" button')
