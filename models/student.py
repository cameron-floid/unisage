from models.user import User
from datetime import datetime


class Student(User):
    def __init__(
            self,
            name,
            email,
            password,
            program,
            uid,
            salt,
            start_date: str,
            graduation_year: str,
            classes=None
    ):

        super().__init__(
            name=name,
            email=email,
            password=password,
            uid=uid,
            salt=salt
        )

        self.classes = classes
        self.program = program
        self.start_date = start_date
        self.graduation_year = graduation_year
