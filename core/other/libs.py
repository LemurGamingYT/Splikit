from typing import Any
from . import is_instance_type, get_arg
from .classes import generate_cls
from ..objects import *
from os import getcwd, cpu_count, getenv
from time import perf_counter, sleep
from ..error import report_error
from requests import get, Response
from requests.exceptions import MissingSchema
from re import findall, error, sub
from sys import argv


class Timer:
    __name__ = 'Timer'

    def __init__(self, time: float):
        self.time = VarObject('time', FloatObject(time))

    def _Since(self, _: tuple[Any, ...], v) -> FloatObject:
        return FloatObject(perf_counter() - self.time.value.value)


class WebResponse:
    __name__ = 'WebResponse'

    def __init__(self, response: Response):
        self.__response = response
        self.content = VarObject('content', StringObject(response.text))
        self.status = VarObject('status', IntObject(response.status_code))
        self.requestedUrl = VarObject('requestedUrl', StringObject(response.url))
        self.encoding = VarObject('encoding', StringObject(response.encoding))
        self.ok = VarObject('ok', BoolObject(response.ok))
        self.elapsed = VarObject('elapsed', FloatObject(response.elapsed.total_seconds()))
        self.history = VarObject('history', ArrayObject(response.history))

    def _Close(self, _: tuple[Any, ...], v) -> NilObject:
        self.__response.close()
        return NilObject()


class FileReader:
    __name__ = 'FileReader'

    def __init__(self, fn: StringObject):
        self.__writeable_file = open(fn.value, 'w')
        self.__readable_file = open(fn.value, 'r')
        self.name = VarObject('name', StringObject(self.__readable_file.name))
        self.contents = VarObject('contents', StringObject(self.__readable_file.read()))
        self.encoding = VarObject('encoding', StringObject(self.__readable_file.encoding))
        self.closed = VarObject('closed', BoolObject(self.__readable_file.closed))

    def _Write(self, args: tuple[Any, ...], v) -> NilObject:
        content = get_arg(0, args)
        if is_instance_type(content, StringObject):
            self.__writeable_file.writelines(content.value.split('\n'))

            return NilObject()

    def _Close(self, _: tuple[Any, ...], v) -> NilObject:
        self.__writeable_file.close()
        self.__readable_file.close()
        return NilObject()


class Lexer:
    __name__ = 'Lexer'

    def __init__(self, content: StringObject):
        self.content = VarObject('content', content)

        self.__tokens = []
        self.__rules = {}
        self.__skip = []

    def Skip(self, args: tuple[Any, ...], _) -> NilObject:
        pattern = get_arg(0, args)
        if is_instance_type(pattern, StringObject):
            self.__skip.append(pattern.value)

            return NilObject()

    def AddRule(self, args: tuple[Any, ...], _) -> NilObject:
        pattern = get_arg(0, args)
        name = get_arg(1, args)

        if is_instance_type(
                pattern,
                StringObject) and is_instance_type(name, StringObject):
            self.__rules[pattern.value] = name.value

        return NilObject()

    def __tokenize(self, text: str) -> None:
        for pattern in self.__skip:
            text = sub(pattern, '', text)

        for pattern, name in self.__rules.items():
            try:
                findall(pattern, text)
            except error:
                return report_error('Type', f'Invalid pattern: {pattern}')

            if findall(pattern, text):
                for m in findall(pattern, text):
                    self.__tokens.append(ArrayObject([StringObject(name), StringObject(m)]))

    def Tokenize(self, _: tuple[Any, ...], v) -> ArrayObject:
        self.__tokens = []

        try:
            with open(self.content.value, 'r') as f:
                self.__tokenize(f.read())

        except TypeError:
            self.__tokenize(self.content.value.value)

        return ArrayObject(self.__tokens)

class Parser:
    # TODO: finish parser
    __name__ = 'Parser'

    def __init__(self, tokens: ArrayObject):
        self.__tokens = tokens.value
        print(self.__tokens)


class Args:
    __name__ = 'ParsedArgs'

class ArgumentParser:
    __name__ = 'ArgumentParser'

    def __init__(self):
        self.__arg_rules = []

    def AddArgumentRule(self, args: tuple[Any, ...], _) -> NilObject:
        name = get_arg(0, args)
        requires_value = get_arg(1, args, optional=True)
        if is_instance_type(name, StringObject) and is_instance_type(
                requires_value, BoolObject):
            self.__arg_rules.append((name.value, requires_value.value))

        return NilObject()

    def Parse(self, _: tuple[Any, ...], v) -> ClassObject:
        p = Args()

        next_idx = 0
        while next_idx < len(argv[2:]) - 1:
            arg = argv[next_idx]
            for dat in self.__arg_rules:
                if arg == dat[0]:
                    if dat[1]:
                        setattr(p, arg.replace('-', ''), StringObject(argv[next_idx + 1]))
                        next_idx += 1
                    else:
                        print(arg.replace('-', ''))
                        setattr(p, arg.replace('-', ''), NilObject())

        return generate_cls(p)


Operators = {
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    '%': '%',
    '==': '==',
    '!=': '!=',
    '<': '<',
    '>': '>',
    '<=': '<=',
    '>=': '>=',
    '&': '&',
    '|': '|',
    'Add': '+',
    'Subtract': '-',
    'Multiply': '*',
    'Divide': '/',
    'Modulo': '%',
    'Equal': '==',
    'NotEqual': '!=',
    'LessThan': '<',
    'GreaterTan': '>',
    'LessEqualTan': '<=',
    'GreaterEqualThan': '>=',
    'And': '&',
    'Or': '|'
}

class Libs:
    class Knock:
        @staticmethod
        def Knock(args: tuple[Any, ...], _):
            url = get_arg(0, args)
            if is_instance_type(url, StringObject):
                try:
                    return generate_cls(WebResponse(get(url.value)))
                except MissingSchema:
                    return report_error('Knock', f'Missing Schema, try https://{url.value}')


    class SplikX:
        @staticmethod
        def NewLexer(args: tuple[Any, ...], _):
            fn = get_arg(0, args)
            if is_instance_type(fn, StringObject):
                return generate_cls(Lexer(fn))

        @staticmethod
        def NewParser(args: tuple[Any, ...], _):
            tokens = get_arg(0, args)
            if is_instance_type(tokens, ArrayObject):
                return generate_cls(Parser(tokens))


    class FStream:
        @staticmethod
        def OpenFile(args: tuple[Any, ...], _):
            fn = get_arg(0, args)
            if is_instance_type(fn, StringObject):
                return generate_cls(FileReader(fn))

    class Time:
        @staticmethod
        def TimeFunction(args: tuple[Any, ...], visitor):
            start = perf_counter()

            func = get_arg(0, args)
            if is_instance_type(func, FuncObject):
                func.call(get_arg(1, args, optional=True), visitor)

            end = perf_counter()
            elapsed = end - start
            return FloatObject(elapsed)

        @staticmethod
        def Time(_: tuple[Any, ...], v) -> ClassObject:
            return generate_cls(Timer(perf_counter()))

        @staticmethod
        def Pause(args: tuple[Any, ...], _) -> NilObject:
            secs = get_arg(0, args)
            if is_instance_type(secs, (FloatObject, IntObject)):
                sleep(secs.value)

                return NilObject()

    class GUI:
        ...

    class ArgumentParser:
        @staticmethod
        def NewArgumentParser(_: tuple[Any, ...], v):
            return generate_cls(ArgumentParser())

    class Operators:
        @staticmethod
        def Op(args: tuple[Any, ...], _):
            operation = get_arg(0, args)
            obj1 = get_arg(1, args)
            obj2 = get_arg(2, args)

            if is_instance_type(operation, StringObject):
                if not operation.value in Operators:
                    return report_error(
                        'Type',
                        f'Invalid operation \'{operation.value}\''
                    )

                return eval('{}{}{}'.format(obj1, Operators[operation.value], obj2))

    class System:
        @staticmethod
        def GetCD(_: tuple[Any, ...], v) -> StringObject:
            return StringObject(getcwd())

        @staticmethod
        def GetEnvironmentValue(args: tuple[Any, ...], _) -> StringObject:
            name = get_arg(0, args)
            if is_instance_type(name, StringObject):
                return StringObject(getenv(name.value))

        @staticmethod
        def CPUCount(_: tuple[Any, ...], v) -> IntObject | NilObject:
            c = cpu_count()
            if c is None:
                return NilObject()

            return IntObject(c)
