import json
import requests
from config import keys




class MyException(Exception):
    pass

class Convertor():
    @staticmethod
    def convert(quote:str, base:str, amount:str):
        if quote == base:
            raise MyException(f'Перевод одинаковой валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise MyException(f'Не обработалась валюта {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise MyException(f'Не обработалась валюта {base}')

        try:
            amount = float(amount)
        except KeyError:
            raise MyException(f'Не обработалось число {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total = json.loads(r.content)[keys[base]]
        return total