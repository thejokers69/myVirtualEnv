from peewee import *

db = SqliteDatabase('example.db')

class Program(Model):
   id = CharField(primary_key=True, max_length=36)
   name = CharField()
   description = TextField()

   class Meta:
       database = db
       table_name = 'program'

class Student(Model):
   id = CharField(primary_key=True, max_length=36)
   fname = CharField()
   lname = CharField()
   program = ForeignKeyField(Program, backref='students')

   class Meta:
       database = db
       table_name = 'student'

db.connect()
db.create_tables([Program, Student])

db.close()
