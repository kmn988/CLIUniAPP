import pickle
import os


class Database:
    """Database class for managing student data persistence"""
    
    FILE_NAME = "students.data"
    
    def __init__(self):
        """Initialize database and create file if it doesn't exist"""
        if not os.path.exists(self.FILE_NAME):
            self.clear()
    
    def save(self, student):
        """
        Save a new student to the database
        
        Args:
            student: Student object to save
        """
        students = self.load_all()
        students.append(student)
        self._write_all(students)
    
    def load_all(self):
        """
        Load all students from database
        
        Returns:
            List of Student objects, empty list if file is empty or doesn't exist
        """
        try:
            with open(self.FILE_NAME, 'rb') as f:
                return pickle.load(f)
        except (EOFError, FileNotFoundError):
            return []
        except Exception as e:
            print(f"Error loading database: {e}")
            return []
    
    def _write_all(self, students):
        """
        Write all students to database file (private method)
        
        Args:
            students: List of Student objects to write
        """
        try:
            with open(self.FILE_NAME, 'wb') as f:
                pickle.dump(students, f)
        except Exception as e:
            print(f"Error writing to database: {e}")
    
    def find_by_email(self, email):
        """
        Find a student by email address
        
        Args:
            email: Email address to search for
            
        Returns:
            Student object if found, None otherwise
        """
        students = self.load_all()
        for student in students:
            if student.email == email:
                return student
        return None
    
    def find_by_id(self, student_id):
        """
        Find a student by ID
        
        Args:
            student_id: Student ID to search for
            
        Returns:
            Student object if found, None otherwise
        """
        students = self.load_all()
        for student in students:
            if student.id == student_id:
                return student
        return None
    
    def update(self, updated_student):
        """
        Update an existing student's data
        
        Args:
            updated_student: Student object with updated data
            
        Returns:
            Boolean indicating success
        """
        students = self.load_all()
        for i, student in enumerate(students):
            if student.id == updated_student.id:
                students[i] = updated_student
                self._write_all(students)
                return True
        return False
    
    def remove(self, student_id):
        """
        Remove a student from database
        
        Args:
            student_id: ID of student to remove
            
        Returns:
            Boolean indicating success
        """
        students = self.load_all()
        for student in students:
            if student.id == student_id:
                students.remove(student)
                self._write_all(students)
                return True
        return False
    
    def clear(self):
        """Clear all data from database"""
        try:
            with open(self.FILE_NAME, 'wb') as f:
                pickle.dump([], f)
        except Exception as e:
            print(f"Error clearing database: {e}")
