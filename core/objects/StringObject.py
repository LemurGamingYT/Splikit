from dataclasses import dataclass, field
from inspect import currentframe
from typing import Any
from .IntObject import IntObject
from .BoolObject import BoolObject
from .FloatObject import FloatObject
from ..error import report_error
from ..other import is_instance_type, get_arg

@dataclass()
class StringObject:
    value: str

    __type__: str = field(init=False, repr=False, default='string')

    def repr(self) -> str:
        if currentframe().f_back.f_code.co_name in ('<genexpr>', 'repr'):
            return f'\'{self.value}\''

        return self.value

    @property
    def type(self) -> str:
        return 'string'

    def Lower(self, _: tuple[Any, ...]):
        return StringObject(self.value.lower())

    def Upper(self, _: tuple[Any, ...]):
        return StringObject(self.value.upper())

    def Title(self, _: tuple[Any, ...]):
        return StringObject(self.value.title())

    def Startswith(self, _: tuple[Any, ...]):
        return BoolObject(self.value.startswith(self.value))

    def Endswith(self, _: tuple[Any, ...]):
        return BoolObject(self.value.endswith(self.value))

    def ReplaceSubstring(self, args: tuple[Any, ...]):
        substring = get_arg(0, args)
        replacement = get_arg(1, args)
        if is_instance_type(substring, StringObject) and is_instance_type(replacement, StringObject):
            return StringObject(self.value.replace(substring.value, replacement.value))

    def AsInt(self, _: tuple[Any, ...] = None, v = None):
        try:
            return IntObject(int(self.value))
        except ValueError:
            return report_error('Type', f'Invalid cast type \'{self.type}\' to \'int\'')

    def AsFloat(self, _: tuple[Any, ...] = None, v = None):
        try:
            return FloatObject(float(self.value))
        except ValueError:
            return report_error('Type', f'Invalid cast type \'{self.type}\' to \'float\'')

    def AsBool(self, _: tuple[Any, ...] = None, v = None):
        try:
            return BoolObject(bool(self.value))
        except ValueError:
            return report_error('Type', f'Invalid cast type \'{self.type}\' to \'bool\'')

    def __add__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return StringObject(self.value + other.value)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            return StringObject(self.value * other.value)

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return BoolObject(self.value == other.value)

    def __ne__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return BoolObject(self.value != other.value)

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return BoolObject(len(self.value) > len(other.value))

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return BoolObject(len(self.value) < len(other.value))

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return BoolObject(len(self.value) >= len(other.value))

    def __le__(self, other: Any) -> Any:
        if isinstance(other, StringObject):
            return BoolObject(len(self.value) <= len(other.value))

    def __not__(self):
        return StringObject(str(reversed(self.value)))
