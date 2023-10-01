import uuid
from data_manager import DataManager


class MODEL:
    def __init__(self):
        self.uid = str(uuid.uuid4())

    def save(self, record_dir=None):
        data_manager = DataManager()
        data_manager.save_record(
            self.__class__.__name__.lower() + '.json' if not record_dir else record_dir,
            self.__dict__
        )

    @classmethod
    def get(cls, uid, records_dir=None):
        records = cls.get_all(record_dir=records_dir)
        for record in records:
            if record['uid'] == uid:
                return cls(**record)
        return None

    @classmethod
    def get_all(cls, record_dir=None):
        filename = cls.__name__.lower() + '.json' if not record_dir else "users.json"
        data_manager = DataManager()
        return data_manager.get_records(filename)

    @classmethod
    def create(cls, records_dir, **kwargs):
        instance = cls(**kwargs)
        instance.save(record_dir=records_dir)
        return instance
