from fastapi import HTTPException
from sqlalchemy import insert, select, update
from src.utils.repository import SQLAlchemyRepository
from src.models.user_model import User
from src.auth.auth_jwt import pwd_context
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


class UserRepository(SQLAlchemyRepository):
    model = User

    async def register(self, data: dict) -> dict:
        data["password"] = pwd_context.hash(data["password"])
        stmt = insert(self.model).values(**data).returning(self.model.id)
        await self.session.execute(stmt)
        return data

    async def authenticate(self, data: dict):  # Подкорректировать, возможна ошибка
        user = super().find_one(filter_by=data["username"])  # Получите пользователя из базы данных

        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        is_password_correct = pwd_context.verify(data["password"], user["password"])

        if not is_password_correct:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        jwt_token = create_jwt_token({"sub": user.username})
        return {"access_token": jwt_token, "token_type": "bearer"}

 #TODO доработать
