from models.model import MODEL


class Course(MODEL):
    def __init__(self, name, professor_id):
        super().__init__()
        self.name = name
        self.professor_id = professor_id
        self.students = []

    def enroll_student(self, student_id):
        self.students.append(student_id)
        self.save()

    @classmethod
    def exists(cls, name):
        courses = cls.get_all()
        return any(course['name'] == name for course in courses)

