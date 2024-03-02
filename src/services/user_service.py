from fastapi import HTTPException
from src.schemas.user_schema import UserCreate, UserUpdate
from src.utils.unit_of_work import IUnitOfWork


class UserService:
    @staticmethod
    async def get_users(uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users

    @staticmethod
    async def add_user(uow: IUnitOfWork, data: UserCreate):
        data_dict = data.model_dump()
        async with uow:
            user_id = await uow.posts.add_one(data_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def edit_user(uow: IUnitOfWork, user_id: int, data: UserUpdate):
        data_dict = data.model_dump()
        async with uow:
            user_id = await uow.users.update_one(user_id, data_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def delete_user(uow: IUnitOfWork):
        async with uow:
            await uow.posts.delete_one()
