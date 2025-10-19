import re
from database import Database
from student import Student


class StudentController:

    EMAIL_PATTERN = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
    PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$'

    def __init__(self):
        self.database = Database()
        self.current_student = None
    
    def validate_email(self, email):

        return re.match(self.EMAIL_PATTERN, email) is not None
    
    def validate_password(self, password):

        return re.match(self.PASSWORD_PATTERN, password) is not None
    
    def register(self, name, email, password):

        if not name or not name.strip():
            return False, "Name cannot be empty"
        
        if not self.validate_email(email):
            return False, "Incorrect email format"
        
        if not self.validate_password(password):
            return False, "Incorrect password format"
        
        if self.database.find_by_email(email):
            return False, "Student already exists"

        student = Student(name, email, password, self.database)
        self.database.save(student)
        return True, student
    
    def login(self, email, password):

        student = self.database.find_by_email(email)
        
        if not student:
            return False, "Student does not exist, return to Student Menu."
        
        if student.password != password:
            return False, "Incorrect password, return to Student Menu."
        
        self.current_student = student
        return True, student


class SubjectController:
    
    def __init__(self, database):
        self.database = database
    
    def enroll_subject(self, student):

        success, result = student.enroll_subject()
        if success:
            self.database.update(student)
        return success, result
    
    def remove_subject(self, student, subject_id):

        success = student.remove_subject(subject_id)
        if success:
            self.database.update(student)
        return success
    
    def change_password(self, student, new_password):

        if not re.match(StudentController.PASSWORD_PATTERN, new_password):
            return False, "Incorrect password format"
        
        student.change_password(new_password)
        self.database.update(student)
        return True, "Password updated successfully"
    
    def show_subjects(self, student):

        return student.subjects


class AdminController:

    def __init__(self):
        self.database = Database()
    
    def show_all_students(self):

        return self.database.load_all()
    
    def group_by_grade(self):

        students = self.database.load_all()
        grouped = {"HD": [], "D": [], "C": [], "P": [], "Z": []}
        
        for student in students:
            if not student.subjects:
                continue
            
            grade = student.get_grade()
            grouped[grade].append(student)
        
        return grouped
    
    def partition_pass_fail(self):

        students = self.database.load_all()
        passed = []
        failed = []
        
        for student in students:
            if student.is_passing():
                passed.append(student)
            else:
                failed.append(student)
        
        return passed, failed
    
    def remove_student(self, student_id):

        return self.database.remove(student_id)
    
    def clear_database(self):

        self.database.clear()
