from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Text, List, TYPE_CHECKING
# from src.models.comment_model import Comment
from src.schemas.post_schema import PostSchema
from src.database.database import Base


if TYPE_CHECKING:
    from src.models.comment_model import Comment


class Post(Base):
    __tablename__ = "post_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(nullable=False, unique=True)
    body: Mapped[Text] = mapped_column(nullable=False, unique=True)
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")

    def to_read_model(self) -> PostSchema:
        return PostSchema(
            id=self.id,
            header=self.header,
            body=self.body
        )
