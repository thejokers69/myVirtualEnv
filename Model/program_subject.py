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
