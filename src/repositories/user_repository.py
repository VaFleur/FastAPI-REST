from src.utils.repository import SQLAlchemyRepository
from src.models.user_model import User


class UserRepository(SQLAlchemyRepository):
    model = User
