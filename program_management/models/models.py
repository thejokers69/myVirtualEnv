from peewee import *

# Define database connection parameters
database = MySQLDatabase('my_database', user='thejokers', password='sexcigareZ2', host='localhost', port=3306)

# Define Program model
class Program(Model):
    id = PrimaryKeyField(null=False)
    prog_name = CharField()
    prog_description = TextField()

    class Meta:
        database = database

# Define Student model
class Student(Model):
    id = PrimaryKeyField(null=False)
    std_fname = CharField()
    std_lname = CharField()
    prog_id = ForeignKeyField(Program, backref='students')

    class Meta:
        database = database

# Create tables
database.create_tables([Program, Student])

# Create a new program
program = Program.create(prog_name='New Program', prog_description='This is a new program')

# Create a new student
student = Student.create(std_fname='Ahmed', std_lname='Amine', prog_id=program)

# Read a record
student = Student.get(Student.id == 1)

# Update a record
student.std_fname = 'Updated Name'
student.save()

# Delete a record
student.delete_instance()

# Querying data
students_in_program = Student.select().where(Student.prog_id == program)