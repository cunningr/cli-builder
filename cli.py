import argparse
import project

# cli = {
#     'class1': project.MyClass,
#     'class2': project.YourClass,
# }


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='cli',
        description='change this description',
        usage='''cli <command> [<args>]

This description will be updated
''')
    subparsers = parser.add_subparsers(help='sub-command help')
    for key, value in project.cli.items():
        # opt = subparsers.add_parser(key, help='Obj help ...')
        opt = value.add_args(key, subparsers)
        opt.set_defaults(func=value)

    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()
        parser.exit()
    # print(args)

