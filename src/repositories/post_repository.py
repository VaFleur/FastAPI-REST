from src.utils.repository import SQLAlchemyRepository
from src.models.post_model import Post


class PostRepository(SQLAlchemyRepository):
    model = Post
