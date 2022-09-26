import json
from pprint import pprint

class HouseManager:

    def get_db(self):
        with open('DB.json', 'r') as file:
            return json.load(file)

    def write_to_db(self, data):
        with open('DB.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_hous_list(self):
        data = self.get_db()
        pprint(data, sort_dicts=False)

    def get_hous(self):
        id = input('Введите id: ')
        data = self.get_db()
        for hous in data:
            if hous['id'] == id:
                pprint(hous, sort_dicts=False)
                return hous
        print('Нет дома под таким Id!')

    def update_object_in_DB(self):
        data = self.get_db()
        id = self.get_hous()
        if id is not None:
            data.remove(id)
            title = input('Введите данные дома: ')
            address = input('Введите адрес: ')
            price = float(input('Введите цену: '))
            date_db = id["date_db"]
            count_view = id['count_view']
            new_hous = self._model(title=title, address=address, price=price, date_db=date_db, count_view=count_view)
            new_hous.__dict__['id'] = id ['id']
            data.append(new_hous.as_dict)
            self.write_to_db(data)               
            print('Успешно обновлено!')

    def delete_object_from_DB(self):
        data = self.get_db()
        id = self.get_hous()
        if id is not None:
            data.remove(id)
            self.write_to_db(data)
            print('Успешно удалено!')

    def max_view(self):
        data = self.get_db()
        maxi = 0
        for i in data:
            if i['count_view'] > maxi:
                maxi = i['count_view']
        for i in data:
            if i['count_view'] == maxi:
                print(i)
                return i
        # x = list(filter(lambda data: data))

        

                

                

