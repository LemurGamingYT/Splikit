from argparse import ArgumentParser
from sys import exit as sys_exit
from subprocess import run
from pathlib import Path

from compiler.constants import BOLD, RED, RESET
from compiler import SplikitCompiler


def compfile(file: Path, compile_args: list) -> Path:
    print(f'{BOLD}Compiling {file.name}{RESET}')

    compiler = SplikitCompiler()
    cpp_file = compiler.compile(file)
    print(f'{BOLD}Compiled {file.name} file{RESET}')
    if args.compile:
        out = compiler.cpp_to_exe(file, cpp_file, *compile_args)
        if out.is_file():
            print(f'{BOLD}Compiled to executable file ({out}){RESET}')
        else:
            print(f'{RED}Failed to compile to executable file{RESET}')

        if args.run and out.is_file():
            run([out.as_posix()])

    if args.clean:
        file.with_suffix('.cpp').unlink(missing_ok=True)

def iterate_dir(file: Path, compile_args: list) -> None:
    for f in file.iterdir():
        if f.is_file() and f.suffix == '.spk':
            compfile(f, compile_args)
        elif f.is_dir():
            iterate_dir(f, compile_args)

def main() -> None:
    file: Path = args.file
    if file.is_file():
        compfile(file, compile_args)
    elif file.is_dir():
        iterate_dir(file, compile_args)


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Splikit compiler')
    arg_parser.add_argument('file', type=Path, help='Splikit source file (.spk)')
    arg_parser.add_argument('--release', action='store_true', help='Compile in release mode')
    arg_parser.add_argument('-c', '--compile', action='store_true', help='Compile to exe')
    arg_parser.add_argument('--clean', action='store_true', help='Delete the .cpp file')
    arg_parser.add_argument('-r', '--run', action='store_true', help='Run executable file')
    args = arg_parser.parse_args()
    
    compile_args = []
    if args.release:
        compile_args.append('-O2')
    
    if args.run and not args.compile:
        print('--run can only be used with --compile')
        sys_exit(1)
    
    if not args.file.exists():
        print(f'{BOLD}File \'{args.file.as_posix()}\' {RED}not found{RESET}')
        sys_exit(1)

    main()
