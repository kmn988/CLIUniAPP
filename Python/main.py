def run_student_system():
    """Run the student subsystem"""
    controller = StudentController()
    
    while True:
        choice = StudentMenu.display()
        
        if choice == 'l':
            # Login
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            
            success, result = controller.login(email, password)
            if success:
                print(f"Welcome {result.name}!")
                run_subject_enrolment_system(result)
            else:
                print(result)
        
        elif choice == 'r':
            # Register
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            
            success, result = controller.register(name, email, password)
            if success:
                print(f"Student registered successfully. ID: {result.id}")
            else:
                print(result)
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def run_subject_enrolment_system(student):
    """Run the subject enrollment subsystem"""
    database = Database()
    controller = SubjectController(database)
    
    while True:
        choice = SubjectEnrolmentMenu.display()
        
        if choice == 'e':
            # Enroll in subject
            success, result = controller.enroll_subject(student)
            if success:
                print(f"Enrolled in subject {result.id}")
                print(f"Current average mark: {student.get_average_mark():.2f}")
            else:
                print(result)
        
        elif choice == 'r':
            # Remove subject
            subject_id = input("Enter subject ID to remove: ").strip()
            success = controller.remove_subject(student, subject_id)
            if success:
                print(f"Subject {subject_id} removed")
            else:
                print("Subject not found")
        
        elif choice == 's':
            # Show subjects
            subjects = controller.show_subjects(student)
            if not subjects:
                print("No subjects enrolled")
            else:
                for subject in subjects:
                    print(subject)
                print(f"Average mark: {student.get_average_mark():.2f}")
        
        elif choice == 'c':
            # Change password
            new_password = input("New password: ").strip()
            success, message = controller.change_password(student, new_password)
            print(message)
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def run_admin_system():
    """Run the admin subsystem"""
    controller = AdminController()
    
    while True:
        choice = AdminMenu.display()
        
        if choice == 's':
            # Show all students
            students = controller.show_all_students()
            if not students:
                print("No students in database")
            else:
                for student in students:
                    print(student)
        
        elif choice == 'g':
            # Group by grade
            grouped = controller.group_by_grade()
            for grade, students in grouped.items():
                if students:
                    print(f"\n{grade} Grade:")
                    for student in students:
                        print(f"  {student}")
        
        elif choice == 'p':
            # Partition PASS/FAIL
            passed, failed = controller.partition_pass_fail()
            print("\nPASS:")
            for student in passed:
                print(f"  {student}")
            print("\nFAIL:")
            for student in failed:
                print(f"  {student}")
        
        elif choice == 'r':
            # Remove student
            student_id = input("Enter student ID to remove: ").strip()
            success = controller.remove_student(student_id)
            if success:
                print(f"Student {student_id} removed")
            else:
                print("Student not found")
        
        elif choice == 'c':
            # Clear database
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == 'y':
                controller.clear_database()
                print("Database cleared")
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def main():
    """Main application entry point"""
    print("Welcome to CLIUniApp")
    
    while True:
        choice = UniversityMenu.display()
        
        if choice == 'A':
            run_admin_system()
        elif choice == 'S':
            run_student_system()
        elif choice == 'X':
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()