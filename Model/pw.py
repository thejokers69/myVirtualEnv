import cmd
import os
from controller import Controller

class BasicShell(cmd.Cmd):
   prompt = 'pw> '

   def do_addprog(self, args):
       """ Add New program to the database."""
       name = input('Enter program name : ')
       desc = input('Enter program description : ')
       Controller.addProgram(name=name,description=desc)
  
   def do_editprog(self, args):
       """ Update an existing program giving its id."""
       pass
      
   def do_delprog(self, args):
       """ Delete an existing program giving its id."""
       id = input('Enter program ID : ')
       Controller.deleteProgram(id)

   def do_getprogs(self, args):
       """ Get list of all programs."""
       pass

   def do_getprog(self, args):
       """ Get programs by ID."""
       pass
  
   def do_addstudent(self, args):
       """Add new student to the database."""
       print("addstudent coming soon ...")
  
   def do_editstudent(self, args):
       """ Update an existing student giving its id."""
       print("updatestudent coming soon ...")

   def do_delstudent(self, args):
       """ Delete an existing student giving its id."""
       print("deletestudent coming soon ...")

   def do_getstudents(self, args):
       """ Get list of students by program."""
       pass

   def do_getstudent(self, args):
       """ Get a student by ID."""
       pass

   def do_cls(self, arg):
       """Clear the screen"""
       os.system('cls' if os.name == 'nt' else 'clear')  

   def do_q(self, line):
       """Exit the shell."""
       print("Goodbye!")
       return True

if __name__ == '__main__':
  BasicShell().cmdloop("Welcome to the Basic Shell.")