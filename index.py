import questionary
import cmd
from general import functionsList, messages
from methods.basic import Basic


basic = Basic() #Class from basic.py
functions = functionsList.basic_functions_list

class General(cmd.Cmd):

    def do_basic(self, *args):
        option = True
        while option != 'exit':
            option = questionary.select("choose: ", choices=functions,).ask()
            method = getattr(basic, option)
            method()

    def do_help(self, *args):
        print(messages.help())

    def do_exit(self, *args):
        basic.exit()


run = General(messages.welcome())

if __name__ == '__main__':
    General().cmdloop()