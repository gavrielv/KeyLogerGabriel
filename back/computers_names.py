import json
import os


COMPUTERS_FILE = 'computers_names.json'

class Computers:
    """
    ניהול וגישה למאגר המחשבים שבמעקב
    """

    def __init__(self):
        """איתחול המאגר במידע השמור"""
        try:
            if os.path.exists(COMPUTERS_FILE):
                with open(COMPUTERS_FILE, 'r') as file:
                    self.computers = json.load(file)
            else:
                self.computers = {'names':{}, 'unknown': {}}
        except Exception as e:
            print(f'Error reading:{e}') # ????????????????????????????????????????????????

    def get_name(self, mac: str) -> str | None:
        """מחזירה את שם המחשב במידה וקיים במאגר"""
        if mac in self.computers['names']:
            return self.computers['names'][mac]
        elif mac in self.computers['unknown']:
            return f"unknown{self.computers['unknown'][mac]}"
        return None


    def add(self, mac_address: str, name: str | None = None) -> None:
        """הוספת מחשב חדש למאגר"""
        if name:
            self.computers['names'][mac_address] = name
        else:
            self.computers['unknown'][mac_address] = max(self.computers['unknown'].values(), default=0) + 1
        self._save()

    def delete(self, mac_address: str) -> None:
        """מחיקת מחשב מהמאגר"""
        is_changed = False
        if mac_address in self.computers['names']:
            del self.computers['names'][mac_address]
            is_changed = True
        elif mac_address in self.computers['unknown']:
            del self.computers['unknown'][mac_address]
            is_changed = True
        if is_changed:
            self._save()

    def _save(self) -> None:
        """שמירת השינויים לקובץ"""
        try:
            with open(COMPUTERS_FILE, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.computers, ensure_ascii=False))
        except Exception as e:
            print(f'Error writing:{e}') # ????????????????????????????????????????????????
