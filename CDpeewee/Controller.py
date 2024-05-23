from models import Program

class Controller:
   @classmethod
   def addProgram(cls, **program_data):
       # Add program to the database
       program = Program.create(**program_data)
       return True if program else False