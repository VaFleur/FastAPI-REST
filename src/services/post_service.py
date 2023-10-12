from src.schemas.post_schema import PostSchemaAdd
from src.utils.repository import AbstractRepository


class PostService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo

    async def add_post(self, schema: PostSchemaAdd):
        post_dict = schema.model_dump()
        post_id = await self.repo.add_one(post_dict)
        return post_id

    async def get_posts(self):
        posts = await self.repo.find_all()
        return posts
