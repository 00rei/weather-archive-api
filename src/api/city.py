import uuid

from fastapi import APIRouter

from src.api.dependencies import UOWDepends
from src.schemas.city import CityAddDTO
from src.services.city import CityService

router = APIRouter(
    prefix='/city',
    tags=['City']
)


@router.post("/")
async def add_city(city: CityAddDTO, uow: UOWDepends):
    city_id = await CityService.add_city(uow=uow, city=city)

    return {"city_id": city_id}


@router.get("/{city_id}/")
async def get_city(city_id: uuid.UUID, uow: UOWDepends):
    city = await CityService.get_city_by_id(uow, city_id)
    return {"city": city}


@router.get("/")
async def get_all_cities(uow: UOWDepends):
    result = await CityService.get_cities(uow)
    return result
