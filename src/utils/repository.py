from abc import ABC, abstractmethod
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):

    @abstractmethod
    async def add_one(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, *args):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()  # Проверить работу

    async def edit_one(self, instance_id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=instance_id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()  # Проверить работу

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]  # Проверить работу
        return res

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res  # Проверить работу
