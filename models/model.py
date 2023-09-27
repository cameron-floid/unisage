import uuid
from datetime import datetime
from data_manager import DataManager


class MODEL:
    """
    MODEL superclass for data management operations.
    """

    def __init__(self, data_directory):
        """
        Intermediate interaction between models and data_manager
        :param data_directory:
        """
        # self.uid = str(uuid.uuid4())  # Generate a random UUID for every model record
        self.data_directory = data_directory

    @staticmethod
    def get_all_models() -> list:
        pass

    def save(self, collection: str, data: dict, data_directory=None) -> bool:
        """
        Save model record to the file system using the data_manager
        :param data_directory:
        :param data:
        :param collection:
        :return: Boolean
        """

        try:
            data_manager = DataManager(data_directory if data_directory else self.data_directory)
            collection_data = data_manager.read_from_file(collection + ".json")

            # Create a dictionary to store object data along with metadata
            record_data = {
                "uid": str(uuid.uuid4()),
                "timestamp": datetime.now().isoformat(),
            }

            for key in data:
                record_data[key] = data[key]

            collection_data[record_data["uid"]] = record_data
            return data_manager.write_to_file(collection + ".json", data)

        except Exception as e:
            print(f"Error saving object to {collection}: {str(e)}")
            return False

    def get(self, collection, uid, data_directory=None) -> dict:
        """
        Get an object from the data collection using DataManager.

        :param uid:
        :param collection:
        :param data_directory:
        :return dict:
        """

        try:
            data_manager = DataManager(data_directory if data_directory else self.data_directory)
            data = data_manager.read_from_file(collection + ".json")
            record_data = data.get(uid)
            return record_data

        except Exception as e:
            print(f"Error getting object from {collection}: {str(e)}")
            return {}

    def get_all(self, collection: str, data_directory=None) -> dict:

        try:
            data_manager = DataManager(data_directory if data_directory else self.data_directory)
            data = data_manager.read_from_file(collection + ".json")
            return data

        except Exception as e:
            print(f"Error getting object from {collection}: {str(e)}")
            return {}
