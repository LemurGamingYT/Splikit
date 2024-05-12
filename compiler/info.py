from dataclasses import dataclass, field
from re import compile as re_compile
from pprint import pprint
from pathlib import Path
from typing import Union

VERSION = '0.0.21'
DEFAULT_HEADER = Path(__file__).parent / 'splikit.hpp'
FUNCTION_REGEX = re_compile(
    r'(?:\/\/\s*(.*)\n)?(?:inline)?\s*(\w+)(?:\<\w+\>(?:\&)?)? (\w+)\((.*?)\)\s*\{'
)
TYPE_REGEX = re_compile(r'struct (\w+)')


op_name_to_symbol_map = {
    'add': '+', 'sub': '-', 'mul': '*', 'div': '/', 'mod': '%', 'eq': '==', 'neq': '!=', 'gt': '>',
    'lt': '<', 'gte': '>=', 'lte': '<=', 'and_': '&&', 'or_': '||', 'not_': '!',
}


def is_type(v: 'DefaultInfoItem') -> bool:
    return isinstance(v, DefaultInfoItem) and v.name == v.type

def is_function(v) -> bool:
    return isinstance(v, InfoFunc) and 'function' in v.comments

def is_method(v: 'InfoFunc') -> bool:
    return isinstance(v, InfoFunc) and 'method' in v.comments

def is_property(v: 'InfoFunc') -> bool:
    return isinstance(v, InfoFunc) and 'property' in v.comments

def is_static(v: 'InfoFunc') -> bool:
    return isinstance(v, InfoFunc) and 'static' in v.comments

def has_overload(v: 'InfoFunc', param_types: list[str]) -> bool:
    for types, _ in v.overloads:
        if types == param_types:
            return True

    return False

def get_overload(v: 'InfoFunc', param_types: list[str]) -> Union['InfoFunc', None]:
    for i, (types, _) in enumerate(v.overloads):
        if types == param_types:
            return InfoFunc(v.name, v.return_type, v.comments, v.overloads[i])

TEMPLATE_PARAMETER = re_compile(r'<(\w+)>')
def simplify_parameters(params: tuple) -> str:
    return ', '.join(
        TEMPLATE_PARAMETER.sub('', param).replace('&', '').replace('const ', '')
        for param in params
        if param != ''
    )

def get_info(header: Path = DEFAULT_HEADER) -> dict:
    info = {}
    src = header.read_text('utf-8')
    for func in FUNCTION_REGEX.findall(src):
        func = list(func)
        func[3] = simplify_parameters(func[3].split(', '))
        param_types, param_names = [], []
        for param in func[3].split(', '):
            splitted = param.split()
            if len(splitted) > 0:
                param_types.append(splitted[0])
            
            if len(splitted) > 1:
                param_names.append(splitted[1])
        
        func[2] = op_name_to_symbol_map.get(func[2], func[2])
        if func[2] in info:
            info[func[2]].overloads.append((param_types, param_names))
        else:
            info[func[2]] = InfoFunc(func[2], func[1], func[0].split(', '), [(param_types, param_names)])

    for struct in TYPE_REGEX.findall(src):
        typ = struct.removesuffix('Type')
        info[typ] = DefaultInfoItem(typ, typ)

    # pprint(info)

    return info

@dataclass(slots=True, unsafe_hash=True, eq=False)
class InfoFunc:
    name: str
    return_type: str
    comments: list[str]
    overloads: list[tuple[list[str], list[str]]] = field(default_factory=list)

@dataclass(slots=True, unsafe_hash=True, eq=False)
class DefaultInfoItem:
    name: str
    type: str
