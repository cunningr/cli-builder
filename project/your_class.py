
class YourClass:
    def __init__(self, args):
        print(args)

    @staticmethod
    def add_args(_key, _subparsers):
        _opt = _subparsers.add_parser(_key, help='Help for YourClass ...')
        _opt.add_argument('--arg1', required=True, help='sub-command1 help')
        _opt.add_argument('--arg2', help='sub-command2 help')
        return _opt