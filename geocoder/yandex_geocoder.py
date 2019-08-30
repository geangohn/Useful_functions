#!pip install requests

import requests

api_key = '805edf7f-f2dd-430b-bb89-7ae5a7787f8b'   # взять из личного кабинета разработчика на сайте Яндекса
def get_lat_lon(location_name):
    if type(location_name) == str:
        response = requests.get('https://geocode-maps.yandex.ru/1.x/?format=json&apikey=' + api_key + '&geocode=' + location_name)
        response = response.json()
        coord = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        lat, lon = float(coord[1]), float(coord[0])

        return lat, lon
    else:
        return None, None
