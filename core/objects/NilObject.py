from dataclasses import dataclass, field

@dataclass()
class NilObject:
    __type__: str = field(init=False, repr=False, default='nil')

    @staticmethod
    def repr() -> str:
        return 'nil'

    @property
    def type(self) -> str:
        return 'nil'
