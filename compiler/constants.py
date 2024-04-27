from typing import NoReturn, Union, Callable
from dataclasses import dataclass, field
from sys import exit as sys_exit
from argparse import Namespace

from compiler.info import is_type


RED = '\033[31m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'


def info(args: Namespace, msg: str) -> None:
    if args.debug:
        print(msg)

def find_function(info: dict, name: str) -> Union[tuple, None]:
    for func in info.values():
        if isinstance(func, tuple) and func[2] == name:
            return func

def add_types(env: dict, info: dict) -> None:
    env.update({
        k: EnvItem(k, k, False)
        for k, v in info.items()
        if is_type(k, v)
    })

def init_env(env: dict, info: dict) -> None:
    from compiler.std import get_functions
    get_functions(env)
    add_types(env, info)
    
    env.update({
        'ONE_BILLION': EnvItem('ONE_BILLION', 'int', False),
        'ONE_MILLION': EnvItem('ONE_MILLION', 'int', False),
        'ONE_THOUSAND': EnvItem('ONE_THOUSAND', 'int', False),
        'MAX_INT': EnvItem('MAX_INT', 'int', False),
        'MIN_INT': EnvItem('MIN_INT', 'int', False),
    })

def base_type(typ: Union[str, list]) -> Union[str, list]:
    if isinstance(typ, str):
        if typ.startswith('array<'):
            return 'array'
        elif typ == 'T':
            return 'any'
        else:
            return typ
    elif isinstance(typ, list):
        new_types = []
        for t in typ:
            if t.startswith('array<'):
                new_types.append('array')
            elif t == 'T':
                new_types.append('any')
            else:
                new_types.append(t)
        
        return new_types
    else:
        print('Invalid argument for base_type()')
        return typ


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
    
    def info_here(self, msg: str, src: Union[str, None] = None) -> None:
        self._print_src(BOLD, src)
        print(f'{BOLD}Info at {self.line}:{self.column}{RESET}: {BOLD}{msg}{RESET}')

@dataclass(slots=True, unsafe_hash=True, eq=False)
class Code:
    text: str
    type: str
    position: Position

@dataclass(slots=True, unsafe_hash=True, eq=False)
class EnvItem:
    name: str
    type: str
    can_be_changed: bool = field(default=True)
    callable: Union[Callable, None] = field(default=None)
