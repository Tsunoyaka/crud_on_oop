from classes.models import House
from classes.managers import HouseManager
from classes.parsing import ModelParse


class Crud(HouseManager, ModelParse):
    _model = House 
    
    def help(self):
        print(
            """
            parsing - парсинг
            list - список записей
            details - получение одной записи
            update - обновление записи
            delete - удаление записи
            max view - дом с наибольшим кол-ом просмотров
            help - список команд
            quit - выход
            """
        )

    def start(self):
        commands = {
            'parsing': self.parse_model_from_cards,
            'list': self.get_hous_list,
            'details': self.get_hous,
            'update': self.update_object_in_DB,
            'delete': self.delete_object_from_DB,
            'max view': self.max_view,
            'help': self.help
        }
        while True:
            command = input('Введите команду или help для списка команд: ').lower().strip()
            if command in commands:
                    commands[command]()
            elif command == 'quit':
                print('Выход')
                break
            else:
                print('Такой команды нет')

a = Crud()
a.start()

