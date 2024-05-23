class Grade:
    def __init__(self, student_id, subject_id, cc, ef):
        self._student_id = student_id
        self._subject_id = subject_id
        self._cc = cc  
        self._ef = ef  


    # Grade's student ID Getter and setter methods
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    # Grade's subject ID Getter and setter methods
    @property
    def subject_id(self):
        return self._subject_id
    
    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value


    # Grade's cc Getter and setter methods
    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        if not 0 <= value <= 20:
            raise ValueError("Continuous assessment grade must be between 0 and 20.")
        self._cc = value


    # Grade's ef Getter and setter methods
    @property
    def ef(self):
        return self._ef

    @ef.setter
    def ef(self, value):
        if not 0 <= value <= 20:
            raise ValueError("Final exam grade must be between 0 and 20.")
        self._ef = value

    def __str__(self):
        return f"Grade[Student ID: {self._student_id}, Subject ID: {self._subject_id}, CC: {self._cc}, EF: {self._ef}]"
