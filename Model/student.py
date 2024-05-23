class Student:
    def __init__(self, id, fname, lname, programid):
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

    def __repr__(self):
        return f"Student(id='{self._id}', fname='{self._fname}', lname='{self._lname}', programid='{self._programid}')"
