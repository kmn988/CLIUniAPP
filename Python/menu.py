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