from abc import abstractmethod, ABC


class FileWriter(ABC):
    """
    תבנית למחלקה המיועדת לכתיבה לקובץ
    בוריאציות שונות, לפי המימוש
    """

    def __init__(self, data = None):
        """קבלת הנתונים, אפשר לקבלם גם באמצעות מתודה ייעודית דלהלן"""
        self.data = data

    def data_receiver(self, data) -> None:
        """קבלת הנתונים"""
        self.data = data

    @abstractmethod
    def file_writer(self, file_name: str) -> None:
        """כתיבה לקובץ"""
        pass

# הושלם