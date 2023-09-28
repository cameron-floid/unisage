from models import HostelManager
from models.user import User
from models.course import Course
from models.student import Student
from models.professor import Professor


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
                self.current_user = User(user['name'], user['email'], password, user['uid'], user['salt'])
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
