import questionary
import cmd


class General(cmd.Cmd):

    def do_index():
        menu = questionary.select("choose: ", choices=['re','rer'],).ask()


run = General()

if __name__ == '__main__':
    General().cmdloop()   