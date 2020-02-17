#!/usr/bin/python3
import cmd
import sys
import json
import subprocess
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to HBNB console.   Type "help" or "?" to list commands.\n'
    prompt = '(hbnb_console)_$ '
    doc_header = "Commands that can help you:\ntype \
\"help <command>\" to know more:"
    undoc_header = "HBNB Comands:"
    ruler = '='
    file = None

    """ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """
    # Commands to HBNB:
    def do_create(self, arg):
        """Create Instances"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show Instances"""
        if len(arg) == 0:
            print("** class name missing **")

        else:
            lis = arg.split(' ')
            if len(lis) == 1:
                if lis[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if lis[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    with open("file.json", "r") as f:
                        data = json.loads(f.read())
                        flag = 0
                        for k, v in data.items():
                            token = k.split('.')
                            if lis[1] == token[1]:
                                obj = BaseModel(**v)
                                print(obj)
                                flag = 1
                    if flag != 1:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy instances"""
        if len(arg) == 0:
            print("** class name missing **")

        else:
            lis = arg.split(' ')
            if len(lis) == 1:
                if lis[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                if lis[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    with open("file.json", "r") as f:
                        data = json.loads(f.read())
                    flag = 0
                    for k, v in data.copy().items():
                        token = k.split('.')
                        if lis[1] == token[1]:
                            flag = 1
                            del data[k]
                    if flag != 1:
                        print("** no instance found **")
                    with open("file.json", "w") as f:
                        f.write(json.dumps(data))
                    f.close()

    def do_all(self, arg):
        """Print all instances"""
        if len(arg) == 0 or arg == "BaseModel":
            with open("file.json", "r") as f:
                data = json.loads(f.read())
            l = []
            for v in data.values():
                obj = BaseModel(**v)
                l.append(str(obj))
            print(l)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        print("All Updated")

    """ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """

    # Basic commands
    last_output = ''

    def do_shell(self, line):
        """ Run a shell command """
        # print("running shell command:", line)
        sub_cmd = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE)
        output = sub_cmd.communicate()[0].decode('utf-8')
        print(output)
        self.last_output = output

    def do_Hello(self, arg):
        print("Hello, welcome to HBNB console")

    def do_prompt(self, line):
        """ Change the interactive prompt """
        self.prompt = line + ': '

    def do_EOF(self, arg):
        print("^D")
        return True

    def do_quit(self, arg):
        sys.exit(1)

    def emptyline(self):
        pass

    do_q = do_quit

    """ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ """
    # Docummented comands
    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Command to close the console")

    def help_q(self):
        print("Shortcut for \"quit\" command\n")

    def help_Hello(self):
        print("Print a welcome message\n")

    def help_emptyline(self):
        print("Do nothing\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
