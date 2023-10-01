from models.faculty import Faculty


class Professor(Faculty):
    def __init__(self, name, email, password, department, role, uid, hire_date, salt,  classes=None):
        super().__init__(
            name=name,
            email=email,
            password=password,
            department=department,
            role=role,
            uid=uid,
            salt=salt,
            hire_date=hire_date
        )
        self.classes = classes
