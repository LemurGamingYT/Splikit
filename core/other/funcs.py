from sys import stdout
from typing import Any, NoReturn

from . import get_arg
from . import report_argument_type_error, is_instance_type
from ..objects import *


class Funcs:
    @staticmethod
    def Print_func(args: tuple[Any, ...], _) -> NilObject:
        if hasattr(get_arg(0, args), 'repr'):
            stdout.write(str(get_arg(0, args).repr()) + '\n')
        else:
            stdout.write(str(get_arg(0, args)) + '\n')

        return NilObject()

    @staticmethod
    def Exit_func(_: tuple[Any, ...], v) -> NoReturn:
        exit(0)

    @staticmethod
    def ExecuteFile_func(args: tuple[Any, ...], _) -> NilObject:
        from main import main
        string = get_arg(0, args)
        if is_instance_type(string, StringObject):
            main(string.value)

            return NilObject()

    @staticmethod
    def AllObjects_func(_: tuple[Any, ...], visitor) -> ArrayObject:
        return ArrayObject(
            [obj for obj in visitor.env.variables.values()] + \
            [obj for obj in visitor.env.functions.values()] + \
            [obj for obj in visitor.env.classes.values()] + \
            [obj for obj in visitor.env.modules.values()])

    # @staticmethod
    # def Call_func(args: tuple[Any, ...], visitor) -> Any:
    #     func = get_arg(0, args)
    #     a = get_arg(1, args, optional=True)
    #
    #     if not isinstance(func, FuncObject) or not callable(func.py):
    #         return report_error('Type', f'\'{func}\' is not callable')
    #
    #     if a is None:
    #         return func.call((), visitor)
    #     else:
    #         try:
    #             return func.call(a.value, visitor)
    #         except TypeError:
    #             return func.call(a.value)

    # @staticmethod
    # def Splik_func(args: tuple[Any, ...], _):
    #     file = get_arg(0, args)
    #     if is_instance_type(file, StringObject, expected_type='string'):
    #         main(file.value)

    @staticmethod
    def Len_func(args: tuple[Any, ...], _) -> IntObject:
        if isinstance(get_arg(0, args), StringObject):
            return IntObject(len(get_arg(0, args).value))
        elif isinstance(get_arg(0, args), ArrayObject):
            return IntObject(len(get_arg(0, args).value))

        return report_argument_type_error('string', get_arg(0, args).type)

    @staticmethod
    def Type_func(args: tuple[Any, ...], _) -> StringObject:
        return StringObject(get_arg(0, args).type)

    @staticmethod
    def IsAlpha_func(args: tuple[Any, ...], _) -> BoolObject:
        value = get_arg(0, args)
        if is_instance_type(value, StringObject):
            return BoolObject(value.value.isalpha())

    @staticmethod
    def IsDigit_func(args: tuple[Any, ...], _) -> BoolObject:
        value = get_arg(0, args)
        if is_instance_type(value, StringObject):
            return BoolObject(value.value.isdigit())

    @staticmethod
    def Prompt_func(args: tuple[Any, ...], _) -> StringObject:
        prompt = get_arg(0, args)
        if is_instance_type(prompt, StringObject):
            return StringObject(input(prompt.value))
