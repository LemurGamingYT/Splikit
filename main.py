from antlr4 import CommonTokenStream, FileStream
from core.gen.SplikitParser import SplikitParser
from core.gen.SplikitLexer import SplikitLexer
from core.env import Environment
from time import perf_counter
from typing import Callable
from core import Visitor

def time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = perf_counter()

        func(*args, **kwargs)

        end = perf_counter()
        elapsed = end - start
        print(f'Execution of func \'{func.__name__}\' took: {elapsed * 1000}ms')

    return wrapper


def main(file: str) -> None:
    start = perf_counter()

    file = FileStream(file)

    lexer = SplikitLexer(file)
    tokens = CommonTokenStream(lexer)

    parser = SplikitParser(tokens)
    parser.removeErrorListeners()

    tree = parser.program()

    env = Environment()

    visitor = Visitor(env)
    visitor.visit(tree)

    end = perf_counter()
    elapsed = end - start
    print(f'Execution took: {elapsed * 1000}ms')


if __name__ == '__main__':
    main('examples/test.spk')
