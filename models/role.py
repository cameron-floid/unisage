from models.model import MODEL


class Role(MODEL):

    def __init__(self, name, privileges=None):
        super().__init__()
        self.name = name
        self.privileges = privileges

    @classmethod
    def exists(cls, name):
        roles = cls.get_all()
        return any(role['name'] == name for role in roles)
