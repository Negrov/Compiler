from PyQt6.QtGui import QSyntaxHighlighter
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QTextCharFormat, QFont, QColor

colors = {
    '#0000ff': r"\b(vivod|int|float|str|masik|only|slovar|razmer|depz|vvod)\b",
    '#408ca3': r"\b(\d+)\b",
    '#ffa500': r"\b(if|else|elif|while|for|as|not|is|class|def|in|from|import|True|False|return)\b",
    '#9b36ad': r"\b(self|(__(init|str|repr|dict)__))\b",
    '#459946': r'''(\'[^\']*\')|(\"[^\"]*\")''',
}


class MyHighlighter(QSyntaxHighlighter):
    def highlightBlock(self, text):
        char_format = QTextCharFormat()
        bold = QFont()
        bold.setBold(True)
        char_format.setFont(bold)

        for color, val in colors.items():
            char_format.setForeground(QColor(color))
            expression = QRegularExpression(val)
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), char_format)
