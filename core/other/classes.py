from math import (
    sin, cos, acos, asin,
    tan, atan, atan2,
    sqrt,
    lcm,
    isinf,
    ceil, floor,
    log, log10,
    degrees, radians,
    pi
)

from threading import Thread
from hashlib import sha256
from . import get_arg, is_instance_type
from random import randint, choice
from ..objects import *
from ..error import report_error
from typing import Any
from sys import stdout

def generate_cls(cls) -> ClassObject:
    attrs = dir(cls)
    attributes = {}
    methods = {}

    for attr in [attr for attr in attrs if not attr.startswith('__')]:
        if callable(getattr(cls, attr)):
            f = getattr(cls, attr)
            methods[f.__name__] = FuncObject(f.__name__, (), None, f)
        else:
            attributes[attr] = getattr(cls, attr)

    return ClassObject(cls.__name__, attributes, methods)


class Logging:
    __name__ = 'Logging'
    __format__ = '{levelname}: {message}'

    def __init__(self, fn: StringObject):
        self.__fn = open(fn.value, 'w')

    def _Document(self, args: tuple[Any, ...], _) -> NilObject:
        level = get_arg(0, args)
        content = get_arg(1, args)
        if is_instance_type(level, StringObject) and is_instance_type(content, StringObject):
            self.__fn.write(self.__format__.format(levelname=level.value, message=content.value))

        return NilObject()

    def _Close(self, _: tuple[Any, ...], v) -> NilObject:
        self.__fn.close()
        return NilObject()


class DictionaryObject:
    __name__ = 'Dict'

    def __init__(self):
        self.__dict = {}

    def Update(self, args: tuple[Any, ...], _) -> NilObject:
        key = get_arg(0, args)
        value = get_arg(1, args)

        self.__dict[key.value] = value.value
        return NilObject()

    def Get(self, args: tuple[Any, ...], _) -> Any:
        key = get_arg(0, args)
        return self.__dict.get(key.value) if self.__dict.get(key.value) is not None else NilObject()

class Classes:
    class Math:
        PI = VarObject('PI', FloatObject(pi))

        @staticmethod
        def Min(args: tuple[Any, ...], _):
            val1 = get_arg(0, args)
            val2 = get_arg(1, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                if is_instance_type(val2, (IntObject, FloatObject)):
                    if val1 < val2:
                        return val1
                    elif val2 < val1:
                        return val2
                    else:
                        return val1

        @staticmethod
        def Max(args: tuple[Any, ...], _):
            val1 = get_arg(0, args)
            val2 = get_arg(1, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                if is_instance_type(val2, (IntObject, FloatObject)):
                    if val2 < val1:
                        return val2
                    elif val1 < val2:
                        return val1
                    else:
                        return val1

        @staticmethod
        def ToRadians(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(radians(val1.value))

        @staticmethod
        def ToDegrees(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(degrees(val1.value))

        @staticmethod
        def Sine(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(sin(val1.value))

        @staticmethod
        def Cosine(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(cos(val1.value))

        @staticmethod
        def Tangent(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(tan(val1.value))

        @staticmethod
        def ArcSine(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(asin(val1.value))

        @staticmethod
        def ArcTangent(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                return FloatObject(atan(val1.value))

        @staticmethod
        def ArcTangent2(args: tuple[Any, ...], _) -> FloatObject:
            val1 = get_arg(0, args)
            val2 = get_arg(1, args)
            if is_instance_type(val1, (IntObject, FloatObject)):
                if is_instance_type(val2, (IntObject, FloatObject)):
                    return FloatObject(atan2(val1.value, val2.value))

        @staticmethod
        def LCM(args: tuple[Any, ...], _) -> IntObject:
            num1 = get_arg(0, args)
            num2 = get_arg(1, args)
            if is_instance_type(num1, IntObject):
                if is_instance_type(num2, IntObject):
                    return IntObject(lcm(num1.value, num2.value))

        @staticmethod
        def SquareRoot(args: tuple[Any, ...], _) -> FloatObject:
            val = get_arg(0, args)
            if is_instance_type(val, (IntObject, FloatObject)):
                return FloatObject(sqrt(val.value))

        @staticmethod
        def ArcCosine(args: tuple[Any, ...], _) -> FloatObject:
            val = get_arg(0, args)
            if is_instance_type(val, (IntObject, FloatObject)):
                return FloatObject(acos(val.value))

        @staticmethod
        def IsInf(args: tuple[Any, ...], _) -> BoolObject:
            val = get_arg(0, args)
            if is_instance_type(val, IntObject):
                return BoolObject(isinf(val.value))

        @staticmethod
        def Round(args: tuple[Any, ...], _) -> IntObject:
            val = get_arg(0, args)
            round_idx = get_arg(1, args)
            if is_instance_type(val, FloatObject):
                if is_instance_type(round_idx, IntObject):
                    return IntObject(round(val.value, round_idx.value))

        @staticmethod
        def Logarithm(args: tuple[Any, ...], _) -> FloatObject:
            val = get_arg(0, args)
            base = get_arg(1, args)
            if is_instance_type(val, (IntObject, FloatObject)):
                if is_instance_type(base, (IntObject, FloatObject)):
                    return FloatObject(log(val.value, base.value))

        @staticmethod
        def Logarithm10(args: tuple[Any, ...], _) -> FloatObject:
            val = get_arg(0, args)
            if is_instance_type(val, (IntObject, FloatObject)):
                return FloatObject(log10(val.value))

        @staticmethod
        def RoundUp(args: tuple[Any, ...], _) -> IntObject:
            val = get_arg(0, args)
            if is_instance_type(val, FloatObject):
                return IntObject(ceil(val.value))

        @staticmethod
        def RoundDown(args: tuple[Any, ...], _) -> IntObject:
            val = get_arg(0, args)
            if is_instance_type(val, FloatObject):
                return IntObject(floor(val.value))

        @staticmethod
        def IsPrime(args: tuple[Any, ...], _) -> BoolObject:
            x = get_arg(0, args)
            if is_instance_type(x, IntObject):
                if x < 2:
                    return BoolObject(False)

                for i in range(2, int(x.value ** .5) + 1):
                    if x % i == 0:
                        return BoolObject(False)

                return BoolObject(True)

        @staticmethod
        def RandomInt(args: tuple[Any, ...], _) -> IntObject:
            lowest = get_arg(0, args)
            highest = get_arg(1, args)
            if is_instance_type(lowest, IntObject) and is_instance_type(highest, IntObject):
                return IntObject(randint(lowest.value, highest.value))

        @staticmethod
        def RandomArray(args: tuple[Any, ...], _) -> Any:
            arr = get_arg(0, args)
            if is_instance_type(arr, ArrayObject):
                return choice(arr.value)


    class Attrs:
        @staticmethod
        def GetAll(args: tuple[Any, ...], _) -> ArrayObject:
            obj = get_arg(0, args)
            attrs = []
            for attr in [attr for attr in dir(obj) if not attr.startswith('__')]:
                attrs.append(StringObject(attr))

            return ArrayObject(attrs)

        @staticmethod
        def GetAttr(args: tuple[Any, ...], _):
            obj = get_arg(0, args)
            attr = get_arg(1, args)
            if is_instance_type(attr, StringObject):
                try:
                    return FuncObject(attr.value, (), None, getattr(obj, attr.value))
                except AttributeError:
                    return report_error('Attribute', f'\'{obj.repr()}\' has no attribute \'{attr.value}\'')

            return StringObject(getattr(obj, attr.value))


    class Thread:
        @staticmethod
        def Start(args: tuple[Any, ...], visitor) -> NilObject:
            func = get_arg(0, args)
            if is_instance_type(func, FuncObject):
                __t = Thread(target=func.call, args=(
                    tuple([get_arg(arg, args) for arg in range(1, len(args)-1)]), visitor)
                )
                __t.daemon = True
                __t.start()

            return NilObject()

    class Dictionary:
        @staticmethod
        def New(_: tuple[Any, ...], v) -> ClassObject:
            return generate_cls(DictionaryObject())


    class Obfuscator:
        @staticmethod
        def Obfuscate(args: tuple[Any, ...], _) -> StringObject:
            s = get_arg(0, args)
            if is_instance_type(s, StringObject):
                h = sha256()
                h.update(s.value.encode())
                return StringObject(h.hexdigest())


    class Logger:
        @staticmethod
        def Create(args: tuple[Any, ...], _) -> ClassObject:
            fn = get_arg(0, args)

            return generate_cls(Logging(fn))


    class Terminal:
        @staticmethod
        def Output(args: tuple[Any, ...], _) -> NilObject:
            stdout.write(get_arg(0, args).repr())
            return NilObject()


    class Python:
        @staticmethod
        def ExecuteCode(args: tuple[Any, ...], _) -> NilObject:
            code = get_arg(0, args)
            if is_instance_type(code, StringObject):
                exec(code.value)
                return NilObject()


    class Converter:
        @staticmethod
        def IntToBinary(args: tuple[Any, ...], _) -> StringObject:
            value = get_arg(0, args)
            if is_instance_type(value, IntObject):
                return StringObject(bin(value.value))
