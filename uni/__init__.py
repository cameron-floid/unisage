from models.student import Student
from error_handler import AuthenticationError


class Uni:

    def __init__(self):
        self.current_user = None  # Type of User
        self.Student = Student

    def create_student(self, data):
        try:
            self.Student.create_student(
                name=data["name"],
                email=data["email"],
                password=data["password"],
                dob=data["dob"],
                enrollment_year=data["enrollment_year"],
                graduation_year=data["enrollment_year"],
                student_class=data["student_class"]
            )

        except AuthenticationError:
            return {
                "success": False,
                "error": "Incorrect username or password"
            }
