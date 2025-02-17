import requests
from datetime import datetime
from I_Writer import Writer
from .env import URL


class NetworkSend(Writer):

    def send_data(self, machine_name: str):
        """שליחת נתונים לשרת"""
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {'mac':machine_name,"time":current_time,'data':self.data}
        try:
            response = requests.post(URL,json=data)
        # צריך להשלים


        # try:
        #     response = requests.post(URL, json=data, timeout=5)  # הגבלת זמן למניעת תקיעות
        #     response.raise_for_status()  # יוודא שהבקשה הצליחה (HTTP 200-299)
        #     return response.json()  # מחזיר את תשובת השרת בפורמט JSON
        # except requests.exceptions.Timeout:
        #     print("Error: Request timed out")
        #     return None
        # except requests.exceptions.RequestException as e:
        #     print(f"Error sending data: {e}")
        #     return None
