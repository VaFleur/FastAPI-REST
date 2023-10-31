from src.schemas.comment_schema import CommentSchemaAdd, CommentSchemaEdit, CommentHistorySchemaAdd
from src.utils.unit_of_work import IUnitOfWork


class CommentService:
    @staticmethod
    async def get_comments(uow: IUnitOfWork):
        async with uow:
            comments = await uow.comments.find_all()
            return comments

    @staticmethod
    async def get_comment_history(uow: IUnitOfWork):
        async with uow:
            history = await uow.comment_history.find_all()
            return history

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
            await uow.comments.edit_one(comment_id, data_dict)

            current_comment = await uow.comments.find_one(id=comment_id)
            comment_history_log = CommentHistorySchemaAdd(
                post_id=current_comment.post_id,
                comment_id=comment_id,
                previous_body=current_comment.body,
                new_body=data.body,
            )
            comment_history_log = comment_history_log.model_dump()
            await uow.comment_history.add_one(comment_history_log)
            await uow.commit()

    @staticmethod
    async def delete_comment(uow: IUnitOfWork):
        async with uow:
            await uow.comments.delete_one()
