#!/usr/bin/python3
"""AirBnB Console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        pass

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
