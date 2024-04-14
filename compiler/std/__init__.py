from typing import Callable, Union
from functools import wraps
from pathlib import Path

from compiler.constants import EnvItem, Code, Position


std = Path(__file__).parent

LIBS = {
}


def verify_params(args: list, params: dict[str, dict], compiler, position: Position) -> dict:
    required_params = {name: param for name, param in params.items() if not param.get('optional', False)}
    len_args = len(args)
    len_required_params = len(required_params)

    if len_args < len_required_params:
        param_length = f'{len(required_params)} required argument{"s" if len(required_params) > 1 else ""}'
        position.error_here(f'Expected {param_length} but got {len(args)}', compiler.src)

    if len_args > len(params):
        diff = len_args - len(params)
        extra_arguments = f'{diff} extra argument{"s" if diff > 1 else ""}'
        position.error_here(f'Passed {extra_arguments}', compiler.src)

    env = compiler.env.copy()
    arg_index = 0
    for name, param in params.items():
        if arg_index < len_args:
            arg = args[arg_index]
            if param.get('type') is not None and arg.type not in param['type'] and 'any' not in param['type']:
                arg.position.error_here(
                    f'Expected {" or ".join(param['type'])} but got {arg.type}',
                    compiler.src
                )
            env[name] = Code(arg.text, arg.type, position)
            arg_index += 1
        elif not param.get('optional', False):
            position.error_here(f'Missing required argument: {name}', compiler.src)

    return env


def std_func(params: Union[dict[str: dict], None] = None) -> Callable:
    params = params or {}
    
    def decorator(func: Callable) -> Callable:
        setattr(func, 'params', params)
        
        @wraps(func)
        def wrapper(compiler, args: list, call_position):
            return func(
                compiler,
                verify_params(args, params, compiler, call_position),
                call_position
            )
        
        return wrapper
    
    return decorator


@std_func({'x': {}})
def _print(_, env: dict, call_position: Position) -> Code:
    x = env['x']
    text = x.text
    if x.type != 'string':
        text = f'repr({text})'

    return Code(
        f'print({text})',
        'nil',
        call_position
    )

@std_func({'x': {}})
def _type(_, env: dict, call_position: Position) -> Code:
    x = env['x']
    return Code(
        f'type({x.text})',
        'string',
        call_position
    )

@std_func({'x': {}})
def _to_string(_, env: dict, call_position: Position) -> Code:
    x = env['x']
    return Code(
        f'repr({x.text})',
        'string',
        call_position
    )

@std_func({'prompt': {'type': {'string'}, 'optional': True}})
def _input(_, env: dict, call_position: Position) -> Code:
    prompt = env.get('prompt')
    return Code(
        f'input({prompt.text if prompt is not None else ""})',
        'string',
        call_position
    )


def get_functions(compiler) -> None:
    compiler.env['print'] = EnvItem('print', 'nil', _print)
    compiler.env['type'] = EnvItem('type', 'string', _type)
    compiler.env['to_string'] = EnvItem('to_string', 'string', _to_string)
    compiler.env['input'] = EnvItem('input', 'string', _input)
