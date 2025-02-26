from abc import ABC, abstractmethod


class IKeyLoggerService(ABC):
    """Interface for the key logging class."""

    @abstractmethod
    def _on_event(self, event):
        """Private function that will be triggered on key press."""
        pass

    @abstractmethod
    def start_logging(self):
        """Function to start logging."""
        pass

    @abstractmethod
    def stop_logging(self):
        """Function to stop logging."""
        pass

    @abstractmethod
    def get_logged_keys(self) -> list:
        """Function to get the pressed keys."""
        pass
