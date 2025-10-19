import random


class Subject:
    """Model class representing a university subject"""
    
    def __init__(self):
        """
        Initialize a new subject with random ID, mark, and calculated grade
        """
        self.id = self.generate_id()
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()
    
    def generate_id(self):
        """
        Generate a unique 3-digit subject ID
        
        Returns:
            String representation of 3-digit ID (001 to 999)
        """
        return f"{random.randint(1, 999):03d}"
    
    def calculate_grade(self):
        """
        Calculate grade based on mark using UTS grading system
        
        Returns:
            Grade string (HD/D/C/P/Z)
        """
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"
    
    def __str__(self):
        """String representation of subject"""
        return f"Subject ID: {self.id}, Mark: {self.mark}, Grade: {self.grade}"
