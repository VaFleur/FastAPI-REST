from src.utils.repository import SQLAlchemyRepository
from src.models.role_model import Role


class RoleRepository(SQLAlchemyRepository):
    model = Role
