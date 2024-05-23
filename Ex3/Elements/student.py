class Student:
    def __init__(self, student_id, fname, lname, program_id):
        self.student_id = student_id # utilise une attribut qui est privée 
        self.fname = fname
        self.lname = lname
        self.program_id = program_id

    #Student ID Getters and Setters
    @property
    def student_id(self):
        return self._student_id # retourne l'attribut privé 
    
    @student_id.setter
    def student_id(self, value):
        self._student_id= value # definir la valeur de l'attribut privé
    

    #Student First Name Getters and Setters
    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, value):
        self._fname = value
    

    #Student Last Name Getters and Setters
    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self, value):
        self._lname = value


    #Student ProgramID Getters and Setters
    @property
    def programId(self):
        return self._programId
    
    @programId.setter
    def programId(self, value):
        self._programId = value

    def __str__(self):
        return f"Student[ID: {self.student_id}, Name: {self._fname} {self._lname}, Program ID: {self._programId}]"