import requests
import json


city = str(input('Enter city: '))
api_key = '59166b5860a0f23c4c72b89f6a8e7411'
url = f'http://api.openweathermap.org/data/2.5/find?q={city}&type=like&APPID={api_key}'


def weather():
    res = requests.get(url)
    # dict_weather = dict(res.json())
    # print(dict_weather.get('weather'))
    data = dict(res)
    print(data('weather'))


weather()
