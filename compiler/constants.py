from typing import NoReturn, Union, Callable
from dataclasses import dataclass, field
from sys import exit as sys_exit
from argparse import Namespace


RED = '\033[31m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'


def info(args: Namespace, msg: str) -> None:
    if args.debug:
        print(msg)


@dataclass(slots=True, unsafe_hash=True, eq=False)
class Position:
    line: int
    column: int
    
    def _print_src(self, arrow_colour: str, src: Union[str, None] = None) -> None:
        if src is not None:
            print(src.splitlines()[self.line - 1])
            print(' ' * self.column + f'{BOLD}{arrow_colour}^{RESET}')
    
    def error_here(self, msg: str, src: Union[str, None] = None) -> NoReturn:
        self._print_src(RED, src)
        print(f'{BOLD}{RED}Error at {self.line}:{self.column}{RESET}: {BOLD}{msg}{RESET}')
        sys_exit(1)
    
    def warn_here(self, msg: str, src: Union[str, None] = None) -> None:
        self._print_src(YELLOW, src)
        print(f'{BOLD}{YELLOW}Warning at {self.line}:{self.column}{RESET}: {BOLD}{msg}{RESET}')

@dataclass(slots=True, unsafe_hash=True, eq=False)
class Code:
    text: str
    type: str
    position: Position

@dataclass(slots=True, unsafe_hash=True, eq=False)
class EnvItem:
    name: str
    type: str
    callable: Union[Callable, None] = field(default=None)
