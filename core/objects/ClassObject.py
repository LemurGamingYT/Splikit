from dataclasses import dataclass

@dataclass()
class ClassObject:
    name: str
    attributes: dict
    methods: dict

    def repr(self) -> str:
        return f'Class \'{self.name}\''
