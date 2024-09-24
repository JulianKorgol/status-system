from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .connection import Base


class Role(Base):
    __tablename__ = "Role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    status: Mapped[int] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column()
    password_salt: Mapped[str] = mapped_column()
    role_id: Mapped[int] = mapped_column(nullable=False)


class Permission(Base):
    __tablename__ = "Permission"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class PermissionToRole(Base):
    __tablename__ = "PermissionToRole"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    permission_id: Mapped[int] = mapped_column()
    role_id: Mapped[int] = mapped_column()


class UserSession(Base):
    __tablename__ = "UserSession"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    token: Mapped[str] = mapped_column(nullable=False, unique=True)
    token_hindrance: Mapped[str] = mapped_column(nullable=False)
    date_start: Mapped[datetime] = mapped_column(nullable=False)
    date_end: Mapped[datetime] = mapped_column(nullable=False)
    ip: Mapped[str] = mapped_column(nullable=False)
