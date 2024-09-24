from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from lib.db.sql.table import User
from lib.db.model.models import UserModel
from lib.db.model.serializers import user_model_serializer


class UserRepository:
    @staticmethod
    async def get_by_id(user_id: int, db: AsyncSession) -> UserModel | None:
        db_results = await db.execute(
            select(User).where(User.id == user_id)
        )

        result = db_results.scalars().first()
        if result is None:
            return None

        return user_model_serializer(result)

    @staticmethod
    async def get_by_email(user_email: str, db: AsyncSession) -> UserModel | None:
        db_results = await db.execute(
            select(User).where(User.email == user_email)
        )

        result = db_results.scalars().first()
        if result is None:
            return None

        return user_model_serializer(result)
