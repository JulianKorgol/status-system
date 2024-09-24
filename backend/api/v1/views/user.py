from fastapi import Depends, Request
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from core.settings import session__active_days
from core import HttpStatus

from lib.db.sql import get_sql_session
from lib.db.repository import UserRepository, UserSessionRepository

from api.v1.controllers.user import UserSignInController

from lib.user.status import check_if_user_is_active
from lib.user.password import check_user_password
from lib.user.session import create_user_session

from lib.cookie import cookie_set


async def user_sign_in(req_data: UserSignInController, req: Request,
                       db: AsyncSession = Depends(get_sql_session)) -> JSONResponse:
    user = await UserRepository.get_by_email(user_email=req_data.email, db=db)
    if user is None:
        return JSONResponse(status_code=HttpStatus.UNAUTHORIZED, content={"message": "Invalid email or password"})

    if check_if_user_is_active(user=user) is False:
        return JSONResponse(status_code=HttpStatus.LOCKED, content={"message": "User is not active"})

    if check_user_password(password=req_data.password, salt=user.password_salt, password_hash=user.password) is False:
        return JSONResponse(status_code=HttpStatus.UNAUTHORIZED, content={"message": "Invalid email or password"})

    user_session_model = await create_user_session(user=user, req=req, db=db)
    user_session_model = await UserSessionRepository.create(user_session_model=user_session_model, db=db)

    res = JSONResponse(status_code=HttpStatus.OK, content={"message": "User signed in"})
    cookie_set(response=res, key="token", value=user_session_model.token, max_age=60 * 60 * 24 * session__active_days,
               httponly=True)
    cookie_set(response=res, key="token_hindrance", value=user_session_model.token_hindrance,
               max_age=60 * 60 * 24 * session__active_days, httponly=True)
    return res


async def user_sign_out(req: Request, db: AsyncSession = Depends(get_sql_session)) -> JSONResponse:
    token = req.cookies.get("token")
    if token is None:
        return JSONResponse(status_code=HttpStatus.BAD_REQUEST, content={"message": "User is not signed in"})

    await UserSessionRepository.delete_by_token(user_session_token=token, db=db)

    res = JSONResponse(status_code=HttpStatus.OK, content={"message": "User signed out"})
    cookie_set(response=res, key="token", value="", max_age=0, httponly=True)
    cookie_set(response=res, key="token_hindrance", value="", max_age=0, httponly=True)
    return res
