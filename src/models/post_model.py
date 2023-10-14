from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.database.mixin import MixinCRUD
from typing import Text, List
from src.models.comment_model import Comment
from src.schemas.post_schema import PostSchemaRead
from src.database.database import Base


class Post(Base, MixinCRUD):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[Text] = mapped_column(nullable=False)
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    def to_read_schema(self) -> PostSchemaRead:
        return PostSchemaRead(
            id=self.id,
            header=self.header,
            body=self.body
        )
