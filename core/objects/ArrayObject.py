from dataclasses import dataclass, field
from .IntObject import IntObject
from .BoolObject import BoolObject
from typing import Any

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

@dataclass()
class ArrayObject:
    value: list[Any, ...]

    __type__: str = field(init=False, repr=False, default='array')

    def repr(self) -> str:
        return f'{{{", ".join(val.repr() for val in self.value)}}}'

    @property
    def type(self) -> str:
        return 'array'

    def TimSort(self, _: tuple[Any, ...]):
        new = self.value
        new.sort()
        return ArrayObject(new)

    def QuickSort(self, _: tuple[Any, ...]):
        return ArrayObject(list(quicksort(self.value)))

    def __add__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return ArrayObject(self.value + other.value)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, IntObject):
            return ArrayObject(self.value * other.value)

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return BoolObject(self.value == other.value)

    def __ne__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return BoolObject(self.value != other.value)

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return BoolObject(self.value > other.value)

    def __lt__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return BoolObject(self.value < other.value)

    def __le__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return BoolObject(self.value <= other.value)

    def __ge__(self, other: Any) -> Any:
        if isinstance(other, ArrayObject):
            return BoolObject(self.value >= other.value)
