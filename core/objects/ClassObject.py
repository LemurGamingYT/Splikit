from dataclasses import dataclass, field

@dataclass()
class ClassObject:
    name: str
    attributes: dict
    methods: dict
    class_type: type = field(default=None)

    def repr(self) -> str:
        return f'Class \'{self.name}\''
