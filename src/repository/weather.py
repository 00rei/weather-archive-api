from src.models.weather import Weather
from src.repository.base import BaseRepository


class WeatherRepository(BaseRepository):
    model = Weather
