from models.user import User


class Faculty(User):
    def __init__(self, name, email, password, faculty_id, department, uid, salt):
        super().__init__(name, email, password, uid, salt)
        self.faculty_id = faculty_id
        self.department = department
