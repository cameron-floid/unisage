from models.model import MODEL


class Role(MODEL):
    def __init__(self, name, privileges=None):
        super().__init__()
        self.name = name
        self.privileges = privileges

    def save(self, records_dir="roles.json"):
        super().save(records_dir=records_dir)

    @classmethod
    def get(cls, uid, records_dir="roles.json"):
        return super().get(uid, records_dir=records_dir)

    @classmethod
    def get_all(cls, records_dir="roles.json"):
        return super().get_all(records_dir=records_dir)

    @classmethod
    def create(cls, records_dir=None, **kwargs):
        super().create(records_dir=records_dir, **kwargs)

    @classmethod
    def exists(cls, role, records_dir="roles.json"):
        roles = cls.get_all(records_dir=records_dir)
        return any(existing_role['name'] == role for existing_role in roles)
