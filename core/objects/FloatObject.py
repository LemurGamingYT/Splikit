from dataclasses import dataclass, field
from typing import Any

@dataclass()
class FloatObject:
    value: float

    __type__: str = field(init=False, repr=False, default='float')

    def repr(self) -> str:
        return str(self.value)

    @property
    def type(self) -> str:
        return 'float'

    def __add__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            return FloatObject(self.value + other.value)

        from .IntObject import IntObject
        if isinstance(other, IntObject):
            i = FloatObject(self.value + float(other.value))
            del IntObject
            return i

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            return FloatObject(self.value - other.value)

        from .IntObject import IntObject
        if isinstance(other, IntObject):
            i = FloatObject(self.value - float(other.value))
            del IntObject
            return i

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            return FloatObject(self.value * other.value)

        from .IntObject import IntObject
        if isinstance(other, IntObject):
            i = FloatObject(self.value * float(other.value))
            del IntObject
            return i

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            return FloatObject(self.value / other.value)

        from .IntObject import IntObject
        if isinstance(other, IntObject):
            i = FloatObject(self.value / float(other.value))
            del IntObject
            return i

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value == other.value)
            del BoolObject
            return b

    def __ne__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value != other.value)
            del BoolObject
            return b

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value > other.value)
            del BoolObject
            return b

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value < other.value)
            del BoolObject
            return b

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value >= other.value)
            del BoolObject
            return b

    def __le__(self, other: Any) -> Any:
        if isinstance(other, FloatObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value <= other.value)
            del BoolObject
            return b
