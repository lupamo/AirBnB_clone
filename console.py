#!/usr/bin/python3
""" This module contains the entry point of  command interpreter"""

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter"""
   
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """The quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Command handles the end of file"""
        print()
        return True
    def emptyline(self):
        """Called when an empty line is entered"""
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
