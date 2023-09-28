import uuid
from data_manager import DataManager


class MODEL:
    def __init__(self):
        self.uid = str(uuid.uuid4())

    def save(self):
        data_manager = DataManager()
        data_manager.save_record(self.__class__.__name__.lower() + '.json', self.__dict__)

    @classmethod
    def get(cls, uid):
        records = cls.get_all()
        for record in records:
            if record['uid'] == uid:
                return cls(**record)
        return None

    @classmethod
    def get_all(cls):
        filename = cls.__name__.lower() + '.json'
        data_manager = DataManager()
        return data_manager.get_records(filename)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance
