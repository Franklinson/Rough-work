#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Thi is my first console"""

    prompt = ("hbnb: ")

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
