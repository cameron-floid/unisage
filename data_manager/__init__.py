import os
import json


class DataManager:
    """
    DataManager class for reading and writing data to the file system.
    """

    def __init__(self, data_directory):
        """
        Initialize the DataManager with a specified data directory.

        Args:
            data_directory (str): The directory where data will be stored.
        """
        self.data_directory = data_directory

    def write_to_file(self, filename, data):
        """
        Write data to a JSON file.

        Args:
            filename (str): The name of the JSON file.
            data (dict): The data to be written as a dictionary.

        Returns:
            bool: True if the write operation was successful, False otherwise.
        """
        try:
            with open(os.path.join(self.data_directory, filename), 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error writing to {filename}: {str(e)}")
            return False

    def read_from_file(self, filename):
        """
        Read data from a JSON file.

        Args:
            filename (str): The name of the JSON file to read.

        Returns:
            dict: The data read from the file as a dictionary, or an empty dictionary if the file does not exist.
        """
        try:
            with open(os.path.join(self.data_directory, filename), 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error reading from {filename}: {str(e)}")
            return {}
