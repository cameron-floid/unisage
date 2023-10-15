from datetime import datetime


class Formatting:

    def __init__(self):
        pass

    @staticmethod
    def to_human_date(date_str: str) -> str:
        try:
            # Assuming the input date_str is in ISO format
            date_object = datetime.fromisoformat(date_str)
            formatted_date = date_object.strftime("%dth %B, %Y")
            return formatted_date
        except ValueError:
            return date_str  # Return the original string if it's not a valid date

    def print_dict_hierarchy(self, dictionary: dict, indentation=0):
        print(f"{' ' * (indentation - 4)}{dictionary['name'].upper()}")
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(f"{' ' * indentation}{key.capitalize()}:")
                self.print_dict_hierarchy(value, indentation + 8)
            elif key.lower().endswith('_date') and isinstance(value, str):
                formatted_date = self.to_human_date(value)
                print(f"{' ' * indentation}{key.capitalize()}: {formatted_date}")
            else:
                print(f"{' ' * indentation}{key.capitalize()}: {value}")
        print()
