import uuid
from models.model import MODEL
from error_handler import RecordNotFound


class Role(MODEL):

    def __init__(self, role: str):
        super().__init__(data_directory="data/iam")
        self.role = role
        role_data = self.get_role_data(role=role)

        if role_data is None:
            raise RecordNotFound(f"The User Role: {role} NOT FOUND.")

        self.auth_level = role_data["auth_level"]
        self.privileges = role_data["privileges"]

    @staticmethod
    def create_role(role: str, auth_level: int, privileges: list = None):
        data = {
            "uid": str(uuid.uuid4()),
            "role": role,
            "auth_level": auth_level,
            "privileges": privileges
        }

        return Role.save_role(role_data=data)

    @staticmethod
    def get_role_data(role):
        role_data = super().get(collection="roles", uid=role)
        return role_data

    @staticmethod
    def save_role(role_data: dict):
        return super().save(collection="roles", data=role_data)
