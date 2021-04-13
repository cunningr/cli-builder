import logging
import prog.common as common

logger = logging.getLogger('main.{}'.format(__name__))


class Command2:
    def __init__(self, args):
        # Run setup tasks
        self.args = args
        self.attribute1 = None
        self.attribute2 = None
        self._setup_func1()

        # Run the command with args
        self.run(args)

    @staticmethod
    def add_args(_key, _subparsers):
        _args = _subparsers.add_parser(_key, help='use prog command1 -h for help')
        _args.add_argument('--arg1', help='value for agr1')
        _args.add_argument('--arg2', help='value for agr2')
        _sub_command2 = _args.add_subparsers(help='sub-command help')
        _sub_command2 = SubCommand2.add_args('sub2', _sub_command2)
        _sub_command2.set_defaults(func=SubCommand2)
        return _args

    def run(self, args):
        logger.info('Executing command2 with --arg1: {}'.format(args.arg1))
        logger.info('--arg2: {}'.format(self.attribute2))
        logger.debug('*** This is a DEBUG level log ***')

    def _setup_func1(self):
        self.attribute1 = common.some_common_var
        if self.args.arg2:
            self.attribute2 = self.args.arg2
        else:
            self.attribute2 = 'NOT_SET'


class SubCommand2:
    def __init__(self, args):
        # Run setup tasks
        self.args = args
        self.attribute1 = None
        self.attribute2 = None
        self._setup_func1()

        # Run the command with args
        self.run(args)

    @staticmethod
    def add_args(_key, _subparsers):
        _args = _subparsers.add_parser(_key, help='use prog command1 -h for help')
        _args.add_argument('--arg1', required=True, help='value for agr1')
        _args.add_argument('--arg2', help='value for agr2')
        return _args

    def run(self, args):
        logger.info('Executing sub_command2 with --arg1: {}'.format(args.arg1))
        logger.info('--arg2: {}'.format(self.attribute2))
        logger.debug('*** This is a DEBUG level log ***')

    def _setup_func1(self):
        self.attribute1 = common.some_common_var
        if self.args.arg2:
            self.attribute2 = self.args.arg2
        else:
            self.attribute2 = 'NOT_SET'
