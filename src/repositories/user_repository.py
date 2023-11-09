from sqlalchemy import insert, select, update
from src.utils.repository import SQLAlchemyRepository
from src.models.user_model import User
from src.auth.auth_jwt import pwd_context
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


class UserRepository(SQLAlchemyRepository):
    model = User

    async def register(self, data: dict) -> int:
        data["password"] = pwd_context.hash(data["password"])
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    def authenticate(self):
        # TODO Add authentication
        pass
