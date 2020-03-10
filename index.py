import questionary
import cmd
from general import types, messages
from methods.basic import Basic


basic = Basic()
functions = types.functions_arr

class General(cmd.Cmd):

    def do_index(line, *args):
        option = True
        while option != 'exit':
            option = questionary.select("choose: ", choices=functions,).ask()
            method = getattr(basic, option)
            method()

    def do_help(line, *args):
        print(messages.help())

run = General()

if __name__ == '__main__':
    General().cmdloop()