import uuid
from datetime import datetime, timezone, timedelta

from fastapi import APIRouter

from src.api.dependencies import UOWDepends
from src.schemas.weather import WeatherAddDTO
from src.services.weather import WeatherService

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")
async def add_weather(uow: UOWDepends):
    # nnn = timezone(timedelta(seconds=25200))
    weather = WeatherAddDTO(
        city_id='9ebfe85c-1fda-4d57-85e6-8b40cccd1f3f',
        description='The weather',
        icon='icon',
        temperature=0,
        pressure=0,
        humidity=0,
        visibility=0,
        wind_speed=0,
        wind_direction=0,
        clouds=0,
        dt=datetime.fromtimestamp(1708487287, timezone.utc),
        sunrise=datetime.fromtimestamp(1708479161, timezone.utc),
        sunset=datetime.fromtimestamp(1708515898, timezone.utc),
        timezone=25200,
    )
    nnn = timezone(timedelta(seconds=25200))

    weather_id = await WeatherService.add_weather(uow, weather)

    return {"weather_id": weather_id}


@router.get("/{city_id}")
async def get_weather(city_id: uuid.UUID, uow: UOWDepends):
    return await WeatherService.get_weather_in_city(uow, city_id)
