from pydantic import BaseModel
from pydantic import constr, EmailStr


class UserSignInController(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=200)
