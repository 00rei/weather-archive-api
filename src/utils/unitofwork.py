from abc import ABC, abstractmethod
from typing import Type

from src.db.db import async_session_maker
from src.repository.city import CityRepository
from src.repository.weather import WeatherRepository


class IUnitOfWork(ABC):
    city: Type[CityRepository]
    weather: Type[WeatherRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.city = CityRepository(self.session)
        self.weather = WeatherRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
