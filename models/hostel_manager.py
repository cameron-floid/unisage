from models.user import User


class HostelManager(User):
    def __init__(self, uid, name, email, password, salt, hostel_name):
        super().__init__(name, email, password)
        self.hostel_name = hostel_name
