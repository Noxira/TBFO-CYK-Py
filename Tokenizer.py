import re
from typing import NamedTuple

# V1.1

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    token_specs = [
        # COMMENTS
        ('COMMENT', r'"""[^"]*"""'),
        ('COMMENT2', r"'''[^']*'''"),

        # VAR TYPES
        ('TYPE_FLOAT', r'\d+\.\d+'),
        ('TYPE_INT', r'\d+'),
        ('TYPE_STR', r'\"[^"]*\"'),
        ('TYPE_STR2', r"\'[^']*\'"),
        ('BOOL_TRUE', r"True"),
        ('BOOL_FALSE', r"False"),
        ('TYPE_NONE', r"None"),
        # ASSIGNMENT OP
        ('ASSOP_PLUS', r'\+='),
        ('ASSOP_MIN', r'\-='),
        ('ASSOP_MULT', r'\*='),
        ('ASSOP_DIV', r'\/='),
        ('ASSOP_MOD', r'%='),
        ('ASSOP_FLOOR', r'\/\/='),
        ('ASSOP_EXP', r'\*\*='),
        # ARITH OP
        ('OP_FLOOR', r'\/\/'),
        ('OP_EXP', r'\*\*'),
        ('OP_PLUS', r'\+'),
        ('OP_MIN', r'\-'),
        ('OP_MULT', r'\*'),
        ('OP_DIV', r'\/'),
        ('OP_MOD', r'%'),
        # COMMA DOT
        ('DOT', r'\.'),
        ('COMMA', r','),

        # COMPARATOR
        ('COMP_EQ', r'=='),
        ('COMP_NEQ', r'!='),
        ('COMP_GREATER_EQ', r'>='),
        ('COMP_LESS_EQ', r'<='),
        ('COMP_GREATER', r'>'),
        ('COMP_LESS', r'<'),

        # LOGICAL OP
        ('LOGIC_NOT', r'!'),
        ('LOGIC_AND', r'&'),
        ('LOGIC_OR', r'\|'),
        ('LOGIC_AND2', r'and\s+'),
        ('LOGIC_NOT2', r'not\s+'),
        ('LOGIC_OR2', r'or\s+'),

        
        # ASSOP
        ('ASSOP', r'='),
        
        # BRACKETS AND FRIENDS
        ('OPEN_PAREN', r'\('),
        ('CLOSE_PAREN', r'\)'),
        ('OPEN_BRACK', r'\['),
        ('CLOSE_BRACK', r'\]'),
        ('OPEN_CBRACK', r'{'),
        ('CLOSE_CBRACK', r'}'),

        # KEYWORDS
        ('FROM', r'from\s+'),
        ('IMPORT', r'import\s+'),
        ('AS', r'as\s+'),
        ('IN', r'in\s+'),
        ('IS', r'is\s+'),
        ('CONT', r'continue'),
        ('CLASS', r'class\s+'),
        ('DEF', r'def\s+',),
        ('PASS', r'pass'),
        ('RETURN', r'return\W'),
        ('IF', r'if\W'),
        ('ELIF', r'elif\W'),
        ('ELSE', r'else'),
        ('FOR', r'for\s+'),
        ('RANGE', r'range'),
        ('WHILE', r'while\W'),
        ('PRINT', r'print'),
        ('RAISE', r'raise\s+'),
        ('WITH', r'with\s+'),
        ('COLON', r':'),

        # IDENTIFIER
        ('ID',       r'[A-Za-z][A-Za-z0-9\_]*'),

        # END
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)
