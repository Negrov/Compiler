class TokenType:
    def __init__(self, name, regex, color='#ffffff'):
        self.name = name
        self.regex = regex
        self.color = color


TOKEN_TYPES = {
    'NUMBER': TokenType('NUMBER', '[0-9]+', '#ffffff'),
    'VARIABLE': TokenType('VARIABLE', '[\w]+', '#ffffff'),

}

reg = {
    '#0000ff': r"\b(print|int|float|str|list|set|dict|len|range|input)\b",
    '#ffa500': r"\b(if|else|elif|while|for|as|not|is|class|def|in|from|import|True|False|return)\b",
    '#9b36ad': r"\b(self|__init|str|repr|dict)__))\b",
    # '#408ca3': r"\b(\d+)\b",
    # '#459946': r'''(\'[^\']*\')|(\"[^\"]*\")''',
}

for color, func in reg.items():

