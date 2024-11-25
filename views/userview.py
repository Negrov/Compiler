from pathlib import Path
from ui.main_w import Ui_MainWindow
from ui.dialog_w import Ui_Dialog

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QDialog

import os


class UserView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.is_save = True
        self.actual_path = None
        self.setupUi(self)
        self.setup_view()

    def setup_view(self):
        self.derict_but.setIcon(QIcon('ui\\Direct.png'))
        self.active_file.setIcon(QIcon('ui\\Active.png'))
        self.setWindowIcon(QIcon('ui\\MainIcon.png'))
        self.setWindowTitle('My Compiler')
        self.save.setIcon(QIcon('ui\\Save.png'))

        self.all_page.addTab(self.active_1, "None file")
        self.actionNew_file.triggered.connect(self.create_file)
        self.active_file.clicked.connect(self.go)
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionClose_file.triggered.connect(self.close_file)
        self.actionOpen_file.triggered.connect(self.open_file)
        self.actionExit.triggered.connect(self.close)
        self.plainTextEdit.setEnabled(False)
        self.double_scroll()
        self.plainTextEdit.updateRequest.connect(self.update_plain)
        self.derict_but.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)
        self.last_code()

    def save_file(self):
        with open(Path('code/lastFile.txt'), 'r', encoding='utf8') as f:
            last_path = f.read()
        if self.actual_path == last_path:
            directory = last_path[:last_path.rfind("/") + 1]
        else:
            directory = QFileDialog.getExistingDirectory(
                self,
                'Select Directory for save',
                os.getenv('HOME'),

            )
        if directory:
            with open(Path(f'{directory}{self.all_page.tabText(0)}.py'), 'w', encoding='utf8') as f:
                f.write(self.plainTextEdit.toPlainText())
            with open(Path('code/lastFile.txt'), 'w', encoding='utf8') as f:
                f.write(f"{directory}{self.all_page.tabText(0)}.py")
                return 1
        return 0

    def last_code(self):
        try:
            with open(Path('code\\lastFile.txt'), 'r', encoding='utf8') as f:
                path = f.read()
            with open(path, 'r', encoding='utf8') as f:
                code = f.read()
            self.all_page.addTab(self.active_1, f'{path[path.rfind("/") + 1: path.rfind(".")]}'.replace('/', '\\'))
            self.plainTextEdit.setPlainText(code)
            self.actual_path = path
            self.plainTextEdit.setEnabled(True)
        except FileNotFoundError:
            """pass"""

    def open_file(self):
        if not self.is_save and self.plainTextEdit.isEnabled():
            if not self.save_file():
                return
        select = QFileDialog.getOpenFileName(self, 'Select file', '', filter='*.py(Python);;Всефайлы(*)')[0]
        if not '.' in select:
            return
        with open(Path(select), 'r', encoding='utf8') as f:
            code = f.read()
        self.all_page.addTab(self.active_1, f'{select[select.rfind(Path("/")) + 1:select.find(".")]}')
        self.plainTextEdit.setPlainText(code)
        with open(Path('code/lastFile.txt'), 'w', encoding='utf8') as f:
            f.write(select)
        self.is_save = False
        self.plainTextEdit.setEnabled(True)
        self.actual_path = select

    def double_scroll(self):
        self.plainTextEdit.verticalScrollBar().valueChanged.connect(
            self.plainTextEdit_2.verticalScrollBar().setValue
        )
        self.plainTextEdit_2.verticalScrollBar().valueChanged.connect(
            self.plainTextEdit.verticalScrollBar().setValue
        )

    def number_left(self):
        if self.plainTextEdit.blockCount() > self.plainTextEdit_2.blockCount():
            self.plainTextEdit_2.setFixedWidth(20 + 5 * (len(str(self.plainTextEdit.blockCount())) - 1))
            self.plainTextEdit_2.setPlainText(
                '\n'.join([str(i) for i in range(1, self.plainTextEdit.blockCount() + 1)]))
        elif self.plainTextEdit.blockCount() < self.plainTextEdit_2.blockCount():
            self.plainTextEdit_2.setFixedWidth(20 + 5 * (len(str(self.plainTextEdit.blockCount())) - 1))
            nums = self.plainTextEdit_2.toPlainText().split('\n')
            self.plainTextEdit_2.setPlainText('\n'.join(nums[:self.plainTextEdit.blockCount()]))

    def update_plain(self):
        self.is_save = False
        self.number_left()

    def close(self):
        # exit()
        a = 1/ 0

    def save_as(self):
        if self.plainTextEdit.isEnabled():
            fname, _ = QFileDialog.getSaveFileName(self, 'Save as', f'/{self.all_page.tabText(0)}.py', os.getenv('HOME'))
            with open(Path(fname), 'w', encoding='utf8') as f:
                f.write(self.plainTextEdit.toPlainText())
            self.close_file()
            with open(Path(f'code/lastFile.txt'), 'w', encoding='utf8') as f:
                f.write(fname)

    def close_file(self):
        self.actual_path = None
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setPlainText('')
        self.all_page.addTab(self.active_1, "None file")
        with open(Path('code/lastFile.txt'), 'w', encoding='utf8') as f:
            f.write('')

    def go(self):
        self.save_file()
        current_directory:str = os.path.dirname(os.path.realpath(__file__))
        current_directory = current_directory[:current_directory.rfind(f"\\")]
        os.startfile(Path(f'{current_directory}\\code\\between.py'))

    def create_file(self):
        self.close_file()
        dial = NewFileDialog()
        dial.exec()
        self.all_page.addTab(self.active_1, dial.namefile.text())
        self.plainTextEdit.setEnabled(True)

class NewFileDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

