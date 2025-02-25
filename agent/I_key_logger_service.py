from abc import ABC, abstractmethod

class IKeyLoggerService(ABC):
    """ ממשק למחלקת הקלטת מקשים """

    """" פונקציה פרטית שתפעל בהקשה על מקש """
    @abstractmethod
    def _on_event(self, event):
        pass
    
    """"" פונקציה להתחלת הקלטה"""
    @abstractmethod
    def start_logging(self):
        pass

    """" פונקציה לסיום הקלטה"""
    @abstractmethod
    def stop_logging(self):
        pass
    
    """" פונקציה לקבלת המקשים שנלחצו"""
    @abstractmethod
    def get_logged_keys(self) -> list:
        pass
