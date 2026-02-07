from __future__ import annotations
from datetime import datetime, UTC
from typing import List

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


# interface table user_roles
user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("auth.users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("auth.roles.id"), primary_key=True),
    schema="auth",
)

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)  # like: ceo, vp, manager, admin, analyst, viewer
    description = Column(String(255), nullable=True)

    users = relationship(
        "User",
        secondary=user_roles,
        back_populates="roles",
    )


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(100), nullable=False)

    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=True)
    phone = Column(String(20), unique=True, index=True, nullable=True)

    hashed_password = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)  # if phone or email is verified

    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(
        DateTime,
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
    )

    roles = relationship(
        "Role",
        secondary=user_roles,
        back_populates="users",
    )



