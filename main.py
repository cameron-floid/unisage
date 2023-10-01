from UI import CMDUI
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    cmd_ui = CMDUI()
    cmd_ui.run()
