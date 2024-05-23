from Elements.grade import Grade

class StudentManager:
    def __init__(self):
        self.students = {} #dict pour stocker les etudiants 
        self.grades = {} # dict pour stocker les notes 

    def add_student(self, student):
        self.students[student.student_id] = student #ajouter un etudiant 

    def delete_student(self, student_id):
        if student_id in self.students: #supprimer un etudiant 
            del self.students[student_id]
            return True
        return False

    def get_students_in_program(self, program_id): #obtenir tous les etudiant sdans un programme specifiquement 
        return [student for student in self.students.values() if student.program_id == program_id]

    def add_grade(self, cc, ef, student_id, subject_id): #ajtouter une note à un etudiant pour une matiere specifiquemenet 
        if student_id in self.students:
            grade = Grade(cc, ef, student_id, subject_id)
            if student_id in self.grades:
                self.grades[student_id].append(grade)
            else:
                self.grades[student_id] = [grade]
            return True
        return False

    def delete_grade(self, student_id, subject_id):
        if student_id in self.grades: # supprimer une note d'un etudiant pour une matiere specifiquement 
            for grade in self.grades[student_id]:
                if grade.subject_id == subject_id:
                    self.grades[student_id].remove(grade)
                    return True
        return False

    def get_grade_of_student(self, student_id, subject_id):
        if student_id in self.grades: # obtenir les notes d'un etudiant speci
            for grade in self.grades[student_id]:
                if grade.subject_id == subject_id:
                    return {"cc": grade.cc, "ef": grade.ef}
        return {}

    def get_all_grades_of_student(self, student_id):
        if student_id in self.grades: #obtenir tous les notes d'un etudaint
            return {grade.subject_id: {"cc": grade.cc, "ef": grade.ef} for grade in self.grades[student_id]}
        return {}