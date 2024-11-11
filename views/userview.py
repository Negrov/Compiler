from ui.main_w import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor
from PyQt6.QtCore import QRegularExpression

from PyQt6.QtWidgets import QApplication
import sys


class UserView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.editor()

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


class MyHighlighter(QSyntaxHighlighter):
    def highlightBlock(self, text):
        char_format = QTextCharFormat()
        bold = QFont()
        bold.setBold(True)
        char_format.setFont(bold)

        colors = {'blue': r"\b(print)\b",
                  'orange': r"\b(if|else|elif|while|for|as|not|is|class|def|in|from|import)\b",
                  'green': r'''\b('|")\b''',
                  'purple': r"\b(self)\b",
                  'light_purple': r"\b(__init__|__str__|__repr__|__dict__)\b"}

        for color, val in colors.items():
            char_format.setForeground(QColor(color))
            expression = QRegularExpression(val)
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), char_format)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserView()
    ex.show()
    highlighter = MyHighlighter(ex.plainTextEdit.document())
    sys.exit(app.exec())
