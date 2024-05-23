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
            for key in list(self._grades.keys()):
                if key[0] == studentid:
                    del self._grades[key]
            return True
        return False
    
    def getStduentslnProgramm(self, programid):
        students = []
        for student in self._students.values():
            if student.programid == programid:
                students.append(student)
        return students
    
    def addGrade(self, programid, studentid, subjectid, cc, ef):
        self._grades[(studentid, subjectid)] = Grade(programid, studentid, subjectid, cc, ef)
        return True
    
    def deleteGrade(self, studentid, subjectid):
        if (studentid, subjectid) in self._grades:
            del self._grades[(studentid, subjectid)]
            return True
        return False
    
    def getGradeOfStudent(self, studentid, subjectid):
        if (studentid, subjectid) in self._grades:
            return self._grades[(studentid, subjectid)]
        return None
    
    def getAllGradesOfStudent(self, studentid, subjectid):
        return [grade for grade in self._grades.values() if grade.studentid == studentid]
    
