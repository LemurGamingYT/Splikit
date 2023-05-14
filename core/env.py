from typing import Union, NoReturn

from .error import report_error
from .objects import FuncObject, VarObject, ClassObject, ModuleObject
from .other.classes import Classes, generate_cls
from .other.funcs import Funcs


class Environment:
    def __init__(self) -> None:
        self.variables: dict[str: VarObject] = {}
        self.functions: dict[str: FuncObject] = {}
        self.classes: dict[str: ClassObject] = {}
        self.modules: dict[str: ModuleObject] = {}

        for func in [f for f in dir(Funcs) if not f.startswith('__')]:
            self.add_func(FuncObject(func[:-5], (), None, getattr(Funcs, func)))

        for cls in [c for c in dir(Classes) if not c.startswith('__')]:
            self.add_cls(generate_cls(getattr(Classes, cls)))

    def add_variable(self, obj: VarObject) -> None:
        self.variables[obj.name] = obj

    def get_variable(self, name: str) -> Union[VarObject, NoReturn]:
        v = self.variables.get(name)
        if v is None:
            return report_error('Name', f'Unknown variable \'{name}\'')
        else:
            return v

    def try_variable(self, name: str) -> Union[VarObject, None]:
        return self.variables.get(name)
    
    def remove_variable(self, name: str) -> None:
        self.variables.pop(name)

    def add_func(self, obj: FuncObject) -> None:
        self.functions[obj.name] = obj

    def get_func(self, name: str) -> Union[FuncObject, NoReturn]:
        f = self.functions.get(name)
        if f is None:
            return report_error('Name', f'Unknown function \'{name}\'')
        else:
            return f

    def try_func(self, name: str) -> Union[FuncObject, None]:
        return self.functions.get(name)

    def add_cls(self, obj: ClassObject) -> None:
        self.classes[obj.name] = obj

    def get_cls(self, name: str) -> Union[ClassObject, None]:
        c = self.classes.get(name)
        if c is None:
            return report_error('Name', f'Unknown class \'{name}\'')
        else:
            return c

    def try_cls(self, name: str) -> Union[ClassObject, None]:
        return self.classes.get(name)

    def add_module(self, obj: ModuleObject) -> None:
        self.modules[obj.name] = obj

    def get_module(self, name: str) -> Union[ModuleObject, None]:
        m = self.modules.get(name)
        if m is None:
            return report_error('Name', f'Unknown module \'{name}\'')
        else:
            return m

    def try_module(self, name: str) -> Union[ModuleObject, None]:
        return self.modules.get(name)
