from models.user import User


class HostelManager(User):
    def __init__(self, uid, name, email, password, user_role, salt, hostel_name):
        super().__init__(name, email, password, user_role, uid, salt)
        self.hostel_name = hostel_name
