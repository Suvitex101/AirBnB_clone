#!/usr/bin/python3
"""AirBnB Console"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models import storage


def check_arg(arg):
    check_curly = re.search(r"\{(.*?)\}", arg)
    check_brackests = re.search(r"\[(.*?)\]", arg)
    if check_curly is None:
        if check_brackests is None:
            return [i.strip(",") for i in split(arg)]
        else:
            spt = split(arg[:check_brackests.span()[0]])
            tmp = [i.strip(",") for i in spt]
            tmp.append(check_brackests.group())
            return tmp
    else:
        spt = split(arg[:check_curly.span()[0]])
        tmp = [i.strip(",") for i in spt]
        tmp.append(check_curly.group())
        return tmp


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    prompt = "(hbnb) "
    __my_class = {
        "BaseModel"
    }

    def emptyarg(self):
        """Do nothing on empty arg"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        Usage: create <class>"""
        first_arg = check_arg(arg)
        if len(first_arg) == 0:
            print("** class name missing **")
        elif first_arg[0] not in HBNBCommand.__my_class:
            print("** class doesn't exist **")
        else:
            print(eval(first_arg[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        Usage: show <class> <id> or <class>.show(<id>)
        """
        first_arg = check_arg(arg)
        obj_dict = storage.all()
        if len(first_arg) == 0:
            print("** class name missing **")
        elif first_arg[0] not in HBNBCommand.__my_class:
            print("** class doesn't exist **")
        elif len(first_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(first_arg[0], first_arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            c_name = first_arg[0]
            obj_id = first_arg[1]
            dis_all = c_name + '.' + obj_id
            print(storage.all()[dis_all])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Usage: destroy <class> <id> or <class>.destroy(<id>)"""
        first_arg = check_arg(arg)
        obj_dict = storage.all()
        if len(first_arg) == 0:
            print("** class name missing **")
        elif first_arg[0] not in HBNBCommand.__my_class:
            print("** class doesn't exist **")
        elif len(first_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(first_arg[0], first_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(first_arg[0], first_arg[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the class name
        Usage: all or all <class> or <class>.all()"""
        my_arg = check_arg(arg)
        if len(my_arg) > 0 and my_arg[0] not in HBNBCommand.__my_class:
            print("** class doesn't exist **")
        else:
            e_obj = []
            for obj in storage.all().values():
                if len(my_arg) > 0 and my_arg[0] == obj.__class__.__name__:
                    e_obj.append(obj.__str__())
                elif len(my_arg) == 0:
                    e_obj.append(obj.__str__())
            print(e_obj)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)"""
        first_arg = check_arg(arg)
        obj_dict = storage.all()
        if len(first_arg) == 0:
            print("** class name missing **")
            return False
        if first_arg[0] not in HBNBCommand.__my_class:
            print("** class doesn't exist **")
            return False
        if len(first_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(first_arg[0], first_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(first_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(first_arg) == 3:
            try:
                type(eval(first_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(first_arg) == 4:
            obj = obj_dict["{}.{}".format(first_arg[0], first_arg[1])]
            if first_arg[2] in obj.__class__.__dict__.keys():
                typeval = type(obj.__class__.__dict__[first_arg[2]])
                obj.__dict__[first_arg[2]] = typeval(first_arg[3])
            else:
                obj.__dict__[first_arg[2]] = first_arg[3]
        elif type(eval(first_arg[2])) == dict:
            obj = obj_dict["{}.{}".format(first_arg[0], first_arg[1])]
            for i, a in eval(first_arg[2]).items():
                if (i in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[i]) in {str, int, float}):
                    typeval = type(obj.__class__.__dict__[i])
                    obj.__dict__[i] = typeval(a)
                else:
                    obj.__dict__[i] = a

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
