class Program:
    def __init__(self, id: str, name: str, description: str):
        self._id = id
        self._name = name
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


class ProgramSubject:
    def __init__(self, programid: str, subjectid: str):
        self._programid = programid
        self._subjectid = subjectid

    @property
    def programid(self):
        return self._programid

    @property
    def subjectid(self):
        return self._subjectid


class Subject:
    def __init__(self, id: str, name: str, description: str, vh: int):
        self._id = id
        self._name = name
        self._description = description
        self._vh = vh

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def vh(self):
        return self._vh


class Student:
    def __init__(self, id: str, fname: str, lname: str, programid: str):
        self._id = id
        self._fname = fname
        self._lname = lname
        self._programid = programid

    @property
    def id(self):
        return self._id

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def programid(self):
        return self._programid


class Grade:
    def __init__(self, cc: float, ef: float, studentid: str, subjectid: str):
        self._cc = cc
        self._ef = ef
        self._studentid = studentid
        self._subjectid = subjectid

    @property
    def cc(self):
        return self._cc

    @property
    def ef(self):
        return self._ef

    @property
    def studentid(self):
        return self._studentid

    @property
    def subjectid(self):
        return self._subjectid


class ProgramManager:
    def __init__(self):
        self._programs = {}
        self._subjects = {}
        self._subjectsByPrograms = {}
        self._programSubjects = {}

    def addProgram(self, program: Program) -> bool:
        pass  # Implement your logic here

    def deleteProgram(self, programid: str) -> bool:
        pass  # Implement your logic here

    def addSubject(self, subject: Subject) -> bool:
        pass  # Implement your logic here

    def addSubjectToProgram(self, programid: str, subjectid: str) -> bool:
        pass  # Implement your logic here

    def deleteSubject(self, subjectid: str) -> bool:
        pass  # Implement your logic here

    def removeSubjectFromProgram(self, programid: str, subjectid: str) -> bool:
        pass  # Implement your logic here


class StudentManager:
    def __init__(self):
        self._students = {}
        self._grades = {}

    def addStudent(self, student: Student) -> bool:
        pass  # Implement your logic here

    def deleteStudent(self, studentid: str) -> bool:
        pass  # Implement your logic here

    def getStudentsInProgram(self, programid: str) -> list:
        pass  # Implement your logic here

    def addGrade(self, studentid: str, subjectid: str, cc: float, ef: float) -> bool:
        pass  # Implement your logic here

    def deleteGrade(self, studentid: str, subjectid: str) -> bool:
        pass  # Implement your logic here

    def getGradeOfStudent(self, studentid: str, subjectid: str) -> dict:
        pass  # Implement your logic here

    def getAllGradesOfStudent(self, studentid: str) -> dict:
        pass  # Implement your logic here