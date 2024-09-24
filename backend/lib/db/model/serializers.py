from .models import *
from lib.db.sql.table import *


def user_model_serializer(data: User) -> UserModel:
    return UserModel(
        id=data.id,
        first_name=data.first_name,
        last_name=data.last_name,
        status=data.status,
        email=data.email,
        password=data.password,
        password_salt=data.password_salt,
        role_id=data.role_id
    )


def user_session_model_serializer(data: UserSession) -> UserSessionModel:
    return UserSessionModel(
        id=data.id,
        user_id=data.user_id,
        token=data.token,
        token_hindrance=data.token_hindrance,
        date_start=data.date_start,
        date_end=data.date_end,
        ip=data.ip
    )
