from uni import Uni


class CMDUI:
    def __init__(self):
        self.uni = Uni()

    def run(self):
        while True and self.uni.current_user is None:
            print("1. Sign In")
            print("2. Sign Up")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                email = input("Enter your email: ")
                password = input("Enter your password: ")

                if self.uni.authenticate(email, password):
                    print("Authentication successful.")
                    self.handle_authenticated_user()
                else:
                    print("Authentication failed. Please try again.")
            elif choice == '2':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                password = input("Enter your password: ")

                if self.uni.signup(name, email, password):
                    print("Account created successfully. Please sign in.")
                else:
                    print("An account with this email already exists.")
            elif choice == '3':
                break

        if self.uni.current_user is not None:
            self.handle_authenticated_user()

    def handle_authenticated_user(self):
        while True:
            print("1. Create Student")
            print("2. Create Professor")
            print("3. Create Course")
            print("4. Enroll Student in Course")
            print("5. List Courses")
            print("6. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                email = input("Enter student's email: ")
                password = input("Enter student's password: ")
                student_id = input("Enter student's ID: ")
                program = input("Enter student's program: ")
                self.uni.create_student(name, email, password, student_id, program)
                print("Student created.")
            elif choice == '2':
                name = input("Enter professor's name: ")
                email = input("Enter professor's email: ")
                password = input("Enter professor's password: ")
                employee_id = input("Enter professor's ID: ")
                department = input("Enter professor's department: ")
                self.uni.create_professor(name, email, password, employee_id, department)
                print("Professor created.")
            elif choice == '3':
                name = input("Enter course name: ")
                self.uni.create_course(name)
                print("Course created.")
            elif choice == '4':
                course_id = input("Enter course ID: ")
                student_id = input("Enter student ID: ")
                if self.uni.enroll_student(course_id, student_id):
                    print("Student enrolled in the course.")
                else:
                    print("Enrollment failed. Please check course and student IDs.")
            elif choice == '5':
                courses = self.uni.list_courses()
                print("Courses:")
                for course in courses:
                    print(f"Course ID: {course['uid']}, Name: {course['name']}")
            elif choice == '6':
                break

