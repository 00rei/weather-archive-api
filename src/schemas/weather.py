import uuid
from datetime import datetime

from pydantic import BaseModel


class WeatherAddDTO(BaseModel):
    city_id: uuid.UUID
    description: str
    icon: str
    temperature: float
    pressure: int
    humidity: int
    visibility: int
    wind_speed: float
    wind_direction: int
    clouds: int
    dt: datetime
    sunrise: datetime
    sunset: datetime
    timezone: int


class WeatherDTO(WeatherAddDTO):
    id: uuid.UUID


class WeatherRelDTO(WeatherDTO):
    city: "CityDTO"
