class ProgramSubject:
    def __init__(self, program_id, subject_id):
        self.program_id = program_id  # Setters are called here for initial validation
        self.subject_id = subject_id

    # Programsubject's programID Getter and Setter
    @property
    def program_id(self):
        return self._program_id

    @program_id.setter
    def program_id(self, value):
        # isinstance() garantit que la valeur passée est bien une chaîne de caractères
        # strip() est utilisé pour s'assurer que l'ID n'est pas juste une chaîne de caractères vide ou composée uniquement d'espaces
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Program ID must be a non-empty string.")
        self._program_id = value

    # Programsubject's subjectID Getter and Setter
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        # la meme chose ici 
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Subject ID must be a non-empty string.")
        self._subject_id = value

    def __str__(self):
        return f"ProgramSubject[Program ID: {self._program_id}, Subject ID: {self._subject_id}]"
