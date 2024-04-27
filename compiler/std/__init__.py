from typing import Callable, Union
from functools import wraps
from pathlib import Path

from compiler.constants import EnvItem, Code, Position, base_type


std = Path(__file__).parent.absolute()

LIBS = {
    'fstream': std / 'fstream.hpp',
    'time': std / 'time.hpp',
    'ui': std / 'ui.hpp'
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
            arg_type = base_type(arg.type)
            typ = base_type(list(param.get('type', ['any'])))

            if arg_type not in typ and 'any' not in typ:
                arg.position.error_here(
                    f'Expected {" or ".join(typ)} but got {arg_type}',
                    compiler.src
                )
            env[name] = Code(arg.text, arg_type, position)
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

@std_func({'exit_code': {'type': {'int'}, 'optional': True}})
def _exit(_, env: dict, call_position: Position) -> Code:
    exit_code = env.get('exit_code')
    return Code(
        f'exit({exit_code.text if exit_code is not None else 0})',
        'nil',
        call_position
    )

@std_func({'message': {'type': {'string'}}})
def _error(_, env: dict, call_position: Position) -> Code:
    message = env['message']
    return Code(
        f'throw splikit_error({message.text})',
        'nil',
        call_position
    )


def get_functions(env: dict) -> None:
    env['print'] = EnvItem('print', 'nil', False, _print)
    env['type'] = EnvItem('type', 'string', False, _type)
    env['to_string'] = EnvItem('to_string', 'string', False, _to_string)
    env['input'] = EnvItem('input', 'string', False, _input)
    env['exit'] = EnvItem('exit', 'nil', False, _exit)
    env['error'] = EnvItem('error', 'nil', False, _error)
    env['range'] = EnvItem('range', 'array', False)
