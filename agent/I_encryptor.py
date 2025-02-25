from abc import ABC, abstractmethod


class IEncryptor(ABC):
    """תבנית למחלקה המצפינה נתונים"""

    @abstractmethod
    def encrypt(self, data, key: str | int):
        """הצפנת הנתונים"""
        pass

    @abstractmethod
    def decrypt(self, data, key: str | int):
        """פענוח הנתונים"""
        pass

# הושלם