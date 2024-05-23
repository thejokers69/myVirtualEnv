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
            for key in list(self._programSubjects.keys()):
                if key[0] == programid:
                    del self._programSubjects[key]
            if programid in self._subjectsByPrograms:
                del self._subjectsByPrograms[programid]
            return True
        return False

    def addSubject(self, subject):
        self._subjects[subject.id] = subject
        return True
    def addSubjectToProgram(self, subject, programid):
        if programid in self._subjectsByPrograms:
            self._subjectsByPrograms[programid].append(subject)
        else:
            self._subjectsByPrograms[programid] = [subject]
        self._programSubjects[(programid, subject.id)] = subject
        return True
    def deleteSubject(self, subjectid):
        if subjectid in self._subjects:
            del self._subjects[subjectid]
            for key in list(self._programSubjects.keys()):
                if key[1] == subjectid:
                    del self._programSubjects[key]
            for key in list(self._subjectsByPrograms.keys()):
                if subjectid in self._subjectsByPrograms[key]:
                    self._subjectsByPrograms[key].remove(subjectid)
            return True
        return False
    
    def removeSubjectFromProgram(self, programid, subjectid):
        if (programid, subjectid) in self._programSubjects:
            self._subjectsByPrograms[programid].remove(subjectid)
            del self._programSubjects[(programid, subjectid)]
            return True
        return False
    
    
