from dataclasses import dataclass
from typing import Any

@dataclass(repr=False)
class VarObject:
    name: str
    value: Any

    def repr(self) -> str:
        return f'<variable at {hex(id(self))}>'
