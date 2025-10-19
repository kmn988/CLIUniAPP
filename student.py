import random
from subject import Subject


class Student:
    """Model class representing a student in the university system"""
    
    MAX_SUBJECTS = 4
    
    def __init__(self, name, email, password, database=None):

        self.id = self.generate_id(database)
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
    
    def generate_id(self, database=None):
        """
        Generate a unique 6-digit student ID
        
        Args:
            database: Database instance to check for ID uniqueness
            
        Returns:
            String representation of 6-digit ID (000001 to 999999)
        """
        if database:
            # Check for uniqueness in database
            while True:
                new_id = f"{random.randint(1, 999999):06d}"
                if not database.find_by_id(new_id):
                    return new_id
        else:
            # No database check
            return f"{random.randint(1, 999999):06d}"
    
    def enroll_subject(self):
        """
        Enroll student in a new subject
        
        Returns:
            Tuple (success, result): 
                - If successful: (True, Subject object)
                - If failed: (False, error message)
        """
        if len(self.subjects) >= self.MAX_SUBJECTS:
            return False, f"Students are allowed to enrol in {self.MAX_SUBJECTS} subjects only"
        
        subject = Subject()
        self.subjects.append(subject)
        return True, subject
    
    def remove_subject(self, subject_id):
        """
        Remove a subject from student's enrollment
        
        Args:
            subject_id: ID of subject to remove
            
        Returns:
            Boolean indicating success
        """
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False
    
    def change_password(self, new_password):
        """
        Update student's password
        
        Args:
            new_password: New password (should be validated before calling)
        """
        self.password = new_password
    
    def get_average_mark(self):
        """
        Calculate average mark across all enrolled subjects
        
        Returns:
            Float representing average mark, or 0 if no subjects enrolled
        """
        if not self.subjects:
            return 0.0
        return sum(subject.mark for subject in self.subjects) / len(self.subjects)
    
    def is_passing(self):
        """
        Determine if student is passing (average >= 50)
        
        Returns:
            Boolean indicating pass/fail status
        """
        if not self.subjects:
            return False
        return self.get_average_mark() >= 50
    
    def get_grade(self):
        """
        Get overall grade based on average mark
        
        Returns:
            Grade string (HD/D/C/P/Z)
        """
        if not self.subjects:
            return "N/A"
        
        avg = self.get_average_mark()
        if avg >= 85:
            return "HD"
        elif avg >= 75:
            return "D"
        elif avg >= 65:
            return "C"
        elif avg >= 50:
            return "P"
        else:
            return "Z"
    
    def __str__(self):
        """String representation of student"""
        return f"Student ID: {self.id}, Name: {self.name}, Email: {self.email}"
