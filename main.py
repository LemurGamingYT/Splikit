from argparse import ArgumentParser
from platform import system
from subprocess import run
from pathlib import Path
from shutil import which

from compiler.constants import BOLD, RED, RESET, info
from compiler.info import DEFAULT_HEADER
from compiler.std import get_functions
from compiler import SplikitCompiler


def main() -> None:
    arg_parser = ArgumentParser(description='Splikit compiler')
    arg_parser.add_argument('file', type=Path, help='Splikit source file (.spk)')
    # arg_parser.add_argument('--debug', action='store_true', help='Print debug info')
    args = arg_parser.parse_args()
    
    # info(args, f'System {system()}')
    # info(args, f'Using {DEFAULT_HEADER.as_posix()}')
    # info(args, f'Compiling {args.file.as_posix()}')

    compiler = SplikitCompiler(args)
    get_functions(compiler)
    src = compiler.compile(args.file)

    c_file: Path = args.file.with_suffix('.cpp').absolute()
    output: Path = args.file.with_suffix('.exe' if system() == 'Windows' else '').absolute()
    c_file.write_text(f'#include "{DEFAULT_HEADER.absolute().as_posix()}"\n\n{src}', 'utf-8')

    # info(args, f'Compiled to {c_file.as_posix()}')

    if which('g++') is not None:
        run(['g++', c_file.as_posix(), '-o', output.as_posix()])
        run([output.as_posix()])
        # info(args, 'Compiled with g++')
    else:
        print(f'{BOLD}{RED}Invalid compiler{RESET}')


if __name__ == '__main__':
    main()
