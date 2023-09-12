from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from src.auth.mixin import MixinCRUD


class Base(DeclarativeBase):
    pass


class Role(Base, MixinCRUD):
    __tablename__ = 'role_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[dict] = mapped_column(type_=JSON, nullable=True)


class User(SQLAlchemyBaseUserTable[int], Base, MixinCRUD):
    __tablename__ = 'user_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role_table.id", use_alter=True))
