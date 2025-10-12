import pickle
import os


class Database:
    
    FILE_NAME = "students.data"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            self.clear()
    
    def save(self, student):

        students = self.load_all()
        students.append(student)
        self._write_all(students)
    
    def load_all(self):

        try:
            with open(self.FILE_NAME, 'rb') as f:
                return pickle.load(f)
        except (EOFError, FileNotFoundError):
            return []
        except Exception as e:
            print(f"Error loading database: {e}")
            return []
    
    def _write_all(self, students):

        try:
            with open(self.FILE_NAME, 'wb') as f:
                pickle.dump(students, f)
        except Exception as e:
            print(f"Error writing to database: {e}")
    
    def find_by_email(self, email):

        students = self.load_all()
        for student in students:
            if student.email == email:
                return student
        return None
    
    def find_by_id(self, student_id):

        students = self.load_all()
        for student in students:
            if student.id == student_id:
                return student
        return None
    
    def update(self, updated_student):

        students = self.load_all()
        for i, student in enumerate(students):
            if student.id == updated_student.id:
                students[i] = updated_student
                self._write_all(students)
                return True
        return False
    
    def remove(self, student_id):

        students = self.load_all()
        for student in students:
            if student.id == student_id:
                students.remove(student)
                self._write_all(students)
                return True
        return False
    
    def clear(self):

        try:
            with open(self.FILE_NAME, 'wb') as f:
                pickle.dump([], f)
        except Exception as e:
            print(f"Error clearing database: {e}")
