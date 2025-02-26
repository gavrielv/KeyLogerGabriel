from abc import abstractmethod, ABC


class IWriter(ABC):
    """
    Interface for a class that writes/sends data
    in different variations, depending on the implementation.
    """

    @abstractmethod
    def send_data(self, data, machine_name: str) -> None:
        """Write/send the data."""
        pass
