from I_Encryptor import Encryptor


class XorEncryptor(Encryptor):
    """
    הצפנה בשיטת {XOR} על פי המפתח שהוזן,
    בעת יצירת מופע יש להכניס בפרמטרים את
    הנתונים ומפתח ההצפנה
    """

    def __init__(self, data, key: str | int):
        """טיפול במקרה של קוד מספרי ארוך"""
        super().__init__(data, key)
        self.key = self.key % 256 if isinstance(self.key, int) else self.key

    def encrypt(self) -> str:
        """הצפנת הנתונים"""
        result = []
        if isinstance(self.key, int): # המפתח הינו מספר
            for char in self.data:
                result.append(chr(ord(char ^ self.key)))
        else: # המפתח הינו מחרוזת
            for i in range(len(self.data)):
                result.append(chr(ord(self.data[i]) ^ ord(self.key[i % len(self.key)])))
        return "".join(result)

    def decrypt(self) -> str:
        """פענוח הנתונים"""
        return self.encrypt()

# הושלם