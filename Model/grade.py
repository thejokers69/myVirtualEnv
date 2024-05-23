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
