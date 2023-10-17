from src.utils.repository import SQLAlchemyRepository
from src.models.comment_model import CommentHistory


class CommentHistoryRepository(SQLAlchemyRepository):
    model = CommentHistory
