from src.utils.repository import SQLAlchemyRepository
from src.models.comment_model import Comment


class CommentRepository(SQLAlchemyRepository):
    model = Comment
