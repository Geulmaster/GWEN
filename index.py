from os import getcwdb
import questionary
import cmd
from general import functionsList, messages
from methods.basic import Basic
import methods.hardware as hardware
from Kingfish.Core import logger
import sys

basic = Basic() #Class from basic.py
basic_functions = functionsList.basic_functions_list
hardware_functions = functionsList.hardware_functions_list

class General(cmd.Cmd):

    def do_files(self, *args):
        option = True
        while option != 'exit':
            option = questionary.select("choose: ", choices=basic_functions,).ask()
            method = getattr(basic, option.lower())
            method()

    def do_hardware(self, *args):
        option = True
        while option != exit:
            option = questionary.select("choose: ", choices=hardware_functions,).ask()
            method = getattr(hardware, option.lower())
            method()

    def do_gwen(self, *args):
        logger.info("Starting G.W.E.N") #TODO: Add the personal assistent

    def do_help(self, *args):
        logger.info(messages.help())

    def do_exit(self, *args):
        basic.exit()


run = General(messages.welcome())

if __name__ == '__main__':
    try:
        if sys.argv[1]:
            method = getattr(General(), sys.argv[1])
            method()
    except:
        General().cmdloop()
