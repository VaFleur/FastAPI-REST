from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.database.mixin import MixinCRUD
from typing import Text
from src.models.post_model import Post
from src.schemas.comment_schema import CommentSchemaRead, CommentHistorySchemaRead
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


class CommentHistory(Base):
    __tablename__ = "comment_history_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    previous_body: Mapped[Text] = mapped_column(nullable=False)
    new_body: Mapped[Text] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))
    comment_id: Mapped[int] = mapped_column(ForeignKey("comment_table.id"))

    def to_read_model(self) -> CommentHistorySchemaRead:
        return CommentHistorySchemaRead(
            id=self.id,
            previous_body=self.previous_body,
            new_body=self.new_body,
            post_id=self.post_id,
            comment_id=self.comment_id,
        )
