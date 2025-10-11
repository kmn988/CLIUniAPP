from student import Student
import pickle
import os

class Database: 
    FILE_NAME = "students.data"
    
    def __init__(self):
        """Initialize database and create file if it doesn't exist"""
        if not os.path.exists(self.FILE_NAME):
            self.clear()
    
    def save(self, student):
        """Save a student to the database"""
        students = self.load_all()
        students.append(student)
        self._write_all(students)
    
    def load_all(self):
        """Load all students from the database"""
        try:
            with open(self.FILE_NAME, 'rb') as f:
                return pickle.load(f)
        except (EOFError, FileNotFoundError):
            return []
    
    def _write_all(self, students):
        """Write all students to the database"""
        with open(self.FILE_NAME, 'wb') as f:
            pickle.dump(students, f)
    
    def find_by_email(self, email):
        """Find a student by email"""
        students = self.load_all()
        for student in students:
            if student.email == email:
                return student
        return None
    
    def find_by_id(self, student_id):
        """Find a student by ID"""
        students = self.load_all()
        for student in students:
            if student.id == student_id:
                return student
        return None
    
    def update(self, updated_student):
        """Update a student's information"""
        students = self.load_all()
        for i, student in enumerate(students):
            if student.id == updated_student.id:
                students[i] = updated_student
                self._write_all(students)
                return True
        return False
    
    def remove(self, student_id):
        """Remove a student by ID"""
        students = self.load_all()
        for student in students:
            if student.id == student_id:
                students.remove(student)
                self._write_all(students)
                return True
        return False
    
    def clear(self):
        """Clear all students from the database"""
        with open(self.FILE_NAME, 'wb') as f:
            pickle.dump([], f)
