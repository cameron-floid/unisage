from datetime import datetime
from models.user import User


class Faculty(User):
    def __init__(
            self,
            name: str,
            email: str,
            dob: datetime,
            position: str,
            department_id: str,
            hire_date: datetime,
    ):

        super().__init__(name=name, email=email, dob=dob)

        self.position = position
        self.hire_date = hire_date
        self.department_id = department_id
