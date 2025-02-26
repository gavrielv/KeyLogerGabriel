from I_encryptor import IEncryptor


class XorEncryptor(IEncryptor):
    """
    XOR encryption method.
    """

    def encrypt(self, data: list, key: str | int) -> str:
        """Encrypt the data."""
        key = key % 256 if isinstance(key, int) else key
        result = []
        if isinstance(key, int):  # If the key is an integer
            for item in data:
                result += [chr(ord(i) ^ key) for i in item]
        else:  # If the key is a string
            key_len = len(key)
            key_index = 0
            for item in data:
                for char in item:
                    key_index %= key_len
                    result.append(chr(ord(char) ^ ord(key[key_index])))
                    key_index += 1
        return "".join(result)
