from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from src.database.mixin import MixinCRUD
from src.database.database import Base


class Role(Base, MixinCRUD):
    __tablename__ = 'role_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[dict] = mapped_column(type_=JSON, nullable=True)

    def to_read_schema(self):
        pass
