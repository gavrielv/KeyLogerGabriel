from abc import abstractmethod, ABC
class FileWriter:
    @abstractmethod
    def data_receiver  (self):
        pass
    @abstractmethod
    def data_encrypter  (self):
        pass
    @abstractmethod
    def file_writer_with_timestamp(self):
        pass
# מקבל נתונים
# מצפין באמצעות Encryptor
# כותב לקובץ עם חותמת זמן
