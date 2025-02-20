import os
import requests
from datetime import datetime
from I_Writer import Writer
from dotenv import load_dotenv

load_dotenv()


class NetworkSend(Writer):
    """שליחת נתונים לשרת"""

    def send_data(self, machine_name: str):
        """שליחת הנתונים בתוספת שם המחשב (נכנס כפרמטר) ובתוספת זמן"""
        url = os.getenv('URL')
        if not url:
            return
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {'mac':machine_name,"time":current_time,'data':self.data}
        try:
            requests.post(url, json=data, timeout=5)
        except:
            pass