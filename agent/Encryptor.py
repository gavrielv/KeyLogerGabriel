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
            for item  in self.data:
                result +=[chr(ord(i) ^ self.key) for i in item ]
        else: # המפתח הינו מחרוזת
            keylen = len(self.key)
            i = 0
            for item  in self.data:
                for j in item:
                    i %= keylen
                    result.append(chr(ord(j) ^ ord(self.key[i])))
                    i += 1
        return "".join(result)

    def decrypt(self) -> str:
        """פענוח הנתונים"""
        return self.encrypt()

# הושלם