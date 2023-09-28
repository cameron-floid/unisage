import uuid
from models.model import MODEL


class Role(MODEL):

    def __init__(self, role: str, auth_level: int, privileges: list):
        super().__init__()
        self.uid = uuid.uuid4()
        self.role = role
        self.auth_level = auth_level
        self.privileges = privileges

    def get_role_data(self, role):
        role_data = super().get(uid=role)
        return role_data

    def save_role(self):
        return super().save()
