from dataclasses import dataclass

from ..gen.SplikitVisitor import SplikitVisitor
from ..gen.SplikitParser import SplikitParser
from typing import Callable, Any, Union

@dataclass()
class FuncObject:
    name: str
    params: tuple[str, ...]
    body: Union[list[SplikitParser.StatementContext], None]
    py: Union[Callable, None]

    def repr(self) -> str:
        return f'Function at {hex(id(self))}'

    def call(self, args: tuple[Any, ...], visitor: SplikitVisitor):
        if self.body is not None:
            for stmt in self.body:
                visitor.visit(stmt)
        else:
            return self.py(args, visitor)
