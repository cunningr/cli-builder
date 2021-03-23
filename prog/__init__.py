from prog.command1 import Command1
from prog.command2 import Command2

name = 'My Prog'
description = 'An example of building a python CLI'
usage = 'prog <command> [<args>]'
model = {
    'command1': Command1,
    'command2': Command2
}
