#!/usr/bin/python3
"""
Entry to the command interpreter
"""

import cmd  
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Hbnb command interpreter. entry point .
    """

    class_dict = {
            "BaseModel": BaseModel
            }
    prompt = "(hbnb) "
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl-D to exit the program"""
        print()
        return True
    
    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, line):
        """create <classname> -> creates an instance of <class> and updates json file"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        else:
            instance = self.class_dict[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objs = storage.all()
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objs = storage.all()
            if key in objs:
                storage.delete(objs[key])
            else:
                print("** no instance found **")
    def do_all(self, line):
        args = line.split()
        list = []
        objs = storage.all()
        if len(args) <  1:
            for val in objs.values():
                list.append(str(val))
                print(list)
        elif args[0] in self.class_dict.keys():
            for key,val in objs.items():
                if args[0] in key:
                    list.append(str(val))
                    print(list)
        else:
            print("** class doesn't exist **")
            return False # why return false here??? and not in the other methods????

if __name__ == "__main__":
    HBNBCommand().cmdloop()1

