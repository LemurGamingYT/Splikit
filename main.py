"""
Splikit

A language made in Python.

"""

from core.error import report_error, SplikitErrorListener
from antlr4 import CommonTokenStream, FileStream
from core.gen.SplikitParser import SplikitParser
from core.gen.SplikitLexer import SplikitLexer
from core.env import Environment
from time import perf_counter
# from typing import Callable
from os.path import isdir
from core import Visitor
from os import listdir
from sys import argv

# def time(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         start = perf_counter()
#
#         func(*args, **kwargs)
#
#         end = perf_counter()
#         elapsed = end - start
#         print(f'Execution of func \'{func.__name__}\' took: {elapsed * 1000}ms')
#
#     return wrapper


def main(f: str) -> None:
    start = perf_counter()

    try:
        fstream = FileStream(f)
    except FileNotFoundError:
        return report_error('File', f'File \'{f}\' does not exist')

    lexer = SplikitLexer(fstream)
    tokens = CommonTokenStream(lexer)

    parser = SplikitParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(SplikitErrorListener())

    tree = parser.program()

    env = Environment()

    visitor = Visitor(env)
    visitor.visit(tree)

    end = perf_counter()
    elapsed = end - start
    print(f'Execution took: {round(elapsed * 1000, 6)}ms')


if __name__ == '__main__' and len(argv) > 1:
    if argv[1] == '--run-tests':
        for file in listdir('examples/'):
            if file.endswith('.spk') and file != 'examples.spk':
                print(f'Running example: {file}')
                main(f'examples/{file}')
            elif isdir(f'examples/{file}'):
                for efile in listdir(f'examples/{file}/'):
                    if efile.endswith('.spk'):
                        print(f'Running example: examples/{file}/{efile}')
                        main(f'examples/{file}/{efile}')
    else:
        main(argv[1])
else:
    main('examples/test.spk')
