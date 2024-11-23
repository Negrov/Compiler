from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from views.userview import UserView
from views.syntax import MyHighlighter
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserView()
    ex.show()
    highlighter = MyHighlighter(ex.plainTextEdit.document())
    sys.exit(app.exec())
