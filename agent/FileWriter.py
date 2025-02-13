from abc import abstractmethod, ABC
import json


class FileWriter(ABC):
    """
    מחלקה הניתנת למימוש באמצעות ירושה,
    מיועדת להצפנת נתונים והעלתם לקובץ,
    בהתאם למימוש המחלקה היורשת
    """

    def __init__(self, data: dict = None):
        self.data = data if data is not None else {}

    def data_receiver(self, buffer: dict) -> None:
        """קבלת מילון עם הנתונים"""
        self.data = buffer

    @abstractmethod

    def data_encrypter(self) -> None:
        """ביצוע ההצפנה - חובה למימוש בעת הירושה"""
        pass

    @abstractmethod

    def file_writer_with_timestamp(self) -> None:
        """כתיבה לקובץ - חובה למימוש בעת הירושה"""
        pass


class EncrypterFileWriter(FileWriter):
    """
    מחלקה המממשת הצפנה בשיטת {encrypter}
    ומעלה את התוכן לקובץ {Key_Logger.txt}
    """

    def data_encrypter(self) -> None:
        """מימוש ההצפנה על בסיס הגדלת כל תו בשלוש ספרות"""
        for datetime, sentence in self.data.items():
            encrypter_result = ""
            for char in sentence:
                encrypter_result += chr(ord(char) + 3)
            self.data[datetime] = encrypter_result

    def file_writer_with_timestamp(self) -> None:
        """מימוש כתיבה לקובץ בפורמט json"""
        json_data = json.dumps(self.data, ensure_ascii=False)
        with open('Key_Logger.txt', 'a', encoding='utf-8') as file:
            file.write(json_data + '\n')

# הושלם

