from datetime import datetime
from models.user import User


class Student(User):
    def __init__(
            self,
            name: str,
            dob: datetime,
            student_class: str,
            enrollment_year: datetime,
            graduation_year: datetime,
            courses: list = None
    ):

        super().__init__(name=name, dob=dob)

        if courses is None:
            courses = []

        self.courses = courses
        self.student_class = student_class
        self.enrollment_year = enrollment_year
        self.graduation_year = graduation_year

    def save_user(self, child_data: dict):

        data = {
            "courses": self.courses,
            "class": self.student_class,
            "enrollment_year": self.enrollment_year,
            "graduation_year": self.graduation_year
        }

        for key in child_data:
            data[key] = child_data[key]

        return super().save_user(child_data=data)

    @staticmethod
    def get_student(student_id: str):
        """
        Gets student_data from the file system through the Person class and the MODEL class and the data_manager
        :param sid:
        :return: Student
        """
        student_data = super().get(collection="users", uid=student_id)
        if student_data:
            return Student(
                sid=student_data["id"],
                name=student_data["name"],
                courses=student_data["courses"],
                enrollment_year=student_data["enrollment_year"],
                graduation_year=student_data["graduation_year"]
            )

        else:
            return None
