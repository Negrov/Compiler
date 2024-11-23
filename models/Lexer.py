import ply.lex as lex


class Lexer:
    def __init__(self):
        self.reserved = None
        self.lexer = None
        self.tokens = None
        self.t_ignore = '\t\r'
        self.init_tokens()

    def input(self, code):
        self.lexer.input(code)

    def token(self):
        return self.lexer.token()

    def build(self):
        self.lexer = lex.lex(object=self)

    def init_tokens(self):
        self.reserved = {
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
            'for': 'FOR',
            'elif': 'ELIF',
            'return': 'RETURN',
            'not': 'NOT',
            '(t|T)rue': 'TRUE',
            '(f|F)alse': 'FALSE',
            'def': 'DEF',
            'int': 'INT',
            'float': 'FLOAT',
            'str': 'STR',
        }
        self.tokens = [
                          'comment'
                          'STRVAL',
                          'NUMBERINT',
                          'NUMBERFLOAT',
                          'PLUS',
                          'MINUS',
                          'TIMES',
                          'DIVIDE',
                          'LPAREN',
                          'RPAREN',
                          'EQUALS',
                          'SEMICOLON',
                          'IDENTIFIER',
                      ] + list(self.reserved.values())

    def t_RETURN(self, t):
        r"""\b(return)\b"""
        return t

    def t_NUMBERINT(self, t):
        r"""\d+"""
        t.value = int(t.value)
        return t

    def t_NUMBERFLOAT(self, t):
        r"""\d+(\.\d+)?"""
        t.value = float(t.value)
        return t

    def t_IDENTIFIER(self, t):
        r"""[a-zA-Z_][a-zA-Z_0-9]*"""
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t

    def t_PLUS(self, t):
        r"""\+"""
        return t

    def t_MINUS(self, t):
        r"""\-"""
        return t

    def t_TIMES(self, t):
        r"""\*"""
        return t

    def t_DIVIDE(self, t):
        r"""/"""
        return t

    def t_EQUALS(self, t):
        r"""="""
        return t

    def t_LPAREN(self, t):
        r"""\("""
        return t

    def t_RPAREN(self, t):
        r"""\)"""
        return t

    def t_SEMICOLON(self, t):
        r""";"""
        return t

    def t_STRVAL(self, t):
        r"""(\'[^\']*\')|(\"[^\"]*\")"""
        return t

    def t_comment(self, t):
        r"""(/\*(.|\n)*?\*/)|(//.*)"""
        pass

    def t_error(self, t):
        if t.value[0] != ' ':
            print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
        t.lexer.skip(1)

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)


lexer = Lexer()
lexer.build()
code = """
x = str(15);
y = int(15);
print(x + y);
"""
lexer.input(code)
for tok in lexer.lexer:
    print(tok)
