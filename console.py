#!/usr/bin/python3
import cmd
import sys
import subprocess


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to HBNB console.   Type "help" or "?" to list commands.\n'
    prompt = '(hbnb_console)_$ '
    doc_header = "Commands that can help you:\ntype \
\"help <command>\" to know more:"
    ruler = '='
    file = None

    # Basic commands
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

    do_q = do_quit

    # Docummented comands
    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Command to close the console")

    def help_q(self):
        print("Shortcut for \"quit\" command\n")

    def help_Hello(self):
        print("Print a welcome message\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
