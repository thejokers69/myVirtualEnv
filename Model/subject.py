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
