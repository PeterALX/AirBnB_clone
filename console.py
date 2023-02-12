#!/usr/bin/python3

import cmd  

class HBNBCommand(cmd.Cmd):
    """
    Hbnb command interpreter. entry point .
    """
    prompt = "(hbnb) "
    def do_quit(self, args):
        """ exit on quit """
        return True

    def do_EOF(self, args):
        """ exit on Ctrl-D"""
        print()
        return True
    
    # def emptyline(self):
    #     pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

