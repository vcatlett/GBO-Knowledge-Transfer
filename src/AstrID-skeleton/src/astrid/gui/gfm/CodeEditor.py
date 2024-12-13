from pathlib import Path

from PyQt5.QtWidgets import QGridLayout, QWidget

from astrid.gui.editor import PyEditorWidget
from astrid.gui.static import get_path_static


class CodeEditor(QWidget):

    def __init__(self, parent=None):
        super(CodeEditor, self).__init__(parent)
        self.STATIC_PATH = get_path_static()
        self.make_layout()
        self.setLayout(self.main_layout)

    def make_layout(self):
        self.main_layout = QGridLayout()

    def make_editor_tabs(self):
        self.editor_pages = self.get_editor_page()

    def get_editor_page(self, path=Path("."), is_python_file=True):
        editor_page = PyEditorWidget(self, path=path, is_python_file=is_python_file)
        return editor_page
