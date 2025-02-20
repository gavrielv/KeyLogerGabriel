from abc import abstractmethod, ABC


class Writer(ABC):
    """
    תבנית למחלקה המיועדת לכתיבת/שליחת נתונים
    בוריאציות שונות, לפי המימוש
    """

    def __init__(self, data = None):
        """קבלת הנתונים, אפשר לקבלם גם באמצעות מתודה ייעודית דלהלן"""
        self.data = data

    def data_receiver(self, data) -> None:
        """קבלת הנתונים"""
        self.data = data

    @abstractmethod
    def send_data(self, machine_name: str) -> None:
        """כתיבת/שליחת הנתונים"""
        pass

# הושלם