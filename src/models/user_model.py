from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database.mixin import MixinCRUD
from src.database.database import Base


class User(SQLAlchemyBaseUserTable[int], Base, MixinCRUD):
    __tablename__ = 'user_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role_table.id", use_alter=True))

    def to_read_schema(self):
        pass
