import requests
import datetime
from bs4 import BeautifulSoup
from bs4 import Tag, ResultSet
from decimal import *



HOST = 'https://www.house.kg/'
Categor = 'kupit'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

def get_html(url: str=HOST, category: str=Categor, headers: dict=HEADERS, params: str=''):
    """ Функция для получения html кода """
    html = requests.get(
        url + category,
        headers=headers,
        params=params,
        verify=False
    )
    return html.text


def get_card_from_html(html: str=get_html()):
    """ Функция для получения карточек из html кода """
    soup = BeautifulSoup(html, 'lxml')
    cards: ResultSet = soup.find_all('div', class_='listing')
    return cards
    

def conver_date(number: int, type_) -> datetime:
    if type_ == "день":
        super_data = datetime.datetime.now() - datetime.timedelta(days=number)  
    elif type_ == "час":
        super_data = datetime.datetime.now() - datetime.timedelta(hours=number)
    elif type_ == "минуты":
        super_data = datetime.datetime.now() - datetime.timedelta(minutes=number)
    return str(super_data)[:-7]


class ModelParse:
    def parse_model_from_cards(self, cards=get_card_from_html()):
        """ Фильтрация данных из карточек """
        # Json = HouseManager()
        result = []
        print("""
        1 = Доллар
        2 = Сом
        """)
        num = input("Выберите валюту: ")
        for card in cards:
            def data():
                day = card.find('div', class_="additional-info").find('div', class_='left-side').text.strip().split('\n')[0]
                number, day_or_hours, _ = day.split(' ')
                number = int(number)
                if day_or_hours == "дней":
                    return conver_date(number, "день")   
                elif day_or_hours == "день":
                    return conver_date(number, "день")  
                elif day_or_hours == "дня":
                    return conver_date(number, "день")                    
                elif day_or_hours == "часов":
                    return conver_date(number, "час")
                elif day_or_hours == "часа":
                    return conver_date(number, "час")
                elif day_or_hours == "час":
                    return conver_date(number, "час")         
                elif day_or_hours == "минуты":
                   return conver_date(number, "минуты")   
            def pri():
                Key = float(card.find('div', class_='price').text.lstrip('$').replace(' ', '')) 
                if num == '1':
                    return Key
                elif num == '2':
                    USD = 81.54
                    return str(Decimal(Key*USD).quantize(Decimal('.00'), rounding=ROUND_UP))

            obj = self._model(
            title = card.find('p', class_='title').text.strip(),
            address = card.find('div', class_='address').text.strip().replace('\"', ''),
            price = float(pri()),
            date_db = data(),
            count_view = int(card.find('div', class_="additional-info").find('div', class_='left-side').text.strip().split('\n')[1])
            )
            result.append(obj.get_to_dict())
        print('Парсинг прошел успешно!')
        return self.write_to_db(result)   


class Price:
    info = {"""
    1 = Сом
    2 = Доллар
    """}
    def price(self, card=None):
        print(self.info)
        num = input('Выберите валюту: ')
        Key = int(card.find('div', class_='price').text.lstrip('$').replace(' ', ''))
        if num == '1':
            return Key*85
        elif num == '2':
            return Key