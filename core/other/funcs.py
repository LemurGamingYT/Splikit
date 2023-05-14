from typing import Any, NoReturn
from . import get_arg
from ..objects import *
from . import report_argument_type_error, is_instance_type

class Funcs:
    @staticmethod
    def Print_func(args: tuple[Any, ...], _) -> NilObject: # visitor is _
        if hasattr(get_arg(0, args), 'repr'):
            print(get_arg(0, args).repr())
        else:
            print(get_arg(0, args))

        return NilObject()

    @staticmethod
    def Exit_func(_: tuple[Any, ...], v) -> NoReturn:
        exit(0)

    @staticmethod
    def ExecuteString_func(args: tuple[Any, ...], _) -> NilObject:
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
    # def Splik_func(args: tuple[Any, ...], _):
    #     file = get_arg(0, args)
    #     if is_instance_type(file, StringObject, expected_type='string'):
    #         main(file.value)

    @staticmethod
    def Any_func(args: tuple[Any, ...], _) -> BoolObject:
        arr = get_arg(0, args)
        if is_instance_type(arr, ArrayObject):
            for val in arr.value:
                if isinstance(val, BoolObject) and val:
                    return BoolObject(True)

            return BoolObject(False)

    @staticmethod
    def All_func(args: tuple[Any, ...], _) -> BoolObject:
        arr = get_arg(0, args)
        if is_instance_type(arr, ArrayObject):
            for val in arr.value:
                if isinstance(val, BoolObject) and val:
                    return BoolObject(False)

            return BoolObject(True)

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
        if isinstance(value, StringObject):
            return BoolObject(value.value.isalpha())

        return report_argument_type_error('string', value.type)

    @staticmethod
    def IsDigit_func(args: tuple[Any, ...], _) -> BoolObject:
        value = get_arg(0, args)
        if isinstance(value, StringObject):
            return BoolObject(value.value.isdigit())

        return report_argument_type_error('string', value.type)

    @staticmethod
    def Prompt_func(args: tuple[Any, ...], _) -> StringObject:
        prompt = get_arg(0, args)
        if isinstance(prompt, StringObject):
            return StringObject(input(prompt.value))

        return report_argument_type_error('string', prompt.type)
