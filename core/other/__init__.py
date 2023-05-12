from ..error import report_error
from typing import Any, Union
from inspect import currentframe, stack

def format_name(s: str) -> str:
    return s.replace('_func', '').replace('_', '')

def get_arg(i: int, args: tuple[Any, ...], optional: bool = False) -> Union[Any, None]:
    try:
        return args[i]
    except IndexError:
        if not optional:
            return report_error(
                'Index',
                f'Not enough arguments to satisfy \'{format_name(currentframe().f_back.f_code.co_name)}\' function'
            )

def report_argument_type_error(expected_type: str, got_type: str, s = None) -> Any:
    if s is None:
        s = currentframe().f_back.f_code.co_name

    return report_error(
        'Type',
        f'Invalid type \'{got_type}\', expected \'{expected_type}\' for \'{format_name(s)}\' func'
    )

def is_instance_type(obj: Any, typ: tuple | Any, *, expected_type: str = 'int') -> bool:
    if isinstance(obj, typ):
        return True
    else:
        return report_argument_type_error(expected_type, obj.type, format_name(stack()[1].function))
