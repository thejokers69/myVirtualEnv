class Program:
    """
    Represents a program.

    Attributes:
        id (int): The ID of the program.
        name (str): The name of the program.
        description (str): The description of the program.
    """
    

    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description

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

    def __repr__(self):
        return f"Program(id='{self._id}', name='{self._name}', description='{self._description}')"
