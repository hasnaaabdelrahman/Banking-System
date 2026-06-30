import uuid
from sqlalchemy import Float, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from DB.db import Base
from common.account_type import AccountType


class BankAccount(Base):
    __tablename__ = 'bank_account'
    id : Mapped[str] = mapped_column(
        String,
        primary_key = True,
        default = lambda: str(uuid.uuid4())
    )
    account_number: Mapped[str] = mapped_column(
        String,
        unique = True,
        nullable = False,
    )
    account_type: Mapped[AccountType] = mapped_column(
        Enum,
        nullable = False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default = True,
    )
    balance: Mapped[float] = mapped_column(
        Float,
        default = 0.0
    )
    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable = False
    )
    user = relationship(
        "User" ,
        back_populates="bank_account"
    )
    transactions = relationship(
        "Transaction",
        back_populates="bank_account"
    )