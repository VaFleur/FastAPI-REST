from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, relationship
from src.mixin import MixinCRUD
from typing import Text
from src.models.post_model import Post


class CommentBase(DeclarativeBase):
    pass


class Comment(CommentBase, MixinCRUD):
    __tablename__ = "comment_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[Text] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))
    post: Mapped["Post"] = relationship(back_populates="comments")

