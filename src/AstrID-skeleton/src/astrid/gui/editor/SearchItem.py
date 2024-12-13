from PyQt5.QtWidgets import QListWidgetItem


class SearchItem(QListWidgetItem):
    def __init__(self, name, full_path, lineno, end, line):
        self.name = name
        self.full_path = full_path
        self.lineno = lineno
        self.end = end
        self.line = line
        self.formatted = f"{self.name}:{self.lineno}:{self.end} - {self.line} ..."
        super().__init__(self.formatted)

    def __str__(self):
        return self.formatted

    def __repr__(self):
        return self.formatted
