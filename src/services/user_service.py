from fastapi import HTTPException

from src.auth.auth_jwt import pwd_context, create_jwt_token
from src.schemas.user_schema import UserSchemaAdd, UserSchemaEdit
from src.utils.unit_of_work import IUnitOfWork


class UserService:
    @staticmethod
    async def get_users(uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    @staticmethod
    async def add_user(uow: IUnitOfWork, data: UserSchemaAdd):
        data_dict = data.model_dump()
        async with uow:
            user_id = await uow.posts.add_one(data_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def edit_user(uow: IUnitOfWork, user_id: int, data: UserSchemaEdit):
        data_dict = data.model_dump()
        async with uow:
            user_id = await uow.users.update_one(user_id, data_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def delete_user(uow: IUnitOfWork):
        async with uow:
            await uow.posts.delete_one()

    @staticmethod
    async def register_user(uow: IUnitOfWork, data: dict) -> dict:
        data["password"] = pwd_context.hash(data["password"])
        async with uow:
            await uow.posts.add_one(data)
            await uow.commit()
            return data

    @staticmethod
    async def authenticate_user(uow: IUnitOfWork, data: dict) -> dict:  # Подкорректировать, возможна ошибка
        async with uow:
            user = await uow.users.find_one(data["username"])

        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")

        is_password_correct = pwd_context.verify(data["password"], user["password"])

        if not is_password_correct:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        jwt_token = create_jwt_token({"sub": user.username})
        return {"access_token": jwt_token, "token_type": "bearer"}

    # TODO доработать