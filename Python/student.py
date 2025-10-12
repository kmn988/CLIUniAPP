import random
from subject import Subject


class Student:
    
    MAX_SUBJECTS = 4
    
    def __init__(self, name, email, password, database=None):

        self.id = self.generate_id(database)
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
    
    def generate_id(self, database=None):

        if database:

            while True:
                new_id = f"{random.randint(1, 999999):06d}"
                if not database.find_by_id(new_id):
                    return new_id
        else:

            return f"{random.randint(1, 999999):06d}"
    
    def enroll_subject(self):

        if len(self.subjects) >= self.MAX_SUBJECTS:
            return False, f"Students are allowed to enrol in {self.MAX_SUBJECTS} subjects only"
        
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
