import prog as prog
from pyfiglet import Figlet
import argparse
import logging
import os

logger = logging.getLogger('main')


def setup_logging(log_level=None):
    # Take logging level from OS ENV $LOGGING
    if log_level is None:
        log_level = os.environ.get('LOGGING', 'INFO')
    level = logging.getLevelName(log_level.upper())
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.propagate = False


def show_version():
    print('Name: {}'.format(prog.name))
    print('Description: {}'.format(prog.description))
    print('Version: {}\n'.format(prog.version))


def main():
    f = Figlet(justify='center')
    print(f.renderText(prog.name))
    parser = argparse.ArgumentParser(
        prog=prog.name,
        description=prog.description,
        usage=prog.usage
    )
    parser.set_defaults(func=lambda args: parser.print_help())
    parser.add_argument('--version', action='store_true', help='Prints program version')
    parser.add_argument('--debug', action='store_true', help='Enable debug level logging')
    args, unknown_args = parser.parse_known_args()
    # Execute any top level args
    if args.version:
        show_version()
        return
    if args.debug:
        setup_logging(log_level='DEBUG')
    else:
        setup_logging()

    # Add all the registered commands
    subparsers = parser.add_subparsers(help='Optional commands:')
    for key, value in prog.model.items():
        opt = value.add_args(key, subparsers)
        opt.set_defaults(func=value)
    args, unknown_args = parser.parse_known_args()

    # Finally, execute the (sub)command
    args.func(args)


if __name__ == "__main__":
    main()
