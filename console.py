#!/usr/bin/python3
""" This module contains the entry point of  command interpreter"""

import cmd
import shlex
import re
import json
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter"""

    prompt = "(hbnb)"
    valid_classes = ["BaseModel", "user"]

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

    def do_create(self, arg):
        """
        It creates a new instance of the BaseModel
        and it saves in the JSON file usage <class.name>
        """
        """split the argument"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            #new_instance = BaseModel() modify this line since code is handling more thanone class
            new_instance = eval(f"{cpmmands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of aninstance
        based on the class name and id
        """

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        elif len(commands) >= 2:  # Added this check
            key = "{}.{}".format(commands[0], commands[1])
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        else:
            print("Insufficient arguments for 'show' command.")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
        name and id (save the change into the JSON file).
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of
        all instances based or not on the class name.
        """
        objects = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
