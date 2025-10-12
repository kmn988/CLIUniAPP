from controller import StudentController, SubjectController, AdminController
from menu import UniversityMenu, StudentMenu, SubjectEnrolmentMenu, AdminMenu
from database import Database


def run_student_system():
    controller = StudentController()
    
    while True:
        choice = StudentMenu.display()
        
        if choice == 'l':

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

    controller = AdminController()
    
    print("\n=== Admin Login ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    success, result = controller.login(username, password)
    if not success:
        print(result)
        return
    
    print(f"Welcome {result.username}!")
    
    while True:
        choice = AdminMenu.display()
        
        if choice == 's':
            students = controller.show_all_students()
            if not students:
                print("No students in database")
            else:
                print(f"\n{'='*60}")
                print(f"Total Students: {len(students)}")
                print(f"{'='*60}")
                for student in students:
                    print(student)
                    if student.subjects:
                        print(f"  Enrolled subjects: {len(student.subjects)}")
                        print(f"  Average mark: {student.get_average_mark():.2f}")
                        print(f"  Status: {'PASS' if student.is_passing() else 'FAIL'}")
                    else:
                        print(f"  No subjects enrolled")
                    print(f"{'-'*60}")
        
        elif choice == 'g':

            grouped = controller.group_by_grade()
            print(f"\n{'='*60}")
            print("Students Grouped by Grade")
            print(f"{'='*60}")
            for grade, students in grouped.items():
                if students:
                    print(f"\n{grade} Grade ({len(students)} students):")
                    for student in students:
                        print(f"  {student.name} (ID: {student.id}) - Avg: {student.get_average_mark():.2f}")
        
        elif choice == 'p':

            passed, failed = controller.partition_pass_fail()
            print(f"\n{'='*60}")
            print("Students Partitioned by PASS/FAIL")
            print(f"{'='*60}")
            print(f"\nPASS ({len(passed)} students):")
            if passed:
                for student in passed:
                    print(f"  {student.name} (ID: {student.id}) - Avg: {student.get_average_mark():.2f}")
            else:
                print("  No passing students")
            
            print(f"\nFAIL ({len(failed)} students):")
            if failed:
                for student in failed:
                    avg = student.get_average_mark()
                    print(f"  {student.name} (ID: {student.id}) - Avg: {avg:.2f if student.subjects else 0}")
            else:
                print("  No failing students")
        
        elif choice == 'r':

            student_id = input("Enter student ID to remove: ").strip()
            success = controller.remove_student(student_id)
            if success:
                print(f"Student {student_id} removed successfully")
            else:
                print("Student not found")
        
        elif choice == 'c':

            confirm = input("Are you sure you want to clear all data? (y/n): ").strip().lower()
            if confirm == 'y':
                controller.clear_database()
                print("Database cleared successfully")
            else:
                print("Operation cancelled")
        
        elif choice == 't':

            stats = controller.get_statistics()
            print(f"\n{'='*60}")
            print("System Statistics")
            print(f"{'='*60}")
            print(f"Total Students: {stats['total_students']}")
            print(f"Students with Subjects: {stats['students_with_subjects']}")
            print(f"Average System Mark: {stats['average_system_mark']:.2f}")
            print(f"Pass Rate: {stats['pass_rate']:.2f}%")
            print(f"{'='*60}")
        
        elif choice == 'x':
            break
        else:
            print("Invalid option")


def main():

    print("=" * 60)
    print(" " * 20 + "CLIUniApp")
    print("=" * 60)
    
    while True:
        choice = UniversityMenu.display()
        
        if choice == 'A':
            run_admin_system()
        elif choice == 'S':
            run_student_system()
        elif choice == 'X':
            print("\nThank you for using CLIUniApp. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()