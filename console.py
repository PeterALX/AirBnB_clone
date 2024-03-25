#!/usr/bin/python3
"""
This is the console.It is the entry point into this program
The console allows a user to interact with the database
    from the command line.
    viewing, creating, deleting, etc models
"""

from cmd import Cmd
from models.base_model import BaseModel
from models import storage

classes = {"BaseModel": BaseModel}


class HBNBCommand(Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Command: create

        Description:
        Create a new model and store it in the storage system.

        Usage:
        create <model_name>
        """
        if not arg:
            print('** class name missing **')
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            model = classes[arg]()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """
        Command: show

        Description:
        Prints the string representation of an instance based on the class name
        and id

        Usage:
        show <model_name> <id>
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        models = storage.all()
        if f'{args[0]}.{args[1]}' not in models:
            print('** no instance found **')
        else:
            print(models[f'{args[0]}.{args[1]}'])

    def do_quit(self, arg):
        """quit command exits the program"""
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
