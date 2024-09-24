from fastapi import Request

from sqlalchemy.ext.asyncio import AsyncSession

from lib.db.repository import UserSessionRepository
from lib.db.model import UserModel, UserSessionModel

from hashlib import pbkdf2_hmac

from uuid import uuid4

import datetime

from core.settings import session__active_days


def create_hashes_for_user_session() -> dict[str, str]:
    hindrance = uuid4().hex
    entry_salt = str(hindrance + str(datetime.datetime.now()))

    session_str = ''
    for i in range(3):
        temp = pbkdf2_hmac('sha256', uuid4().hex.encode('utf-8'), entry_salt.encode('utf-8'), 100).hex()
        session_str += temp[0:100]

    return {'token': session_str, 'hindrance': hindrance}


async def create_user_session(user: UserModel, req: Request, db: AsyncSession) -> UserSessionModel:
    session_keys = create_hashes_for_user_session()
    while await UserSessionRepository.get_by_token(token=session_keys['token'], db=db) is not None:
        session_keys = create_hashes_for_user_session()

    return UserSessionModel(
        id=None,
        user_id=user.id,
        token=session_keys['token'],
        token_hindrance=session_keys['hindrance'],
        date_start=datetime.datetime.now(),
        date_end=datetime.datetime.now() + datetime.timedelta(days=session__active_days),
        ip=req.client.host
    )
