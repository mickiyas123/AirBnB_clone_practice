#!/usr/bin/python3
"""console module that contains the
   entry point of the command interpreter
"""

# Standard Library imports
import cmd

# Local application imports
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ class for command interpreter implimentation """
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "Place": Place, "State": State,
               "Review": Review}

    def do_create(self, input_class):
        """ Method for creating new instance of the input class """
        if input_class:
            if input_class in self.classes:
                new_instance = self.classes[input_class]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, class_and_id):
        """Prints the string representation of
           an instance based on the class name and id
           the changed is saved into the JSON file
        """
        if not class_and_id:
            print("** class name missing **")
        elif len(class_and_id.split()) == 1:
            if class_and_id not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(class_and_id.split()) == 2:
            inputs = class_and_id.split()
            key_to_find = inputs[0] + "." + inputs[1]
            all_obj = storage.all()
            key_list = list(all_obj.keys())
            if key_to_find not in key_list:
                print("** no instance found **")
            else:
                for key in all_obj.keys():
                    if key_to_find == key:
                        print(all_obj[key])

    def do_destroy(self, class_and_id):
        """Deletes an instance
           based on the class name and id
           the changed is saved into the JSON file
        """
        if not class_and_id:
            print("** class name missing **")
        elif len(class_and_id.split()) == 1:
            if class_and_id not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(class_and_id.split()) == 2:
            inputs = class_and_id.split()
            key_to_find = inputs[0] + "." + inputs[1]
            all_objects = storage.all()
            key_list = list(all_objects.keys())
            if key_to_find in key_list:
                del all_objects[key_to_find]
            else:
                print("** no instance found **")
            storage.save()

    def do_all(self, input_class):
        """Prints all string representation of all
           instances based or not on the class name
        """
        list_of_str = []
        all_objects = storage.all()

        if input_class == '':
            for key in all_objects.keys():
                list_of_str.append(str(all_objects[key]))
            print(list_of_str)
        elif input_class in self.classes:
            for key, val in all_objects.items():
                if input_class == type(val).__name__:
                    list_of_str.append(str(all_objects[key]))
            print(list_of_str)
        else:
            print("** class doesn't exist **")

    def do_update(self, input_argument):
        """Updates an instance based on the class name and id by
           adding or updating attribute
           the change  is saved into the JSON file
        """
        if not input_argument:
            print("** class name missing **")
        elif len(input_argument.split()) == 1:
            if input_argument not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(input_argument.split()) == 2:
            inputs = input_argument.split()
            key_to_find = inputs[0] + "." + inputs[1]
            all_objects = storage.all()
            key_list = list(all_objects.keys())
            if key_to_find not in key_list:
                print("** no instance found **")
            else:
                print("** attribute name missing **")

        elif len(input_argument.split()) == 3:
            print("** value missing **")
        else:
            inputs = input_argument.split()
            key_to_find = inputs[0] + "." + inputs[1]
            all_objects = storage.all()
            key_list = list(all_objects.keys())
            inputs[3] = inputs[3][1:-1]
            if key_to_find in key_list:
                setattr(all_objects[key_to_find], inputs[2], inputs[3])
            storage.save()

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
