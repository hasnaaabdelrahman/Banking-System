import uuid
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from DB.db import Base


class User(Base):
    __tablename__ = 'users'
    id: Mapped[str] = mapped_column(
        String,
        primary_key = True,
        default= lambda: str(uuid.uuid4())
    )
    username: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique = True,
    )
    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique = True,
    )
    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    img_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    bank_account = relationship(
        "BankAccount", # class name
        back_populates="user", # point to relationship variable in another class
    )
