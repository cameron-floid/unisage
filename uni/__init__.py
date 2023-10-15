import os
from models.role import Role
from models.uad import UAD
from models import HostelManager
from models.user import User
from models.course import Course
from models.student import Student
from models.professor import Professor


class Uni:
    def __init__(self):
        self.current_user = None
        self.create_default_roles()
        self.ensure_uad_exists()

    # create UAD Role
    @staticmethod
    def create_default_roles():

        default_roles = os.environ.get('DEFAULT_ROLES').split(",")

        for role in default_roles:
            if Role.exists(role):
                continue
            r = Role(name=role, privileges=[])
            r.save()

    # create UAD
    @staticmethod
    def create_uad():
        """
        Create UAD - University Administrator using environment variables
        :return: UAD object if creation is successful, otherwise None
        """

        uad_email = os.environ.get('UAD_EMAIL')

        # Check if UAD already exists
        if User.exists(uad_email):
            print("User with the specified email already exists.")
            return False

        uad_name = os.environ.get('UAD_NAME')
        uad_password = os.environ.get('UAD_PASSWORD')
        uad_reset_code = os.environ.get('UAD_RESET_CODE')
        uad_department = os.environ.get('UAD_DEPARTMENT')

        if not uad_name or not uad_email or not uad_password or not uad_reset_code or not uad_department:
            print("Error: Missing required environment variables for UAD creation.")
            return False

        # Create UAD
        uad = UAD(
            name=uad_name,
            email=uad_email,
            password=uad_password,
            department=uad_department,
            classes=[],
            reset_code=uad_reset_code,
            salt=None,
            uid=None
        )

        uad.save()

        if uad:
            print("UAD created successfully.")
            return True

        else:
            print("Error: Failed to create UAD.")
            return False

    def ensure_uad_exists(self):
        uad_email = os.environ.get('UAD_EMAIL')
        if User.exists(uad_email):
            return

        if not self.create_uad():
            raise Exception("Failed to create UAD")

    def authenticate(self, email, password):
        # Authenticate the user based on email and password
        users = User.get_all()
        for user in users:
            if user['email'] == email and User.verify_password(
                    password=password,
                    salt=user["salt"],
                    password_hash=user["password_hash"]
            ):
                self.current_user = User(
                    name=user["name"],
                    email=user["email"],
                    password=password,
                    uid=user["uid"],
                    salt=user["salt"],
                    role=user["role"]["name"]
                )
                return True
        return False

    def sign_out(self):
        self.current_user = None
        print("Signed out successfully.")

    def create_student(self, name, email, password, program, graduation_year) -> bool:

        # TODO: replace UAD check with Role.permissions check
        if self.current_user and self.current_user.role["name"] == "UAD":

            # check if the given student course exists
            if Student.exists(email):
                print(f"User with the given student email already exists.")
                return False

            student = Student(
                name=name,
                email=email,
                password=password,
                program=program,
                graduation_year=graduation_year
            )
            student.save()
            return True

        else:
            print("Insufficient permissions to create enroll student.")
            print(type(self.current_user))
            return False

    def create_professor(self, name, email, password, employee_id, department):
        if self.current_user and isinstance(self.current_user, HostelManager):
            professor = Professor.create(
                name=name,
                email=email,
                password=password,
                employee_id=employee_id,
                department=department
            )
            return professor
        return None

    def create_course(self, name):
        if self.current_user.role["name"] == "UAD":
            course = Course.create(name=name, professor_uid=self.current_user.uid, records_dir=None)
            return course
        return None

    def enroll_student(self, course_id, student_id):
        course = Course.get(course_id)
        if course and self.current_user and isinstance(self.current_user, Student):
            course.enroll_student(student_id)
            return True
        return False

    @staticmethod
    def list_roles():
        return Role.get_all()

    @staticmethod
    def list_courses():
        return Course.get_all()

    @staticmethod
    def list_students():
        return Student.get_all()

    @staticmethod
    def list_users():
        return User.get_all()
