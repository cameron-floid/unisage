from models.user import User


class Faculty(User):
    def __init__(self, name, email, password, department, role, uid, salt, hire_date):
        super().__init__(
            name=name,
            email=email,
            password=password,
            role=role,
            uid=uid,
            salt=salt
        )
        self.department = department
        self.hire_date = hire_date
