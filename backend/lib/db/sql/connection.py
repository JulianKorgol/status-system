from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from os import environ as env

engine = create_async_engine(env.get('DB_SQL_URI'))
sessionLocal = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


async def get_sql_session() -> AsyncSession:
    db = sessionLocal()

    try:
        yield db
    finally:
        await db.close()
