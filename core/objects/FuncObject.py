from dataclasses import dataclass
from typing import Callable, Any, Union

from . import VarObject
from ..gen.SplikitParser import SplikitParser


@dataclass()
class FuncObject:
    name: str
    params: tuple[str, ...]
    body: Union[list[SplikitParser.StatementContext], None]
    py: Union[Callable, None]
    
    @property
    def type(self) -> str:
        return 'func'

    def repr(self) -> str:
        return f'Function \'{self.name}\''

    def __add_params(self, args: tuple[Any, ...], visitor) -> None:
        env = visitor.env
        for arg, param in zip(args, self.params):
            env.add_variable(VarObject(param, arg))
    
    def __remove_params(self, visitor) -> None:
        env = visitor.env
        for param in self.params:
            env.remove_variable(param)

    def call(self, args: tuple[Any, ...], visitor) -> None:
        if self.body is not None:
            self.__add_params(args, visitor)
            
            for stmt in self.body:
                visitor.visit(stmt)
            
            self.__remove_params(visitor)
        elif self.py is not None:
            return self.py(args, visitor)
