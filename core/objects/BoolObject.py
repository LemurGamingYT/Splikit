from dataclasses import dataclass, field
from typing import Any

@dataclass(unsafe_hash=True)
class BoolObject:
    value: bool

    __type__: str = field(init=False, repr=False, default='bool')

    def repr(self) -> str:
        return str(self.value).lower()

    @property
    def type(self) -> str:
        return 'bool'

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, BoolObject):
            return BoolObject(self.value == other.value)

    def __ne__(self, other: Any) -> Any:
        if isinstance(other, BoolObject):
            return BoolObject(self.value != other.value)

    def __bool__(self):
        return self.value

    def __or__(self, other: Any) -> Any:
        if isinstance(other, BoolObject):
            return BoolObject(self.value or other.value)

    def __and__(self, other: Any) -> Any:
        if isinstance(other, BoolObject):
            return BoolObject(self.value and other.value)

    def __not__(self):
        return BoolObject(not self.value)
