from src.schemas.comment_schema import CommentSchemaAdd, CommentSchemaEdit
from src.utils.unit_of_work import IUnitOfWork


class CommentService:
    @staticmethod
    async def get_comments(uow: IUnitOfWork):
        async with uow:
            comments = await uow.comments.find_all()
            return comments

    @staticmethod
    async def add_comment(uow: IUnitOfWork, data: CommentSchemaAdd):
        data_dict = data.model_dump()
        async with uow:
            comment_id = await uow.comments.add_one(data_dict)
            await uow.commit()
            return comment_id

    @staticmethod
    async def edit_comment(uow: IUnitOfWork, comment_id: int, data: CommentSchemaEdit):
        data_dict = data.model_dump()
        async with uow:
            comment_id = await uow.comments.edit_one(comment_id, data_dict)
            await uow.commit()
            return comment_id

    @staticmethod
    async def delete_comment(uow: IUnitOfWork):
        async with uow:
            await uow.comments.delete_one()
