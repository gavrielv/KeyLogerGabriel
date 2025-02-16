from I_Encryptor import Encryptor


class XorEncryptor(Encryptor):
    """הצפנה בשיטת {XOR} על פי המפתח שהוזן"""

    def encrypt(self) -> str:
        """הצפנת הנתונים"""
        result = []
        if isinstance(self.key, int): #המפתח הינו מספר
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