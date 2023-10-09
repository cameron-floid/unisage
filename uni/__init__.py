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
        self.ensure_uad_exists()

    # create UAD Role
    @staticmethod
    def create_uad_role():

        # Check if the role already exists
        if Role.exists("UAD"):
            return

        # Create and save the UAD role
        uad_role = Role(name="UAD", privileges=[])
        uad_role.save()

    # create UAD
    def create_uad(self):
        """
        Create UAD - University Administrator using environment variables
        :return: UAD object if creation is successful, otherwise None
        """

        uad_email = os.environ.get('UAD_EMAIL')

        # Check if UAD already exists
        if User.exists(uad_email):
            print("User with the specified email already exists.")
            return None

        self.create_uad_role()  # create UAD role if it doesn't exit

        uad_name = os.environ.get('UAD_NAME')
        uad_password = os.environ.get('UAD_PASSWORD')
        uad_reset_code = os.environ.get('UAD_RESET_CODE')
        uad_department = os.environ.get('UAD_DEPARTMENT')

        if not uad_name or not uad_email or not uad_password or not uad_reset_code or not uad_department:
            print("Error: Missing required environment variables for UAD creation.")
            return None

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
            return uad

        else:
            print("Error: Failed to create UAD.")
            return None

    def ensure_uad_exists(self):
        uad_email = os.environ.get('UAD_EMAIL')
        if User.exists(uad_email):
            return

        if self.create_uad() is None:
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
                    role=user["role"]
                )
                return True
        return False

    def create_student(self, name, email, password, program) -> bool:

        # TODO: replace UAD check with Role.permissions check
        if self.current_user and self.current_user.role["name"] == "UAD":

            # check if the given student course exists
            if Student.exists(email):
                print(f"User with the given student email already exists.")
                return False

            student = Student.create(name=name, email=email, password=password, program=program)
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
