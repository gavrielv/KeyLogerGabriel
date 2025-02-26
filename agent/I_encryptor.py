from abc import ABC, abstractmethod


class IEncryptor(ABC):
    """Interface for the data encryption class."""

    @abstractmethod
    def encrypt(self, data, key: str | int):
        """Encrypt the data."""
        pass
