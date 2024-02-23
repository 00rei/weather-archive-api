import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_API_URL = os.environ.get("WEATHER_API_URL")


def test():
    params = {'lat': 53.3606,
              'lon': 83.7636,
              'units': 'metric',
              'appid': str(WEATHER_API_KEY),
              'lang': 'ru'}

    r = []

    for _ in range(10):
        r.append(requests.get(
            WEATHER_API_URL,
            params=params).json())

    # response_json = res.json()
    # pprint.pprint(response_json)
    return r
