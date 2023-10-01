from datetime import datetime
from models.professor import Professor


class UAD(Professor):
    def __init__(self, name, email, password, department, classes, reset_code, uid, salt):
        super().__init__(
            name=name,
            email=email,
            password=password,
            department=department,
            classes=classes,
            role="UAD",
            uid=uid,
            salt=salt,
            hire_date=datetime.now().isoformat()
        )

        self.reset_code = reset_code
