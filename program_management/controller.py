from models import models

class Controller:
   @classmethod
   def addProgram(cls, **program_data):
       # Add program to the database
       program = Program.create(prog_name='New Program', prog_description='This is a new program')
       return True if program else False