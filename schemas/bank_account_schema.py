from pydantic import BaseModel

from common.account_type import AccountType


class BankAccountSchema(BaseModel):
    account_number: str
    account_type: AccountType
    is_active: bool
    balance: float
    user_id: str
