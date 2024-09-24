from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    status: int
    email: str
    password: str
    password_salt: str
    role_id: int


class UserSessionModel(BaseModel):
    id: Optional[int]
    user_id: int
    token: str
    token_hindrance: str
    date_start: datetime
    date_end: datetime
    ip: str
