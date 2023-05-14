from dataclasses import dataclass
from .FuncObject import FuncObject

@dataclass()
class ModuleObject:
    name: str
    attributes: dict
    methods: dict

    def repr(self) -> str:
        return f'Module \'{self.name}\''

    def __import__(self, env) -> None:
        env.add_module(self)
