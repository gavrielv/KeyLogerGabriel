import json
import os
from computers_names import ComputersNames
from users_data import UsersData
from datetime import datetime
from flask import request


class RequestFunctions:

    def __init__(self, base_dir_path: str, decryption_key, computer_file_path: str, users_file_path: str):
        """
        אתחול מופע למחלקה שאחראית על שמות המחשבים שבמעקב,
        קבלת נתיב לספריית בסיס המידע, קבלת מפתח ההצפנה
        """
        self.computers_names = ComputersNames(computer_file_path)
        self.users_data = UsersData(users_file_path)
        self.base_dir = base_dir_path
        self.decryption_key = decryption_key

    def upload(self):
        """העלאת מידע למאגר"""
        try:
            data = request.get_json()
            # בדיקת תקינות הנתונים
            if not isinstance(data, dict):
                return {'Error': 'Invalid JSON format'}
            mac = data.get('mac')
            time = data.get('time')
            log_data = data.get('data')
            if (not isinstance(mac, str)) or (not isinstance(time, str)) or (not isinstance(log_data, str)):
                return {'Error': 'Invalid payload'}

            # בדיקה שהזמן בפורמט הנדרש
            try:
                time_tamp = datetime.strptime(time, "%d-%m-%Y %H:%M:%S")
                file_name = f'{time_tamp.strftime("%d-%m-%Y")}.txt'
            except ValueError:
                return {'Error': 'Invalid time format'}

            # בירור שם המשתמש של המחשב
            try:
                machine = self.computers_names.get_name(mac)
                if not machine:
                    self.computers_names.add(mac)
                    machine = self.computers_names.get_name(mac)
            except Exception as e:
                return {'Error': f'Error find computer name {e}'}

            # במקרה של שגיאה בהוספת המחשב לקובץ המשמש את מחלקת ComputerNames
            if 'Error' in self.computers_names.computers:
                return {'Error': self.computers_names.computers['Error']}

            # הגדרת שם התיקייה ויצירתה במידת הצורך
            machine_folder = os.path.join(self.base_dir, machine)
            try:
                os.makedirs(machine_folder, exist_ok=True)
            except Exception as e:
                return {'Error': f'Error creating folder: {e}'}

            # עיצוב המידע והכנסתו לקובץ המתאים
            new_data = json.dumps({time: log_data})
            file_path = os.path.join(machine_folder, file_name)
            with open(file_path, 'a', encoding="utf-8") as file:
                file.write(new_data + '\n')
            return {"status": "success", "file": file_name}
        except Exception as e:
            return {'Error': f'Error processing upload: {e}'}

    def login(self):
        """אימות כניסת משתמש"""
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'Error': 'Invalid JSON format'}
            user_name = data.get('user_name')
            password = data.get('password')
            if not isinstance(user_name, str) or not isinstance(password, str):
                return {'Error': 'Invalid payload'}
            if self.users_data.check_user(user_name, password):
                return {'Status': 'Confirm'}
            return {'Failed': 'Not confirm'}
        except Exception as e:
            return {'Error': f'Data validation error: {e}'}

    def get_machines_names(self):
        """קבלת רשימת שמות המחשבים שבמעקב"""
        try:
            machines = os.listdir(self.base_dir)
            return {'machines': machines}
        except Exception as e:
            return {'Error': f'Error retrieving machine list: {e}'}

    def get_dates_by_name(self, name):
        """קבלת רשימת התאריכים שנאספו עד כה על מחשב ספציפי"""
        try:
            machine_path = os.path.join(self.base_dir, name)
            if not os.path.exists(machine_path):
                return {'Error': f'Machine folder "{name}" not found'}
            dates = os.listdir(machine_path)
            return {'dates': dates}
        except Exception as e:
            return {'Error': f'Error retrieving dates list: {e}'}

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
            data_path = os.path.join(self.base_dir, name, date)
            if not os.path.exists(data_path):
                return {'Error': f'Date file "{date}" not found'}

            try: # פתיחת הקובץ במצב קריאה, פענוח הנתונים והחזרתם בפורמט הנדרש
                result = {}
                with open(data_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        try:
                            data_dict = json.loads(line.strip())
                            for time, log_data in data_dict.items():
                                result[time] = self._decrypt(log_data, self.decryption_key)
                        except Exception as e:
                            return {'Error': f'Invalid JSON format in file: {e}'}
                return result
            except Exception as e:
                return {'Error': f'Error reading file: {e}'}
        except Exception as e:
            return {'Error': f'Error retrieving keystrokes: {e}'}
