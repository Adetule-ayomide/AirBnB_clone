#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """cmd class definition"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
        to the JSON file and prints the id
        Args:
            args: argument
        """
        if not args:
            print("** class name missing **")
        if args in models.classNames:
            new_instance = models.classNames[args]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string repr of an instance based on the
        class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] in models.classNames:
            cls_name, instance_id = args[0], args[1]
            search_instance = f"{cls_name}.{instance_id}"
            if search_instance in models.storage.all():
                print(models.storage.all()[search_instance])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        if args[0] in models.classNames:
            cls_name, instance_id = args[0], args[1]
            search_instance = f"{cls_name}.{instance_id}"
            if search_instance in models.storage.all():
                del models.storage.all()[search_instance]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all String Rep of all instances
        based or not on the class name"""
        if not args or args in models.classNames:
            str_rep = [str(value) for value in models.storage.all().values()]
            print(str_rep)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name
        and id or by adding or updating attribute"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in models.classNames:
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[
                                    key], args[2], args[3].strip('"'))
                            models.storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Method called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
