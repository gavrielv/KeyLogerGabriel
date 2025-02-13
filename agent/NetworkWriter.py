from abc import abstractmethod, ABC

class NetworkWriter:

    @abstractmethod
    def data_input_receiver(self):
        pass

    @abstractmethod
    def send_to_server(self):
        pass


# מקבל נתונים
# שולח לשרת באמצעות IWriter