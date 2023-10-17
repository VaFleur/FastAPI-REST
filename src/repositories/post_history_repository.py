from src.utils.repository import SQLAlchemyRepository
from src.models.post_model import PostHistory


class PostHistoryRepository(SQLAlchemyRepository):
    model = PostHistory
