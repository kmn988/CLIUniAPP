import random


class Subject:
    """Subject class representing an enrolled subject"""
    
    def __init__(self):
        """Initialize a new subject with random ID and mark"""
        self.id = self.generate_id()
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()
    
    def generate_id(self):
        """
        Generate a unique 3-digit subject ID
        
        Returns:
            str: 3-digit subject ID with zero-padding
        """
        return f"{random.randint(1, 999):03d}"
    
    def calculate_grade(self):
        """
        Calculate grade based on mark using UTS grading system
        
        Grading scale:
        - mark >= 85: HD (High Distinction)
        - 75 <= mark < 85: D (Distinction)
        - 65 <= mark < 75: C (Credit)
        - 50 <= mark < 65: P (Pass)
        - mark < 50: Z (Fail)
        
        Returns:
            str: Grade letter (HD, D, C, P, or Z)
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