from models import CMDUI


def main():

    while True:
        print("\nUniSage - University Management System Menu:")
        print("1. Create Course")
        print("2. Edit Course")
        print("3. Display Course")
        print("4. Add Student to Course")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            instructor_id = input("Enter instructor ID: ")
            prerequisites = input("Enter prerequisites (comma-separated): ").split(",")
            CMDUI.create_course(name, course_code, instructor_id, prerequisites)

        elif choice == "2":
            course_code = input("Enter course code to edit: ")
            new_name = input("Enter new course name: ")
            new_instructor_id = int(input("Enter new instructor ID: "))
            new_prerequisites = input("Enter new prerequisites (comma-separated): ").split(",")
            CMDUI.edit_course(course_code, new_name, new_instructor_id, new_prerequisites)

        elif choice == "3":
            course_code = input("Enter course code to display: ")
            CMDUI.display_course(course_code)

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            course_code = input("Enter course code: ")
            CMDUI.add_student_to_course(student_id, course_code)

        elif choice == "5":
            print("Exiting University Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
