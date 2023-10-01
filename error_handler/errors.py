class RecordNotFound(Exception):
    def __init__(self, message="Record Not Found."):
        raise Exception(message)


class WrongPassword(Exception):
    def __init__(self, message="Wrong password provided."):
        raise Exception(message)


class AuthenticationError(Exception):
    def __init__(self, message="Incorrect Username or Password."):
        raise Exception(message)
