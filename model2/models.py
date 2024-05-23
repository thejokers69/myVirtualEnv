from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"  # Customize table name if desired

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    program_id = Column(Integer, ForeignKey("programs.id"))

    program = relationship("Program", backref="students")

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', program_id={self.program_id})"

class Program(Base):
    __tablename__ = "programs"  # Customize table name if desired

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))

    def __repr__(self):
        return f"Program(id={self.id}, name='{self.name}', description='{self.description}')"

engine = create_engine('mysql+pymysql://thejokers:sexcigareZ2@localhost/model')
Base.metadata.create_all(engine)  # This line creates the tables in your database

Session = sessionmaker(bind=engine)
session = Session()

students = session.query(Student).all()
for student in students:
    print(student)

programs = session.query(Program).all()
for program in programs:
    print(program)