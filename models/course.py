from models.model import MODEL
from models.student import Student


class Course:
    def __init__(self, name: str, course_code: str, instructor_id: int, prerequisites: list):
        self.name = name
        self.course_code = course_code
        self.instructor_id = instructor_id
        self.prerequisites = prerequisites
        self.students = []

    @classmethod
    def get_by_code(cls, course_code: str):
        # Use the 'get' method from the MODEL class to retrieve course data by course_code
        course_data = MODEL(data_directory="data/models").get("courses", course_code)
        if course_data:
            # Create a Course object from the retrieved data
            return cls(
                course_data["data"]["name"],
                course_data["data"]["course_code"],
                course_data["data"]["instructor_id"],
                course_data["data"]["prerequisites"]
            )
        return None

    def save(self):
        # Use the 'save' method from the MODEL class to save course data
        data = {
            "name": self.name,
            "course_code": self.course_code,
            "instructor_id": self.instructor_id,
            "prerequisites": self.prerequisites,
        }
        return MODEL(data_directory="data/models").save(data, "courses", self.course_code)

    @staticmethod
    def get(course_code: str):
        # Use the 'get' method from the MODEL class to retrieve course data by course_code
        return Course.get_by_code(course_code)

    def enroll_student(self, student: Student):
        if student in self.students:
            print(f"{student.name} is already enrolled in {self.name}")
            return True
        else:
            self.students.append(student)
            return True
