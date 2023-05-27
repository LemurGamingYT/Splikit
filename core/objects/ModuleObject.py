from dataclasses import dataclass

@dataclass()
class ModuleObject:
    name: str
    attributes: dict
    methods: dict

    def repr(self) -> str:
        return f'Module \'{self.name}\''
    
    @property
    def type(self) -> str:
        return 'module'

    def __import__(self, env) -> None:
        env.add_module(self)
