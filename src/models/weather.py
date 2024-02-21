import uuid

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.schemas.weather import WeatherDTO


class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    city_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('city.id'), nullable=False)
    description: Mapped[str]
    icon: Mapped[str]
    temperature: Mapped[float]
    pressure: Mapped[int]
    humidity: Mapped[int]
    visibility: Mapped[int]
    wind_speed: Mapped[float]
    wind_direction: Mapped[int]
    clouds: Mapped[int]
    dt: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    sunrise: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    sunset: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    timezone: Mapped[int]

    city: Mapped["City"] = relationship(
        back_populates="weather"
    )

    # repr_cols_num = 3

    # repr_cols = ("created_at",)

    def to_read_model(self) -> WeatherDTO:
        return WeatherDTO.model_validate(self, from_attributes=True)
