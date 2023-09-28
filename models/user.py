import hashlib
import os
import uuid
from models.model import MODEL


class User(MODEL):
    def __init__(self, name, email, password, uid=None, salt=None):
        super().__init__()
        self.uid = str(uuid.uuid4()) if uid is None else uid  # Generate a random UID
        self.name = name
        self.email = email
        self.salt = self._generate_salt() if salt is None else salt  # Auto-generate a salt
        self.password_hash = self._hash_password(password, self.salt)

    @staticmethod
    def _generate_salt():
        # Generate a random salt (you can use os.urandom to create a secure salt)
        return os.urandom(16).hex()

    @staticmethod
    def _hash_password(password, salt):
        # Hash the password using a secure hash algorithm (e.g., SHA-256) with the salt
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return hashed_password

    @staticmethod
    def verify_password(password: str, salt: str, password_hash: str):
        # Verify if the provided password matches the stored hash
        return User._hash_password(password, salt) == password_hash
