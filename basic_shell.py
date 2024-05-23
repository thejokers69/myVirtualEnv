import cmd

class BasicShell(cmd.Cmd):
    prompt = '>>> '  # Sets the command prompt to '>>> '

    def do_sayhelloTo(self, name):
        """Greet the user in English."""
        print("Hello,", name)

    def do_disbonjourA(self, name):
        """Greet the user in French."""
        print("Bonjour,", name)

    def do_quit(self, line):
        """Exit the shell."""
        print("Goodbye!")
        return True

if __name__ == '__main__':
    BasicShell().cmdloop("Welcome to the Basic Shell.")
