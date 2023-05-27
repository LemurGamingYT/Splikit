from ..error import report_error
from typing import Any, Union
from ..objects import *
from inspect import currentframe, stack

builtin_methods = ('repr', 'type', 'value', 'call')

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

def infer_type(obj: Any):
    if isinstance(obj, str):
        return StringObject(obj)
    elif isinstance(obj, bool):
        return BoolObject(obj)
    elif isinstance(obj, int):
        return IntObject(obj)
    elif isinstance(obj, float):
        return FloatObject(obj)
    elif isinstance(obj, list):
        return ArrayObject(obj)
    else:
        return NilObject()

def report_argument_type_error(expected_type: str, got_type: str, s = None) -> Any:
    if s is None:
        s = currentframe().f_back.f_code.co_name

    return report_error(
        'Type',
        f'Invalid type \'{got_type}\', expected \'{expected_type}\' for \'{format_name(s)}\' func'
    )

def is_instance_type(obj: Any, typ: Union[tuple, Any], *, strict: bool = True) -> bool:
    if isinstance(obj, typ):
        return True
    elif strict:
        expected_types = typ
        if isinstance(typ, tuple):
            expected_types = ''
            for i, t in enumerate(typ):
                if i > 0:
                    expected_types += ' or '

                expected_types += t.__type__

        return report_argument_type_error(expected_types, obj.type, format_name(stack()[1].function))
    else:
        return False
