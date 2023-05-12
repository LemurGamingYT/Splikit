from typing import Any
from . import is_instance_type, get_arg
from .classes import generate_cls
from ..objects import *
from os import getcwd, cpu_count, getenv
from time import perf_counter

class Timer:
    __name__ = 'Timer'

    def __init__(self, time: float):
        self.time = VarObject('time', FloatObject(time))

    def _Since(self, _: tuple[Any, ...], v) -> FloatObject:
        return FloatObject(perf_counter() - self.time.value.value)

class Libs:
    class Time:
        @staticmethod
        def _TimeFunction(args: tuple[Any, ...], visitor):
            start = perf_counter()

            func = get_arg(0, args)
            if is_instance_type(func, FuncObject, expected_type='func'):
                func.call(get_arg(1, args, optional=True), visitor)

            end = perf_counter()
            elapsed = end - start
            return FloatObject(elapsed)

        @staticmethod
        def _Time(_: tuple[Any, ...], v):
            return generate_cls(Timer(perf_counter()))

    class GUI:
        ...

    class ArgumentParser:
        ...

    class Os:
        @staticmethod
        def _GetCD(_: tuple[Any, ...], v) -> StringObject:
            return StringObject(getcwd())

        @staticmethod
        def _GetEnvironmentValue(args: tuple[Any, ...], _) -> StringObject:
            name = get_arg(0, args)
            if is_instance_type(name, StringObject, expected_type='string'):
                return StringObject(getenv(name.value))

        @staticmethod
        def _CPUCount(_: tuple[Any, ...], v) -> IntObject | NilObject:
            c = cpu_count()
            if c is None:
                return NilObject()

            return IntObject(c)
