#!/usr/bin/python3
"""
This is the console.It is the entry point into this program
The console allows a user to interact with the database
    from the command line.
    viewing, creating, deleting, etc models
"""

from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import re

classes = {"BaseModel": BaseModel, 'User': User}


def parse_string(string):
    # regular expression to match words within quotes and words without quotes
    pattern = r'"([^"]*)"|(\S+)'
    # Find all matches in the string
    matches = re.findall(pattern, string)
    # Concatenate the non-empty groups from the matches
    result = [match[0] or match[1] for match in matches]
    return result


# ensure excess args result in error?
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

    def do_destroy(self, arg):
        """
        Command: destroy

        Description:
        Deletes an instance based on the class name and id
        (saves the change into the JSON file)

        Usage:
        destroy <model_name> <id>
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
            del models[f'{args[0]}.{args[1]}']
            storage.save()

    def do_all(self, arg):
        """
        Command: all

        Description:
        Prints all string representations of all instances of  <model_name>
        if no model name is provided, prints all instances

        Usage:
        all [<model_name>]
        """
        if not arg:
            models = storage.all()
            st = [value.__str__() for value in models.values()]
            print(st)
        elif arg in classes:
            models = storage.all()
            st = [value.__str__() for value in models.values()
                  if value.__class__.__name__ == arg]
            print(st)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Command: update

        Description:
        Updates an instance based on the model name and id
        by adding or updating attribute

        Usage:
        update <model_name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print('** class name missing **')
            return
        args = parse_string(arg)
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        models = storage.all()
        if f'{args[0]}.{args[1]}' not in models:
            print('** no instance found **')
            return
        instance = models[f'{args[0]}.{args[1]}']
        if (len(args) < 3):
            print('** attribute name missing **')
            return
        if (len(args) < 4):
            print('** value missing **')
            return
        setattr(instance, args[2], args[3])
        instance.save()

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
