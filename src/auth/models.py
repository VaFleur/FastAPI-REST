from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from src.database.mixin import MixinCRUD


class AuthBase(DeclarativeBase):
    pass


class Role(AuthBase, MixinCRUD):
    __tablename__ = 'role_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[dict] = mapped_column(type_=JSON, nullable=True)


class User(SQLAlchemyBaseUserTable[int], AuthBase, MixinCRUD):
    __tablename__ = 'user_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role_table.id", use_alter=True))
