from os import path
import json


class UsersData:
    """Managing and accessing the users names and their passwords"""

    def __init__(self, users_file_path):
        self.users_file_path = users_file_path
        try:
            if path.exists(users_file_path):
                with open(users_file_path, 'r', encoding='utf-8') as file:
                    self.users = json.load(file)
            else:
                self.users = {}
        except Exception as e:
            self.users = {'Error': f'Error reading file: {str(e)}'}

    def check_user(self, user, password) -> bool:
        """Validates the username and password against the database"""
        return self.users.get(user) == password

    def add(self, user, password):
        """Adds a user to the database, returns the status of the addition"""
        if user in self.users:
            return {'Error': 'User already exists'}
        self.users[user] = password
        return self._save()

    def delete(self, user, password):
        """Removes a user from the database, returns the status of the deletion"""
        if user not in self.users:
            return {'Error': 'User not found'}
        del self.users[user]
        return self._save()

    def _save(self) -> dict:
        """Saves changes to the file, returns the status of the save"""
        try:
            with open(self.users_file_path, 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.users, ensure_ascii=False, indent=4))
                return {'Status': "Saving successfully"}
        except Exception as e:
            return {'Error': f'Error writing file: {str(e)}'}
