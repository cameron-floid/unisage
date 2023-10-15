from models.model import MODEL


class Course(MODEL):
    def __init__(self, name, professor_uid):
        super().__init__()
        self.name = name
        self.professor_id = professor_uid
        self.students = []

    def enroll_student(self, student_id):
        self.students.append(student_id)
        self.save()

    @classmethod
    def get_all(cls, records_dir="courses.json"):
        return super().get_all(records_dir=records_dir)

    @classmethod
    def exists(cls, name):
        courses = cls.get_all()
        return any(course['name'] == name for course in courses)

    @classmethod
    def create(cls, records_dir=None, **kwargs):
        return super().create(records_dir="courses.json", **kwargs)
