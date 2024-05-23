class Subject:
    def __init__(self, subject_id, name, description, vh):
        self._id = subject_id
        self._name = name
        self._description = description
        self._vh = vh

    # Subject Id Getter and Setter
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value


    # Subject Name Getter and Setter
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


    # Subject Description Getter and Setter
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value


    # Subject Hourly volume Getter and Setter
    @property
    def vh(self):
        return self._vh
    
    @vh.setter
    def vh(self, value):
        # Verifying if the value is positive
        if value < 0:
            raise ValueError("Volume hours must be a positive number.")
        self._vh = value

    def __str__(self):
        return f"Subject[ID: {self._id}, Name: {self._name}, Description: {self._description}, VH: {self._vh}]"
