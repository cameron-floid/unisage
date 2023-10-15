import uuid
from data_manager import DataManager


class MODEL:
    def __init__(self):
        self.uid = str(uuid.uuid4())

    def save(self, records_dir=None):
        data_manager = DataManager()
        records = data_manager.get_records(records_dir)
        records[self.uid] = self.__dict__
        data_manager.save_record(records_dir, records)

    @classmethod
    def get(cls, uid, records_dir=None):
        records = cls.get_records_dict(records_dir=records_dir)
        return records.get(uid)

    @classmethod
    def get_records_dict(cls, records_dir=None):
        data_manager = DataManager()
        records_dict = data_manager.get_records(records_dir)
        return records_dict

    @classmethod
    def get_all(cls, records_dir=None):
        data_manager = DataManager()
        records_dict = data_manager.get_records(records_dir)
        records_list = list(records_dict.values())
        return records_list

    @classmethod
    def create(cls, records_dir=None, **kwargs):
        instance = cls(**kwargs)
        instance.save(records_dir=records_dir)
        return instance
