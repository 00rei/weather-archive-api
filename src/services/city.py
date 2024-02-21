from src.schemas.city import CityAddDTO, CityDTO
from src.utils.unitofwork import IUnitOfWork


class CityService:

    @staticmethod
    async def add_city(uow: IUnitOfWork, city: CityAddDTO) -> int:
        city_dict = city.model_dump()
        async with uow:
            city_id = await uow.city.add_one(city_dict)
            await uow.commit()
            return city_id

    @staticmethod
    async def get_city_by_id(uow, city_id) -> CityDTO:
        async with uow:
            city = await uow.city.get_by_id(city_id)
            return city

    @staticmethod
    async def get_cities(uow):
        async with uow:
            return await uow.city.get_all()
