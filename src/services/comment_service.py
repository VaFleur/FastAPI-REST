from src.schemas.comment_schema import CommentSchemaAdd
from src.utils.repository import AbstractRepository


class CommentService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo

    async def add_comment(self, schema: CommentSchemaAdd):
        comment_dict = schema.model_dump()
        comment_id = await self.repo.add_one(comment_dict)
        return comment_id

    async def get_comments(self):
        comments = await self.repo.find_all()
        return comments
