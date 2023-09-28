from models.user import User


class Student(User):
    def __init__(self, name, email, password, student_id, program, uid, salt):
        super().__init__(name, email, password, uid, salt)
        self.student_id = student_id
        self.program = program
