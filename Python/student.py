import random
from subject import Subject


class Student:
    """Student class representing a registered student"""
    
    MAX_SUBJECTS = 4
    
    def __init__(self, name, email, password, database=None):
        """
        Initialize a new student
        
        Args:
            name: Student's full name
            email: Student's email
            password: Student's password
            database: Database instance for ID collision checking (optional)
        """
        self.id = self.generate_id(database)
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
    
    def generate_id(self, database=None):
        """
        Generate a unique 6-digit student ID
        
        Args:
            database: Database instance to check for ID collisions
            
        Returns:
            str: 6-digit student ID with zero-padding
        """
        if database:
            # Check for collisions
            while True:
                new_id = f"{random.randint(1, 999999):06d}"
                if not database.find_by_id(new_id):
                    return new_id
        else:
            # Generate without collision checking
            return f"{random.randint(1, 999999):06d}"
    
    def enroll_subject(self):
        """
        Enroll in a new subject
        
        Returns:
            tuple: (success: bool, result: Subject or error message)
        """
        if len(self.subjects) >= self.MAX_SUBJECTS:
            return False, f"Students are allowed to enrol in {self.MAX_SUBJECTS} subjects only"
        
        subject = Subject()
        self.subjects.append(subject)
        return True, subject
    
    def remove_subject(self, subject_id):
        """
        Remove a subject from enrollment list
        
        Args:
            subject_id: ID of subject to remove
            
        Returns:
            bool: True if successful, False if subject not found
        """
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False
    
    def change_password(self, new_password):
        """
        Change student's password
        
        Args:
            new_password: New password
        """
        self.password = new_password
    
    def get_average_mark(self):
        """
        Calculate average mark across all enrolled subjects
        
        Returns:
            float: Average mark, or 0 if no subjects enrolled
        """
        if not self.subjects:
            return 0
        return sum(subject.mark for subject in self.subjects) / len(self.subjects)
    
    def is_passing(self):
        """
        Check if student is passing (average mark >= 50)
        
        Returns:
            bool: True if passing, False otherwise
        """
        return self.get_average_mark() >= 50
    
    def __str__(self):
        """String representation of student"""
        return f"Student ID: {self.id}, Name: {self.name}, Email: {self.email}"
