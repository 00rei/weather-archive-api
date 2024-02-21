from src.schemas.weather import WeatherAddDTO, WeatherDTO
from src.utils.unitofwork import IUnitOfWork


class WeatherService:

    @staticmethod
    async def add_weather(uow: IUnitOfWork, weather: WeatherAddDTO) -> int:
        weather_dict = weather.model_dump()
        async with uow:
            weather_id = await uow.weather.add_one(data=weather_dict)
            await uow.commit()
            return weather_id

    @staticmethod
    async def get_weather_in_city(uow: IUnitOfWork, city_id):
        async with uow:
            filter_by = {"city_id": city_id}
            return await uow.weather.get_all(filter_by=filter_by)
            