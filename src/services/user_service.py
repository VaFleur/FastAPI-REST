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
    async def edit_post(uow: IUnitOfWork, post_id: int, data: UserSchemaEdit):
        data_dict = data.model_dump()
        async with uow:
            await uow.posts.edit_one(post_id, data_dict)

            current_post = await uow.posts.find_one(id=post_id)
            post_history_log = PostHistorySchemaAdd(
                post_id=post_id,
                previous_header=current_post.header,
                previous_body=current_post.body,
                new_header=data.header,
                new_body=data.body,
            )
            post_history_log = post_history_log.model_dump()
            await uow.post_history.add_one(post_history_log)
            await uow.commit()

    @staticmethod
    async def delete_one(uow: IUnitOfWork):
        async with uow:
            await uow.posts.delete_one()
