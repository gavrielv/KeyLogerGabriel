from abc import ABC, abstractmethod


class IEncryptor(ABC):
    """תבנית למחלקה המצפינה נתונים"""

    @abstractmethod
    def encrypt(self, data, key: str | int):
        """הצפנת הנתונים"""
        pass

# הושלם