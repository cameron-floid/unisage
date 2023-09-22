import uuid
import datetime
from datetime import datetime

from data_manager import DataManager

# DATA STORES - TEMPORARY
COURSES = []
PEOPLE = []
STUDENTS = []


class MODEL:
    """
    MODEL superclass for data management operations.
    """

    def __init__(self, data_directory):
        """
        Initialize the MODEL with a randomly generated model ID.

        Args:
            data_directory (str): The directory where data will be stored.
        """
        self.model_id = str(uuid.uuid4())  # Generate a random UUID as the model ID
        self.data_directory = data_directory

    def save(self, obj, collection, uid, metadata=None):
        """
        Save an object to the data collection using DataManager.

        Args:
            obj (dict): The object to be saved as a dictionary.
            collection (str): The name of the data collection.
            uid (str): The unique identifier for the object.
            metadata (dict, optional): Additional metadata to include in the saved data.

        Returns:
            bool: True if the save operation was successful, False otherwise.
        """
        try:
            data_manager = DataManager(self.data_directory)
            data = data_manager.read_from_file(collection + ".json")

            # Create a dictionary to store object data along with metadata
            object_data = {
                "data": obj,
                "uid": uid,
                "timestamp": datetime.now().isoformat(),
            }

            if metadata:
                object_data["metadata"] = metadata

            data[uid] = object_data
            return data_manager.write_to_file(collection + ".json", data)
        except Exception as e:
            print(f"Error saving object to {collection}: {str(e)}")
            return False

    def get(self, collection, uid):
        """
        Get an object from the data collection using DataManager.

        Args:
            collection (str): The name of the data collection.
            uid (str): The unique identifier for the object to retrieve.

        Returns:
            dict: The retrieved object as a dictionary, including metadata, or None if not found.
        """
        try:
            data_manager = DataManager(self.data_directory)
            data = data_manager.read_from_file(collection + ".json")
            object_data = data.get(uid)
            return object_data
        except Exception as e:
            print(f"Error getting object from {collection}: {str(e)}")
            return None


class Person:

    def __init__(self, name: str, pid: str, dob: datetime):
        self.name = name
        self.id = pid
        self.dob = dob

    def save(self):
        """
        Save Person record to disk using the program's data manager module
        :return: Boolean
        """
        data = {
            "name": self.name,
            "id": self.id,
            "dob": self.dob.isoformat()
        }
        return MODEL(data_directory="models").save(data, "people", self.id)

    @staticmethod
    def get(pid: str):
        """
        Get Person record from disk
        :param pid:
        :return: Person
        """
        person_data = MODEL(data_directory="models").get("people", pid)
        if person_data:
            return Person(
                person_data["data"]["name"],
                person_data["data"]["id"],
                datetime.fromisoformat(person_data["data"]["dob"])
            )
        return None


class Student(Person):
    def __init__(self, name, sid, dob: datetime):
        super().__init__(name=name, pid=sid, dob=dob)
        self.courses = []

    def save(self):
        return super().save()

    @staticmethod
    def get(sid: str):
        return super().get(sid)


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
        course_data = MODEL(data_directory="models").get("courses", course_code)
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
        return MODEL(data_directory="models").save(data, "courses", self.course_code)

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


class CMDUI:
    @staticmethod
    def create_course(name, course_code, instructor_id, prerequisites=None):
        course = Course(name, course_code, instructor_id, prerequisites)
        if course.save():
            print(f"Course '{course.name}' created successfully!")
        else:
            print("Failed to create the course.")

    @staticmethod
    def edit_course(course_code, new_name, new_instructor_id, new_prerequisites):
        course = Course.get(course_code)
        if course:
            course.name = new_name
            course.instructor_id = new_instructor_id
            course.prerequisites = new_prerequisites
            if course.save():
                print(f"Course '{course.name}' edited successfully!")
            else:
                print("Failed to edit the course.")
        else:
            print(f"Course with code '{course_code}' not found.")

    @staticmethod
    def display_course(course_code):
        course = Course.get(course_code)
        if course:
            print(f"Course Name: {course.name}")
            print(f"Course Code: {course.course_code}")
            print(f"Instructor ID: {course.instructor_id}")
            print(f"Prerequisites: {', '.join(course.prerequisites)}")
            print(f"Enrolled Students: {', '.join(student.name for student in course.students)}")
        else:
            print(f"Course with code '{course_code}' not found.")

    @staticmethod
    def add_student_to_course(student_id, course_code):
        student = Student.get(student_id)
        course = Course.get(course_code)
        if student and course:
            if course.enroll_student(student):
                student.courses.append(course)
                print(f"{student.name} enrolled in {course.name} successfully!")
            else:
                print(f"{student.name} is already enrolled in {course.name}.")
        else:
            print("Student or course not found.")
