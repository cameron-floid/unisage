class RecordNotFound(Exception):
    raise Exception("Record Not Found.")


class WrongPassword(Exception):
    raise Exception("Wrong password provided.")


class AuthenticationError(Exception):
    raise Exception("Incorrect Username or Password.")
