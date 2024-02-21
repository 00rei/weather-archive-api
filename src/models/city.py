import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.schemas.city import CityDTO


class City(Base):
    __tablename__ = "city"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str]

    weather: Mapped[list["Weather"]] = relationship(
        back_populates="city"
    )

    def to_read_model(self) -> CityDTO:
        return CityDTO.model_validate(self, from_attributes=True)
