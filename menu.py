class UniversityMenu:
    """Display main university system menu"""
    @staticmethod
    def display():

 
        print("A - Admin System")
        print("S - Student System") 
        print("X - Exit")
        print("\nChoose one: ", end="")
        choice = input().strip().upper()
        return choice


class StudentMenu:

    @staticmethod
    def display():

        print("\n--- Student System ---")
        print("L - Login")
        print("R - Register")
        print("X - Back to University menu")
        print("\nChoose one: ", end="")
        choice = input().strip().lower()
        return choice


class SubjectEnrolmentMenu:

    @staticmethod
    def display():

        print("\n--- Subject Enrolment System ---")
        print("C - Change password")
        print("E - Enroll in subject")
        print("R - Remove a subject")
        print("S - Show enrolled subjects")
        print("X - Logout")
        print("\nChoose one: ", end="")
        choice = input().strip().lower()
        return choice


class AdminMenu:

    @staticmethod
    def display():

        print("\n--- Admin System ---")
        print("C - Clear database")
        print("G - Group students by grade")
        print("P - Partition students (Pass/Fail)")
        print("R - Remove student by ID")
        print("S - Show all students")
        print("X - Back to University menu")
        print("\nChoose one: ", end="")
        choice = input().strip().lower()
        return choice
