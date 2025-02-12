from abc import abstractmethod, ABC
class KeyLoggerService:
    @abstractmethod
    def start_logging(self):
        pass
    @abstractmethod
    def stop_logging(self):
        pass
    @abstractmethod
    def get_logged_keys(self):
        pass

# start_logging()
# stop_logging()
# get_logged_keys()