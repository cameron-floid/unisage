from datetime import datetime
from models.model import MODEL
from utils import SecurityUtils
from error_handler.errors import RecordNotFound, WrongPassword


class User(MODEL):

    DATA_DIRECTORY = "data/iam"

    def __init__(self, name: str, email: str, dob: datetime):
        super().__init__(data_directory="users")

        self.dob = dob
        self.name = name
        self.email = email

    @staticmethod
    def get_user(email: str, password: str):

        # get user hash and uid
        hash_and_uid = User.get_hash_and_uid(email=email)

        if not hash_and_uid:
            raise RecordNotFound(f"No User with the email {email} was found.")

        # compare provided hash with the user hash
        if SecurityUtils.verify_password(password=password, password_hash=hash_and_uid["hash"]):
            return User.get_user_data(hash_and_uid["uid"])

        else:
            raise WrongPassword(f"Wrong password provided.")

    @staticmethod
    def create_user(user_data: dict) -> bool:
        """
        Create a new user record
        :return: Boolean
        """

        # hash user password
        password_hash = SecurityUtils.hash_password(password=user_data["password"])

        del user_data["password"]
        user_data["hash"] = password_hash

        return super().save(data=user_data, collection="users", data_directory=User.DATA_DIRECTORY)

    @staticmethod
    def get_hash_and_uid(email: str) -> dict:
        users = super().get_all(collection="users", data_directory=User.DATA_DIRECTORY)
        for user in users:
            for key in users[user]:
                if key == "email":
                    if users[users][key] == email:
                        return {
                            "uid": users[users]["uid"],
                            "hash": users[users]["hash"]
                        }

        return {}

    @staticmethod
    def get_users():
        return super().get_all(collection="users", data_directory=User.DATA_DIRECTORY)

    @staticmethod
    def get_user_data(uid: str):
        """
        Get user_data from disk
        :param uid:
        :return: user_data
        """

        user_data = super().get("users", uid=uid, data_directory=User.DATA_DIRECTORY)
        if user_data:
            return user_data

        print(f"User with PID: {uid} NOT FOUND.")
        return None
