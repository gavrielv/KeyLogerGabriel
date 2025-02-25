from abc import abstractmethod, ABC


class IWriter(ABC):
    """
    תבנית למחלקה המיועדת לכתיבת/שליחת נתונים
    בוריאציות שונות, לפי המימוש
    """

    @abstractmethod
    def send_data(self, data, machine_name: str) -> None:
        """כתיבת/שליחת הנתונים"""
        pass