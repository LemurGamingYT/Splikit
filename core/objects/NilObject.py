from dataclasses import dataclass

@dataclass()
class NilObject:
    @staticmethod
    def repr() -> str:
        return 'nil'

    @property
    def type(self) -> str:
        return 'nil'
