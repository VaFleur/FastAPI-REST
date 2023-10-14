from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.database.mixin import MixinCRUD
from typing import Text
from src.models.post_model import Post
from src.schemas.comment_schema import CommentSchemaRead
from src.database.database import Base


class Comment(Base, MixinCRUD):
    __tablename__ = "comment_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[Text] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))
    post: Mapped["Post"] = relationship(back_populates="comments")

    def to_read_model(self) -> CommentSchemaRead:
        return CommentSchemaRead(
            id=self.id,
            body=self.body,
            post_id=self.post_id,
        )
