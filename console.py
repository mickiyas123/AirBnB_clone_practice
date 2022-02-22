#!/usr/bin/python3
"""console module that contains the
   entry point of the command interpreter
"""

# Standard Library imports
import cmd


class HBNBCommand(cmd.Cmd):
    """ class for command interpreter implimentation """
    prompt = '(hbnb) '

    def emptyline(self):
        """ Quit command to exit the program """
        pass

    def do_quit(self, inputs):
        """ a method to quit """
        quit()

    def do_EOF(self, inputs):
        """ method for exit """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
