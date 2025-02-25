from os import path
import json


class UsersData:
    """ניהול וגישה למאגר שמות המשתמשים וסיסמאותיהם"""

    def __init__(self, users_file_path):
        self.users_file_path = users_file_path
        try:
            if path.exists(users_file_path):
                with open(users_file_path, 'r') as file:
                    self.users = json.load(file)
            else:
                self.users = {}
        except Exception as e:
            self.users = {'Error': f'Error reading file: {e}'}

    def check_user(self, user, password) -> bool:
        """מחזירה אם שם המשתמש והסיסמה קיימים ותואמים"""
        return self.users.get(user) == password

    def add(self, user, password):
        """הוספת מחשב חדש למאגר, מחזירה האם השמירה לקובץ הצליחה"""
        pass

    def delete(self, user, password):
        """מחיקת מחשב מהמאגר, מחזירה האם השמירה לקובץ הצליחה"""
        is_changed = False
        pass

    # TODO fix except
    def _save(self) -> bool:
        """שמירת השינויים לקובץ"""
        try:
            with open(self.users_file_path, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.users, ensure_ascii=False))
                return True
        except Exception as e:
            return False
