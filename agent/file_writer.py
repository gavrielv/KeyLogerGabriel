from I_writer import IWriter
from datetime import datetime
import json


class FileWriter(IWriter):
    """
    Writing data to a file in {json} format,
    with the addition of the current date and time to each write.
    The data must be of type {str}.
    """

    def send_data(self, data, file_name: str) -> None:
        """Write data to a {json} file with a timestamp."""
        if (data is None) or (not isinstance(data, str)):
            raise ValueError('The data was not received or is not of type string.')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_with_time = {current_time: data}
        json_data = json.dumps(data_with_time, ensure_ascii=False)
        try:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(json_data + '\n')
        except Exception as e:
            print(f'error: {e}')
