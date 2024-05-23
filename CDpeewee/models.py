from peewee import *

db = SqliteDatabase('demo.db')

class Program(Model):
   prog_name = CharField(max_length=50)
   prog_description = CharField(max_length=80)
  
   class Meta:
       database = db

db.connect()