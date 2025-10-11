import random
import re
import pickle
import os
from subject import Subject

class Student:
    def __init__(self, name, email, password):
        self.id = self.generate_id()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
    
    def generate_id(self):
        return f"{random.randint(1, 999999):06d}"
    
    def enroll_subject(self):
        if len(self.subjects) >= 4:
            return False, "Students are allowed to enrol in 4 subjects only"
        subject = Subject()
        self.subjects.append(subject)
        return True, subject
    
    def remove_subject(self, subject_id):
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False
    
    def change_password(self, new_password):
        self.password = new_password
    
    def get_average_mark(self):
        if not self.subjects:
            return 0
        return sum(subject.mark for subject in self.subjects) / len(self.subjects)
    
    def is_passing(self):
        return self.get_average_mark() >= 50
    
    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}, Email: {self.email}"




# ==================== CONTROLLER CLASSES ====================

class StudentController:
    """Handles student registration and login operations"""
    
    EMAIL_PATTERN = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
    PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{4,}[0-9]{3,}$'
    
    def __init__(self):
        self.database = Database()
        self.current_student = None
    
    def validate_email(self, email):
        """Validate email format"""
        return re.match(self.EMAIL_PATTERN, email) is not None
    
    def validate_password(self, password):
        """Validate password format"""
        return re.match(self.PASSWORD_PATTERN, password) is not None
    
    def register(self, name, email, password):
        """Register a new student"""
        # Validate email
        if not self.validate_email(email):
            return False, "Incorrect email format"
        
        # Validate password
        if not self.validate_password(password):
            return False, "Incorrect password format"
        
        # Check if student already exists
        if self.database.find_by_email(email):
            return False, "Student already exists"
        
        # Create and save new student
        student = Student(name, email, password)
        self.database.save(student)
        return True, student
    
    def login(self, email, password):
        """Login an existing student"""
        student = self.database.find_by_email(email)
        
        if not student:
            return False, "Student does not exist"
        
        if student.password != password:
            return False, "Incorrect password"
        
        self.current_student = student
        return True, student


class SubjectController:
    """Handles subject enrollment operations"""
    
    def __init__(self, database):
        self.database = database
    
    def enroll_subject(self, student):
        """Enroll student in a new subject"""
        success, result = student.enroll_subject()
        if success:
            self.database.update(student)
        return success, result
    
    def remove_subject(self, student, subject_id):
        """Remove a subject from student's enrollment"""
        success = student.remove_subject(subject_id)
        if success:
            self.database.update(student)
        return success
    
    def change_password(self, student, new_password):
        """Change student's password"""
        # Validate new password
        if not re.match(StudentController.PASSWORD_PATTERN, new_password):
            return False, "Incorrect password format"
        
        student.change_password(new_password)
        self.database.update(student)
        return True, "Password changed successfully"
    
    def show_subjects(self, student):
        """Return list of enrolled subjects"""
        return student.subjects


class AdminController:
    """Handles admin operations"""
    
    def __init__(self):
        self.database = Database()
    
    def show_all_students(self):
        """Show all students"""
        return self.database.load_all()
    
    def group_by_grade(self):
        """Group students by grade"""
        students = self.database.load_all()
        grouped = {"HD": [], "D": [], "C": [], "P": [], "F": []}
        
        for student in students:
            if not student.subjects:
                continue
            
            # Calculate average grade
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
                grade = "F"
            
            grouped[grade].append(student)
        
        return grouped
    
    def partition_pass_fail(self):
        """Partition students into PASS/FAIL"""
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
        """Remove a student by ID"""
        return self.database.remove(student_id)
    
    def clear_database(self):
        """Clear all student data"""
        self.database.clear()


# ==================== MENU/VIEW CLASSES ====================

class UniversityMenu:
    """Main university system menu"""
    
    @staticmethod
    def display():
        print("\nUniversity System")
        print("(A) Admin")
        print("(S) Student")
        print("(X) Exit")
        choice = input("Select an option: ").strip().upper()
        return choice


class StudentMenu:
    """Student login/register menu"""
    
    @staticmethod
    def display():
        print("\nStudent System")
        print("(l) login")
        print("(r) register")
        print("(x) exit")
        choice = input("Select an option: ").strip().lower()
        return choice


class SubjectEnrolmentMenu:
    """Subject enrollment menu"""
    
    @staticmethod
    def display():
        print("\nSubject Enrolment System")
        print("(c) change: Change password")
        print("(e) enrol: Enrol in a subject")
        print("(r) remove: Remove a subject")
        print("(s) show: Show enrolled subjects")
        print("(x) exit")
        choice = input("Select an option: ").strip().lower()
        return choice


class AdminMenu:
    """Admin system menu"""
    
    @staticmethod
    def display():
        print("\nAdmin System")
        print("(c) clear database")
        print("(g) group students")
        print("(p) partition students")
        print("(r) remove student")
        print("(s) show")
        print("(x) exit")
        choice = input("Select an option: ").strip().lower()
        return choice


# ==================== MAIN APPLICATION ====================

def run_student_system():
    """Run the student subsystem"""
    controller = StudentController()
    
    while True:
        choice = StudentMenu.display()
        
        if choice == 'l':
            # Login
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            
            success, result = controller.login(email, password)
            if success:
                print(f"Welcome {result.name}!")
                run_subject_enrolment_system(result)
            else:
                print(result)
        
        elif choice == 'r':
            # Register
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            
            success, result = controller.register(name, email, password)
            if success:
                print(f"Student registered successfully. ID: {result.id}")
            else:
                print(result)
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def run_subject_enrolment_system(student):
    """Run the subject enrollment subsystem"""
    database = Database()
    controller = SubjectController(database)
    
    while True:
        choice = SubjectEnrolmentMenu.display()
        
        if choice == 'e':
            # Enroll in subject
            success, result = controller.enroll_subject(student)
            if success:
                print(f"Enrolled in subject {result.id}")
                print(f"Current average mark: {student.get_average_mark():.2f}")
            else:
                print(result)
        
        elif choice == 'r':
            # Remove subject
            subject_id = input("Enter subject ID to remove: ").strip()
            success = controller.remove_subject(student, subject_id)
            if success:
                print(f"Subject {subject_id} removed")
            else:
                print("Subject not found")
        
        elif choice == 's':
            # Show subjects
            subjects = controller.show_subjects(student)
            if not subjects:
                print("No subjects enrolled")
            else:
                for subject in subjects:
                    print(subject)
                print(f"Average mark: {student.get_average_mark():.2f}")
        
        elif choice == 'c':
            # Change password
            new_password = input("New password: ").strip()
            success, message = controller.change_password(student, new_password)
            print(message)
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def run_admin_system():
    """Run the admin subsystem"""
    controller = AdminController()
    
    while True:
        choice = AdminMenu.display()
        
        if choice == 's':
            # Show all students
            students = controller.show_all_students()
            if not students:
                print("No students in database")
            else:
                for student in students:
                    print(student)
        
        elif choice == 'g':
            # Group by grade
            grouped = controller.group_by_grade()
            for grade, students in grouped.items():
                if students:
                    print(f"\n{grade} Grade:")
                    for student in students:
                        print(f"  {student}")
        
        elif choice == 'p':
            # Partition PASS/FAIL
            passed, failed = controller.partition_pass_fail()
            print("\nPASS:")
            for student in passed:
                print(f"  {student}")
            print("\nFAIL:")
            for student in failed:
                print(f"  {student}")
        
        elif choice == 'r':
            # Remove student
            student_id = input("Enter student ID to remove: ").strip()
            success = controller.remove_student(student_id)
            if success:
                print(f"Student {student_id} removed")
            else:
                print("Student not found")
        
        elif choice == 'c':
            # Clear database
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == 'y':
                controller.clear_database()
                print("Database cleared")
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def main():
    """Main application entry point"""
    print("Welcome to CLIUniApp")
    
    while True:
        choice = UniversityMenu.display()
        
        if choice == 'A':
            run_admin_system()
        elif choice == 'S':
            run_student_system()
        elif choice == 'X':
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()