from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from lib.db.sql.table import UserSession
from lib.db.model.models import UserSessionModel
from lib.db.model.serializers import user_session_model_serializer


class UserSessionRepository:
    @staticmethod
    async def get_by_token(token: str, db: AsyncSession) -> UserSessionModel | None:
        db_results = await db.execute(
            select(UserSession).where(UserSession.token == token)
        )

        result = db_results.scalars().first()
        if result is None:
            return None

        return user_session_model_serializer(result)

    @staticmethod
    async def create(user_session_model: UserSessionModel, db: AsyncSession) -> UserSessionModel:
        user_session = UserSession(
            user_id=user_session_model.user_id,
            token=user_session_model.token,
            token_hindrance=user_session_model.token_hindrance,
            date_start=user_session_model.date_start,
            date_end=user_session_model.date_end,
            ip=user_session_model.ip
        )

        db.add(user_session)
        await db.commit()
        await db.refresh(user_session)

        return user_session_model_serializer(user_session)

    @staticmethod
    async def delete_by_token(user_session_token: str, db: AsyncSession) -> None:
        await db.execute(
            delete(UserSession).where(UserSession.token == user_session_token)
        )
        await db.commit()
