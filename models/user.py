import os
import uuid
import hashlib
from models.role import Role
from models.model import MODEL
from error_handler.errors import RecordNotFound


class User(MODEL):
    def __init__(self, name, email, password, role, uid=None, salt=None):
        super().__init__()
        self.uid = str(uuid.uuid4()) if uid is None else uid
        self.name = name
        self.email = email
        self.salt = self._generate_salt() if salt is None else salt
        self.password_hash = self._hash_password(password, self.salt)
        self.role = None

        # get role
        roles = Role.get_all()
        for user_role in roles:
            if user_role["name"] == role["name"]:
                self.role = user_role

        roles = Role.get_all()
        for user_role in roles:
            if user_role["name"] == role:
                self.role = user_role

        if self.role is None:
            raise RecordNotFound("The Given Role Does Not Exist, Please Ask the University Administrator (UAD) to "
                                 "create it.")

    @staticmethod
    def _generate_salt():
        return os.urandom(16).hex()

    @staticmethod
    def _hash_password(password, salt):
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return hashed_password

    @staticmethod
    def verify_password(password: str, salt: str, password_hash: str):
        return User._hash_password(password, salt) == password_hash

    def save(self, record_dir="users.json"):
        super().save(record_dir=record_dir)
        
    @classmethod
    def get(cls, uid, records_dir="users.json"):
        return super().get(uid, records_dir=records_dir)
    
    @classmethod
    def get_all(cls, record_dir="users.json"):
        return super().get_all(record_dir=record_dir)
    
    @classmethod
    def create(cls, records_dir=None, **kwargs):
        super().create(records_dir=records_dir, **kwargs)

    @classmethod
    def exists(cls, email):
        users = cls.get_all()
        return any(user['email'] == email for user in users)
