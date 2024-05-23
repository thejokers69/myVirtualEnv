class Program:
    def __init__(self, id, name, description):
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
    
    @description.setter
    def description(self, value):
        self._description = value

    def __repr__(self):
        return f"Program(id='{self._id}', name='{self._name}', description='{self._description}')"


class Subject:
    def __init__(self, id, name, description, vh):
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
    
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def vh(self):
        return self._vh

    def __repr__(self):
        return f"Subject(id='{self._id}', name='{self._name}', description='{self._description}', vh={self._vh})"
class Student:
    def __init__(self, id, first_name, last_name, programid):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._programid = programid

    @property
    def id(self):
        return self._id
    
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def programid(self):
        return self._programid

    def __repr__(self):
        return f"Student(id='{self._id}', first_name='{self._first_name}', last_name='{self._last_name}', programid='{self._programid}')"

class ProgramSubject:
    def __init__(self, programid, subjectid):
        self._programid = programid
        self._subjectid = subjectid

    @property
    def programid(self):
        return self._programid
    
    @property
    def subjectid(self):
        return self._subjectid

    def __repr__(self):
        return f"ProgramSubject(programid='{self._programid}', subjectid='{self._subjectid}')"


class Grade:
    def __init__(self, cc, ef, studentid, subjectid):
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

    def __repr__(self):
        return f"Grade(cc={self._cc}, ef={self._ef}, studentid='{self._studentid}', subjectid='{self._subjectid}')"


class ProgramManager:
    def __init__(self):
        self._programs = {}
        self._subjects = {}
        self._subjectsByPrograms = {}
        self._programSubjects = {}

    def addProgram(self, program):
        self._programs[program.id] = program
        return True

    def deleteProgram(self, programid):
        if programid in self._programs:
            del self._programs[programid]
            return True
        return False

    def addSubject(self, subject):
        self._subjects[subject.id] = subject
        return True

    def addSubjectToProgram(self, programid, subjectid):
        self._programSubjects[(programid, subjectid)] = ProgramSubject(programid, subjectid)
        if programid not in self._subjectsByPrograms:
            self._subjectsByPrograms[programid] = []
        self._subjectsByPrograms[programid].append(subjectid)
        return True

    def deleteSubject(self, subjectid):
        if subjectid in self._subjects:
            del self._subjects[subjectid]
            for programid, subjects in self._subjectsByPrograms.items():
                if subjectid in subjects:
                    subjects.remove(subjectid)
                    del self._programSubjects[(programid, subjectid)]
            return True
        return False

    def removeSubjectFromProgram(self, programid, subjectid):
        if (programid, subjectid) in self._programSubjects:
            self._subjectsByPrograms[programid].remove(subjectid)
            del self._programSubjects[(programid, subjectid)]
            return True
        return False
    
    def deleteGrade(self, studentid, subjectid):
        if (studentid, subjectid) in self._grades:
            del self._grades[(studentid, subjectid)]
            return True
        return False

    def deleteStudent(self, studentid):
        if studentid in self._students:
            del self._students[studentid]
            # Remove student grades associated with the deleted student
            for key in list(self._grades.keys()):
                if key[0] == studentid:
                    del self._grades[key]
            return True
        return False



class StudentManager:
    def __init__(self):
        self._students = {}
        self._grades = {}

    def addStudent(self, student):
        self._students[student.id] = student
        return True

    def deleteStudent(self, studentid):
        if studentid in self._students:
            del self._students[studentid]
            return True
        return False

    def getStudentsInProgram(self, programid):
        return [student for student in self._students.values() if student.programid == programid]

    def addGrade(self, studentid, subjectid, cc, ef):
        self._grades[(studentid, subjectid)] = Grade(cc, ef, studentid, subjectid)
        return True

    def deleteGrade(self, studentid, subjectid):
        if (studentid, subjectid) in self._grades:
            del self._grades[(studentid, subjectid)]
            return True
        return False

    def getGradeOfStudent(self, studentid, subjectid):
        return self._grades.get((studentid, subjectid), None)

    def getAllGradesOfStudent(self, studentid):
        return {key: value for (key, value) in self._grades.items() if key[0] == studentid}


program1 = Program("1", "Computer Science", "Study of computers and computational systems")
subject1 = Subject("1", "Data Structures", "Study of organizing and managing data", 4)
program_subject = ProgramSubject("1", "1")
student1 = Student("1", "John", "Doe", "1")
grade1 = Grade(90, 85, "1", "1")


program_manager = ProgramManager()
student_manager = StudentManager()

program_manager.addProgram(program1)
program_manager.addSubject(subject1)
program_manager.addSubjectToProgram("1", "1")
student_manager.addStudent(student1)
student_manager.addGrade("1", "1", 90, 85)

print(program_manager._programs)
print(student_manager._students)
print(student_manager._grades)
