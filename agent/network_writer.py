import requests
from datetime import datetime

from fontTools.merge.util import current_time

from I_Writer import IWriter


class NetworkWriter(IWriter):
    """שליחת נתונים לשרת"""

    def __init__(self, url: str):
        self.url = url

    def send_data(self, data, machine_name: str):
        """שליחת הנתונים בתוספת שם המחשב (נכנס כפרמטר) ובתוספת זמן"""
        time_now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        data = {'mac':machine_name,'time':time_now,'data':data}
        try:
            requests.post(self.url + '/api/upload', json=data, timeout=5)
        except Exception as e:
            self.send_error(e)

    #TODO: use it in manager
    def send_error(self, error_data):
        """ניסיון שליחת סוג השגיאה לשרת באם התרחשה שגיאה בצד המחשב הנעקב"""
        try:
            requests.post(self.url + '/api/error', json={f'Error time: {datetime.now()}': str(error_data)}, timeout=5)
        except requests.exceptions.RequestException:
            pass