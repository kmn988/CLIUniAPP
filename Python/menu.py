class UniversityMenu:
    
    @staticmethod
    def display():

        print("\n" + "=" * 40)
        print("University System")
        print("=" * 40)
        print("(A) Admin")
        print("(S) Student")
        print("(X) Exit")
        print("=" * 40)
        choice = input("Select an option: ").strip().upper()
        return choice


class StudentMenu:

    @staticmethod
    def display():

        print("\n" + "=" * 40)
        print("Student System")
        print("=" * 40)
        print("(l) login")
        print("(r) register")
        print("(x) exit")
        print("=" * 40)
        choice = input("Select an option: ").strip().lower()
        return choice


class SubjectEnrolmentMenu:

    @staticmethod
    def display():

        print("\n" + "=" * 40)
        print("Subject Enrolment System")
        print("=" * 40)
        print("(c) change: Change password")
        print("(e) enrol: Enrol in a subject")
        print("(r) remove: Remove a subject")
        print("(s) show: Show enrolled subjects")
        print("(x) exit")
        print("=" * 40)
        choice = input("Select an option: ").strip().lower()
        return choice


class AdminMenu:

    @staticmethod
    def display():

        print("\n" + "=" * 40)
        print("Admin System")
        print("=" * 40)
        print("(c) clear database")
        print("(g) group students")
        print("(p) partition students")
        print("(r) remove student")
        print("(s) show")
        print("(t) statistics")
        print("(x) exit")
        print("=" * 40)
        choice = input("Select an option: ").strip().lower()
        return choice