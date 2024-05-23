# main.py
from Elements.program import Program
from Elements.subject import Subject
from Elements.student import Student
from Elements.grade import Grade
from managers.program_manager import ProgramManager
from managers.student_manager import StudentManager
from cli import CLI


def initialize_data(program_manager, student_manager):
    # Inittialiser le programme 
    programs_data = {
        "P01": Program("P01", "Program 1", "Description of Program 1"),
        "P02": Program("P02", "Program 2", "Description of Program 2")
    }
    for program in programs_data.values():
        program_manager.add_program(program)

    # Initialiser les matières
    subjects_data = {
        "S01": Subject("S01", "Subject 1", "Description of Subject 1", 3),
        "S02": Subject("S02", "Subject 2", "Description of Subject 2", 4),
        "S03": Subject("S03", "Subject 3", "Description of Subject 3", 5),
        "S04": Subject("S04", "Subject 4", "Description of Subject 4", 4),
        "S05": Subject("S05", "Subject 5", "Description of Subject 5", 3)
    }
    for subject in subjects_data.values():
        program_manager.add_subject(subject)

    # Initialiser les matières par programme 
    subjects_by_programs_data = {
        "P01": ["S01", "S02", "S03"],
        "P02": ["S01", "S04", "S05"]
    }
    for program_id, subject_ids in subjects_by_programs_data.items():
        for subject_id in subject_ids:
            program_manager.add_subject_to_program(program_id, subject_id)

    # Initialiser les etudiants
    students_data = {
        "S001": Student("S001", "John", "Doe", "P01"),
        "S002": Student("S002", "Jane", "Smith", "P01"),
        "S003": Student("S003", "Alice", "Johnson", "P02"),
        "S004": Student("S004", "Bob", "Brown", "P02"),
        "S005": Student("S005", "Eve", "Williams", "P02")
    }
    for student in students_data.values():
        student_manager.add_student(student)

    # Initialiser les notes
    grades_data = {
        "S001": [
            Grade(80.0, 90.0, "S001", "S01"),
            Grade(75.0, 85.0, "S001", "S02"),
            Grade(85.0, 95.0, "S001", "S03")
        ],
        "S002": [
            Grade(70.0, 80.0, "S002", "S01"),
            Grade(65.0, 75.0, "S002", "S02")
        ]
    }
    for student_id, grades_list in grades_data.items():
        for grade in grades_list:
            student_manager.add_grade(grade.cc, grade.ef, student_id, grade.subject_id)

def main():
    program_manager = ProgramManager()
    student_manager = StudentManager()
    initialize_data(program_manager, student_manager)
    
    cli = CLI(program_manager, student_manager)
    cli.run()

if __name__ == "__main__":
    main()