from uni import Uni
from utils import Formatting


class CMDUI:
    def __init__(self):
        self.uni = Uni()
        self.format = Formatting()

    def run(self):
        run = True
        while run:
            print()

            if self.uni.current_user is None:
                print("1. Sign In")
                print("2. Quit")
                choice = input("\nEnter your choice: ")

                if choice == '1':
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")

                    if self.uni.authenticate(email, password):
                        print("Authentication successful.")
                    else:
                        print("Authentication failed. Please try again.")

                elif choice == '2':
                    run = False

            else:
                options = [
                    "Create Student",
                    "Create Professor",
                    "Create Course",
                    "Enroll Student in Course",
                    "List Roles",
                    "List Courses",
                    "List Students",
                    "List Users",
                    "Sign Out",
                    "Quit",
                ]

                for i, op in enumerate(options):
                    print(f"{i + 1}. {op}")

                try:
                    choice = int(input("\nEnter your choice: "))

                except ValueError:
                    print("Invalid option entered, try again.")
                    continue

                if not 1 <= choice <= len(options):
                    print("Invalid option entered, try again.")
                    continue

                match choice:
                    case 1:
                        name = input("Enter student's name: ")
                        email = input("Enter student's email: ")
                        password = input("Enter student's password: ")
                        program = input("Enter student's program: ")
                        graduation_year = input("Enter students graduation year (20XX): ")

                        if len(graduation_year) < 4:
                            print("Invalid graduation year provided must be in the format: 20XX")
                            return

                        if self.uni.create_student(
                            name=name,
                            email=email,
                            password=password,
                            program=program,
                            graduation_year=graduation_year
                        ):
                            print("Student created.")
                        else:
                            print("Failed to create Student.")

                    case 2:
                        name = input("Enter professor's name: ")
                        email = input("Enter professor's email: ")
                        password = input("Enter professor's password: ")
                        employee_id = input("Enter professor's ID: ")
                        department = input("Enter professor's department: ")
                        self.uni.create_professor(name, email, password, employee_id, department)
                        print("Professor created.")

                    case 3:
                        name = input("Enter course name: ")
                        self.uni.create_course(name)
                        print("Course created.")

                    case 4:
                        course_id = input("Enter course ID: ")
                        student_id = input("Enter student ID: ")
                        if self.uni.enroll_student(course_id, student_id):
                            print("Student enrolled in the course.")
                        else:
                            print("Enrollment failed. Please check course and student IDs.")

                    case 5:
                        roles = self.uni.list_roles()
                        print("\nROLES:\n")
                        for role in roles:
                            self.format.print_dict_hierarchy(role, indentation=8)

                    case 6:
                        courses = self.uni.list_courses()
                        print("\nCOURSES:\n")
                        for course in courses:
                            self.format.print_dict_hierarchy(course, indentation=8)

                    case 7:
                        students = self.uni.list_students()
                        print("\nSTUDENTS:\n")
                        for student in students:
                            self.format.print_dict_hierarchy(student, indentation=8)

                    case 8:
                        users = self.uni.list_users()
                        print("\nUSERS:\n")
                        for user in users:
                            self.format.print_dict_hierarchy(user, indentation=8)

                    case 9:
                        self.uni.sign_out()

                    case 10:
                        run = False

        print("\n\t### * Thank you for using Unisage - The Comprehensive University Management Software * ###")
