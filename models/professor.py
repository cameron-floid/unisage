from models.faculty import Faculty


class Professor(Faculty):
    def __init__(self, name, email, password, faculty_id, department, classes, uid, salt):
        super().__init__(name, email, password, faculty_id, department, uid, salt)
        self.classes = classes
