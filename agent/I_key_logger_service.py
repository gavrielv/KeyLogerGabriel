from abc import ABC, abstractmethod

class KeyLoggerService(ABC):



    @abstractmethod
    def _on_event(self, event):
        pass

    @abstractmethod
    def start_logging(self):
        pass

    @abstractmethod
    def stop_logging(self):
        pass

    @abstractmethod
    def get_logged_keys(self) -> list:
        pass
