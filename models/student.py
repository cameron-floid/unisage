from datetime import datetime
from models.user import User
from error_handler import RecordNotFound, WrongPassword, AuthenticationError


class Student(User):
    def __init__(
            self,
            name: str,
            email: str,
            dob: datetime,
            courses: list,
            major: str,
            enrollment_year: datetime,
            graduation_year: datetime,
    ):

        super().__init__(name=name, email=email, dob=dob)

        self.courses = courses
        self.student_class = student_class
        self.enrollment_year = enrollment_year
        self.graduation_year = graduation_year

    @staticmethod
    def create_student(
            name: str,
            email: str,
            dob: datetime,
            student_class: str,
            enrollment_year: datetime,
            graduation_year: datetime,
            password: str,
            courses: list = None
    ) -> bool:

        if courses is None:
            courses = []

        data = {
            "name": name,
            "email": email,
            "dob": dob,
            "student_class": student_class,
            "enrollment_year": enrollment_year,
            "graduation_year": graduation_year,
            "courses": courses,
            "password": password
        }

        return super().create_user(user_data=data)

    @staticmethod
    def get_student(email: str, password: str):
        """
        Get User object when provided email and password
        :param email:
        :param password:
        :return:
        """

        try:
            student_data = super().get_user(email=email, password=password)

            return Student(
                uid=student_data["uid"],
                name=student_data["name"],
                email=student_data["email"],
                dob=student_data["dob"],
                student_class=student_data["student_class"],
                enrollment_year=student_data["enrollment_year"],
                graduation_year=student_data["graduation_year"],
                courses=student_data["courses"]
            )

        except RecordNotFound:
            # print(f"Invalid User Email: {email}")  # log error
            raise AuthenticationError()

        except WrongPassword:
            # print(f"Invalid User Password for: {email}")  # log error
            raise AuthenticationError()
