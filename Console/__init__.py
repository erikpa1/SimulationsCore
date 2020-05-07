import builtins

console_end = '\033[0m'
console_red = '\033[91m'
console_blue = '\033[94m'
console_warning = '\u001b[35m'


def print_err(self, *args):
    print(console_red)
    print(self, *args)
    print(console_end)


def print_warn(self, *args):
    print(console_warning)
    print(self, *args)
    print(console_end)


def print_debug(self, *args):
    print(console_blue)
    print(self, *args)
    print(console_end)


def print_info(self, *args):
    print(self, *args)

def expand_console_to_builtins():
    builtins.print_err = print_err
    builtins.print_warn = print_warn
    builtins.print_debug = print_debug
    builtins.print_info = print_info
    pass

