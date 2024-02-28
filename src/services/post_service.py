from src.schemas.post_schema import PostSchemaAdd, PostSchemaEdit
from src.utils.unit_of_work import IUnitOfWork


class PostService:
    @staticmethod
    async def get_posts(uow: IUnitOfWork):
        async with uow:
            posts = await uow.posts.find_all()
            return posts

    @staticmethod
    async def add_post(uow: IUnitOfWork, data: PostSchemaAdd):
        data_dict = data.model_dump()
        async with uow:
            post_id = await uow.posts.add_one(data_dict)
            await uow.commit()
            return post_id

    @staticmethod
    async def edit_post(uow: IUnitOfWork, post_id: int, data: PostSchemaEdit):
        data_dict = data.model_dump()
        async with uow:
            post_id = await uow.posts.edit_one(post_id, data_dict)
            await uow.commit()
            return post_id

    @staticmethod
    async def delete_one(uow: IUnitOfWork):
        async with uow:
            await uow.posts.delete_one()
