from dataclasses import dataclass, field
from ..error import report_error
from typing import Any

@dataclass()
class IntObject:
    value: int

    __type__: str = field(init=False, repr=False, default='int')

    def AsString(self, _: tuple[Any, ...] = None, v = None):
        from .StringObject import StringObject
        try:
            return StringObject(str(self.value))
        except ValueError:
            return report_error('Type', f'Invalid cast type \'{self.type}\' to \'string\'')

    def repr(self) -> str:
        return str(self.value)

    @property
    def type(self) -> str:
        return 'int'

    def __add__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            return IntObject(self.value + other.value)

        from .FloatObject import FloatObject
        if isinstance(other, FloatObject):
            f = FloatObject(float(self.value) + other.value)
            del FloatObject
            return f

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            return IntObject(self.value - other.value)

        from .FloatObject import FloatObject
        if isinstance(other, FloatObject):
            f = FloatObject(float(self.value) - other.value)
            del FloatObject
            return f

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            return IntObject(self.value * other.value)

        from .FloatObject import FloatObject
        if isinstance(other, FloatObject):
            f = FloatObject(float(self.value) * other.value)
            del FloatObject
            return f

    def __truediv__(self, other: Any) -> Any:
        from .FloatObject import FloatObject
        if isinstance(other, IntObject):
            f = FloatObject(self.value / other.value)
            del FloatObject
            return f
        elif isinstance(other, FloatObject):
            f = FloatObject(float(self.value) / other.value)
            del FloatObject
            return f

    def __mod__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            return IntObject(self.value % other.value)

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value == other.value)
            del BoolObject
            return b

    def __ne__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value != other.value)
            del BoolObject
            return b

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value > other.value)
            del BoolObject
            return b

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value < other.value)
            del BoolObject
            return b

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value >= other.value)
            del BoolObject
            return b

    def __le__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            from .BoolObject import BoolObject
            b = BoolObject(self.value <= other.value)
            del BoolObject
            return b
