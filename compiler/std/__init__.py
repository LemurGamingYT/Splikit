from typing import Callable, Union
from functools import wraps
from pathlib import Path

from compiler.constants import EnvItem, Code, Position


std = Path(__file__).parent

LIBS = {
    'LL': std / 'LL.hpp'
}


def std_func(params: Union[dict[str: dict], None] = None) -> Callable:
    params = params or {}
    
    def decorator(func: Callable) -> Callable:
        setattr(func, 'params', params)
        
        @wraps(func)
        def wrapper(compiler, args: list, call_position, src: Union[str, None] = None):
            len_args = len(args)
            len_params = len(params)
            if len_args < len_params:
                param_length = f'{len(params)} argument{"s" if len(params) > 1 else ""}'
                call_position.error_here(
                    f'Expected {param_length} but got {len(args)}', src
                )

            if len_args > len_params:
                diff = len_args - len_params
                extra_arguments = f'{diff} extra argument{"s" if diff > 1 else ""}'
                call_position.warn_here(
                    f'Passed {extra_arguments}, clamping to {len_params}', src
                )
                args = args[:len_params]
                len_args = len(args)

            env = compiler.env.copy()
            for arg in args:
                for name, param in params.items():
                    if param.get('type') is not None:
                        if arg.type not in param.type and 'any' not in param.type:
                            call_position.error_here(
                                f'Expected {" or ".join(param.type)} but got {arg.type}'
                            )

                    env[name] = Code(arg.text, arg.type, call_position)

            return func(compiler, env, call_position)
        
        return wrapper
    
    return decorator


@std_func({'x': {}})
def _print(_, env: dict, call_position: Position):
    x = env['x']
    text = x.text
    if x.type != 'string':
        text = f'repr({text})'

    return Code(
        f'print({text})',
        x.type,
        call_position
    )

@std_func({'x': {}})
def _type(_, env: dict, call_position: Position):
    x = env['x']
    return Code(
        f'type({x.text})',
        x.type,
        call_position
    )

@std_func({'x': {}})
def _to_string(_, env: dict, call_position: Position):
    x = env['x']
    return Code(
        f'repr({x.text})',
        x.type,
        call_position
    )


def get_functions(compiler) -> None:
    compiler.env['print'] = EnvItem('print', 'nil', _print)
    compiler.env['type'] = EnvItem('type', 'string', _type)
    compiler.env['to_string'] = EnvItem('to_string', 'string', _to_string)
