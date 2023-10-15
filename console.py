#!/usr/bin/python3
"""This module is a simple console that
handles EOF and exit"""


import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """This is the class for the cmd module"""
    prompt = "(hbnb) "
    __classes = ["BaseModel",
                 "User",
                 "Place",
                 "City", "State", "Review", "Amenity"]

    def do_quit(self, line):
        """This method exits the cmd line"""
        return True

    def do_EOF(self, line):
        """This method exits the cmd line"""
        return True

    def do_create(self, line):
        """This method creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return False
        try:
            cls = line.split()[0]
            new_instance = eval(cls)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """This prints the str format of the created object"""
        if not line:
            print("** class name missing **")
            return False
        args = line.split()
        cls = args[0]
        if cls not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        inst_id = args[1]
        storage.reload()
        try:
            instance = storage.all()[f"{cls}.{inst_id}"]
            if instance:
                print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """This method deletes an instance of BaseModel"""
        if not line:
            print('** class name missing **')
            return False
        args = line.split()
        cls = args[0]
        if cls not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        inst_id = args[1]
        storage.reload()
        try:
            instance = storage.all()[f"{cls}.{inst_id}"]
            if instance:
                del storage.all()[f"{cls}.{inst_id}"]
                storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """This method prints all instances based on or not on classname"""
        storage.reload()
        objects = storage.all()

        if not line:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = line.split()[0]
                if cls not in HBNBCommand.__classes:
                    print("** class doesn't exist **")
                    return False
                print([str(obj) for key, obj in objects.items() if cls in key])
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, line):
        """This method updates one instance at a time"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return False
        cls = args[0]
        storage.reload()
        if cls not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        inst_id = args[1]
        try:
            instance = storage.all()[f"{cls}.{inst_id}"]
            if not instance:
                print("** no instance found **")
                return False
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                    return False
                else:
                    if len(args) < 4:
                        print("** value missing **")
                        return False
                    else:
                        key = args[2]
                        value = args[3]
                        setattr(instance, key, value)
                        instance.save()
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        """This does nothing"""
        pass

    def precmd(self, line):
        """This method handles what happens before a command is run"""
        if not sys.stdin.isatty() and line != 'EOF':
            print()
        else:
            pass
        return line

    def postloop(self):
        """This method handles what happens before a command is run"""
        if not sys.stdin.isatty():
            print()
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
