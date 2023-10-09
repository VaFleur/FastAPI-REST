from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship
from src.mixin import MixinCRUD
from typing import Text, List
from src.models.comment_model import Comment


class PostBase(DeclarativeBase):
    pass


class Post(PostBase, MixinCRUD):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[Text] = mapped_column(nullable=False)
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")
