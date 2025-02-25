import json
import os
from dotenv import load_dotenv

load_dotenv()

class ComputersNames:
    """
    ניהול וגישה למאגר המחשבים שבמעקב
    """

    def __init__(self, computers_file):
        """איתחול המאגר במידע השמור + קבלת נתיב לקובץ המאגר"""
        self.computers_file = computers_file
        try:
            if os.path.exists(computers_file):
                with open(computers_file, 'r') as file:
                    self.computers = json.load(file)
            else:
                self.computers = {'names':{}, 'unknown': {}}
        except Exception as e:
            self.computers = {'Error':f'Error reading file: {str(e)}'}

    def get_name(self, mac: str) -> str | None:
        """מחזירה את שם המחשב במידה וקיים במאגר"""
        if mac in self.computers['names']:
            return self.computers['names'][mac]
        elif mac in self.computers['unknown']:
            return f"unknown{self.computers['unknown'][mac]}"
        return None


    def add(self, mac_address: str, name: str | None = None) -> dict:
        """הוספת מחשב חדש למאגר, מחזירה האם השמירה לקובץ הצליחה"""
        if mac_address in self.computers['names'] or mac_address in self.computers['unknown']:
            return {False: 'Already in data (use update to change)'}
        if name:
            self.computers['names'][mac_address] = name
        else:
            self.computers['unknown'][mac_address] = max(self.computers['unknown'].values(), default=0) + 1
        return self._save()

    def update(self, mac_address: str, name: str) -> dict:
        """עדכון שם לכתובת mac קיימת"""
        if mac_address in self.computers['names']:
            self.computers['names'][mac_address] = name
            return {'Status': 'Successful update'}
        elif mac_address in self.computers['unknown']:
            self.computers['unknown'][mac_address] = name
            return {}
        return {'Error': 'Not find error'}

    def delete(self, mac_address: str) -> dict:
        """מחיקת מחשב מהמאגר, מחזירה סטטוס המחיקה"""
        is_changed = False
        if mac_address in self.computers['names']:
            del self.computers['names'][mac_address]
            is_changed = True
        elif mac_address in self.computers['unknown']:
            del self.computers['unknown'][mac_address]
            is_changed = True
        if is_changed:
            return self._save()
        return {False: "not find"}

    def _save(self) -> dict:
        """שמירת השינויים לקובץ, מחזירה סטטוס השמירה"""
        try:
            with open(self.computers_file, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.computers, ensure_ascii=False))
                return {'Status': "Saving successfully"}
        except Exception as e:
            return {'Error': f'Error reading file: {str(e)}'}
