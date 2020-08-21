import questionary
import cmd
from general import functionsList, messages
from methods.basic import Basic
from Kingfish.Core import logger


basic = Basic() #Class from basic.py
functions = functionsList.basic_functions_list

class General(cmd.Cmd):

    def do_files(self, *args):
        option = True
        while option != 'exit':
            option = questionary.select("choose: ", choices=functions,).ask()
            method = getattr(basic, option)
            method()

    def do_gwen(self, *args):
        logger.info("Starting G.W.E.N") #TODO: Add the personal assistent

    def do_help(self, *args):
        logger.info(messages.help())

    def do_exit(self, *args):
        basic.exit()


run = General(messages.welcome())

if __name__ == '__main__':
    General().cmdloop()