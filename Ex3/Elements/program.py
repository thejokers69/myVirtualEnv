class Program:
    def __init__(self, program_id, name, description):
        self._id = program_id
        self._name = name
        self._description = description


    # Program ID Getter and Setter
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value


    # Program Name Getter and Setter
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


    # Program Description Getter and Setter
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value

    def __str__(self):
        return f"Program[ID: {self._id}, Name: {self._name}, Description: {self._description}]"
