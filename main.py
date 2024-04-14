from argparse import ArgumentParser
from platform import system
from subprocess import run
from pathlib import Path
from shutil import which

from compiler.constants import BOLD, RED, RESET
from compiler.info import DEFAULT_HEADER
from compiler import SplikitCompiler


def main() -> None:
    arg_parser = ArgumentParser(description='Splikit compiler')
    arg_parser.add_argument('file', type=Path, help='Splikit source file (.spk)')
    args = arg_parser.parse_args()

    compiler = SplikitCompiler(args)
    src = compiler.compile(args.file)

    c_file: Path = args.file.with_suffix('.cpp').absolute()
    output: Path = args.file.with_suffix('.exe' if system() == 'Windows' else '').absolute()
    c_file.write_text(f'#include "{DEFAULT_HEADER.absolute().as_posix()}"\n\n{src}', 'utf-8')

    if which('g++') is not None:
        run(['g++', c_file.as_posix(), '-o', output.as_posix()])
        run([output.as_posix()])
    elif which('clang++') is not None:
        run(['clang++', c_file.as_posix(), '-o', output.as_posix()])
        run([output.as_posix()])
    else:
        print(f'{BOLD}{RED}Invalid compiler{RESET}')


if __name__ == '__main__':
    main()
