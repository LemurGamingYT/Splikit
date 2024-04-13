from sys import exit as sys_exit
from typing import Union

from antlr4.error.ErrorListener import ErrorListener

from compiler.constants import BOLD, RED, RESET


class SplikitErrorListener(ErrorListener):
    def __init__(self, src: Union[str, None] = None):
        self.src = src

    
    def syntaxError(self, _, offendingSymbol, line, column, msg, _e):
        if self.src is not None:
            print(self.src.splitlines()[line - 1])
            print(' ' * column + '^')

        msg = f'Invalid syntax \'{offendingSymbol.text}\''
        print(f'{BOLD}{RED}Error at {line}:{column}{RESET}: {msg}')
        sys_exit(1)
