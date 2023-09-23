from datetime import datetime
from models.user import User


class Faculty(User):
    def __init__(
            self,
            name: str,
            position: str,
            dob: datetime,
            department_id: str,
            hire_date: datetime,
    ):

        super().__init__(name=name, dob=dob)

        self.position = position
        self.hire_date = hire_date
        self.department_id = department_id

    def save(self, child_data: dict):

        data = {
            "courses": self.courses,
            "class": self.student_class,
            "enrollment_year": self.enrollment_year,
            "graduation_year": self.graduation_year
        }

        for key in child_data:
            data[key] = child_data[key]

        return super().save(child_data=data)

    @staticmethod
    def get(sid: str):
        """
        Gets student_data from the file system through the Person class and the MODEL class and the data_manager
        :param sid:
        :return: Faculty
        """
        student_data = super().get(sid)
        if student_data:
            return Faculty(
                sid=student_data["id"],
                name=student_data["name"],
                courses=student_data["courses"],
                enrollment_year=student_data["enrollment_year"],
                graduation_year=student_data["graduation_year"]
            )

        else:
            return None
