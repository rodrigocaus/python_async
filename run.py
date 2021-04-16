import importlib
from argparse import ArgumentParser


def optparse():
    parser = ArgumentParser(
        'ASYNC Class', description='Run examples comparing sync and async')

    parser.add_argument('example', type=str, metavar='MODULE',
                        default='dummy', help='Module name to run')

    return parser.parse_args()


if __name__ == '__main__':
    args = optparse()
    module = 'examples.' + args.example
    importlib.import_module(module, '.')
