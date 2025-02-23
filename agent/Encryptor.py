from I_Encryptor import IEncryptor


class XorEncryptor(IEncryptor):
    """
    הצפנה בשיטת {XOR}
    """

    def encrypt(self, data: list, key: str | int) -> str:
        """הצפנת הנתונים"""
        key = key % 256 if isinstance(key, int) else key
        result = []
        if isinstance(key, int): # המפתח הינו מספר
            for item  in data:
                result +=[chr(ord(i) ^ key) for i in item ]
        else: # המפתח הינו מחרוזת
            key_len = len(key)
            key_index = 0
            for item  in data:
                for char in item:
                    key_index %= key_len
                    result.append(chr(ord(char) ^ ord(key[key_index])))
                    key_index += 1
        return "".join(result)

    def decrypt(self, data: str, key: str | int) -> str:
        """פענוח הנתונים"""
        key = key % 256 if isinstance(key, int) else key
        result = ""
        if isinstance(key, int): # המפתח הינו מספר
            for char in data:
                result +=chr(ord(char) ^ key)
        else: # המפתח הינו מחרוזת
            for i in range(len(data)):
                result += chr(ord(data[i]) ^ ord(key[i % len(key)]))
        return result

# הושלם