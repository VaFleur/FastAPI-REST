from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.database.mixin import MixinCRUD
from typing import Text, List
from src.models.comment_model import Comment
from src.schemas.post_schema import PostSchema
from src.schemas.post_schema import PostHistorySchemaRead
from src.database.database import Base


class Post(Base, MixinCRUD):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[Text] = mapped_column(nullable=False)
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    def to_read_schema(self) -> PostSchema:
        return PostSchema(
            id=self.id,
            header=self.header,
            body=self.body
        )


class PostHistory(Base):  # TODO проверить работу
    __tablename__ = "post_history_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post_table.id"))
    previous_header: Mapped[str] = mapped_column(ForeignKey("post_table.header"))
    previous_body: Mapped[Text] = mapped_column(ForeignKey("post_table.body"))
    new_header: Mapped[str] = mapped_column(ForeignKey("post_table.header"))
    new_body: Mapped[Text] = mapped_column(ForeignKey("post_table.header"))

    def to_read_model(self) -> PostHistorySchemaRead:
        return PostHistorySchemaRead(
            id=self.id,
            post_id=self.post_id,
            previous_header=self.previous_header,
            previous_body=self.previous_body,
            new_header=self.new_header,
            new_body=self.new_body,
        )
