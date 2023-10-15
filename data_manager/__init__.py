import os
import json


class DataManager:
    @staticmethod
    def save_record(filename, records):
        # Get the absolute path to the project directory
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        # Create the data directory if it doesn't exist
        data_dir = os.path.join(project_dir, 'data')
        os.makedirs(data_dir, exist_ok=True)

        file_path = os.path.join(data_dir, filename)

        with open(file_path, 'w') as file:
            # Save the entire records dictionary as a single JSON object
            json.dump(records, file)
            file.write('\n')

    @staticmethod
    def get_records(filename):
        # Get the absolute path to the project directory
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        data_dir = os.path.join(project_dir, 'data')
        file_path = os.path.join(data_dir, filename)

        records = {}

        try:
            with open(file_path, 'r') as file:
                records = json.load(file)
        except FileNotFoundError:
            pass

        return records
