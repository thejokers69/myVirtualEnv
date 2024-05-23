from Elements.program import Program
from Elements.subject import Subject
from Elements.student import Student
from Elements.grade import Grade
from managers.program_manager import ProgramManager
from managers.student_manager import StudentManager

class CLI:
    def __init__(self, program_manager, student_manager):
        self.program_manager = program_manager
        self.student_manager = student_manager
    
    def run(self):
        pass

    def init_data(self):
        pass

    def add_program(self, program_id, name, description):
        program = Program(program_id, name, description)
        self.program_manager.add_program(program)

    def delete_program(self, program_id):
        return self.program_manager.delete_program(program_id)

    def add_subject(self, subject_id, name, description, vh):
        subject = Subject(subject_id, name, description, vh)
        self.program_manager.add_subject(subject)

    def add_subject_to_program(self, program_id, subject_id):
        return self.program_manager.add_subject_to_program(program_id, subject_id)

    def delete_subject(self, subject_id):
        return self.program_manager.delete_subject(subject_id)

    def remove_subject_from_program(self, program_id, subject_id):
        return self.program_manager.remove_subject_from_program(program_id, subject_id)

    def get_all_programs(self):
        return self.program_manager.get_all_programs()

    def get_all_subjects(self):
        return self.program_manager.get_all_subjects()

    def add_student(self, student_id, fname, lname, program_id):
        student = Student(student_id, fname, lname, program_id)
        self.student_manager.add_student(student)

    def delete_student(self, student_id):
        return self.student_manager.delete_student(student_id)

    def get_students_in_program(self, program_id):
        return self.student_manager.get_students_in_program(program_id)

    def add_grade(self, cc, ef, student_id, subject_id):
        return self.student_manager.add_grade(cc, ef, student_id, subject_id)

    def delete_grade(self, student_id, subject_id):
        return self.student_manager.delete_grade(student_id, subject_id)

    def get_grade_of_student(self, student_id, subject_id):
        return self.student_manager.get_grade_of_student(student_id, subject_id)

    def get_all_grades_of_student(self, student_id):
        return self.student_manager.get_all_grades_of_student(student_id)
