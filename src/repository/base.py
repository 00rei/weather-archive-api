from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def get_by_id(self, model_id):
        stmt = select(self.model).filter_by(id=model_id)
        res = await self.session.execute(stmt)
        res = res.scalar().to_read_model()
        # res = [row[0].to_read_model() for row in res.all()]
        return res

    async def get_all(self, filter_by: dict = None) -> object:
        stmt = select(self.model)
        if filter_by:
            stmt = stmt.filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
