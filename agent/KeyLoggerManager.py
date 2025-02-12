from abc import abstractmethod, ABC
class KeyLoggerManager:
    @abstractmethod
    def collect_keystrokes_interval (self):
        pass
    @abstractmethod
    def buffer_collector (self):
        pass
    @abstractmethod
    def data_dispatcher (self):
        pass

# אוסף הקשות כל X שניות
# מאגד ל-Buffer
# מעביר ל-
# FileWriter/NetworkWriter
