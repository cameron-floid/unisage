import os
import uuid
import json
import hashlib
from pprint import pprint


class DataManager:
    @staticmethod
    def save_record(filename, record):

        current_directory = os.path.dirname(__file__)
        f_name = os.path.join(current_directory, filename)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(f_name), exist_ok=True)

        with open(f_name, 'a') as file:
            json.dump(record, file)
            file.write('\n')

    @staticmethod
    def get_records(filename):

        current_directory = os.path.dirname(__file__)
        f_name = os.path.join(current_directory, filename)

        records = []

        try:
            with open(f_name, 'r') as file:
                for line in file:
                    record = json.loads(line)
                    records.append(record)
        except FileNotFoundError:
            pass
        return records


class Model:
    def __init__(self):
        self.uid = str(uuid.uuid4())

    def save(self):
        data_manager = DataManager()
        data_manager.save_record("data/demo/" + self.__class__.__name__.lower() + '.json', self.__dict__)

    @classmethod
    def get(cls, uid):
        records = cls.get_all()
        for record in records:
            if record['uid'] == uid:
                return cls(**record)
        return None

    @classmethod
    def get_all(cls):
        filename = "data/demo/" + cls.__name__.lower() + '.json'
        data_manager = DataManager()
        return data_manager.get_records(filename)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance


class User(Model):
    def __init__(self, uid, name, email, password, salt):
        super().__init__()
        self.uid = uid  # Assign the uid passed as a parameter
        self.name = name
        self.email = email
        self.salt = salt  # Assign the salt passed as a parameter
        self.password_hash = self._hash_password(password, self.salt)

    @staticmethod
    def _hash_password(password, salt):
        # Hash the password using a secure hash algorithm (e.g., SHA-256) with the salt
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return hashed_password

    @staticmethod
    def verify_password(password: str, salt: str, password_hash: str):
        # Verify if the provided password matches the stored hash
        return User._hash_password(password, salt) == password_hash


class Student(User):
    def __init__(self, name, email, password, student_id, program):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.program = program


class Professor(User):
    def __init__(self, name, email, password, employee_id, department):
        super().__init__(name, email, password)
        self.employee_id = employee_id
        self.department = department


class HostelManager(User):
    def __init__(self, name, email, password, hostel_name):
        super().__init__(name, email, password)
        self.hostel_name = hostel_name


class Course(Model):
    def __init__(self, name, professor_id):
        super().__init__()
        self.name = name
        self.professor_id = professor_id
        self.students = []

    def enroll_student(self, student_id):
        self.students.append(student_id)
        self.save()


class Uni:
    def __init__(self):
        self.current_user = None

    @staticmethod
    def _user_exists(email):
        users = User.get_all()
        for user in users:
            if user['email'] == email:
                return True
        return False

    def authenticate(self, email, password):
        # Authenticate the user based on email and password
        users = User.get_all()
        for user in users:
            if user['email'] == email and User.verify_password(
                password=password,
                salt=user["salt"],
                password_hash=user["password_hash"]
            ):
                self.current_user = User(user['uid'], user['name'], user['email'], '', user['salt'])
                return True
        return False

    def signup(self, name, email, password):
        # Create a new account (User) with the provided information
        if not self._user_exists(email):
            User.create(name=name, email=email, password=password)
            return True
        return False

    def create_student(self, name, email, password, student_id, program):
        if self.current_user and isinstance(self.current_user, Professor):
            student = Student.create(name=name, email=email, password=password, student_id=student_id, program=program)
            return student
        return None

    def create_professor(self, name, email, password, employee_id, department):
        if self.current_user and isinstance(self.current_user, HostelManager):
            professor = Professor.create(name=name, email=email, password=password, employee_id=employee_id, department=department)
            return professor
        return None

    def create_course(self, name):
        if self.current_user and isinstance(self.current_user, Professor):
            course = Course.create(name=name, professor_id=self.current_user.uid)
            return course
        return None

    def enroll_student(self, course_id, student_id):
        course = Course.get(course_id)
        if course and self.current_user and isinstance(self.current_user, Student):
            course.enroll_student(student_id)
            return True
        return False

    @staticmethod
    def list_courses():
        return Course.get_all()


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


if __name__ == "__main__":
    cmd_ui = CMDUI()
    cmd_ui.run()

