from abc import ABC, abstractmethod


class Encryptor(ABC):
    """תבנית למחלקה המצפינה נתונים"""

    def __init__(self, data, key: str | int):
        """מקבל נתונים ומפתח להצפנה"""
        self.data = data
        self.key = key

    @abstractmethod
    def encrypt(self):
        """הצפנת הנתונים"""
        pass

    @abstractmethod
    def decrypt(self):
        """פענוח הנתונים"""
        pass

# הושלם