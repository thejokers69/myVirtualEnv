from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase('model', user='thejoker', password='sexcigareZ2', host='localhost', port=5443)

class Program(Model):
    """
    Represents a program in the system.
    
    Attributes:
        prog_name (str): The name of the program.
        prog_description (str): The description of the program.
    """
    prog_name = CharField(max_length=50)
    prog_description = CharField(max_length=80)
  
    class Meta:
        database = db

db.create_tables([Program])  # Add this line here

if db.is_closed():
    db.connect()