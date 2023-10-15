from models.user import User
from datetime import datetime


class Student(User):
    def __init__(
            self,
            name,
            email,
            password,
            program,
            graduation_year: str,
            salt=None,
            uid=None,
            classes=None
    ):

        super().__init__(
            name=name,
            email=email,
            password=password,
            role='STUDENT',
            uid=uid,
            salt=salt
        )

        self.classes = classes
        self.program = program
        self.start_date = datetime.now().isoformat()
        self.graduation_year = graduation_year

    @classmethod
    def get_all(cls, record_dir="users.json"):
        return [student for student in super().get_all() if student["role"]["name"] == "STUDENT"]

