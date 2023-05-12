from typing import NoReturn
from inspect import stack
from traceback import print_stack

debug = True

def report_error(typ: str, msg: str) -> NoReturn:
    if debug:
        print_stack(f=stack()[1][0], limit=None)

    print(f'{typ}Error: {msg}')
    exit(1)
