import argparse
from config import Configuration


def setup_parser():
    """Argument parser for Code Secret
    """

    config = Configuration()
    parser = argparse.ArgumentParser(
        prog='code-secret',
        description='Encrypt/Decrypt automatically git repository'
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-v",
        "--version",
        action="version",
        version="Version: {ver}".format(ver=config.get_default['version']),
        help="Show program's version and exit."
    )

    group.add_argument(
        "argument",
        help="Code Secret argument options.",
        nargs='?',
        action="append",
        choices=('init', 'add', 'remove', 'terminate')
    )

    parser.add_argument('value', nargs='*', action='append')

    return parser
