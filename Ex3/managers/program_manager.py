class ProgramManager:

    def __init__(self):
        self._programs = {}
        self._subjects = {}
        self._subjects_by_program = {}

    def init_data(self):
        pass

    # Ajouter un nouveau programme.
    def add_program(self, program):
        if program.id in self._programs:
            raise ValueError(f"Program with ID {program.id} already exists.") # return false
        self._programs[program.id] = program
        self._subjects_by_program[program.id] = []
        return True

    # Supprimer un programme existant.
    def delete_program(self, program_id):
        if program_id not in self._programs:
            return False
        del self._programs[program_id]
        del self._subjects_by_program[program_id]
        return True

    # Ajouter un nouveau sujet.
    def add_subject(self, subject):
        if subject.id in self._subjects:
            raise ValueError(f"Subject with ID {subject.id} already exists.") #return false
        self._subjects[subject.id] = subject
        return True

    # Associer un sujet à un programme.
    def add_subject_to_program(self, program_id, subject_id):
        if program_id not in self._programs:
            raise ValueError(f"Program with ID {program_id} does not exist.")
        if subject_id not in self._subjects:
            raise ValueError(f"Subject with ID {subject_id} does not exist.")
        
        self._subjects_by_program[program_id].append(subject_id)
        return True

    # Supprimer un sujet existant.
    def delete_subject(self, subject_id):
        if subject_id not in self._subjects:
            return False
        del self._subjects[subject_id]

        for program_id in self._subjects_by_program:
            if subject_id in self._subjects_by_program[program_id]:
                self._subjects_by_program[program_id].remove(subject_id)
        return True

    # Retirer un sujet d'un programme.
    def remove_subject_from_program(self, program_id, subject_id):
        if program_id not in self._subjects_by_program:
            raise ValueError(f"Program with ID {program_id} does not exist.")
        if subject_id not in self._subjects_by_program[program_id]:
            raise ValueError(f"Subject with ID {subject_id} is not associated with program ID {program_id}.")
        
        self._subjects_by_program[program_id].remove(subject_id)
        return True
