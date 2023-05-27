from typing import NoReturn
from inspect import stack
from traceback import print_stack
from antlr4.error.ErrorListener import ErrorListener

debug = False

class SplikitErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        report_error('Syntax', f'Invalid syntax \'{offendingSymbol.text}\' at ln {line}, col {column}')

def report_error(typ: str, msg: str) -> NoReturn:
    if debug:
        print_stack(f=stack()[1][0], limit=None)

    print(f'{typ}Error: {msg}')
    exit(0)
