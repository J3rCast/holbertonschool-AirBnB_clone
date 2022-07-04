#!/usr/bin/env python3
""" AirBnB Console """

import sys
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb) '
    __all_count = 0

    def emptyline(self):
        """Pass if no command is given"""
        pass

    def precmd(self, line):
        """ Edit given command to allow second type of input"""
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            HBNBCommand.__all_count = 1
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            cmd_argv = line.split()
            cmd_argv[0], cmd_argv[1] = cmd_argv[1], cmd_argv[0]
            line = " ".join(cmd_argv)
        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, arg):
        'Create an instance if the Model exists'
        if not arg:
            print('** class name missing **')
            return None
        try:
            my_model = eval(arg + '()')
            my_model.save()
            print(my_model.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "Print dict of a instance in base of it's ID"
        cmd_argv = arg.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return None

        cmd_argv[1] = cmd_argv[1].replace("\"", "")
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        "Deletes an instance based on it's ID and save the changes\n\
        Usage: destroy <class name> <id>"

        cmd_argv = arg.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()
        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return None

        cmd_argv[1] = cmd_argv[1].replace("\"", "")
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, arg):
        "Print all the instances saved in file.json"
        cmd_argv = arg.split()

        if cmd_argv:
            try:
                eval(cmd_argv[0])
            except:
                print("** class doesn't exist **")
                return None

        all_objs = storage.all()
        print_list = []
        len_objs = len(all_objs)
        for key, value in all_objs.items():
            if not cmd_argv:
                if HBNBCommand.__all_count == 0:
                    print_list.append("\"" + str(value) + "\"")
                else:
                    print_list.append(str(value))
            else:
                check = key.split('.')
                if cmd_argv[0] == check[0]:
                    if HBNBCommand.__all_count == 0:
                        print_list.append("\"" + str(value) + "\"")
                    else:
                        print_list.append(str(value))
        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
