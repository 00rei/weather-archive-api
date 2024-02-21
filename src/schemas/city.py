import uuid

from pydantic import BaseModel


class CityAddDTO(BaseModel):
    name: str


class CityDTO(CityAddDTO):
    id: uuid.UUID


class CityRelDTO(CityDTO):
    weather: list["WeatherDTO"]