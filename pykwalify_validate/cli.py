import argparse, io, sys
from pathlib import Path


def load_settings():
    print("load_settings")
    path = Path(".") / ".pykwalifyvalidate.yaml"
    if not path.exists():
        raise OSError(":(")


def main(argv=None):
    print("main")
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)
    print(args)
    print(load_settings())
    # errors_found = False
    # for filename in args.filenames:
    #     linter_error = get_linter_error(filename)
    #     if linter_error:
    #         errors_found = True
    #         print('Syntax error found in ', filename, file=sys.stderr)
    #         print(linter_error, file=sys.stderr)

    # return 1 if errors_found else 0
    return 1



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))