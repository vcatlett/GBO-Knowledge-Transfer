from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget


class ObservationControlWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

        self.title = QLabel("Observation Control:")
        self.make_content()

        self.main_layout.addWidget(self.title, 0, 0, 1, 1)
        self.main_layout.addWidget(self.content, 1, 0, 1, 1)

    def make_content(self):
        self.content = QWidget()
        self.content_layout = QGridLayout()
        self.content.setLayout(self.content_layout)

        self.button_Pause = QPushButton("Pause")
        self.button_Pause.clicked.connect(self.func_button_Pause)

        self.button_Stop = QPushButton("Stop")
        self.button_Stop.clicked.connect(self.func_button_Stop)

        self.button_Abort = QPushButton("Abort")
        self.button_Abort.clicked.connect(self.func_button_Abort)

        self.button_Interactive = QPushButton("Interactive")
        self.button_Interactive.clicked.connect(self.func_button_Interactive)

        self.content_layout.addWidget(self.button_Pause, 0, 0, 1, 1)
        self.content_layout.addWidget(self.button_Stop, 1, 0, 1, 1)
        self.content_layout.addWidget(self.button_Abort, 2, 0, 1, 1)
        self.content_layout.addWidget(self.button_Interactive, 3, 0, 1, 1)

    def func_button_Pause(self):
        print("Pushed the 'Observation Control > Pause\" button")

    def func_button_Stop(self):
        print("Pushed the 'Observation Control > Stop\" button")

    def func_button_Abort(self):
        print("Pushed the 'Observation Control > Abort\" button")

    def func_button_Interactive(self):
        print("Pushed the 'Observation Control > Interactive\" button")
