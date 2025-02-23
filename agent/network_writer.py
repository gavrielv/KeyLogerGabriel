import requests
from datetime import datetime
from I_Writer import IWriter


class NetworkWriter(IWriter):
    """שליחת נתונים לשרת"""

    def __init__(self, url: str):
        self.url = url
        self.time_now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def send_data(self, data, machine_name: str):
        """שליחת הנתונים בתוספת שם המחשב (נכנס כפרמטר) ובתוספת זמן"""
        data = {'mac':machine_name,'time':self.time_now,'data':data}
        try:
            requests.post(self.url + '/api/upload', json=data, timeout=5)
        except Exception as e:
            self.send_error(e)

    def send_error(self, error_data):
        """ניסיון שליחת סוג השגיאה לשרת באם התרחשה"""
        try:
            requests.post(self.url + '/api/error', json={f'Error time: {self.time_now}': str(error_data)}, timeout=5)
        except requests.exceptions.RequestException:
            pass