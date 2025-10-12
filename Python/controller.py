import re
from database import Database
from student import Student
from admin import Admin

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
            return False, "Student does not exist"
        
        if student.password != password:
            return False, "Incorrect password"
        
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
        return True, "Password changed successfully"
    
    def show_subjects(self, student):

        return student.subjects


class AdminController:

    def __init__(self):
        self.database = Database()
        self.current_admin = None
    
    def login(self, username, password):

        success, result = Admin.authenticate(username, password)
        if success:
            self.current_admin = result
        return success, result
    
    def show_all_students(self):

        return self.database.load_all()
    
    def group_by_grade(self):

        students = self.database.load_all()
        grouped = {"HD": [], "D": [], "C": [], "P": [], "Z": []}
        
        for student in students:
            if not student.subjects:
                continue
            
            avg_mark = student.get_average_mark()
            if avg_mark >= 85:
                grade = "HD"
            elif avg_mark >= 75:
                grade = "D"
            elif avg_mark >= 65:
                grade = "C"
            elif avg_mark >= 50:
                grade = "P"
            else:
                grade = "Z"
            
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
    
    def get_statistics(self):

        students = self.database.load_all()
        if not students:
            return {
                'total_students': 0,
                'students_with_subjects': 0,
                'average_system_mark': 0,
                'pass_rate': 0
            }
        
        students_with_subjects = [s for s in students if s.subjects]
        passing_students = [s for s in students if s.is_passing()]
        
        total_marks = sum(s.get_average_mark() for s in students_with_subjects)
        avg_mark = total_marks / len(students_with_subjects) if students_with_subjects else 0
        
        return {
            'total_students': len(students),
            'students_with_subjects': len(students_with_subjects),
            'average_system_mark': round(avg_mark, 2),
            'pass_rate': round((len(passing_students) / len(students)) * 100, 2) if students else 0
        }