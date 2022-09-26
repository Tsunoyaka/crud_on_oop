import datetime
from utils import Id

class House:
    def __init__(
        self,
        title: str,
        address: str,
        price: float,
        count_view:int,
        date_db: datetime.date,
        *args, **kwargs
        ):
        self.id = Id().id_
        self.title = title
        self.address = address
        self.price = price
        self.date_db = date_db
        self.count_view = count_view

    @property
    def as_dict(self):
        self.__dict__
        return self.__dict__


    def get_to_dict(self):
        result = self.__dict__
        result['date_db'] = str(result['date_db'])
        return result


# TODO методы для конвертирования времени
# TODO методы для конвертирования даты

# TODO методы для конвертирования цен в зависимости от выбора
# TODO методы для нахождени object(House) max количество просмотра по атрибуту

# TODO сохранять у себя ввиде json and send email 


