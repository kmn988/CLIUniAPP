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


# ==================== MAIN APPLICATION ====================
