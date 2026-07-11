from datetime import datetime
from  pydantic import BaseModel, Field

from common.transaction_type import TransactionType


class TransactionSchema(BaseModel):
    account_id: str
    transaction_type: TransactionType
    amount: float
    date: datetime = Field(default_factory=datetime.now)