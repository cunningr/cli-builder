# cli-builder

A generic python CLI framework

A design pattern for creating CLI tools in python.

```prog``` is the main executable code has a few key attributes:

 1. ```__init__``` file loads the program modules and classes and indexes them in a dictionary.  You should also update the program ```name```, ```description``` and basic ```usage``` here.

```
from prog.command1 import Command1
from prog.command2 import Command2

name = 'My Prog'
description = 'An example of building a python CLI'
usage = 'prog <command> [<args>]'
model = {
    'command1': Command1,
    'command2': Command2
}
```

To add more or change the names of the sub-commands you will need to update the ```model``` and the import statements in ```__init__.py```_

 2. Each sub-command has a python module file with the same name and defines a class. It is intended to be with a 1:1 mapping of module:class definition.  Here you can see the two example files ```command1.py``` and ```command2.py```.  When you want to create a new CLI sub-command you can use one of these as the template.

You can test this design pattern by using ```python3 prog_cli.py command1 --arg1``` within this project directory for example:

```
(general) CUNNINGR-M-X436:cli-builder cunningr$ python3 prog_cli.py command1 --arg1 WOW --arg2 NOW
                      __  __         ____
                     |  \/  |_   _  |  _ \ _ __ ___   __ _
                     | |\/| | | | | | |_) | '__/ _ \ / _` |
                     | |  | | |_| | |  __/| | | (_) | (_| |
                     |_|  |_|\__, | |_|   |_|  \___/ \__, |
                             |___/                   |___/

2021-03-23 12:53:44,485 - INFO - main.prog.command1 - Executing command1 with --arg1: WOW
2021-03-23 12:53:44,485 - INFO - main.prog.command1 - --arg2: NOW
```

 3. The ```setup.py``` is configured to install a script called ```prog``` in the users path that will point to the entrypoint of the ```prog.cli:main```

```
    entry_points={
        'console_scripts': [
            'prog = prog.cli:main'
        ]
    }
```

Update this part to suit your program
