from ui.main_w import Ui_MainWindow

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton


class UserView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_view()

    def setup_view(self):
        self.editor()
        self.derict_but.setIcon(QIcon('ui/Direct.png'))
        self.active_file.setIcon(QIcon('ui/Active.png'))
        self.setWindowIcon(QIcon('ui/MainIcon.png'))
        self.setWindowTitle('My Compiler')
        self.save.setIcon(QIcon('ui/Save.png'))


    def editor(self):
        self.plainTextEdit.verticalScrollBar().valueChanged.connect(
            self.plainTextEdit_2.verticalScrollBar().setValue
        )
        self.plainTextEdit_2.verticalScrollBar().valueChanged.connect(
            self.plainTextEdit.verticalScrollBar().setValue
        )

        self.plainTextEdit.updateRequest.connect(self.number_left)

    def number_left(self):
        if self.plainTextEdit.blockCount() > self.plainTextEdit_2.blockCount():
            self.plainTextEdit_2.setFixedWidth(20 + 5 * (len(str(self.plainTextEdit.blockCount())) - 1))
            self.plainTextEdit_2.setPlainText(
                '\n'.join([str(i) for i in range(1, self.plainTextEdit.blockCount() + 1)]))
        elif self.plainTextEdit.blockCount() < self.plainTextEdit_2.blockCount():
            self.plainTextEdit_2.setFixedWidth(20 + 5 * (len(str(self.plainTextEdit.blockCount())) - 1))
            nums = self.plainTextEdit_2.toPlainText().split('\n')
            self.plainTextEdit_2.setPlainText('\n'.join(nums[:self.plainTextEdit.blockCount()]))
