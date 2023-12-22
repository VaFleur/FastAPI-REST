from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database.mixin import MixinCRUD
from src.database.database import Base
from src.schemas.user_schema import UserSchema


class User(Base, MixinCRUD):
    __tablename__ = 'user_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column()
    role_id: Mapped[int] = mapped_column(ForeignKey("role_table.id", use_alter=True))
    password: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            username=self.username,
            email=self.email,
            role_id=self.role_id,
            password=self.password,
        )
