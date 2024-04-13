from re import compile as re_compile
from pprint import pprint
from pathlib import Path

VERSION = '0.0.1'
DEFAULT_HEADER = Path(__file__).parent / 'splikit.hpp'
FUNCTION_REGEX = re_compile(r'(?:\/\/\s*(.*)\n)?(?:inline)?\s*(\w+) (\w+)\((.*?)\)')
TYPE_REGEX = re_compile(r'struct (\w+)')


op_name_to_symbol_map = {
    'add': '+',
    'sub': '-',
    'mul': '*',
    'div': '/',
    'mod': '%',
    'eq': '==',
    'neq': '!=',
    'gt': '>',
    'lt': '<',
    'gte': '>=',
    'lte': '<=',
    'and_': '&&',
    'or_': '||',
    'not_': '!',
}

reserved = {'repr', 'type', 'to_bool'}


def get_info(header: Path = DEFAULT_HEADER, debug: bool = False) -> dict:
    info = {}
    src = header.read_text('utf-8')
    for func in FUNCTION_REGEX.findall(src):
        if func[2] not in reserved:
            info[(
                op_name_to_symbol_map.get(func[2], func[2]),
                tuple(param.split()[0] for param in func[3].split(', ') if param != '')
            )] = func
    
    for struct in TYPE_REGEX.findall(src):
        info[struct.removesuffix('Type')] = struct

    if debug:
        pprint(info)

    return info
