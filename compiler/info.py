from re import compile as re_compile
from pprint import pprint
from pathlib import Path

VERSION = '0.0.2'
DEFAULT_HEADER = Path(__file__).parent / 'splikit.hpp'
FUNCTION_REGEX = re_compile(
    r'(?:\/\/\s*(.*)\n)?(?:inline)?\s*(\w+)(?:\<\w+\>(?:\&)?)? (\w+)\((.*?)\)'
)
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


def is_type(k, v) -> bool:
    return k == v

def is_function(v) -> bool:
    return 'function' in v[0].split()

def is_method(v) -> bool:
    return 'method' in v[0].split()

def is_property(v) -> bool:
    return 'property' in v[0].split()

def is_static(v) -> bool:
    return 'static' in v[0].split()

TEMPLATE_PARAMETER = re_compile(r'<(\w+)>')
def simplify_parameters(params: tuple) -> str:
    return ', '.join(
        TEMPLATE_PARAMETER.sub('', param).replace('&', '')
        for param in params
        if param != ''
    )

def get_info(header: Path = DEFAULT_HEADER) -> dict:
    info = {}
    src = header.read_text('utf-8')
    for func in FUNCTION_REGEX.findall(src):
        func = list(func)
        func[3] = simplify_parameters(func[3].split(', '))
        if func[2] not in reserved:
            info[(
                op_name_to_symbol_map.get(func[2], func[2]),
                tuple(param.split()[0] for param in func[3].split(', ') if param != ''),
            )] = tuple(func)

    for struct in TYPE_REGEX.findall(src):
        info[struct.removesuffix('Type')] = struct.removesuffix('Type')

    # pprint(info)

    return info
