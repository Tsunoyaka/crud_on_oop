from datetime import datetime

class Id:
    def __init__(self) -> None:
        self._id = self.generate_id()

    
    @staticmethod
    def generate_id():
        id = datetime.now().strftime('%M%S%f')[:-2]
        return id

    @property
    def id_(self):
        return self._id


class Time:
    def data_now(self):
        data_now = datetime.now()
        return str(data_now)
