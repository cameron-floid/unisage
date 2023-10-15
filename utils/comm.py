"""
Transaction Packet/ Communication packet
For communicating process success or failure between the application class Uni and different interfaces
"""


class Comm:

    def __init__(self, success: bool, message: str = None, error: str = None):
        self.success = success
        self.message = "" if message is None else message
        self.error = "" if error is None else error

    def as_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "error": self.error
        }

    @staticmethod
    def from_dict(data: dict):
        return Comm(success=data["success"], message=data["message"], error=data["error"])

    def display(self):
        print(self.__dict__)
