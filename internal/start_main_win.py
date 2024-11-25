from pathlib import Path
import sys

from PyQt6.QtWidgets import QApplication

from views.userview import UserView
from views.syntax import MyHighlighter


class Userview(UserView):
    def __init__(self):
        super().__init__()

    def update_plain(self):
        super().update_plain()
        self.save_to_file()

    def save_to_file(self):
        with open(Path('code/between.py'), 'w', encoding='utf8') as f:
            f.write(self.plainTextEdit.toPlainText())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def start_main_win():
    app = QApplication(sys.argv)
    win = Userview()
    win.show()
    highlighter = MyHighlighter(win.plainTextEdit.document())
    sys.exit(app.exec())

