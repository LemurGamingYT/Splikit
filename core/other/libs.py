from json import load
from os import getcwd, cpu_count, getenv
from re import error, sub, compile
from sys import argv
from time import perf_counter, sleep
from typing import Any, Union

from customtkinter import CTk
from pyautogui import (
    click, leftClick, rightClick, keyDown, keyUp, mouseUp, mouseInfo, mouseDown, displayMousePosition, size)
from requests import get, Response
from requests.exceptions import MissingSchema

from . import is_instance_type, get_arg, infer_type
from .classes import DictionaryObject
from .classes import generate_cls
from ..error import report_error
from ..objects import *


class Timer:
    __name__ = 'Timer'

    def __init__(self, time: float):
        self.time = FloatObject(time)


class WebResponse:
    __name__ = 'WebResponse'

    def __init__(self, response: Response):
        self.__response = response
        self.content = StringObject(response.text)
        self.status = IntObject(response.status_code)
        self.requestedUrl = StringObject(response.url)
        self.encoding = StringObject(response.encoding)
        self.ok = BoolObject(response.ok)
        self.elapsed = FloatObject(response.elapsed.total_seconds())
        self.history = ArrayObject(response.history)

    def Close(self, _: tuple[Any, ...], v) -> NilObject:
        self.__response.close()
        return NilObject()


class File:
    __name__ = 'FileClass'

    def __init__(self, fn: StringObject):
        self.__writeable_file = open(fn.value, 'w')
        self.__readable_file = open(fn.value, 'r')
        self.name = StringObject(self.__readable_file.name)
        self.contents = StringObject(self.__readable_file.read())
        self.encoding = StringObject(self.__readable_file.encoding)
        self.closed = BoolObject(self.__readable_file.closed)

    def Write(self, args: tuple[Any, ...], v) -> NilObject:
        content = get_arg(0, args)
        if is_instance_type(content, StringObject):
            self.__writeable_file.writelines(content.value.split('\n'))

            return NilObject()

    def Close(self, _: tuple[Any, ...], v) -> NilObject:
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
                regex = compile(pattern)
            except error:
                return report_error('Type', f'Invalid pattern: {pattern}')
            
            while text:
                m = regex.match(text)
                if m:
                    value = m.group(0)
                    self.__tokens.append(ArrayObject([StringObject(name), StringObject(value)]))
                    text = text[len(value):].lstrip()
                else:
                    break

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
    # TODO: finish argument parser
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


class JsonReader(DictionaryObject):
    __name__ = 'JsonReader'

    def __init__(self, fn: StringObject) -> None:
        super().__init__()

        self.fn = fn.value
        self.fp = open(self.fn, 'r')

        for key, value in load(self.fp).items():
            self[key] = infer_type(value)

        self.fp.close()


# TODO: implement window keybindings
window_keybindings = {
    'q': 'q',
    'w': 'w',
    'e': 'e',
    'r': 'r',
    't': 't',
    'y': 'y',
    'u': 'u',
    'i': 'i',
    'o': 'o',
    'p': 'p',
    '[': '[',
    ']': ']',
    'a': 'a',
    's': 's',
    'd': 'd',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    ';': ';',
    "'": "'",
    ',': ',',
    '`': '`',
    '\\': '\\',
    'z': 'z',
    'x': 'x',
    'c': 'c',
    'v': 'v',
    'b': 'b',
    'n': 'n',
    'm': 'm',
    '<': '<',
    '>': '>',
    '?': '?',
    '!': '!',
    '@': '@',
    '#': '#',
    '$': '$',
    '%': '%',
    '^': '^',
    '&': '&',
    '*': '*',
    '(': '(',
    ')': ')',
    '{': '{',
    '}': '}',
    '|': '|',
    '~': '~',
    '+': '+',
    '-': '-',
    '=': '=',
    '_': '_',
    '.': '.',
    'Enter': '<Enter>'
}

class Window:
    __name__ = 'Window'

    def __init__(self, title: str, width: int, height: int):
        self.title = VarObject('title', StringObject(title))
        self.width = VarObject('width', IntObject(width))
        self.height = VarObject('height', IntObject(height))

        self.__window = CTk()
        self.__window.geometry(f'{width}x{height}')
        self.__window.title(title)

        self.__window.mainloop()

    def SetTitle(self, args: tuple[Any, ...], _) -> NilObject:
        new = get_arg(0, args)
        if is_instance_type(new, StringObject):
            self.__window.title(new.value)

            return NilObject()

    def Width(self, _: tuple[Any, ...], v) -> IntObject:
        return IntObject(self.__window.winfo_width())

    def Height(self, _: tuple[Any, ...], v) -> IntObject:
        return IntObject(self.__window.winfo_height())

    def Destroy(self, _: tuple[Any, ...], v) -> NilObject:
        self.__window.destroy()
        return NilObject()

    def SetFullscreen(self, args: tuple[Any, ...], _) -> NilObject:
        fullscreen = get_arg(0, args)
        if is_instance_type(fullscreen, BoolObject):
            self.__window.attributes('-fullscreen', fullscreen.value)
            return NilObject()

    def SetWindowSize(self, args: tuple[Any, ...], _) -> NilObject:
        width = get_arg(0, args)
        height = get_arg(1, args)
        if is_instance_type(width, IntObject) and is_instance_type(height, IntObject):
            self.__window.geometry(f'{width}x{height}')

            return NilObject()

    def BindKey(self, args: tuple[Any, ...], _) -> NilObject:
        # TODO: finish this function
        raise NotImplemented('This function is not implemented')


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


    class Json:
        @staticmethod
        def Parse(args: tuple[Any, ...], _):
            fn = get_arg(0, args)
            if is_instance_type(fn, StringObject):
                return generate_cls(JsonReader(fn))


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
                return generate_cls(File(fn))


    class Time:
        @staticmethod
        def TimeFunction(args: tuple[Any, ...], visitor):
            start = perf_counter()

            func = get_arg(0, args)
            if is_instance_type(func, FuncObject):
                func.call((), visitor)

            end = perf_counter()
            elapsed = end - start
            return FloatObject(elapsed)

        @staticmethod
        def Time(_: tuple[Any, ...], v) -> ClassObject:
            return generate_cls(Timer(perf_counter()))

        @staticmethod
        def Since(args: tuple[Any, ...], _) -> FloatObject:
            start = get_arg(0, args)
            if is_instance_type(start, ClassObject):
                if isinstance(start.class_type, Timer):
                    return FloatObject(perf_counter() - start.attributes['time'].value.value)
                else:
                    return report_error('Type', f'Invalid class, expected Class \'Timer\'')

        @staticmethod
        def Pause(args: tuple[Any, ...], _) -> NilObject:
            secs = get_arg(0, args)
            if is_instance_type(secs, (FloatObject, IntObject)):
                sleep(secs.value)

                return NilObject()


    class AdvancedCls:
        @staticmethod
        def New(args: tuple[Any, ...], _) -> ClassObject:
            name = get_arg(0, args)
            cls = ClassObject(name.value, {}, {})

            for arg in args:
                if isinstance(arg, StringObject):
                    cls.attributes[arg.value] = NilObject()
                else:
                    return report_error('Type', f'Invalid argument, expected type \'string\'')

            return cls


    class GUI:
        @staticmethod
        def NewWindow(args: tuple[Any, ...], _) -> ClassObject:
            title = get_arg(0, args)
            width = get_arg(1, args)
            height = get_arg(2, args)

            if is_instance_type(
                title, StringObject) and is_instance_type(width, IntObject) and is_instance_type(height, IntObject):
                return generate_cls(Window(title.value, width.value, height.value))


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
        ScreenWidth = IntObject(size()[0])
        ScreenHeight = IntObject(size()[1])

        @staticmethod
        def GetCD(_: tuple[Any, ...], v) -> StringObject:
            return StringObject(getcwd())

        @staticmethod
        def GetEnvironmentValue(args: tuple[Any, ...], _) -> StringObject:
            name = get_arg(0, args)
            if is_instance_type(name, StringObject):
                return StringObject(getenv(name.value))

        @staticmethod
        def CPUCount(_: tuple[Any, ...], v) -> Union[IntObject, NilObject]:
            c = cpu_count()
            if c is None:
                return NilObject()

            return IntObject(c)

        @staticmethod
        def Click(args: tuple[Any, ...], _) -> NilObject:
            x = get_arg(0, args)
            y = get_arg(1, args)
            if is_instance_type(x, IntObject) and is_instance_type(y, IntObject):
                click(x.value, y.value)

                return NilObject()

        @staticmethod
        def LeftClick(args: tuple[Any, ...], _) -> NilObject:
            x = get_arg(0, args)
            y = get_arg(1, args)
            if is_instance_type(x, IntObject) and is_instance_type(y, IntObject):
                leftClick(x.value, y.value)

                return NilObject()

        @staticmethod
        def RightClick(args: tuple[Any, ...], _) -> NilObject:
            x = get_arg(0, args)
            y = get_arg(1, args)
            if is_instance_type(x, IntObject) and is_instance_type(y, IntObject):
                rightClick(x.value, y.value)

                return NilObject()

        @staticmethod
        def KeyUp(args: tuple[Any, ...], _) -> NilObject:
            key = get_arg(0, args)
            if is_instance_type(key, StringObject):
                keyUp(key.value)

                return NilObject()

        @staticmethod
        def KeyDown(args: tuple[Any, ...], _) -> NilObject:
            key = get_arg(0, args)
            if is_instance_type(key, StringObject):
                keyDown(key.value)

                return NilObject()

        @staticmethod
        def MouseDown(args: tuple[Any, ...], _) -> NilObject:
            x = get_arg(0, args)
            y = get_arg(1, args)
            if is_instance_type(x, IntObject) and is_instance_type(y, IntObject):
                mouseDown(x.value, y.value)

                return NilObject()

        @staticmethod
        def MouseUp(args: tuple[Any, ...], _) -> NilObject:
            x = get_arg(0, args)
            y = get_arg(1, args)
            if is_instance_type(x, IntObject) and is_instance_type(y, IntObject):
                mouseUp(x.value, y.value)

                return NilObject()

        @staticmethod
        def MouseInfo(_: tuple[Any, ...], v) -> NilObject:
            mouseInfo()

            return NilObject()

        @staticmethod
        def PrintMouseInfo(_: tuple[Any, ...], v) -> NilObject:
            displayMousePosition()

            return NilObject()
